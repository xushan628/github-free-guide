# GitHub 免费福利指南 · 8 个真正能白嫖的功能

> 把"GitHub 只是下代码的地方"这个用法升级成：**免费素材库 + 免费云算力 + 免费定时任务 + 免费网站 + 免费 AI 工作台**。
> 本仓库既能当清单读，也是一个**可直接运行**的模板仓库：素材已下载入库，Actions 模板可直接复制，站点已用本仓库的 `docs/` 通过 GitHub Pages 部署。

**来源说明（重要）**：本仓库的内容依据是抖音视频《GitHub 白嫖指南》的公开简介与章节索引（素材检索 / 在线工具 / 本地 AI / Actions / Pages / 学生包 / 避坑）。
视频正文无法直接抓取解析，因此章节是对索引的**工程化重建**：不编造视频原话，每条资源都实测可达、许可证可查、额度以官方文档为准。

---

## 8 个功能速览

| # | 功能 | 一句话价值 | 免费额度（个人账号） | 入口 |
|---|------|-----------|---------------------|------|
| 1 | 免费商用素材 | 图标 / 字体 / 插画 / 头像，不用再怕版权 | 无限（按各库许可证） | [01-assets](01-assets/README.md) |
| 2 | 在线轻工具 | 格式转换、PDF、图片、编码，浏览器即可 | 无限 | [02-tools](02-tools/README.md) |
| 3 | 开源本地 AI | 本地跑大模型、免代码 AI 工作流 | 无限（吃自己显卡） | [03-ai](03-ai/README.md) |
| 4 | GitHub Actions | 云端跑脚本，**定时任务免挂机** | 公开仓库不限时长；私有仓库 2000 分钟/月 | [04-actions](04-actions/README.md) |
| 5 | GitHub Pages | 静态网站 / 博客 / 文档，零成本托管 | 100 GB 流量/月、1 GB 站点、10 次构建/小时 | [05-pages](05-pages/README.md) |
| 6 | GitHub Codespaces | 云端 VS Code，开箱即用的开发环境 | 120 core-hours/月 + 15 GB-month 存储 | [06-codespaces](06-codespaces/README.md) |
| 7 | Student Developer Pack | 学生认证后一大票商业工具免费用 | 需学生身份，有效期最长至毕业 | [07-student-pack](07-student-pack/README.md) |
| 8 | 额度与避坑 | 免费额度的真实边界 + 4 个高频陷阱 | —— | [08-limits](08-limits/README.md) |

> 额度数字会变。**以 `08-limits` 里的官方文档链接为准**，本仓库的表格只做速查。

---

## 这个仓库里已经有什么（真下载了，不是链接堆）

| 内容 | 数量 | 许可证 | 位置 |
|------|------|--------|------|
| Tabler 图标（SVG） | 106 个 | MIT | `01-assets/icons/tabler/` |
| Lucide 图标（SVG） | 94 个 | ISC | `01-assets/icons/lucide/` |
| JetBrains Mono 可变字体 | 1 个（183 KB） | OFL-1.1 | `01-assets/fonts/` |
| Inter 可变字体 | 1 个（856 KB） | OFL-1.1 | `01-assets/fonts/` |
| 原始许可证文本 | 4 份 | —— | `01-assets/LICENSES/` |

每个文件的来源仓库、上游路径、字节数、SHA-256、许可证，全部记在 [`MANIFEST.json`](MANIFEST.json) 里，可校验：

```bash
python scripts/fetch_assets.py      # 重下 / 补齐（幂等，自动更新 MANIFEST）
# 校验示例（Windows）
certutil -hashfile "01-assets/fonts/Inter[opsz,wght].ttf" SHA256
```

素材只用 API 下载（`api.github.com` → `git/blobs`），不依赖 `raw.githubusercontent.com`，在受限网络下也能跑。详见 [`scripts/fetch_assets.py`](scripts/fetch_assets.py)。

---

## 三步上手

**第 1 步：拿模板（不用会 git）**

- 在 GitHub 网页上点 `Use this template`（本仓库是模板仓库）或直接 `Fork`；

**第 2 步：白嫖云端定时任务（Actions）**

把 [`04-actions/templates/cron-job.yml`](04-actions/templates/cron-job.yml) 复制到你自己仓库的 `.github/workflows/` 下，改两行（`cron` 表达式 + 要跑的命令），提交即生效。
不需要服务器、不需要一直开着电脑，每天定时跑，跑完还能自动提交结果回仓库。

**第 3 步：白嫖个人网站（Pages）**

仓库 `Settings → Pages → Source: Deploy from a branch → Branch: main / docs`，几十秒后你就有了 `https://<你的用户名>.github.io/<仓库名>/`。
本仓库的 [`docs/index.html`](docs/index.html) 就是一个可直接用的站点，单文件、零依赖、移动端适配。

---

## 仓库结构

```
github-free-guide/
├─ 01-assets/        免费商用素材（已下载：图标 200 / 字体 2 / 许可证 4）
├─ 02-tools/         在线轻工具与格式转换
├─ 03-ai/            开源本地 AI 模型 + 免代码工作流
├─ 04-actions/       Actions 免费算力 / 定时任务模板
├─ 05-pages/         免费建站方案
├─ 06-codespaces/    免费云开发环境
├─ 07-student-pack/  学生包申请与权益
├─ 08-limits/        免费额度速查 + 4 个坑
├─ docs/             ← GitHub Pages 站点源（已部署）
├─ scripts/          fetch_assets / verify_links / deploy_github
├─ .github/workflows 本仓库每周自动跑的外链体检 workflow
└─ MANIFEST.json     全部素材的来源 / 许可证 / SHA-256
```

---

## 三条硬性原则（避免踩坑）

1. **只收"可商用"的许可证**：MIT / ISC / Apache-2.0 / OFL / CC0 才进本仓库。GPL 类会传染，AGPL 更严格，商用前必须看清。
2. **不信"免费"两个字，信额度表**：Actions 分钟数按**私有仓库**计费，公开仓库不计费但滥用会被封；Pages 有 10 次/小时构建限制。
3. **凭据永不上传**：`.gitignore` 已排除 `.env`、`*.pem`、`github_token*`。仓库公开后，任何一次误提交都等于公开泄露，且会被爬虫秒抓。

详细坑位见 [08-limits/README.md](08-limits/README.md)。

---

## 许可证

- 本仓库自有内容（文档、脚本、站点）：MIT，见 [LICENSE](LICENSE)。
- `01-assets/` 下的素材：**分别**适用各自上游许可证，见 `01-assets/LICENSES/` 与 `MANIFEST.json`。使用时请保留原许可证与版权声明。
- 本仓库与 GitHub、Microsoft 无隶属关系，为个人整理。

## 维护

```bash
python scripts/verify_links.py     # 外链体检 → docs/link-check.md
python scripts/fetch_assets.py     # 素材补齐
```

外链体检已配置为每周自动运行：见 [.github/workflows/link-check.yml](.github/workflows/link-check.yml)。
