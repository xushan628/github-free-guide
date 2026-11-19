# 第 133 期 · 给 AI Agent 开家公司

> 来源：抖音「Github一周热点133期」 <https://v.douyin.com/0oBRAzfFBDI/>
> 数据核对于 2026-11-19；星数会变，**以仓库页面为准**。

| # | 项目 | 仓库 | ★ | 许可证 | 语言 |
|---|---|---|---|---|---|
| 1 | Paperclip | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | 114.8k | MIT | TypeScript |
| 2 | video-use | [browser-use/video-use](https://github.com/browser-use/video-use) | 31.3k | MIT | Python |
| 3 | Octop | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | 12.2k | MIT | Python |
| 4 | OpenStock | [Open-Dev-Society/OpenStock](https://github.com/Open-Dev-Society/OpenStock) | 21.8k | **AGPL-3.0** | TypeScript |
| 5 | DBX | [t8y2/dbx](https://github.com/t8y2/dbx) | 30.8k | Apache-2.0 | Rust |

---

## 1. Paperclip · 管理 AI Agent 团队的开源工作台

**是什么**：*The open-source app everyone uses to manage agents at work* —— 把一堆 AI agent 当成"员工"来管的开源工作台（分配任务、看状态、审产出）。

**能干什么**：给 agent 团队做统一的入口：领任务、跑任务、汇总结果，比在几个终端窗口之间来回切强。

**注意**：
- **别搜错仓库**：GitHub 上还有个 ★9k 的老牌 `thoughtbot/paperclip`（Rails 附件管理库），跟这个完全没关系；
- 给 agent 发权限时按最小权限来，能只读就别给写。

---

## 2. video-use · 用 coding agent 剪视频

**是什么**：*Edit videos with coding agents* —— 让 Claude Code / Codex 这类 agent 直接对视频做剪辑（裁切、拼接、字幕、转码等）。

**能干什么**：批量处理素材、按脚本自动剪辑，适合做日更视频的流水线。

**注意**：素材版权要自己确认；agent 剪出来的东西仍要人工过一遍，尤其是字幕与时间轴。

---

## 3. Octop · 自托管的多人多 Agent AI 助手

**是什么**：腾讯云开源的 *self-hosted AI assistant — multi-user, multi-agent*，可以自己部署，支持多用户与多 agent 协作。

**能干什么**：团队内部搭一个自用的 AI 助手平台，数据和账号都在自己机器上。

**注意**：多用户意味着要配认证与配额；自托管不等于安全，公网暴露前先加反代和访问控制。

---

## 4. OpenStock · 开源股票看板

**是什么**：*Open-source alternative to expensive market platforms* —— 实时行情看板 + 自选股 + 图表，替代付费行情站。

**能干什么**：自建一个干净的行情面板，盯自己关注的标的。

**注意（两条都要看）**：
- **许可证是 AGPL-3.0**：自己内部用没事；但如果你改完**对外提供网络服务**，就必须按 AGPL 开源你的修改。想闭源商用请另选方案；
- **数据不是实时权威行情**，延迟和准确性取决于数据源，**不构成任何投资建议**。

---

## 5. DBX · 轻量跨平台数据库客户端

**是什么**：*25 MB lightweight cross-platform database client for 100+ databases* —— 一个 25 MB 的数据库客户端，Rust 写的，支持上百种数据库（含 MySQL、PostgreSQL 等）。

**能干什么**：替代又大又慢的桌面 DB 工具，连开发库、跑 SQL、看表结构。

**注意**：连**生产库**请用只读账号；客户端里保存的凭据要确认存在哪（本地加密还是明文），共享电脑上尤其注意。

---

## 一句话总结

| 你想干什么 | 看第几个 |
|---|---|
| 管一支 AI agent 团队 | 1 |
| 让 agent 帮你剪视频 | 2 |
| 自建团队 AI 助手 | 3 |
| 自建行情看板（注意 AGPL） | 4 |
| 找个轻量数据库客户端 | 5 |
