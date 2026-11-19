# 第 137 期 · 5 个项目

> 来源：抖音「Github一周热点137期」 <https://v.douyin.com/RQd4yLbc1fY/>
> 数据核对于 2026-11-19；星数会变，**以仓库页面为准**。

| # | 项目 | 仓库 | ★ | 许可证 | 语言 |
|---|---|---|---|---|---|
| 1 | dsh-superagent-prototype | [deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype) | 23.9k | MIT | TypeScript |
| 2 | agent-desktop | [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | 25.4k | Apache-2.0 | Rust |
| 3 | claude-seo | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | 30.7k | MIT | Python |
| 4 | awesome-dsh-plugin | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | 25.1k | CC0-1.0 | JavaScript |
| 5 | see-through | [shitagaki-lab/see-through](https://github.com/shitagaki-lab/see-through) | 5.8k | Apache-2.0 | Python |

---

## 1. dsh-superagent-prototype · 超级智能体研究原型

**是什么**：DeepSeek 官方组织（`deepseek-ai`）放出的研究原型，README 一句话是 *Towards a More Autonomous Agent System*（走向更自主的 agent 系统）。

**能干什么**：给"agent 怎么自己规划、执行、评估"提供一套可跑的参考实现，适合拿来做二次开发或研究对比。

**注意**：名字里带 `prototype`，它是**研究原型**而不是成熟产品；接口和结构随时可能变，别直接压在生产上。

```bash
git clone https://github.com/deepseek-ai/dsh-superagent-prototype
cd dsh-superagent-prototype && cat README.md   # 先看依赖与运行方式
```

---

## 2. agent-desktop · 让 AI 操作桌面软件

**是什么**：Vercel Labs 出品，*Computer use CLI for AI agents* —— 一个给 agent 用的命令行工具，让 AI 能真的去点/读桌面应用，而不是只会调网页。

**怎么做到的**：走 macOS 的无障碍（Accessibility）API，并通过 MCP 对外暴露能力；语言是 Rust。

**官网**：<https://agent-browser.dev/desktop>

**注意**：桌面自动化 = 把控制权交给一个会犯错的模型。先在**虚拟机或小号账号**里试，别对着装了导出密码的浏览器跑。

---

## 3. claude-seo · 网站 SEO 的 skill

**是什么**：给 Claude Code 用的通用 SEO skill，README 写明 **26 个子技能 + 19 个 sub-agent**。

**覆盖面**（照抄仓库描述，不做延伸）：技术 SEO、E-E-A-T、schema 结构化数据、GEO/AEO、agent readiness（Lighthouse Agentic Browsing、WebMCP、`llms.txt`）、外链、本地 SEO、电商 SEO、国际化 SEO、Google APIs，以及 PDF/Excel 报告；另有 9 个可选扩展接实时 SEO 数据。

**注意**：这类 skill 是"提示词 + 脚本"的组合，产出质量取决于你给的数据。**别把未审校的 SEO 建议直接上线**，尤其是批量改标题/结构化数据那种操作。

> **为什么选它**：搜「Claude SEO」还有更火的通用营销技能库（如 ★6.1 万的 `coreyhaines31/marketingskills`），但视频说的是"网站 SEO 的 skill"，所以收录这个专做 SEO 的。

---

## 4. awesome-dsh-plugin · DSH 社区插件合集

**是什么**：DeepSeek Harness（DSH）的插件精选列表，CC0 授权（列表本身可随意转载）。

**官网**：<https://awesome-dsh-plugin.com>

**怎么用**：按分类找插件 → 点进各自仓库 → **每个插件有自己的许可证**，CC0 只覆盖这份清单，不覆盖插件代码。

---

## 5. see-through · 动漫角色图拆成可编辑分层

**是什么**：SIGGRAPH 2026 会议论文 *Single-image Layer Decomposition for Anime Characters* 的官方实现 —— 输入一张动漫角色图，输出**可编辑的分层素材**（头发、衣服、配饰等分开）。

**能干什么**：给画师做二次创作、给 Live2D/游戏做素材拆解、给模型训练做数据预处理。

**注意**：这是论文实现，跑之前先看仓库里的依赖与权重说明；产出的分层质量取决于原图，复杂遮挡会拆错。

---

## 一句话总结

| 你想干什么 | 看第几个 |
|---|---|
| 研究 agent 自主性 | 1 |
| 让 AI 真的操作桌面软件 | 2 |
| 给网站做技术 SEO 体检 | 3 |
| 给 DSH 装插件 | 4 |
| 把一张动漫图拆成图层 | 5 |
