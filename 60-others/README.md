# 🗃️ 其他项目（暂未归类，后续再分）

这里放**暂时没有合适功能归属**的项目。不是不重要，是分类轴还没想清楚 —— 等同类多了，自然会长成一个新分组。

| 项目 | 仓库 | 许可证 | 干什么 | 来源 |
|---|---|---|---|---|
| **闲鱼超级管家** | [23Star/xianyu-super-butler](https://github.com/23Star/xianyu-super-butler) | AGPL-3.0 | 闲鱼自动发货/自动擦亮/评价的运营工具，Python 写；★1.4k、830 fork | 抖音 |
| **daily_stock_analysis** | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | MIT | LLM 驱动的股票智能分析：多源行情 + 新闻 + 决策看板 + 自动推送 | 73 |

**三步装法（视频给的，实测路径合理）**：
1. **Fork** 仓库到你自己的 GitHub；
2. 在 `Settings → Secrets and variables → Actions` 里填**模型 Key**（DeepSeek 也能接）和**自选股代码**；
3. 打开 **Actions** 开关，工作日收盘后自动跑，报告推到飞书或邮箱。

> 零成本的关键：跑在 GitHub Actions 上，公开仓库不收时长费。
> **它自己写着"不构成任何投资建议"** —— 别把自动报告当买卖信号。
| **Disc Image Studio** | [JiaFeiMiao-K-Cat/DiscImageStudio](https://github.com/JiaFeiMiao-K-Cat/DiscImageStudio) | GPL-3.0 | 用普通刻录光驱在光盘盘面上刻出图案 | 73 |
| **OpenStock** | [Open-Dev-Society/OpenStock](https://github.com/Open-Dev-Society/OpenStock) | **AGPL-3.0** | 开源股票行情看板：自选股 + 实时图表，替代付费行情平台 | 133 |
| **ziwei-doushu** | [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu) | MIT | 紫微斗数开源排盘引擎：排盘算法、四化系统、格局知识库、古籍原文 | 138 |

## 为什么放这里

- **OpenStock** 是金融数据工具，既不属于"找资源"（不是素材），也不属于"用 AI"（它的价值在行情面板）—— 真要归类得再开一个"数据看板"，为一个项目开组不划算。
- **ziwei-doushu** 是传统文化/命理计算库，跟"GitHub 免费福利"这条主线不搭，但它确实是开源的、确实能跑。

**同一个坑位满了（比如再攒到 4–5 个），就拆成独立分组。** 现在放这里，比硬塞进 AI 或工具更诚实。

## 为什么「闲鱼自动化」只放其他、还单独警告

| 风险 | 具体是什么 |
|---|---|
| **平台规则** | 闲鱼（阿里）用户协议禁止用脚本/外挂做自动化运营，这类工具本质是在和风控对抗，被判定后**限流、降权、封号**都是常见处理 |
| **自动过滑块** | README 自己写着"自动过滑块"——这是绕过人机验证，属于明确的违规行为，不是"技术中性" |
| **账号托管最危险** | 它主推"在线托管（xy.corleom.com）"，意思是**把闲鱼账号的 cookie 交给第三方服务器**。等于把账号控制权交出去，对方能读你的消息、发布商品、甚至清空店铺 |
| **AGPL-3.0** | 自己改自己用没问题；对外提供服务要按 AGPL 开源你的修改 |

**结论**：这类工具我不推荐当"副业神器"用——收益是卖货，成本可能是账号。真要运营二手生意，平台自带的"闲鱼卖家中心 + 自动回复模板"能覆盖 80% 的需求，而且是合规的。

## 用之前要知道的

- **OpenStock 是 AGPL-3.0**：自己内部用没事；改完**对外提供网络服务**要按 AGPL 开源修改。
- OpenStock 的行情数据**不是权威实时源**，延迟和准确性取决于上游，**不构成投资建议**。
- **ziwei-doushu 是命理文化工具**，不是科学预测，别拿它做医疗/投资/人生决策依据；引用古籍原文时注意出处。
