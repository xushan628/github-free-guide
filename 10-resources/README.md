# 10 · 找资源：现成的图标、字体、数据

**这一组回答一个问题：我不想自己做，GitHub 上有没有能直接拿来用的东西？**

有，而且许可证干净。分两类：

| 子目录 | 是什么 | 数量 | 许可证 |
|---|---|---|---|
| [assets/](assets/README.md) | 图标、字体、插画库 | 200 个 SVG + 2 套可变字体 | MIT / ISC / OFL-1.1 |
| [datasets/](datasets/README.md) | 可直接下载的开源数据集 | 5 个（22 万行已入 SQLite） | 按各数据集 |

## 素材（assets/）

- **Tabler Icons** 106 个 + **Lucide** 94 个，覆盖常用 UI 图标；已下载进仓库，带原始许可证
- **JetBrains Mono** / **Inter** 两套可变字体（OFL-1.1）
- 每个文件的来源、SHA-256 记在 [`MANIFEST.json`](../MANIFEST.json)
- 想扩充：改 [`scripts/fetch_assets.py`](../scripts/fetch_assets.py) 里的名字列表再跑一次

## 数据（datasets/）

- 5 个上游仓库：chinese-poetry / word-atlas / exercises-dataset / countries-states-cities / the_well
- 已打成可查询的 SQLite，在线图鉴：<https://xushan628.github.io/open-data-atlas/>
- 目录由 [`scripts/sync_atlas.py`](../scripts/sync_atlas.py) 从上游 manifest 自动同步，每周跟着更新

> 更多跨期收录的素材/设计类项目见 [assets/README.md](assets/README.md)，数据类见 [datasets/README.md](datasets/README.md)。

## 项目发现：用排行榜代替一页页翻

| 榜单 | 仓库 | 许可证 | 说明 |
|---|---|---|---|
| **GitHub 中文排行榜** | [ChHsiching/GitHub-Chinese-Top-Charts](https://github.com/ChHsiching/GitHub-Chinese-Top-Charts) | GPL-3.0 | 1 个总榜 + 18 个语言分榜，每周自动同步；入选要求项目近半年有活跃，把停更的挡在门外 |

**怎么用**：想找某语言的优质中文项目，直接看对应分榜；比在 GitHub 搜索里按 star 排更干净，因为它把长期不更新的过滤掉了。

**一个要说明的坑**：视频里说的很可能是原作者 `kon9chunkit/GitHub-Chinese-Top-Charts`，但**那个仓库现在 404 了**。这里收录的是仍在维护、可访问的版本（★3k）。榜单口径与同步频率以仓库自己的说明为准，别当"权威排名"。

## 知识手册（Markdown，可直接用 Obsidian 打开）

| 项目 | 仓库 | 许可证 | 内容 |
|---|---|---|---|
| **AI 赚钱手册** | [XiaomingX/ai-money-maker-handbook](https://github.com/XiaomingX/ai-money-maker-handbook) | Apache-2.0 | 530 个文件、521 篇 Markdown，分《程序员的副业赚钱宝典》和《创业者早期的烦恼树洞》两大目录；投稿制合集，持续更新 |

**怎么用**：`git clone` 后用 Obsidian 把整个目录当 vault 打开，就是一本能全局搜索的副业笔记库。

**但必须先看清这三条**（不然很容易被带偏）：
- **它是合辑，不是教程**：内容来自投稿与转载，作者自己也在 README 里说仓库经过多次易手、部分内容已作废；
- **"AI 赚钱"类内容水很深**：里面混着付费课引流、拉人头、卖铲子的推广链接，看到"付费进群/买课"直接跳过；
- **只当索引，不当承诺**：任何"月入 X 万"的说法都没有可验证证据；涉及投资、刷单、代运营的，先假设是坑。

> 判决标准很简单：**能自己动手复现的才是方法，要你先交钱的都是生意。**

## 设计系统（当资源库用）

| 项目 | 仓库 | 许可证 | 说明 |
|---|---|---|---|
| **Astryx** | [meta/astryx](https://github.com/meta/astryx) | MIT | Meta 开源的设计系统：组件 + 设计 token，可定制、"agent ready"（配合 AI 生成界面时更容易对齐规范） | 

> 收录的是**官方 `meta/astryx`**；网上有 Svelte / Flutter 的第三方移植版，用之前确认它跟进到哪个版本。

## 用之前先看许可证

MIT / ISC / Apache-2.0 可商用；OFL 字体可嵌入但不可单卖；ODbL 有传染性；**没有 LICENSE 文件的默认不能商用**。
细节：[assets/README.md](assets/README.md) 与 [datasets/README.md](datasets/README.md)。
