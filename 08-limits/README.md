# 08 · 免费额度速查 + 4 个最容易踩的坑

白嫖的前提是**不越界**。这一章是"别被封号"的说明书。

---

## 一、免费额度速查表（个人 Free 账号）

| 资源 | 免费额度 | 关键限制 | 官方文档 |
|------|---------|---------|---------|
| 仓库 | 无限公开 + 无限私有 | 单文件 100 MB，仓库建议 < 1 GB | [docs.github.com](https://docs.github.com/repositories/creating-and-managing-repositories/about-repositories) |
| Actions（公开仓库） | 不限时长 | 单 job ≤ 6 小时，遵守公平使用 | [计费说明](https://docs.github.com/billing/managing-billing-for-your-products/about-billing-for-github-actions) |
| Actions（私有仓库） | 2,000 分钟/月 | Windows 2×、macOS 10× 倍率 | 同上 |
| Artifacts / Packages 存储 | 500 MB | 超出需付费 | 同上 |
| Pages | 1 GB 站点 / 100 GB 流量/月 | 10 次构建/小时，仅静态 | [Pages 限制](https://docs.github.com/pages/getting-started-with-github-pages/github-pages-limits) |
| Codespaces | 120 core-hours + 15 GB-month | 空闲 30 分钟自动停 | [Codespaces 计费](https://docs.github.com/billing/managing-billing-for-your-products/about-billing-for-github-codespaces) |
| Copilot | Free 档有限次数 | 学生/开源维护者可全免 | [Copilot 计划](https://docs.github.com/copilot/about-github-copilot/plans-for-github-copilot) |
| Gist | 无限（公开+私密） | 单文件 100 MB | [Gist 文档](https://docs.github.com/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists) |
| Discussions / Wiki / Issues | 无限 | —— | —— |

> 表格是速查，**数字会变**。真要下单前点最后一列核对。

---

## 二、4 个高频坑（视频里点名的"权限与额度陷阱"）

### 坑 1：Actions 默认是只读权限，`git push` 静默失败

2023 年起新仓库的 `GITHUB_TOKEN` 默认只有 `contents: read`。脚本跑完想提交结果，会报 403。

```yaml
# 必须在 workflow 顶层显式声明
permissions:
  contents: write
```

**更隐蔽的版本**：`push` 成功了但**没有触发后续 workflow**——因为 `GITHUB_TOKEN` 推的提交不会触发新流程（防递归）。需要连锁触发就用 PAT（Personal Access Token）。

---

### 坑 2：`cron` 是 UTC，你的"每天 8 点"实际是下午 4 点

GitHub 的 `schedule.cron` 一律按 **UTC** 解析，没有时区参数。

| 北京时间 | 应写 |
|---------|------|
| 08:00 | `0 0 * * *` |
| 12:00 | `0 4 * * *` |
| 20:00 | `0 12 * * *` |
| 22:30 | `30 14 * * *` |

另外：定时任务**可能延迟几分钟到几十分钟**，不要用它做精确计时；仓库 **60 天无活动会自动停用定时 workflow**。

---

### 坑 3：密钥泄露 —— 最贵的免费

一旦提交进公开仓库，**几秒内就会被爬虫抓走**（GitHub 上有实时扫 token 的机器人），删掉提交也没用，历史还在。

三个必做动作：

```gitignore
# .gitignore 里必须有
.env
.env.*
*.pem
*.key
github_token*
secrets.*
```

```bash
# 提交前自查（能扫出常见密钥格式）
git diff --cached | grep -iE 'ghp_|gho_|github_pat_|sk-|AKIA|BEGIN .*PRIVATE KEY'
```

**已经泄露了怎么办**：立刻去对应平台**吊销 token**（不是改密码），然后 `git filter-repo` 清理历史。吊销永远排第一，清理历史排第二——因为爬虫比你先跑。

---

### 坑 4：许可证误用 —— "免费"不等于"能商用"

| 许可证 | 能商用 | 能闭源分发 | 注意 |
|--------|-------|-----------|------|
| MIT / ISC / BSD | ✅ | ✅ | 保留版权声明 |
| Apache-2.0 | ✅ | ✅ | 保留 NOTICE，含专利授权 |
| OFL（字体） | ✅ | ✅ | 字体本身不能单独卖，保留版权 |
| CC0 | ✅ | ✅ | 几乎无限制 |
| GPL-2.0 / 3.0 | ✅ | ❌ 传染 | 你分发就必须开源 |
| AGPL-3.0 | ✅ | ❌ 更强 | **提供网络服务也算分发**（SaaS 也会被要求开源） |
| CC-BY-NC | ❌ | ❌ | 非商用，最容易踩雷 |
| 无 LICENSE 文件 | ❌ | ❌ | **默认保留所有权利**，不能当免费素材用 |

**最容易出事的场景**：从某仓库拿了一套图标做进公司产品，仓库 README 写 "free icons"，实际图标子目录另有 CC-BY-NC 许可。

> 记住：**没有 LICENSE 文件 = 不能商用**。这是版权法的默认规则，不是 GitHub 的规则。

---

## 三、被限流/封号前会有什么信号

- Actions 莫名排队很久、job 直接 `cancelled`
- Pages 部署失败提示 "build failed, rate limit"
- API 返回 `403 rate limit exceeded`（未认证 60 次/小时，认证 5,000 次/小时）
- 收到 GitHub 邮件警告 "your account is being rate limited"

**应对**：降低频率、加缓存、把频繁任务合并、别用 Actions 挖矿或跑持续高负载。

---

## 四、一句话原则

> 白嫖的边界是**别给别人添成本**：不改公开仓库的历史、不刷免费额度、不把免费服务当生产基础设施。
> 在这个边界内，GitHub 给的额度基本用不完。
