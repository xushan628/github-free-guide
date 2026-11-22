#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""外链 + 站内链接体检，输出 docs/link-check.md。

为什么需要它：这个仓库的价值全在"链接是不是还活着"。资源类仓库烂掉的方式只有一个——
推荐的项目改名/删库/换许可证，而没人发现。所以让机器每周查一遍。

检查策略：
  * github.com/<owner>/<repo>            → 改走 api.github.com/repos/<owner>/<repo>（本机 github.com 直连受限）
  * 其他 http(s)                         → HEAD，失败退 GET，超时/连接重置记为「未验证」
  * 站内相对链接（*.md / 目录 / 文件）    → 直接查本地文件是否存在

用法：
  python scripts/verify_links.py            # 生成报告
  python scripts/verify_links.py --strict   # 有失效链接时返回退出码 1
"""

from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORT = ROOT / "docs" / "link-check.md"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gh_auth import resolve_token  # noqa: E402  同目录共享模块

TOKEN = resolve_token("xushan628", required=False)
SKIP_DIRS = ("openwiki",)  # 生成的知识库，含示例链接
LOCAL_HOSTS = ("http://localhost", "http://127.0.0.1", "https://localhost", "https://127.0.0.1")
UA = "Mozilla/5.0 (compatible; github-free-guide-link-check/1.0)"
TIMEOUT = 12

MD_LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
BARE_URL = re.compile(r"(?<![(\[])\bhttps?://[^\s<>\"`)）]+")
GH_REPO = re.compile(r"^https?://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)/?(?:$|\?|#)")
# github.com/<owner>/<repo>/blob/<branch>/<path> → 改走 contents API，避免直连 github.com 被重置
GH_BLOB = re.compile(r"^https?://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)/blob/([^/]+)/(.+)$")


def http_status(url: str) -> tuple[str, str]:
    """返回 (状态, 说明)。状态取值：ok / dead / unverified / local。"""
    if url.startswith(LOCAL_HOSTS):
        return "local", "本地服务示例，跳过"
    blob = GH_BLOB.match(url)
    if blob:
        owner, repo, branch, path = blob.group(1), blob.group(2), blob.group(3), blob.group(4)
        path = path.split("?")[0].split("#")[0]
        url = (f"https://api.github.com/repos/{owner}/{repo}/contents/"
               f"{urllib.parse.quote(path, safe='/')}?ref={branch}")
    else:
        match = GH_REPO.match(url)
        if match:
            owner, repo = match.group(1), match.group(2).removesuffix(".git")
            url = f"https://api.github.com/repos/{owner}/{repo}"

    for method in ("HEAD", "GET"):
        try:
            headers = {"User-Agent": UA}
            if TOKEN and url.startswith("https://api.github.com"):
                headers["Authorization"] = f"Bearer {TOKEN}"
            req = urllib.request.Request(url, method=method, headers=headers)
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                return "ok", str(resp.status)
        except urllib.error.HTTPError as exc:
            if exc.code in (403, 405, 429) and method == "HEAD":
                continue
            if exc.code in (403, 429):
                return "unverified", f"HTTP {exc.code}（可能限流）"
            return "dead", f"HTTP {exc.code}"
        except Exception as exc:  # 超时 / 连接重置 / DNS
            last = f"{type(exc).__name__}: {str(exc)[:60]}"
            if method == "HEAD":
                continue
            return "unverified", last
    return "unverified", locals().get("last", "unknown")


def collect() -> dict[str, dict]:
    found: dict[str, dict] = {}
    for md in sorted(ROOT.rglob("*.md")):
        if md.name == REPORT.name:
            continue
        rel = md.relative_to(ROOT).as_posix()
        # openwiki/ 是自动生成的知识库，正文里有大量“示例链接”（如 [<repo>](<repo_url>)），
        # 它们不是真实链接，检查它们只会制造假警报。
        if rel.split("/")[0] in SKIP_DIRS:
            continue
        text = md.read_text(encoding="utf-8", errors="replace")
        # 去掉围栏代码块与行内代码：里面的链接是示例，不是要访问的资源
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        text = re.sub(r"`[^`\n]*`", "", text)
        for label, target in MD_LINK.findall(text):
            if target.startswith(("http://", "https://")):
                found.setdefault(target, {"kind": "external", "refs": []})["refs"].append(f"{rel} → {label or target}")
            elif target.startswith(("#", "mailto:")):
                continue
            else:
                found.setdefault(target, {"kind": "local", "refs": []})["refs"].append(f"{rel} → {label or target}")
        for url in BARE_URL.findall(text):
            url = url.rstrip(".,;:，。；）)")
            found.setdefault(url, {"kind": "external", "refs": []})["refs"].append(rel)
    return found


def check_local(target: str, source: str) -> tuple[str, str]:
    base = ROOT / source.split(" → ")[0]
    path = (base.parent / target.split("#")[0]).resolve()
    try:
        path.relative_to(ROOT.resolve())
    except ValueError:
        return "dead", "越出仓库目录"
    return ("ok", "存在") if path.exists() else ("dead", "文件不存在")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    items = collect()
    print(f"共 {len(items)} 个链接，开始检查 …", flush=True)

    results = []
    externals = [(u, m) for u, m in items.items() if m["kind"] == "external"]

    def run(pair):
        url, meta = pair
        return url, meta, http_status(url)

    with ThreadPoolExecutor(max_workers=8) as pool:
        for url, meta, (status, detail) in pool.map(run, externals):
            results.append({"url": url, "status": status, "detail": detail, "refs": meta["refs"]})
            time.sleep(0)

    for url, meta in items.items():
        if meta["kind"] != "local":
            continue
        status, detail = check_local(url, meta["refs"][0])
        results.append({"url": url, "status": status, "detail": detail, "refs": meta["refs"]})

    dead = [r for r in results if r["status"] == "dead"]
    unverified = [r for r in results if r["status"] == "unverified"]
    ok = [r for r in results if r["status"] == "ok"]
    skipped = [r for r in results if r["status"] == "local"]

    lines = [
        "# 外链体检报告", "",
        f"- 生成时间：{datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        f"- 生成脚本：`scripts/verify_links.py`（本仓库的 `.github/workflows/link-check.yml` 每周自动跑一次）",
        f"- 总计 **{len(results)}** 个链接：✅ 正常 {len(ok)} ／ ❌ 失效 {len(dead)} ／ "
        f"⚠️ 未验证 {len(unverified)} ／ ⏭️ 跳过（本地服务）{len(skipped)}", "",
        "> ⚠️「未验证」= 本机网络无法直连（例如 `github.com` 页面在部分网络环境会被重置）。"
        "脚本对 `github.com/<owner>/<repo>` 会自动改走 `api.github.com`，所以仓库类链接的结论是可信的；"
        "`docs.github.com` 等文档页若显示未验证，属于网络环境限制，不代表链接失效。", "",
    ]
    if dead:
        lines += ["## ❌ 失效链接（需要修）", "", "| 链接 | 原因 | 出现在 |", "|---|---|---|"]
        for r in dead:
            lines.append(f"| {r['url']} | {r['detail']} | {', '.join(sorted(set(r['refs'])))} |")
        lines.append("")
    if unverified:
        lines += ["## ⚠️ 未验证", "", "| 链接 | 原因 |", "|---|---|"]
        for r in unverified:
            lines.append(f"| {r['url']} | {r['detail']} |")
        lines.append("")
    lines += ["## ✅ 全部结果", "", "| 状态 | 链接 | 说明 |", "|---|---|---|"]
    for r in sorted(results, key=lambda x: (x["status"] != "ok", x["url"])):
        mark = {"ok": "✅", "dead": "❌", "unverified": "⚠️", "local": "⏭️"}[r["status"]]
        lines.append(f"| {mark} | {r['url']} | {r['detail']} |")
    lines.append("")

    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"✅ {len(ok)}  ⚠️ {len(unverified)}  ❌ {len(dead)}  ⏭️ {len(skipped)}  → {REPORT.relative_to(ROOT)}")
    for r in dead[:10]:
        print(f"  ❌ {r['url']}  ({r['detail']})")
    return 1 if (args.strict and dead) else 0


if __name__ == "__main__":
    raise SystemExit(main())
