#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把本目录完整推送到 GitHub（纯 REST API 实现，不需要 git 客户端联网）。

为什么不用 `git push`：本机 shell 的 TLS 走 Windows schannel，会报
`AcquireCredentialsHandle failed: SEC_E_NO_CREDENTIALS`，git/curl/PowerShell 全部无法出网。
Python 自带 OpenSSL，于是改用 GitHub 的 Git Data API 直接建 tree / commit / ref。

用法：
  python scripts/deploy_github.py                       # 推送到 xushan628/github-free-guide
  python scripts/deploy_github.py --repo demo --private
  GITHUB_TOKEN=xxx python scripts/deploy_github.py

凭据顺序：环境变量 GITHUB_TOKEN / GH_TOKEN → Windows 凭据管理器。
"""

from __future__ import annotations

import argparse
import base64
import json
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = "https://api.github.com"
UA = "github-free-guide-deployer/1.0"
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv", "venv"}


sys.path.insert(0, str(Path(__file__).resolve().parent))
from gh_auth import resolve_token  # noqa: E402  同目录共享模块


class GitHub:
    def __init__(self, token: str):
        self.token = token
        self.calls = 0

    def call(self, method: str, path: str, payload: dict | None = None, retries: int = 3):
        url = path if path.startswith("http") else API + path
        body = json.dumps(payload).encode() if payload is not None else None
        for attempt in range(retries):
            req = urllib.request.Request(url, data=body, method=method, headers={
                "Authorization": f"Bearer {self.token}",
                "Accept": "application/vnd.github+json",
                "Content-Type": "application/json",
                "User-Agent": UA,
                "X-GitHub-Api-Version": "2022-11-28",
            })
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    self.calls += 1
                    raw = resp.read()
                    return json.loads(raw) if raw else {}
            except urllib.error.HTTPError as exc:
                detail = exc.read().decode("utf-8", "replace")[:400]
                if exc.code in (500, 502, 503, 504) and attempt < retries - 1:
                    time.sleep(2 * (attempt + 1))
                    continue
                raise RuntimeError(f"{method} {path} → HTTP {exc.code}: {detail}") from None
            except Exception as exc:
                if attempt < retries - 1:
                    time.sleep(1.5 * (attempt + 1))
                    continue
                raise RuntimeError(f"{method} {path} → {type(exc).__name__}: {exc}") from None
        raise RuntimeError("unreachable")


def iter_files(base: Path):
    for path in sorted(base.rglob("*")):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(base).parts):
            continue
        yield path, path.relative_to(base).as_posix()


def ensure_repo(gh: GitHub, owner: str, repo: str, *, private: bool, description: str, homepage: str) -> None:
    try:
        info = gh.call("GET", f"/repos/{owner}/{repo}")
        print(f"· 仓库已存在：{info['html_url']}（{info['visibility']}）")
        return
    except RuntimeError as exc:
        if "HTTP 404" not in str(exc):
            raise
    print(f"· 创建仓库 {owner}/{repo} …")
    gh.call("POST", "/user/repos", {
        "name": repo,
        "description": description,
        "homepage": homepage,
        "private": private,
        "has_issues": True,
        "has_wiki": False,
        "has_projects": False,
        "auto_init": True,   # 必须初始化，否则空仓库建 blob 会 409
    })


def ensure_initial_commit(gh: GitHub, owner: str, repo: str, branch: str) -> None:
    """空仓库（没有任何提交）建 blob 会返回 409，先补一个初始提交把 git 仓库建起来。"""
    try:
        gh.call("GET", f"/repos/{owner}/{repo}/git/ref/heads/{branch}")
        return
    except RuntimeError as exc:
        msg = str(exc)
        # 空仓库：GET ref 会返回 404 或 409（Git Repository is empty）
        if "HTTP 404" not in msg and "HTTP 409" not in msg:
            raise
    print("· 仓库为空，先创建初始提交 …")
    gh.call("PUT", f"/repos/{owner}/{repo}/contents/README.md", {
        "message": "chore: 初始化仓库",
        "content": base64.b64encode("# init\n".encode()).decode(),
        "branch": branch,
    })


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--login", default="xushan628")
    parser.add_argument("--owner", default=None, help="默认等于 --login")
    parser.add_argument("--repo", default="github-free-guide")
    parser.add_argument("--dir", default=str(ROOT))
    parser.add_argument("--branch", default="main")
    parser.add_argument("--message", default=None)
    parser.add_argument("--description", default="GitHub 免费福利指南：素材 / 工具 / 本地 AI / Actions / Pages / Codespaces / 学生包 / 避坑")
    parser.add_argument("--homepage", default=None)
    parser.add_argument("--private", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--squash", action="store_true", help="忽略历史，用单个根提交覆盖（适合首次发布）")
    args = parser.parse_args()

    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    owner = args.owner or args.login
    base = Path(args.dir).resolve()
    homepage = args.homepage or f"https://{owner}.github.io/{args.repo}/"
    message = args.message or f"feat: 初始化 GitHub 免费福利指南（{time.strftime('%Y-%m-%d')}）"

    files = list(iter_files(base))
    total = sum(p.stat().st_size for p, _ in files)
    print(f"· 待推送 {len(files)} 个文件，{total/1024:.1f} KB")

    gh = GitHub(resolve_token(args.login))
    if args.dry_run:
        for _, rel in files[:200]:
            print("   ", rel)
        print("· dry-run 结束（未做任何修改）")
        return 0

    ensure_repo(gh, owner, args.repo, private=args.private,
                description=args.description, homepage=homepage)
    ensure_initial_commit(gh, owner, args.repo, args.branch)

    print("· 上传 blob …")
    def upload(item):
        path, rel = item
        data = path.read_bytes()
        res = gh.call("POST", f"/repos/{owner}/{args.repo}/git/blobs", {
            "content": base64.b64encode(data).decode(),
            "encoding": "base64",
        })
        return {"path": rel, "mode": "100644", "type": "blob", "sha": res["sha"]}

    with ThreadPoolExecutor(max_workers=6) as pool:
        tree = list(pool.map(upload, files))
    print(f"  完成 {len(tree)} 个")

    print("· 创建 tree / commit …")
    new_tree = gh.call("POST", f"/repos/{owner}/{args.repo}/git/trees", {"tree": tree})

    parents = []
    if not args.squash:
      try:
        ref = gh.call("GET", f"/repos/{owner}/{args.repo}/git/ref/heads/{args.branch}")
        parents = [ref["object"]["sha"]]
        print(f"  基于现有提交 {ref['object']['sha'][:7]}")
      except RuntimeError as exc:
        if "HTTP 404" not in str(exc):
            raise
        print("  首次提交（无父提交）")

    commit = gh.call("POST", f"/repos/{owner}/{args.repo}/git/commits", {
        "message": message, "tree": new_tree["sha"], "parents": parents,
    })

    if args.squash or parents:
        gh.call("PATCH", f"/repos/{owner}/{args.repo}/git/refs/heads/{args.branch}", {
            "sha": commit["sha"], "force": bool(args.squash),
        })
    else:
        try:
            gh.call("POST", f"/repos/{owner}/{args.repo}/git/refs", {
                "ref": f"refs/heads/{args.branch}", "sha": commit["sha"],
            })
        except RuntimeError:
            gh.call("PATCH", f"/repos/{owner}/{args.repo}/git/refs/heads/{args.branch}", {
                "sha": commit["sha"], "force": True,
            })

    print(f"\n✅ 推送完成：https://github.com/{owner}/{args.repo}/commit/{commit['sha']}")
    print(f"   提交 {commit['sha'][:7]} · 文件 {len(tree)} · API 调用 {gh.calls} 次")
    print(f"   站点将部署在：{homepage}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
