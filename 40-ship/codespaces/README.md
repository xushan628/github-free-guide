# 06 · Codespaces：免费云端 VS Code（0 门槛的"云端算力"）

视频里"0 门槛免费白嫖云端算力"的另一半就是它：**浏览器里打开一个完整的 Linux 开发环境**，不用装 Python、不用配环境、换台电脑也能接着写。

---

## 免费额度（个人账号 Free 计划）

| 项目 | 额度 |
|------|------|
| 计算时长 | 120 core-hours/月 |
| 存储 | 15 GB-month/月 |
| 机器规格 | 2 核 / 8 GB 内存 / 32 GB 磁盘（默认，1 core-hour = 1 小时） |
| 空闲超时 | 默认 30 分钟自动停止（可调到 240 分钟） |

**换算**：2 核机器跑 1 小时 = 2 core-hours。所以 120 core-hours ≈ **每月 60 小时的双核使用**，每天 2 小时够用一个月。

> 额度每月初重置，不累积。以 [GitHub Codespaces 计费文档](https://docs.github.com/billing/managing-billing-for-your-products/about-billing-for-github-codespaces) 为准。

---

## 三种打开方式

1. **网页**：仓库页面 → 绿色 `Code` 按钮 → `Codespaces` → `Create codespace on main`
2. **快捷键**：按 `.`（英文句号）在 github.com 任意仓库直接打开网页版 VS Code（不是 Codespaces，但也免费）
3. **本地 VS Code**：装 `GitHub Codespaces` 扩展，远程连上去，体验和本地一样

---

## 让环境"开箱即用"：devcontainer

在仓库里放 `.devcontainer/devcontainer.json`，Codespaces 每次创建都会自动装好环境：

```jsonc
{
  "name": "python-dev",
  "image": "mcr.microsoft.com/devcontainers/python:3.12",
  "features": {
    "ghcr.io/devcontainers/features/node:1": {},
    "ghcr.io/devcontainers/features/github-cli:1": {}
  },
  "postCreateCommand": "pip install -r requirements.txt",
  "customizations": {
    "vscode": {
      "extensions": ["ms-python.python", "charliermarsh.ruff"]
    }
  },
  "forwardPorts": [8000, 3000]
}
```

模板仓库：[devcontainers/templates](https://github.com/devcontainers/templates)（几十种现成组合，直接 `Use this template`）。

---

## 它和 Actions 的分工

| | Codespaces | Actions |
|---|---|---|
| 性质 | 交互式开发环境 | 无人值守的批处理 |
| 计时 | 你开着就算 | 跑完就停 |
| 适合 | 写代码、调 bug、跑测试 | 定时任务、构建、发布 |
| 免费额度 | 120 core-hours/月 | 公开仓库不限 / 私有 2000 分钟/月 |

**白嫖思路**：平时用 Codespaces 开发，用 Actions 做定时任务。两个额度互不占用。

---

## 坑

1. **忘了关 = 烧额度**：浏览器标签关了但 codespace 还在跑。养成 `Codespaces` 页面手动 `Stop` 的习惯，或把超时调短。
2. **2 核 8 G 跑不动大模型**：想跑 7B 模型至少 24 G 内存，Codespaces 免费档不行。
3. **存储也计费**：每个 codespace 占空间，15 GB-month 很快用完。不用的要 **Delete**，不是 Stop。
4. **别在里面放密钥**：codespace 是临时环境，但 `~/.bash_history` 和未提交文件可能被保留在快照里。
5. **端口默认私有**：转发端口要手动改成 `Public` 才能被外部访问，别不小心把调试端口公开。
