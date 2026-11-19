# 第 130 期 · Skill 与智能体专场

> 来源：抖音「GitHub一周热点第130期」 <https://v.douyin.com/L4GRFhPqXOo/>
> 数据核对于 2026-11-19；星数会变，**以仓库页面为准**。

| # | 项目 | 仓库 | ★ | 许可证 | 语言 |
|---|---|---|---|---|---|
| 1 | archify | [tt-a1i/archify](https://github.com/tt-a1i/archify) | 97.8k | Apache-2.0 | JavaScript |
| 2 | gods-eye-view | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | 65.8k | **NOASSERTION** | JavaScript |
| 3 | OpenMAIC | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | 43.9k | MIT | TypeScript |
| 4 | scientific-agent-skills | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 57.7k | MIT | Python |
| 5 | VoiceStudio | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | 113.6k | **AGPL-3.0** | Python |

---

## 1. archify · 把想法/代码变成可交互架构图

**是什么**：*Turn any idea, plan, or codebase into a beautiful interactive diagram* —— 给 Claude Code / Codex 用的 **agent skill**，把一句话需求或一整个代码库画成可点击的架构图。

**能干什么**：接手陌生项目时先让它出图；写方案时把口头描述变成能评审的图。

**注意**：图是**从代码推断**出来的，漏掉动态调用、配置注入这类"非字面"关系很正常。图上标了"可信"也要人对着代码核一遍——它画错的时候看起来同样漂亮。

官网：<https://archify.si>

---

## 2. gods-eye-view · 浏览器里的"上帝视角"

**是什么**：*a spy satellite simulator in your browser, except the data is real* —— 基于真实公开数据的 3D 地球观测台，把卫星影像、航班、船舶等公开空间情报叠在一个地球上。

**能干什么**：做地理/OSINT 类可视化演示；理解"公开数据能拼出多少信息"。

**注意（三条）**：
- **许可证是 NOASSERTION**：GitHub 认不出标准许可证，**商用前必须自己读 LICENSE**；
- 数据来自第三方公开源，**各源有自己的使用条款**，二次分发前逐条确认；
- 这类聚合天然涉及位置隐私，别拿它做追踪个人的事。

官网：<https://godseyeview.ai/>

---

## 3. OpenMAIC · 多智能体交互式课堂

**是什么**：清华 MAIC 团队的 *Open Multi-Agent Interactive Classroom* —— 一键生成一门有多智能体参与的互动课（讲解、提问、演示）。

**能干什么**：把一份资料变成"能对话的课"；做培训、做课程演示。

**注意**：它要接 LLM（云端 API 或本地模型）才有内容；课堂内容仍是模型生成，**教学场景里事实性错误代价很高**，上线前要审。

---

## 4. scientific-agent-skills · 把 agent 变成"AI 科学家"

**是什么**：*Turn any AI agent into an AI Scientist* —— 面向科研的 Agent Skills 库，仓库自称被 25 万+ 科研人员使用，并附论文（arXiv 2609.00065）。

**能干什么**：文献综述、实验设计、数据分析、写作辅助这类科研流程，用技能包喂给现成的 agent。

**注意**：**科研产物必须人工复核**。技能包能提高效率，但不改变"模型会编参考文献"这个事实；投稿前每一处引用都要回源核对。

---

## 5. VoiceStudio · 完全本地的 AI 语音工作台

**是什么**：*the open-source, fully-local ElevenLabs alternative* —— 本地跑语音克隆、音色设计、视频配音、听写转写、有声书。

**能干什么**：不想把声音素材传给云端服务时的替代方案；批量配音、做多语言版本。

**注意（两条都要看）**：
- **许可证是 AGPL-3.0**：自己用没问题；改完**对外提供网络服务**要按 AGPL 开源修改；
- **声音克隆涉及人格权**：克隆他人声音必须拿到本人书面授权，拿来做诈骗/冒充是违法的，平台也会封。

官网：<https://voicestudio.sh>

---

## 一句话总结

| 你想干什么 | 看第几个 |
|---|---|
| 让 agent 画架构图 | 1 |
| 做地理/OSINT 可视化 | 2 |
| 把资料变成互动课 | 3 |
| 给 agent 装科研技能 | 4 |
| 本地做语音克隆/配音 | 5 |
