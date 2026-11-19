#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从**你自己的网络**体检 GitHub Pages 站点，判断是"站点挂了"还是"你被缓存/网络坑了"。

用法：
  python scripts/check_site.py
  python scripts/check_site.py https://xushan628.github.io/github-free-guide/

输出：HTTP 状态、边缘节点、缓存命中情况、是否拿到 GitHub 的 "Site not found" 404，
以及一条结论 + 建议动作。
"""

from __future__ import annotations

import sys
import time
import urllib.error
import urllib.request

URL = sys.argv[1] if len(sys.argv) > 1 else "https://xushan628.github.io/github-free-guide/"
UA = "Mozilla/5.0 (check_site.py)"
KEYS = ("server", "x-served-by", "x-cache", "age", "etag", "last-modified", "content-type")


def probe(url: str, fresh: bool) -> tuple[int | None, dict, bytes, str]:
    headers = {"User-Agent": UA}
    if fresh:
        headers["Cache-Control"] = "no-cache, no-store"
        headers["Pragma"] = "no-cache"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, dict(resp.headers), resp.read(), ""
    except urllib.error.HTTPError as exc:
        return exc.code, dict(exc.headers), exc.read(), f"HTTPError {exc.code}"
    except Exception as exc:  # 超时 / DNS / TLS
        return None, {}, b"", f"{type(exc).__name__}: {exc}"


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print(f"目标：{URL}\n时间：{time.strftime('%Y-%m-%d %H:%M:%S')}\n")

    status, headers, body, err = probe(URL, fresh=False)
    text = body.decode("utf-8", "replace")
    lower = {k.lower(): v for k, v in headers.items()}
    print("① 普通请求")
    print(f"   status      : {status or '连接失败'}")
    for key in KEYS:
        if key in lower:
            print(f"   {key:12s}: {lower[key]}")
    if err:
        print(f"   错误        : {err}")

    site_missing = "There isn't a GitHub Pages site here" in text or "Site not found" in text
    served_by = lower.get("x-served-by", "")
    cache = lower.get("x-cache", "")
    print(f"   是 404 页    : {'是（GitHub 说这里没有站点）' if site_missing else '否'}")
    print(f"   内容长度    : {len(body)} 字节\n")

    status2, headers2, body2, err2 = probe(f"{URL}{'&' if '?' in URL else '?'}_probe={int(time.time())}", fresh=True)
    print("② 绕过缓存再请求一次")
    print(f"   status      : {status2 or '连接失败'}"
          + (f"   （{err2}）" if err2 else ""))
    print(f"   x-cache     : {dict((k.lower(), v) for k, v in headers2.items()).get('x-cache', '-')}\n")

    print("—" * 44)
    if status == 200 and not site_missing:
        print("✅ 结论：站点正常，内容已返回。")
        print("   如果你浏览器里看到的还是 404，那是你本机缓存了旧的 404：")
        print("   Ctrl+Shift+R 强制刷新，或用无痕窗口打开，或等 10 分钟缓存过期。")
        return 0
    if status == 404 and site_missing:
        print("❌ 结论：GitHub 确实没有为这个地址提供站点（不是缓存问题）。")
        print("   检查：仓库 Settings → Pages 是否指向 main / docs，构建是否报错。")
        return 1
    if status is None:
        print("⚠️ 结论：连不上。多半是网络/DNS 问题，不是站点问题。")
        print("   试试换 DNS（223.5.5.5 / 1.1.1.1）或换网络（手机热点）。")
        return 2
    print(f"⚠️ 结论：HTTP {status}，站点存在但返回了异常状态，看上方响应头。")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
