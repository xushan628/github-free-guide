# 文件

- [素材入库流水线（fetch_assets.py → MANIFEST.json）](asset-ingestion.md) - 从三张模块常量到 10-resources/assets/ 的逐文件落地与 MANIFEST.json 记账：contents API 优先、git/blobs 兜底、8 线程并发、分级失败语义，以及 --only 的按 path 合并与排序去重规则。
- [数据集目录同步（sync_atlas.py 与生成块）](dataset-catalog-sync.md) - 以姊妹仓库 open-data-atlas 的 data/manifest.json 为唯一输入，生成 datasets.json、10-resources/datasets/README.md 的表格区与 docs/index.html 的 atlas-datasets 数据块：结构校验、BEGIN/END 覆盖边界、幂等判定与 --check 退出码。
- [外链体检：一条链接如何被判成四态](link-health-check.md) - 拆解 scripts/verify_links.py 的判定内核——全仓 Markdown 的链接收集与去重、github.com 到 api.github.com 的改写、HEAD 退 GET 的探测阶梯、ok/dead/unverified/local 四态语义、站内相对路径的越界围栏，以及 docs/link-check.md 的报告形状与 --strict 退出码。
