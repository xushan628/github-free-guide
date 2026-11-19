# 第 138 期 · 5 个项目

> 来源：抖音「Github一周热点138期」 <https://v.douyin.com/74U3srU4JQ4/>
> 数据核对于 2026-11-19；星数会变，**以仓库页面为准**。

| # | 项目 | 仓库 | ★ | 许可证 | 语言 |
|---|---|---|---|---|---|
| 1 | OpenMausBot | [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | 25.5k | Apache-2.0 | TypeScript |
| 2 | T3 Code | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | 65.4k | MIT | TypeScript |
| 3 | ziwei-doushu | [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu) | 18.7k | MIT | TypeScript |
| 4 | Scrapling | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | 104.3k | BSD-3-Clause | Python |
| 5 | Astryx | [meta/astryx](https://github.com/meta/astryx) | 30.6k | MIT | TypeScript |

---

## 1. OpenMausBot · 开源版 Grok Bot

**是什么**：仓库描述是 *Open-source Grok Bot alternative with a virtual machine that bots can use* —— 给 AI bot 配一台它能操作的虚拟机。

**能干什么**：让 agent 在一个隔离的 VM 里跑命令、开浏览器、装软件，而不是直接动你的主系统。

**注意**：VM **降低**风险但不等于安全 —— 里面如果挂了你的 API key、登录态，照样会被 agent 误用。给它单独的账号和最小权限。

---

## 2. T3 Code · 跨设备控制 coding agent

**是什么**：*The best way to control Claude Code, Codex and more from any computer or phone* —— 把本机跑的 coding agent 变成可以从任意设备接入的工作台。

**能干什么**：电脑上跑 Claude Code / Codex，手机上接着看进度、下指令；多设备共享同一个会话。

**注意**：它的便利来自"把你的机器暴露给别的设备"，**远程访问那一层要自己加认证**（别裸奔到公网）。

---

## 3. ziwei-doushu · 紫微斗数排盘引擎

**是什么**：*紫微斗数开源排盘引擎 —— 基于倪海厦《天纪》体系*，含完整排盘算法、四化系统、格局知识库、古籍原文数据。

**能干什么**：做命盘计算、四化推演、格局判读的底层库；也可以拿排盘结果做可视化。

**注意**：这是**命理文化**工具，不是科学预测。别把它的结论当医疗/投资/人生决策依据；引用古籍原文时注意出处标注。

---

## 4. Scrapling · 现代化爬虫框架

**是什么**：Python 爬虫框架，README 的口号是 *The BEST Web Scraping framework*，从单个请求到大规模抓取都覆盖（自适应选择器、反爬处理、并发）。

**能干什么**：抓静态页、处理 JS 渲染页、批量采集；比手写 requests + BeautifulSoup 省很多事。

**注意**：
- **合规第一**：先看目标站 `robots.txt` 与用户协议，限速，别把人家打挂；
- 反爬绕过能力越强，越要自己设边界（对方明确禁止抓取的别抓）；
- 抓到的数据可能有版权，二次分发前确认许可。

---

## 5. Astryx · Agent 友好的设计系统

**是什么**：Meta 开源的设计系统，*fully customizable and agent ready* —— 组件库 + 设计 token，专门考虑了"让 AI 生成 UI 时也能对齐设计规范"。

**能干什么**：做后台/产品界面时直接拿组件与主题；因为 agent ready，配合 AI 生成页面的效果比手搓一致。

**注意**：网上有若干 Svelte / Flutter 的第三方移植版，收录的是**官方 `meta/astryx`**。用移植版前先确认它跟进到哪个版本。

---

## 一句话总结

| 你想干什么 | 看第几个 |
|---|---|
| 给 agent 一台隔离的机器 | 1 |
| 手机/别的电脑接着管 coding agent | 2 |
| 算紫微命盘 | 3 |
| 写爬虫、批量采集 | 4 |
| 找一套 AI 也能对齐的设计系统 | 5 |
