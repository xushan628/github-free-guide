# 09 · 开源数据集：GitHub 上的免费数据

前 8 章讲的是 GitHub 的**功能**怎么白嫖。这一章讲它另一种被低估的用途：**GitHub 是全世界最大的免费数据仓库之一**。

很多高质量数据集的唯一官方发布渠道就是一个 GitHub 仓库 —— 没有注册墙、没有 API key、没有"申请演示"。`git clone` 下来就能用，许可证写在 `LICENSE` 文件里。

本仓库收录了 5 个，并且把它们做成了一个**能在线查、能本地跑 SQL** 的产物：[Open Data Atlas](https://xushan628.github.io/open-data-atlas/)（姊妹项目）。

---

## 数据集目录

<!-- BEGIN GENERATED: datasets -->
| 数据集 | 上游仓库 | 许可证 | 收录 | 能拿来做什么 |
|---|---|---|---|---|
| **The Well 物理模拟数据集**<br><sub>仅收录元数据（README / YAML）；本体体量远超 git 上限，按上游说明另行下载</sub> | [PolymathicAI/the_well](https://github.com/PolymathicAI/the_well) | BSD-3-Clause | 49 个文件 · 39 KB | 科学计算与 ML 训练：15 TB 级物理模拟场 |
| **chinese-poetry 中华古典诗歌** | [chinese-poetry/chinese-poetry](https://github.com/chinese-poetry/chinese-poetry) | MIT | 37 个文件 · 14.7 MB | 分词、词频、作者统计；做古典诗词检索或生成 |
| **countries-states-cities-database** | [dr5hn/countries-states-cities-database](https://github.com/dr5hn/countries-states-cities-database) | ODbL-1.0 | 3 个文件 · 11.1 MB | 国家/州/城市数据：地图、时区、人口统计 |
| **exercises-dataset 健身动作库** | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | 见上游 LICENSE | 3 个文件 · 16.6 MB | 做健身计划工具：动作、部位、器械、图示 |
| **word-atlas 词光·文字图集**<br><sub>manifest 标记 skipped：记录了校验和但未纳入本地库</sub> | [designfuchen/word-atlas](https://github.com/designfuchen/word-atlas) | 见上游 LICENSE | 3 个文件 · 7.7 MB | 词典/背单词应用：释义、例句、多语言对照 |
<!-- END GENERATED: datasets -->

> 表格由 [`scripts/sync_atlas.py`](../scripts/sync_atlas.py) 从上游 manifest 生成，每周随外链体检一起自动同步；机器可读版本见 [`datasets.json`](datasets.json)。
> 想要 star 数、字段字典、取样策略，看 [Open Data Atlas 的数据集说明](https://github.com/xushan628/open-data-atlas/blob/main/DATASETS.md)。

---

## 想直接查？别自己建库了

这 5 个数据集已被打成 12 张表、223,784 行、约 46.8 MB 的 SQLite，并做成了只读查询站：

| 入口 | 地址 |
|---|---|
| 在线图鉴（长什么样、有哪些表） | <https://xushan628.github.io/open-data-atlas/> |
| 在线 SQL 练习（15 道带答案） | <https://xushan628.github.io/open-data-atlas/sql-practice.html> |
| 许可证说明 | <https://xushan628.github.io/open-data-atlas/licenses.html> |
| 源码仓库 | <https://github.com/xushan628/open-data-atlas> |

本地跑起来（需要 Python，约 51 MB 数据）：

```bash
git clone https://github.com/xushan628/open-data-atlas
cd open-data-atlas
python scripts/fetch_data.py    # 拉数据：断点续传 + sha256 校验
python scripts/build_db.py      # 建库：data/atlas.sqlite，12 张表
python scripts/serve.py         # 起服务 → http://127.0.0.1:8790
```

Windows 下双击 `start-atlas.cmd` 也行。数据库以 `mode=ro` 打开，只允许 `SELECT / WITH / EXPLAIN`，结果上限 500 行 —— 这个"只读边界"值得抄进任何你自己做的查询服务里。

---

## 许可证：这一类最容易踩雷

数据集的许可证比代码更杂，判断规则只有一条：**看仓库里的 `LICENSE` / `NOTICE` 原文，不看 README 的一句 "free to use"**。

| 许可证 | 能商用 | 能改 | 义务 |
|---|---|---|---|
| MIT | ✅ | ✅ | 保留版权声明 |
| BSD-3-Clause | ✅ | ✅ | 保留版权声明，不能拿作者名义背书 |
| CC BY 4.0 | ✅ | ✅ | **必须署名**（作者 + 许可链接 + 是否改动） |
| ODbL-1.0 | ✅ | ✅ | **传染性**：基于它做的衍生数据库也要 ODbL 开放 |
| 仓库自带 NOTICE / 自定义 | ⚠️ | ⚠️ | 逐条读，常见"数据可研究用途，不可再分发" |

本仓库里 `countries-states-cities-database` 是 **ODbL-1.0**：如果你把它整库塞进产品对外提供服务，衍生的数据库部分需要同样开放。只做内部分析或输出统计结果不受影响。

另外两个标 `NOASSERTION` 的（`exercises-dataset`、`word-atlas`），GitHub 识别不出标准许可证，**必须逐个点开上游 LICENSE 看**。本仓库不替上游下结论。

---

## 收录标准（为什么是这 5 个）

1. **有明确许可证文件**，且允许下载与二次使用；
2. **数据在仓库里直接可取**（不是在某个网盘或需要申请的表单后面）；
3. **有实际用途**：能撑起一个项目，而不是只有几行示例；
4. **可校验**：每个文件的 git sha 与 sha256 都记录在 manifest 里，能发现上游被悄悄改动。

第 4 点尤其重要：数据集仓库被 force-push 或替换文件是常事。`open-data-atlas` 的 `data/manifest.json` 记了每个文件的 `sha256` 和抓取时间，这就是一份可审计的快照。
