---
type: quickstart
title: 快速上手：这套 wiki 怎么用
description: 任务路由页：按「改内容 / 改脚本 / 查外链 / 发站点 / 排查 CI」给出最短阅读路径、涉及的关键文件与可复制的验证命令及退出码语义，是进入 architecture / concepts / workflows / integrations / operations / testing 各层的入口。
tags: [quickstart, navigation, task-routing, verification, maintenance]
verified:
  - by: openwiki/0.9.0
    at: 2026-11-21T01:55:26.634Z
sources:
  - id: openwiki-source-73d7f0054cd50abf1b343d3b
    resource: repo://docs/index.html
  - id: openwiki-source-2f7710207dbb0c4ab6afe92b
    resource: repo://docs/link-check.md
  - id: openwiki-source-23775c3de52f3ab95a13cb8b
    resource: repo://README.md
  - id: openwiki-source-abd1dd6f19ca6c611fb8988e
    resource: repo://scripts/check_site.py
  - id: openwiki-source-87e786eea03e086a744a0567
    resource: repo://scripts/deploy_github.py
  - id: openwiki-source-119b583b5a56d22bae02cc6e
    resource: repo://scripts/gh_auth.py
  - id: openwiki-source-443d2e3693c0855ededcfee1
    resource: repo://scripts/sync_atlas.py
  - id: openwiki-source-4a863e259025d7e3327a396d
    resource: repo://scripts/verify_links.py
generated: { by: "openwiki/0.9.0", at: "2026-11-21T01:55:26.634Z" }
---

# 快速上手：这套 wiki 怎么用

**这个仓库不是应用代码。** 它是「内容仓库 + 自动化脚本」：六个中文内容目录（`10-resources` … `60-others`）是正本，`scripts/` 下 6 个 Python 文件负责抓素材、同步数据集、体检外链、纯 API 发布、诊断线上站点，`docs/` 是一个手写维护的单页站点，`.github/workflows/` 的两个工作流把其中两个脚本挂到定时任务上。没有依赖安装、没有构建步骤、没有测试框架——**「验证」这件事完全由脚本自带的开关承担**（`--strict` / `--check` / `--dry-run` / `check_site.py`）。

本页只做一件事：按你要做的事，把你送到对应页面。

## 先分清两类改动，风险面完全不同

| | 改内容 | 改脚本 |
|---|---|---|
| 典型动作 | 加一条项目、改一段说明、补一个坑位 | 改 `scripts/*.py`、改 `.github/workflows/*.yml`、改生成区逻辑 |
| 危险在哪 | 内容散落在「成对位置」：条目在分组 `.md` 里，卡片在 `docs/index.html` 的 `DATA`（手写）里，页头数字与卡片 `tags` 的「N 个」也要同步 | 会重写生成产物：`MANIFEST.json`、`10-resources/datasets/` 三处、`docs/link-check.md` |
| 验收 | `python scripts/verify_links.py --strict` 退出码 0 + 本地打开 `docs/index.html` 看卡片/搜索/下载 | 脚本自检开关 + `git diff` 逐字看生成物差异 |
| 入口 | [内容分类法](concepts/content-taxonomy.md)、[条目约定](concepts/entry-conventions.md) | [仓库全景](architecture/repository-map.md)、[验证手段](testing/validation-harness.md) |

一条硬边界先记住：`MANIFEST.json`、`10-resources/datasets/` 下的文件、`docs/link-check.md`，以及两处 `<!-- BEGIN GENERATED: … -->` 区块都由脚本写。手改要么被下次运行覆盖，要么让脚本直接拒写。

## 按「我要做什么」找路径

