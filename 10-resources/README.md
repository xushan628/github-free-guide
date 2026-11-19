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

## 用之前先看许可证

MIT / ISC / Apache-2.0 可商用；OFL 字体可嵌入但不可单卖；ODbL 有传染性；**没有 LICENSE 文件的默认不能商用**。
细节：[assets/README.md](assets/README.md) 与 [datasets/README.md](datasets/README.md)。
