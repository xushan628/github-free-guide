#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把姊妹项目 Open Data Atlas 的数据集目录同步进本仓库的 09-datasets/。

数据源（唯一真相）：xushan628/open-data-atlas 的 data/manifest.json
产物：
  09-datasets/datasets.json   —— 精简机器可读目录（repo / license / 文件数 / 体积）
  09-datasets/README.md       —— 只重写 <!-- BEGIN GENERATED --> 之间的表格

设计取舍：
  * 不带 star 数：每周都会变，会制造无意义提交；需要看热度请点上游链接。
  * 幂等：内容没变就不写文件，CI 里不会产生空提交。
  * 结构不对就报错退出，绝不写半截文件。

用法：
  python scripts/sync_atlas.py            # 同步
  python scripts/sync_atlas.py --check    # 只检查是否最新（不同步），有差异返回 1
"""

from __future__ import annotations

import argparse
import base64
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "09-datasets"
JSON_OUT = OUT_DIR / "datasets.json"
README = OUT_DIR / "README.md"
MANIFEST_API = "https://api.github.com/repos/xushan628/open-data-atlas/contents/data/manifest.json"
INDEX = ROOT / "docs" / "index.html"

BEGIN = "<!-- BEGIN GENERATED: datasets -->"
END = "<!-- END GENERATED: datasets -->"
BEGIN_IDX = "<!-- BEGIN GENERATED: atlas-items -->"
END_IDX = "<!-- END GENERATED: atlas-items -->"

# 每个数据集"能拿来做什么"——人工判断，随数据集本身稳定，不随 manifest 变化
PURPOSE = {
    "poetry": "分词、词频、作者统计；做古典诗词检索或生成",
    "words": "词典/背单词应用：释义、例句、多语言对照",
    "exercises": "做健身计划工具：动作、部位、器械、图示",
    "geo": "国家/州/城市数据：地图、时区、人口统计",
    "thewell": "科学计算与 ML 训练：15 TB 级物理模拟场",
}


def load_token() -> str | None:
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from gh_auth import resolve_token
        return resolve_token("xushan628", required=False)
    except Exception:
        return None


def fetch_manifest() -> dict:
    headers = {"User-Agent": "github-free-guide-sync/1.0", "Accept": "application/vnd.github+json"}
    token = load_token()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(MANIFEST_API, headers=headers)
    with urllib.request.urlopen(req, timeout=40) as resp:
        payload = json.load(resp)
    content = base64.b64decode(payload["content"]).decode("utf-8")
    return json.loads(content)


def build_catalog(manifest: dict) -> dict:
    datasets = manifest.get("datasets")
    if not isinstance(datasets, dict) or not datasets:
        raise SystemExit("manifest 结构不符：缺少 datasets 字典，拒绝生成")
    entries = []
    for slug, ds in datasets.items():
        for key in ("name", "repo", "repo_url", "license"):
            if not ds.get(key):
                raise SystemExit(f"manifest 结构不符：{slug} 缺少字段 {key}")
        files = ds.get("files") or []
        entries.append({
            "slug": slug,
            "name": ds["name"],
            "repo": ds["repo"],
            "repo_url": ds["repo_url"],
            "license": ds["license"],
            "files": len(files),
            "bytes": sum(int(f.get("bytes") or 0) for f in files),
            "purpose": PURPOSE.get(slug, ""),
        })
        entries[-1]["note"] = NOTE.get(slug, "")
    entries.sort(key=lambda e: e["name"])
    return {"source": "xushan628/open-data-atlas", "source_path": "data/manifest.json",
            "generated_at": manifest.get("generated_at"), "datasets": entries}


# 需要额外说明的收录边界（事实性描述，不替上游下结论）
NOTE = {
    "thewell": "仅收录元数据（README / YAML）；本体体量远超 git 上限，按上游说明另行下载",
    "words": "manifest 标记 skipped：记录了校验和但未纳入本地库",
}


def fmt_mb(n: int) -> str:
    if n < 1024 * 1024:
        return f"{n / 1024:.0f} KB"
    return f"{n / 1024 / 1024:.1f} MB"


def license_label(license_id: str) -> str:
    if not license_id or license_id.upper() == "NOASSERTION":
        return "见上游 LICENSE"
    return license_id


def render_table(catalog: dict) -> str:
    lines = [
        "| 数据集 | 上游仓库 | 许可证 | 收录 | 能拿来做什么 |",
        "|---|---|---|---|---|",
    ]
    for d in catalog["datasets"]:
        repo_link = f"[{d['repo']}]({d['repo_url']})"
        purpose = d["purpose"] or "——"
        note = f"<br><sub>{d['note']}</sub>" if d.get("note") else ""
        lines.append(f"| **{d['name']}**{note} | {repo_link} | {license_label(d['license'])} "
                     f"| {d['files']} 个文件 · {fmt_mb(d['bytes'])} | {purpose} |")
    return "\n".join(lines)


def render_index_block(catalog: dict) -> str:
    """站点卡片用的数据块：只放卡片要展示的字段，顺序与 README 一致。"""
    rows = [{
        "name": d["name"],
        "license": "见 LICENSE" if license_label(d["license"]) == "见上游 LICENSE" else d["license"],
        "repo_url": d["repo_url"],
    } for d in catalog["datasets"]]
    payload = json.dumps(rows, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return f'<script id="atlas-datasets" type="application/json">{payload}</script>' 


def sync(check_only: bool) -> int:
    manifest = fetch_manifest()
    catalog = build_catalog(manifest)
    changed: list[str] = []

    new_json = json.dumps(catalog, ensure_ascii=False, indent=2) + "\n"
    old_json = JSON_OUT.read_text(encoding="utf-8") if JSON_OUT.exists() else ""
    if new_json != old_json:
        changed.append(str(JSON_OUT.relative_to(ROOT)))
        if not check_only:
            OUT_DIR.mkdir(parents=True, exist_ok=True)
            JSON_OUT.write_text(new_json, encoding="utf-8")

    if README.exists():
        text = README.read_text(encoding="utf-8")
        if BEGIN not in text or END not in text:
            raise SystemExit(f"{README.name} 缺少生成区标记，拒绝覆盖")
        head, rest = text.split(BEGIN, 1)
        _, tail = rest.split(END, 1)
        table = render_table(catalog)
        new_text = f"{head}{BEGIN}\n{table}\n{END}{tail}"
        if new_text != text:
            changed.append(str(README.relative_to(ROOT)))
            if not check_only:
                README.write_text(new_text, encoding="utf-8")
    else:
        print(f"· {README.relative_to(ROOT)} 不存在，跳过表格同步")

    if INDEX.exists():
        text = INDEX.read_text(encoding="utf-8")
        if BEGIN_IDX in text and END_IDX in text:
            head, rest = text.split(BEGIN_IDX, 1)
            _, tail = rest.split(END_IDX, 1)
            block = render_index_block(catalog)
            new_text = f"{head}{BEGIN_IDX}\n{block}\n{END_IDX}{tail}"
            if new_text != text:
                changed.append("docs/index.html")
                if not check_only:
                    INDEX.write_text(new_text, encoding="utf-8")
        else:
            print("· docs/index.html 缺少生成区标记，跳过站点卡片同步")
    else:
        print("· docs/index.html 不存在，跳过站点卡片同步")

    if changed:
        verb = "需要更新" if check_only else "已更新"
        print(f"{verb}: {', '.join(changed)}（{len(catalog['datasets'])} 个数据集）")
        return 1 if check_only else 0
    print(f"已是最新：{len(catalog['datasets'])} 个数据集，无需改动")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="只检查，不写文件")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    return sync(args.check)


if __name__ == "__main__":
    raise SystemExit(main())
