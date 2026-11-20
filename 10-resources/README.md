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
| **HelloGitHub** | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | **无 LICENSE** | 每月 28 号更新的开源项目月刊，专收有趣、入门级项目——找项目练手的固定入口 |
| **cn-math-taxonomy** | [xiaoyang111222/cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy) | **NOASSERTION** | 中小学知识图谱：1644 个知识点、2403 条先修依赖、6720 道题，支持自适应诊断与静态离线运行 |

**怎么用**：想找某语言的优质中文项目，直接看对应分榜；比在 GitHub 搜索里按 star 排更干净，因为它把长期不更新的过滤掉了。

**一个要说明的坑**：视频里说的很可能是原作者 `kon9chunkit/GitHub-Chinese-Top-Charts`，但**那个仓库现在 404 了**。这里收录的是仍在维护、可访问的版本（★3k）。榜单口径与同步频率以仓库自己的说明为准，别当"权威排名"。

## 知识手册（Markdown，可直接用 Obsidian 打开）

| 项目 | 仓库 | 许可证 | 内容 |
|---|---|---|---|
| **高性价比人生指南（官方）** | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | **CC-BY-4.0** | 34 章节、数百条循证建议：金银钱、法律、健康、婚育、创业，每条标成本/收益/证据等级；有 PDF、电子书、HTML 三种版本，附生活自查页 |
> 《人生指南》另有一个第三方做的[在线阅读单页版](https://github.com/cdyforever/how-to-live-better)（★14.9k、528 条），版本落后于官方仓库，**优先看官方版**。

| **AI 赚钱手册** | [XiaomingX/ai-money-maker-handbook](https://github.com/XiaomingX/ai-money-maker-handbook) | Apache-2.0 | 530 个文件、521 篇 Markdown，分《程序员的副业赚钱宝典》和《创业者早期的烦恼树洞》两大目录；投稿制合集，持续更新 |

**怎么用**：`git clone` 后用 Obsidian 把整个目录当 vault 打开，就是一本能全局搜索的副业笔记库。

**但必须先看清这三条**（不然很容易被带偏）：
- **它是合辑，不是教程**：内容来自投稿与转载，作者自己也在 README 里说仓库经过多次易手、部分内容已作废；
- **"AI 赚钱"类内容水很深**：里面混着付费课引流、拉人头、卖铲子的推广链接，看到"付费进群/买课"直接跳过；
- **只当索引，不当承诺**：任何"月入 X 万"的说法都没有可验证证据；涉及投资、刷单、代运营的，先假设是坑。

> 判决标准很简单：**能自己动手复现的才是方法，要你先交钱的都是生意。**

## 学习与教材

| 项目 | 仓库 | 许可证 | 说明 |
|---|---|---|---|
| **microsoft/AI-For-Beginners** | [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | MIT | 微软 AI 入门课：12 周 24 课，有官方中文翻译 |
| **ChinaTextbook** | [TapXWorld/ChinaTextbook](https://github.com/TapXWorld/ChinaTextbook) | **无 LICENSE** | 小初高到大学的 PDF 教材合集；**教材版权归原出版方，仅供个人学习，别商用/二次分发** |
| **public-apis** | [public-apis/public-apis](https://github.com/public-apis/public-apis) | MIT | 50 万星免费 API 集合：开发、金融、安全、天气、加密货币等入口；**列表 MIT，各 API 有自己的条款** |

## 数据与可视化（自己起服务，不依赖第三方）

| 项目 | 仓库 | 许可证 | 说明 |
|---|---|---|---|
| **诗泉 chinese-poetry-api** | [palemoky/chinese-poetry-api](https://github.com/palemoky/chinese-poetry-api) | GPL-3.0 | 把近 40 万首唐诗宋词做成现成 API：REST + GraphQL 双接口，按作者/朝代/诗体/飞花令取诗，简繁切换，一条 Docker 起服务；也能当大模型的 RAG 知识库 |
| **江山时序** | [DeanChensj/jiangshan-map](https://github.com/DeanChensj/jiangshan-map) | GPL-3.0 | 中国历史交互地图时间轴（前 403 年至今），适合历史/古诗文群文教学 |

> 两个都是**自己跑、不上传数据**的项目；诗泉的数据底座就是本页 [datasets](datasets/README.md) 里的 chinese-poetry。

## 设计系统（当资源库用）

| 项目 | 仓库 | 许可证 | 说明 |
|---|---|---|---|
| **Astryx** | [meta/astryx](https://github.com/meta/astryx) | MIT | Meta 开源的设计系统：组件 + 设计 token，可定制、"agent ready"（配合 AI 生成界面时更容易对齐规范） | 

> 收录的是**官方 `meta/astryx`**；网上有 Svelte / Flutter 的第三方移植版，用之前确认它跟进到哪个版本。

## 用之前先看许可证

MIT / ISC / Apache-2.0 可商用；OFL 字体可嵌入但不可单卖；ODbL 有传染性；**没有 LICENSE 文件的默认不能商用**。
细节：[assets/README.md](assets/README.md) 与 [datasets/README.md](datasets/README.md)。