| 我要做什么 | 先读（按顺序） | 关键文件 | 验收信号 |
|---|---|---|---|
| 加 / 改一条项目条目 | [内容分类法](concepts/content-taxonomy.md) → [条目约定](concepts/entry-conventions.md) | 目标分组的分期表（`20-tools/projects.md`、`30-ai/projects.md`、`60-others/README.md` 之一）；`docs/index.html` 的 `DATA` 与页头数字 | `verify_links.py --strict` 退出 0；页面卡片、搜索、下载链接都正常 |
| 判断「这条该不该收、放哪」 | [内容分类法](concepts/content-taxonomy.md) → [许可证与风险边界](concepts/licensing-and-risk-policy.md) | `60-others/pending.md`（待核实清单）、`MANIFEST.json` 里的 `license` 字段 | 分级归属明确；无 LICENSE / NOASSERTION 的写成「见上游 LICENSE」并留警告 |
| 补图标 / 字体 / 许可证素材 | [素材入库流水线](workflows/asset-ingestion.md) | `scripts/fetch_assets.py` 的 `ICON_NAMES` / `FONTS` / `LICENSES`、`MANIFEST.json` | `fetch_assets.py --only icons`（或 `fonts` / `licenses`）跑完；`git diff MANIFEST.json` 有对应 `path` 与 `sha256` |
| 同步数据集目录 | [数据集目录同步](workflows/dataset-catalog-sync.md) | 上游 `open-data-atlas` 的 `data/manifest.json`（正本）、`scripts/sync_atlas.py`、两处生成区 | `sync_atlas.py --check` 退出 1 = 需要更新，再跑一次不带 `--check` 的 |
| 查死链 / 改体检策略 | [外链体检](workflows/link-health-check.md) → [仓库自己的 CI](operations/ci-workflows.md) | `scripts/verify_links.py`、`docs/link-check.md`（只读报告）、`link-check.yml` 的 `push.paths` | `verify_links.py --strict` 退出 0；❌ 表清空 |
| 改站点卡片 / 样式 / 页头 | [静态站点](architecture/static-site.md) | `docs/index.html`（生成区之外）、`docs/404.html`、`docs/disclaimer.html`、`docs/.nojekyll` | 本地打开页面看渲染；线上异常用 `check_site.py` 诊断 |
| 发布 / 推送（`git` 出不了网时） | [发布与部署](operations/publishing-and-deploy.md) → [GitHub API 通道与凭据](integrations/github-api-transport.md) | `scripts/deploy_github.py`、`scripts/gh_auth.py` | `deploy_github.py --dry-run` 的文件清单里没有 `.env` / `*.pem` / `github_token*` |
| 排查 CI 没跑 / 跑红 / 站点忽新忽旧 | [仓库自己的 CI](operations/ci-workflows.md) → [验证手段](testing/validation-harness.md) | `.github/workflows/link-check.yml`、`.github/workflows/openwiki-update.yml` | 用 `workflow_dispatch` 手动重跑；`push.paths` 不匹配写回提交里的文件 |
| 配 token / 换凭据 | [GitHub API 通道与凭据](integrations/github-api-transport.md) | `scripts/gh_auth.py`、`.gitignore` | 环境变量 `GITHUB_TOKEN` 生效；凭据不进磁盘、不进仓库 |
| 改对外示例（模板 / 安装脚本） | [示例即产品](concepts/reference-artifacts.md) | `40-ship/actions/templates/`、`30-ai/install/` | 复制走能在别人仓库直接跑通 |
| 走一遍每周维护循环 | [维护手册](operations/maintenance-runbook.md) | 上面所有涉及文件 | 见该页的「每周循环」表 |

几个容易误判的点：`40-ship/actions/templates/*.yml` 是**给人复制的示例**，真正在跑的工作流只有 `.github/workflows/` 下那两个；`docs/link-check.md` 是脚本产物，修死链要改条目所在的 `.md`，不是改报告。

## 可复制的验证命令

```bash
# 1) 外链 + 站内相对链接体检，整份重写 docs/link-check.md
python scripts/verify_links.py
python scripts/verify_links.py --strict     # 有 dead 链接时退出码 1

# 2) 数据集目录是否最新（只读不写）
python scripts/sync_atlas.py --check        # 有差异退出码 1
python scripts/sync_atlas.py                # 真同步，最多改 3 个文件

# 3) 发布预演：解析凭据后立刻打印待推送清单并退出，不发任何 API 写请求
python scripts/deploy_github.py --dry-run

# 4) 从你自己的网络体检线上 Pages（可传 URL 覆盖默认站点）
python scripts/check_site.py
```

