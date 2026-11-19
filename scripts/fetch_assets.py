#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""下载「免费商用」素材（图标 / 字体 / 许可证）到 01-assets/，并生成 MANIFEST.json。

为什么要用 API 而不是 raw.githubusercontent.com：
  本机 shell 出网受限，raw / github.com 直连会被重置，只有 api.github.com 可达。
  因此统一走 GitHub REST API（contents → git/blobs 回退），这条路在受限网络下依然可用。

用法：
  python scripts/fetch_assets.py                 # 下载全部素材
  python scripts/fetch_assets.py --only icons    # 只下图标
  GITHUB_TOKEN=xxx python scripts/fetch_assets.py

凭据顺序：环境变量 GITHUB_TOKEN → Windows 凭据管理器（target = GitHub - https://api.github.com/<login>）。
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "01-assets"
MANIFEST = ROOT / "MANIFEST.json"
API = "https://api.github.com"
UA = "github-free-guide/1.0 (+https://github.com/xushan628)"

# 精选常用 UI 图标名（kebab-case，tabler 与 lucide 的命名高度一致）
ICON_NAMES = [
    "home", "user", "users", "settings", "search", "heart", "star", "bell",
    "bookmark", "calendar", "camera", "clock", "cloud", "cloud-upload",
    "download", "upload", "mail", "map-pin", "menu", "message-circle",
    "message-square", "moon", "sun", "edit", "trash", "plus", "minus",
    "check", "x", "arrow-left", "arrow-right", "arrow-up", "arrow-down",
    "chevron-down", "chevron-up", "chevron-left", "chevron-right",
    "external-link", "file", "file-text", "folder", "image", "link", "lock",
    "unlock", "play", "pause", "refresh", "rotate", "save", "send", "share",
    "shopping-cart", "tag", "terminal", "wifi", "zoom-in", "zoom-out",
    "alert-circle", "alert-triangle", "info-circle", "help-circle", "eye",
    "eye-off", "filter", "grid", "list", "more-horizontal", "more-vertical",
    "printer", "copy", "clipboard", "database", "server", "cpu", "code",
    "git-branch", "git-pull-request", "brand-github", "globe", "key",
    "layers", "layout", "loader", "login", "logout", "microphone", "monitor",
    "music", "package", "paperclip", "phone", "chart-pie", "pin", "power",
    "repeat", "scissors", "shield", "device-mobile", "volume", "table",
    "thumb-up", "thumb-down", "tool", "trending-up", "truck", "video",
    "wand", "zap", "bolt", "bulb", "camera-off", "headphones", "puzzle",
    "rocket", "school", "trophy", "wallet",
]

# 免费可商用字体（OFL 1.1），取自 google/fonts 官方仓库
FONTS = [
    ("google/fonts", "ofl/jetbrainsmono/JetBrainsMono[wght].ttf", "JetBrainsMono[wght].ttf", "OFL-1.1"),
    ("google/fonts", "ofl/inter/Inter[opsz,wght].ttf", "Inter[opsz,wght].ttf", "OFL-1.1"),
]

LICENSES = [
    ("tabler/tabler-icons", "LICENSE", "tabler-MIT.txt", "MIT"),
    ("lucide-icons/lucide", "LICENSE", "lucide-ISC.txt", "ISC"),
    ("google/fonts", "ofl/jetbrainsmono/OFL.txt", "JetBrainsMono-OFL.txt", "OFL-1.1"),
    ("google/fonts", "ofl/inter/OFL.txt", "Inter-OFL.txt", "OFL-1.1"),
]


# ---------------------------------------------------------------- 凭据
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gh_auth import resolve_token  # noqa: E402  同目录共享模块


# ---------------------------------------------------------------- HTTP
class Client:
    def __init__(self, token: str):
        self.token = token
        self.calls = 0

    def _request(self, url: str, method: str = "GET") -> urllib.request.Request:
        return urllib.request.Request(url, method=method, headers={
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
            "User-Agent": UA,
            "X-GitHub-Api-Version": "2022-11-28",
        })

    def json(self, url: str, retries: int = 3):
        last = None
        for attempt in range(retries):
            try:
                with urllib.request.urlopen(self._request(url), timeout=30) as resp:
                    self.calls += 1
                    self._respect_rate(resp.headers)
                    return json.loads(resp.read().decode("utf-8"))
            except urllib.error.HTTPError as exc:
                if exc.code in (403, 429) and attempt < retries - 1:
                    time.sleep(3 + attempt * 3)
                    last = exc
                    continue
                raise
            except Exception as exc:  # 网络抖动重试
                last = exc
                if attempt < retries - 1:
                    time.sleep(1.5 * (attempt + 1))
                    continue
                raise
        raise last  # pragma: no cover

    def _respect_rate(self, headers) -> None:
        remaining = headers.get("x-ratelimit-remaining")
        reset = headers.get("x-ratelimit-reset")
        if remaining is not None and int(remaining) < 20 and reset:
            wait = int(reset) - int(time.time()) + 2
            if 0 < wait < 900:
                print(f"  · 触发限流，等待 {wait}s", flush=True)
                time.sleep(wait)

    def contents(self, repo: str, path: str) -> dict:
        quoted = urllib.parse.quote(path, safe="/")
        return self.json(f"{API}/repos/{repo}/contents/{quoted}")

    def blob(self, repo: str, sha: str) -> bytes:
        data = self.json(f"{API}/repos/{repo}/git/blobs/{sha}")
        return base64.b64decode(data["content"])


