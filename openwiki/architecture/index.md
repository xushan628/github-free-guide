# 文件

- [仓库全景：内容分组、站点与自动化脚本](repository-map.md) - 一页说清本仓库四类资产（手写内容目录、脚本生成的产物、Python 自动化脚本、CI 工作流与 docs 站点）的职责边界与数据流方向，并标明哪些文件由脚本生成、不可手改，帮助 agent 判断一次改动该落在哪个系统。
- [静态站点（docs/ 单页应用与页面契约）](static-site.md) - docs/index.html 的运行时结构：内联 DATA 的十五个分类卡片、由生成块注入的 atlas-datasets JSON 与其驱动的数据集计数、搜索与分类 pill 的过滤规则、esc 转义与 repo_url/dl 的拼接约定，以及 404 兜底、.nojekyll 与 main:/docs 部署契约。
