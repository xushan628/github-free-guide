# 文件

- [内容分类法：唯一分类轴「你想干什么」](content-taxonomy.md) - 说明本仓库六个内容目录如何按「你想干什么」这一条轴划分、编号与命名遵循什么规则、README 组内导航与 projects.md 跨期精选如何分层，以及 60-others 兜底区和 pending.md 待核实清单的收录与补录规则。
- [条目约定：表格列、来源标注与「坑」章节](entry-conventions.md) - 一条项目条目的标准写法：五列表格（项目 / 仓库 / 许可证 / 干什么 / 来源）、许可证加粗的信号、来源列的溯源语义、站内「只做索引」推导出的下载入口写法，以及为何「数字会变」免责声明与「坑」章节必须保留、改动为何常要同时落在 Markdown 与 docs/index.html 两处。
- [许可证与风险边界](licensing-and-risk-policy.md) - 本仓库的收录决策规则：白名单只约束「真把文件拷进来」的托管层，GPL/AGPL 与 ODbL 如何标注，无 LICENSE 与 NOASSERTION 为何一律回落到「见上游 LICENSE」，灰产与高危工具为何单独警告，以及 sync_atlas.py 与 fetch_assets.py 如何把这些规则写进代码、MANIFEST 与下架响应。
- [示例即产品：可复用模板与自举示例](reference-artifacts.md) - 仓库里有一类文件不是给人读的，而是给人复制走的——40-ship/actions/templates 的三个 workflow、30-ai/install/install-ollama.sh 与文档内嵌的 YAML 片段；它们与仓库自己运行的 .github/workflows 构成「对外示例」，因此 TODO 占位、UTC cron、permissions 等约束不能删，改完还必须自己验证语法与复制步骤。