def fetch_file(client: Client, repo: str, path: str) -> bytes:
    """contents API 优先（<1MB 直接带 base64），否则回退 git/blobs。"""
    meta = client.contents(repo, path)
    if isinstance(meta, list):
        raise ValueError(f"{repo}/{path} 是目录，不是文件")
    if meta.get("content"):
        return base64.b64decode(meta["content"])
    return client.blob(repo, meta["sha"])


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_bytes(dest: Path, data: bytes) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)


def record(entry: dict, repo: str, src: str, rel: str, license_id: str, data: bytes) -> dict:
    entry["files"].append({
        "path": rel,
        "repo": repo,
        "source_path": src,
        "license": license_id,
        "bytes": len(data),
        "sha256": sha256_bytes(data),
        "source_url": f"https://github.com/{repo}/blob/main/{urllib.parse.quote(src, safe='/')}",
    })
    return entry


# ---------------------------------------------------------------- 任务
def download_icons(client: Client, entry: dict, name: str, wanted: list[str]) -> int:
    dest_dir = ASSETS / "icons" / name
    prefix = "icons/outline/" if name == "tabler" else "icons/"
    repo = "tabler/tabler-icons" if name == "tabler" else "lucide-icons/lucide"
    license_id = "MIT" if name == "tabler" else "ISC"

    def one(icon: str):
        try:
            data = fetch_file(client, repo, f"{prefix}{icon}.svg")
        except Exception:
            return False
        write_bytes(dest_dir / f"{icon}.svg", data)
        record(entry, repo, f"{prefix}{icon}.svg", f"01-assets/icons/{name}/{icon}.svg", license_id, data)
        return True

    ok = 0
    with ThreadPoolExecutor(max_workers=8) as pool:
        for hit in pool.map(one, wanted):
            ok += int(hit)
    print(f"  · {name}: 命中 {ok}/{len(wanted)}", flush=True)
    return ok


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--login", default="xushan628")
    parser.add_argument("--only", choices=["icons", "fonts", "licenses"], default=None)
    args = parser.parse_args()

    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    client = Client(resolve_token(args.login))
    entry = {"generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
             "generator": "scripts/fetch_assets.py", "files": []}

    do_all = args.only is None
    if do_all or args.only == "icons":
        print("下载图标 …", flush=True)
        download_icons(client, entry, "tabler", ICON_NAMES)
        download_icons(client, entry, "lucide", ICON_NAMES)

    if do_all or args.only == "fonts":
        print("下载字体 …", flush=True)
        for repo, src, fname, lic in FONTS:
            data = fetch_file(client, repo, src)
            write_bytes(ASSETS / "fonts" / fname, data)
            record(entry, repo, src, f"01-assets/fonts/{fname}", lic, data)
            print(f"  · {fname} {len(data)/1024:.0f} KB", flush=True)

    if do_all or args.only == "licenses":
        print("下载许可证 …", flush=True)
        for repo, src, fname, lic in LICENSES:
            data = fetch_file(client, repo, src)
            write_bytes(ASSETS / "LICENSES" / fname, data)
            record(entry, repo, src, f"01-assets/LICENSES/{fname}", lic, data)
            print(f"  · {fname}", flush=True)

    entry["total_files"] = len(entry["files"])
    entry["total_bytes"] = sum(f["bytes"] for f in entry["files"])
    if MANIFEST.exists() and args.only:
        old = json.loads(MANIFEST.read_text(encoding="utf-8"))
        kept = [f for f in old.get("files", []) if f["path"] not in {n["path"] for n in entry["files"]}]
        entry["files"] = sorted(kept + entry["files"], key=lambda f: f["path"])
        entry["total_files"] = len(entry["files"])
        entry["total_bytes"] = sum(f["bytes"] for f in entry["files"])
    entry["files"].sort(key=lambda f: f["path"])
    MANIFEST.write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"\n完成：{entry['total_files']} 个文件，{entry['total_bytes']/1024:.1f} KB，"
          f"API 调用 {client.calls} 次 → {MANIFEST.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
