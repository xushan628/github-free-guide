# GitHub 免费福利指南 · 按功能分类

> 把 GitHub 当成：免费资源库 + 免费云算力 + 免费托管 + 免费 AI 工作台。
> **分类轴只有一条：你想干什么。** 暂时归不了类的，统一放 [60-others](60-others/README.md)，不硬塞。

**姊妹项目**：[Open Data Atlas](https://xushan628.github.io/open-data-atlas/) —— 本仓库「找资源」里的 5 个数据集，被打成了可在线查询的 SQLite 图鉴。

---

## 按功能找（5 组）

| 我想… | 去哪 | 里面有什么 |
|---|---|---|
| 🎨 **找现成的资源** | [10-resources](10-resources/README.md) | 200 个图标、2 套开源字体、5 个开源数据集 |
| 🧰 **用现成的工具** | [20-tools](20-tools/README.md) | IT-Tools、CyberChef、Stirling-PDF、DBX… 在线即用或一条 Docker 起服务 |
| 🧠 **用 AI 干活** | [30-ai](30-ai/README.md) | Ollama 本地模型、n8n/Dify 工作流、港大 DeepTutor 私人 AI 家教 |
| 🚀 **让它自动跑 / 上线** | [40-ship](40-ship/README.md) | Codespaces 写代码 → Actions 定时跑 → Pages 发布成网站 |
| 💰 **少花钱、别犯规** | [50-benefits](50-benefits/README.md) | 学生开发者大礼包、免费额度速查、4 个高频陷阱 |
| 🗃️ **其他** | [60-others](60-others/README.md) | 暂时没有功能归属的（OpenStock 行情看板、ziwei-doushu 命理排盘），攒够了再拆新组 |

---

## 仓库结构

```
github-free-guide/
├─ 10-resources/          找资源
│  ├─ assets/             200 图标 + 2 套字体 + 原始许可证
│  └─ datasets/           5 个开源数据集目录（自动同步上游）
├─ 20-tools/              用工具（projects.md：跨期精选）
├─ 30-ai/                 用 AI（含 DeepTutor 案例、Ollama 安装脚本、projects.md 精选）
├─ 40-ship/               自动化与上线
│  ├─ actions/            定时任务模板（3 个可直接复制）
│  ├─ pages/              建站三种方式
│  └─ codespaces/         免费云开发环境
├─ 50-benefits/           省钱与避坑
│  ├─ student-pack/       学生包申请与权益
│  └─ limits/             免费额度速查 + 4 个坑
├─ 60-others/             其他项目（暂未归类，后续再分）
├─ docs/                  ← GitHub Pages 站点源（已部署）
├─ scripts/               fetch_assets / verify_links / deploy_github / check_site / sync_atlas
├─ .github/workflows      每周外链体检 + 数据集同步
└─ MANIFEST.json          素材的来源 / 许可证 / SHA-256
```

---

## 三条硬性原则

1. **只收可商用的许可证**：MIT / ISC / Apache-2.0 / OFL / CC0 才进本仓库；GPL/AGPL 会传染，单独标注。
2. **不信"免费"两个字，信额度表**：Actions 私有仓库按时长计费，Pages 有构建次数限制。
3. **凭据永不上传**：`.gitignore` 已排除 `.env`、`*.pem`、`github_token*`。

详细坑位见 [50-benefits/limits](50-benefits/limits/README.md)。

---

## 许可证

- 本仓库自有内容（文档、脚本、站点）：MIT，见 [LICENSE](LICENSE)。
- `10-resources/assets/` 下的素材分别适用上游许可证，见该目录 `LICENSES/` 与 `MANIFEST.json`。
- 与 GitHub、Microsoft 无隶属关系，个人整理。

## 维护

```bash
python scripts/verify_links.py     # 外链 + 站内链接体检 → docs/link-check.md
python scripts/fetch_assets.py     # 素材补齐（写 MANIFEST.json）
python scripts/sync_atlas.py       # 同步数据集目录
python scripts/check_site.py       # 从你的网络体检线上站点
python scripts/deploy_github.py    # 纯 API 推送（本机 git 无法出网时用）
```
