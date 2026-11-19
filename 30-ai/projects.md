# 精选 AI 项目（按功能归位，来源见「来源」列）

这些是追更「Github一周热点」时收录进来看的项目。**不按第几期排，按它们解决什么问题排** —— 想找 AI 相关的东西，看这一页就够了。

| 项目 | 仓库 | 许可证 | 干什么 | 来源 |
|---|---|---|---|---|
| **DeepTutor** | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | 港大私人 AI 家教：RAG 知识库、引导式学习、出题测评 | 专题 |
| **Archify** | [tt-a1i/archify](https://github.com/tt-a1i/archify) | Apache-2.0 | 把想法/代码库变成可交互架构图（Claude Code / Codex 的 skill） | 130 |
| **OpenMAIC** | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | MIT | 清华团队的多智能体交互式课堂，一键生成互动课 | 130 |
| **scientific-agent-skills** | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | MIT | 给 agent 装科研技能：综述、实验设计、数据分析 | 130 |
| **VoiceStudio** | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **AGPL-3.0** | 完全本地的 ElevenLabs 替代品：语音克隆、配音、转写 | 130 |
| **Paperclip** | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | MIT | 管理 AI agent 团队的工作台（不是同名 Rails 附件库） | 133 |
| **video-use** | [browser-use/video-use](https://github.com/browser-use/video-use) | MIT | 让 coding agent 直接剪视频 | 133 |
| **Octop** | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | MIT | 腾讯云开源自托管 AI 助手：多用户、多 agent | 133 |
| **dsh-superagent-prototype** | [deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype) | MIT | DeepSeek 官方更自主 agent 研究原型 | 137 |
| **claude-seo** | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | MIT | Claude Code 的 SEO skill：26 子技能 + 19 sub-agent | 137 |
| **awesome-dsh-plugin** | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | CC0-1.0 | DSH 社区插件精选列表 | 137 |
| **see-through** | [shitagaki-lab/see-through](https://github.com/shitagaki-lab/see-through) | Apache-2.0 | SIGGRAPH 2026：单张动漫角色图拆成可编辑分层 | 137 |
| **OpenMausBot** | [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | Apache-2.0 | 开源版 Grok Bot：给 bot 一台可操作的虚拟机 | 138 |
| **T3 Code** | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | MIT | 从任意电脑/手机控制 Claude Code、Codex 等 agent | 138 |

> 「专题」= 本仓库单独写过完整一节的项目，见 [README.md](README.md) 的 DeepTutor 部分。

## 用之前要知道的

- **许可证不是都干净**：`VoiceStudio` 是 **AGPL-3.0**（改完对外提供网络服务要开源），`awesome-dsh-plugin` 的 CC0 只覆盖清单、不覆盖插件代码。
- **agent 产出要复核**：Archify 的架构图是从代码推断的，画错的时候同样好看；scientific-agent-skills 不能改变"模型会编参考文献"，投稿前每处引用回源核对。
- **声音克隆涉人格权**：VoiceStudio 克隆他人声音必须拿到书面授权。
- **研究原型别上生产**：`dsh-superagent-prototype` 名字里就写着 prototype。
- 插件/技能类项目通常要接自己的 LLM（云端 API 或本地 Ollama）才有内容。

## 相关章节

- 想在本地跑模型、搭免代码工作流：[README.md](README.md)
- 想看这些项目出自哪一期：条目右侧的「来源」列
