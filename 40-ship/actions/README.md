# 04 · GitHub Actions：免费云端算力 + 定时任务（免挂机）

这是视频里"**每日免服务器定时运行脚本**"的那一段。你不需要买服务器、不需要一直开电脑：把脚本丢进仓库，写个时间表，GitHub 用它的机器帮你跑。

---

## 免费额度（个人账号）

| 项目 | 公开仓库 | 私有仓库（Free 计划） |
|------|---------|---------------------|
| 计算时长 | **不限**（公平使用原则） | 2,000 分钟/月 |
| 单 job 最长 | 6 小时 | 6 小时 |
| 并发 job | 20 | 20 |
| 缓存 | 10 GB/仓库 | 10 GB/仓库 |
| 存储（产物/包） | 500 MB（Free） | 500 MB |

> 公开仓库"不限"≠"随便刷"：挖矿、持续高强度跑会被限制甚至封号。正当用途（每天跑几分钟的采集/构建/通知）几乎不会踩线。
> 额度会调整，以 [GitHub 官方计费文档](https://docs.github.com/billing/managing-billing-for-your-products/about-billing-for-github-actions) 为准。

**Windows / macOS runner 按 2× / 10× 倍率计费，Linux 是 1×。** 白嫖就选 `ubuntu-latest`。

---

## 最小可用例子：每天定时跑一次

复制 [`templates/cron-job.yml`](templates/cron-job.yml) 到你仓库的 `.github/workflows/` 下，改三处：

```yaml
on:
  schedule:
    - cron: "0 22 * * *"   # ① 时间（UTC！22:00 UTC = 次日 06:00 北京时间）
jobs:
  run:
    runs-on: ubuntu-latest # ② Linux 最便宜
    steps:
      - run: python main.py  # ③ 换成你的命令
```

**cron 一律按 UTC 算**，这是新手第一个坑：

| 你想要 | 北京时间的写法 | 对应的 cron |
|--------|--------------|------------|
| 每天 08:00 | 00:00 | `0 0 * * *` |
| 每天 20:00 | 12:00 | `0 12 * * *` |
| 每小时 | —— | `0 * * * *` |
| 每周一 09:00 | 01:00 周一 | `0 1 * * 1` |
| 每 15 分钟 | —— | `*/15 * * * *` |

> 定时任务**不保证准点**：高峰期可能延迟几分钟到几十分钟（GitHub 明确说明 scheduled workflow 可能被延后）。做"每天一次"够用，做"精确到秒的定时器"不行。

---

## 三个高频玩法

### 1. 每天抓数据 → 自动提交回仓库（本仓库的邻居项目就是这么跑的）

```yaml
permissions:
  contents: write          # 必须显式给写权限（2023 年后默认只读）
steps:
  - uses: actions/checkout@v4
  - run: python scrape.py
  - run: |
      git config user.name "github-actions[bot]"
      git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
      git add data/
      git commit -m "chore: 采集数据 $(date -u +%F)" || echo "无变化"
      git push
```

### 2. 定时给手机发通知（把 Actions 当免费 cron + 免费短信）

```yaml
- name: 推送
  env:
    WEBHOOK: ${{ secrets.FEISHU_WEBHOOK }}
  run: |
    curl -s -X POST "$WEBHOOK" -H 'Content-Type: application/json' \
      -d '{"msg_type":"text","content":{"text":"✅ 今日任务完成"}}'
```

密钥放 `Settings → Secrets and variables → Actions`，**永远不要写进 YAML**。见 [50-benefits/limits](../../50-benefits/limits/README.md)。

### 3. 手动触发的参数化任务

```yaml
on:
  workflow_dispatch:
    inputs:
      target:
        description: "要处理的仓库"
        required: true
        default: "ollama/ollama"
```

之后在 Actions 页面点 `Run workflow` 填参数即可，手机上也能点。

---

## 可用的模板

| 文件 | 用途 |
|------|------|
| [`templates/cron-job.yml`](templates/cron-job.yml) | 定时跑脚本 + 自动提交结果回仓库 |
| [`templates/manual-run.yml`](templates/manual-run.yml) | 手动触发 + 参数 + 产物上传 |
| [`templates/matrix.yml`](templates/matrix.yml) | 多版本/多平台并行测试 |

---

## 坑（这一节比正文重要）

1. **cron 是 UTC**：写 `0 8 * * *` 期望早上 8 点，实际是北京时间 16:00。
2. **默认权限只读**：想 `git push` 必须加 `permissions: contents: write`，否则报 403。
3. **`GITHUB_TOKEN` 推的提交不会触发新的 workflow**（防递归），需要的话用 PAT。
4. **定时 workflow 会在仓库 60 天无活动后被自动停用**，GitHub 会发邮件提醒。长期维护的仓库要留意。
5. **别把密钥 echo 出来**：`run: echo ${{ secrets.X }}` 会在日志里被打码，但拼进 URL、写进文件、传给第三方 API 都可能泄露。用 `env:` 注入，别字符串拼接。
6. **公开仓库的 fork PR 拿不到你的 secrets**（这是设计如此），别指望 PR 里跑需要密钥的任务。