| 命令 | 退出码语义 | 副作用 | 出网目标 |
|---|---|---|---|
| `verify_links.py` | 默认**总是 0**；`--strict` 且存在 `dead` 才 1 | 整份重写 `docs/link-check.md`（含 UTC 时间戳，所以每周必有一次提交） | `github.com/<owner>/<repo>` 与 `/blob/` 链接被改写成 `api.github.com/repos/...`、`contents/...`；其他 http(s) 仍请求原地址，`HEAD` 失败退 `GET` |
| `sync_atlas.py --check` | 需要更新 = 1，最新 = 0；上游 manifest 结构不符则 `SystemExit` | 不写文件 | 拉 `api.github.com` 上 `xushan628/open-data-atlas` 的 `contents/data/manifest.json`——**`--check` 不是离线检查** |
| `deploy_github.py --dry-run` | 成功 0 | 不写文件、不发 API 写请求（只打印，最多 200 个路径） | 先 `resolve_token()`；无凭据时 `SystemExit`，所以「能跑 dry-run」本身就等于凭据可用 |
| `check_site.py` | 0 正常 / 1 站点缺失或 HTTP 异常 / 2 连不上 | 无 | **唯一不碰 `api.github.com` 的命令**：直接请求 `https://xushan628.github.io/github-free-guide/`，复现读者视角 |

三条通用事实：所有脚本用 `Path(__file__).resolve().parent.parent` 定位仓库根，从任何目录调用都行；GitHub 访问统一走 `api.github.com`（本机直连 `github.com` 会被重置），token 来自 `GITHUB_TOKEN` / `GH_TOKEN` 环境变量，其次 Windows 凭据管理器，不落盘不打印；`verify_links.py` 与 `sync_atlas.py` 都会改工作区，跑完全套后用 `git status` 分清哪些是产物漂移、哪些是你的手动改动。

## 一个会静默出错的坑

两处生成区标记的失败语义**不对称**：`10-resources/datasets/README.md` 缺 `<!-- BEGIN GENERATED: datasets -->` / `<!-- END GENERATED: datasets -->` 时脚本 `SystemExit` 拒写（硬失败，CI 变红）；`docs/index.html` 缺 `<!-- BEGIN GENERATED: atlas-items -->` / `<!-- END GENERATED: atlas-items -->` 时只打印一句「跳过站点卡片同步」就继续（静默降级，退出码通常还是 0）。结果是「数据集表格更新了、站点卡片永远不动」这种漂移长期潜伏——重排 `index.html` 时先确认两行标记还在原位。完整清单见 [验证手段](testing/validation-harness.md)。

## 六层索引：想深挖就去对应层

| 层 | 回答什么 |
|---|---|
| [architecture](architecture/repository-map.md) | 仓库哪四类资产、谁生成谁只读、改动该落在哪个系统；站点（[static-site](architecture/static-site.md)）的页面契约与 Pages 部署面 |
| [concepts](concepts/content-taxonomy.md) | 为什么只有一条分类轴、条目怎么写（[entry-conventions](concepts/entry-conventions.md)）、收录的许可证与风险边界（[licensing-and-risk-policy](concepts/licensing-and-risk-policy.md)）、[示例即产品](concepts/reference-artifacts.md) |
| [workflows](workflows/asset-ingestion.md) | 三条自动化流水线：素材入库 → `MANIFEST.json`（[asset-ingestion](workflows/asset-ingestion.md)）、数据集同步 → 两处生成区（[dataset-catalog-sync](workflows/dataset-catalog-sync.md)）、外链体检 → 报告（[link-health-check](workflows/link-health-check.md)） |
| [integrations](integrations/github-api-transport.md) | 所有出网行为的共同底座：只走 `api.github.com`、凭据两级回退、统一请求头/API 版本、重试与限流等待 |
| [operations](operations/maintenance-runbook.md) | 每周循环与改动清单（[maintenance-runbook](operations/maintenance-runbook.md)）、两个工作流的触发与写回（[ci-workflows](operations/ci-workflows.md)）、纯 API 发布与站点诊断（[publishing-and-deploy](operations/publishing-and-deploy.md)） |
| [testing](testing/validation-harness.md) | 没有单测时拿什么证明改动安全：各脚本自检开关、生成区守卫、每类改动最易静默失败的坑 |

如果只想记一句话：**改内容盯「成对位置」，改脚本盯「生成产物」，两边都用脚本自检开关而不是肉眼验收。**
