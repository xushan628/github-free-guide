# 文件

- [仓库自己的 CI：外链体检与 OpenWiki 更新](ci-workflows.md)
- [维护手册：每周循环与常见改动路径](maintenance-runbook.md) - 把日常维护落成可执行清单——每周机器跑什么、人要看什么，新增条目 / 补素材 / 同步数据集 / 改站点卡片 / 修死链分别触及哪些文件、按什么顺序跑哪条命令、拿什么判据验收，以及不可手改的生成产物、三组必须成对更新的位置与定时任务、密钥、部署的运维底线。
- [发布与部署（deploy_github.py、Pages 与 check_site.py）](publishing-and-deploy.md) - 不依赖 git 客户端的发布路径与线上验收：Git Data API 的 blob→tree→commit→ref 流程、空仓库引导为何必须先跑、--dry-run/--squash 语义与 iter_files 和 .gitignore 的落差，以及 check_site.py 的四类结论、退出码与 Pages 的缓存延迟和 10 次/小时构建限制。
