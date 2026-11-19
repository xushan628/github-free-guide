# 40 · 自动化与上线：让它自己跑，把东西发到公网

**这一组回答：我不想一直开着电脑，也不想买服务器。**

三个子指南，正好是一条流水线：

| 步骤 | 子目录 | 解决什么 |
|---|---|---|
| ① 写代码 | [codespaces/](codespaces/README.md) | 浏览器里的完整开发环境，120 core-hours/月 |
| ② 定时跑 | [actions/](actions/README.md) | 免费云端自动化，cron 定时任务免挂机 |
| ③ 发出去 | [pages/](pages/README.md) | 静态站点托管，1 GB / 100 GB 月流量 |

## 典型组合

```
Codespaces 里写完 → Actions 每天定时跑（抓数据/构建）
                  → Pages 自动发布成网站
```

本站就是这条链路做出来的：`docs/` 是页面，Pages 从 `main:/docs` 构建，`link-check.yml` 每周自动体检外链并提交。

## 各自的免费边界

- **Actions**：公开仓库不限时长；私有仓库 2000 分钟/月；单 job 上限 6 小时；**cron 是 UTC**
- **Pages**：1 GB 站点、100 GB 月流量、10 次构建/小时；**只能静态**
- **Codespaces**：120 core-hours + 15 GB-month；空闲 30 分钟自动停

坑位细节见 [50-benefits/limits](../50-benefits/limits/README.md)。
