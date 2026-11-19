# 03 · 开源本地 AI：在自己电脑上跑模型 + 免代码 AI 工作流

视频第三类的核心是：**模型和工具都开源，不用订阅、不用把数据传给云端**。代价是吃你自己的显卡/内存。

---

## 一、本地跑模型：选一个引擎

| 引擎 | 适合谁 | 特点 | 许可证 |
|------|--------|------|--------|
| [ollama/ollama](https://github.com/ollama/ollama) | **最推荐新手** | 一条命令跑模型，自带模型仓库、OpenAI 兼容 API | MIT |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 想压榨性能 | C++ 推理引擎，量化格式（GGUF）的源头 | MIT |
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | 想要 ChatGPT 那样的界面 | 给 Ollama 套一层 Web UI，支持多用户、RAG | 自有许可（源码可用，非 OSI；去品牌/商用前看 LICENSE） |
| [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI) | 玩 AI 绘图 | 节点式工作流，出图可控性最强 | GPL-3.0 |
| [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | 玩 AI 绘图（老牌） | 上手简单，插件生态大 | AGPL-3.0 |

### 5 分钟跑起来（Ollama）

```bash
# Windows: 官网下载安装包；macOS/Linux:
curl -fsSL https://ollama.com/install.sh | sh

# 拉一个中文可用的小模型（约 2 GB）
ollama pull qwen2.5:3b

# 对话
ollama run qwen2.5:3b

# 它同时起了一个 OpenAI 兼容服务：http://localhost:11434/v1
curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"qwen2.5:3b","messages":[{"role":"user","content":"用一句话解释什么是 GitHub Actions"}]}'
```

> 模型权重有几个 GB，**不适合放进代码仓库**（GitHub 单文件上限 100 MB，仓库建议 < 1 GB）。所以本仓库只放脚本，`.gitignore` 已排除 `models/`、`*.gguf`、`*.safetensors`。

一键脚本见 [`install/install-ollama.sh`](install/install-ollama.sh)。

### 显存 / 内存对照（跑 4-bit 量化模型的粗略门槛）

| 模型规模 | 最低内存 | 体验 |
|---------|---------|------|
| 0.5B – 1.5B | 4 GB | 能跑，能力有限，适合做格式化/分类 |
| 3B – 4B | 8 GB | **日常可用的最低档**，中文问答够用 |
| 7B – 8B | 16 GB | 通用能力明显更好 |
| 14B | 24 GB | 本地写作/代码辅助的甜点 |
| 32B+ | 48 GB+ | 接近云端小模型水平 |

> 没独显也能跑：CPU 推理慢 5–20 倍，3B 模型大概每秒几个字，做后台批处理够了。

---

## 二、免代码 AI 工作流：把模型接进业务流程

| 项目 | 能干什么 | 许可证 |
|------|---------|--------|
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | 400+ 节点的自动化编排，带 AI Agent 节点，可自部署（开源版免费） | Sustainable Use License（非 OSI，商用需看清条款） |
| [langgenius/dify](https://github.com/langgenius/dify) | 可视化搭 LLM 应用：知识库 RAG、Agent、工作流、对外发布 API | 见仓库 LICENSE（Apache-2.0 + 附加条款） |
| [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | 可视化拖拽搭 LLM 应用（Flowise 原作者已停止维护，改用这个） | MIT |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 要写代码时的标准框架 | MIT |

### n8n 一条命令起服务

```bash
docker run -d --name n8n -p 5678:5678 \
  -v n8n_data:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n
# 打开 http://localhost:5678
```

典型玩法：**每天早上 8 点抓一个 RSS/网页 → 交给本地 Ollama 总结 → 发到飞书/Telegram**。
其中"每天 8 点"这一步不需要服务器，用 GitHub Actions 就能跑，见 [04-actions](../04-actions/README.md)。

---

## 三、AI 应用案例：港大 DeepTutor · 私人 AI 家教

> 抖音上热传的"港大开源私人 AI 家教"就是它：**[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)**，
> HKUDS 团队出品，隶属于香港大学 **Data Intelligence Lab**。README 里的定位是 *Lifelong Personalized Tutoring*（终身个性化辅导）。

| 项目 | 值 |
|---|---|
| 热度 | ★60,000+，fork 7,300+，仍在高频迭代（最新 v1.7.3，2026-11 发布） |
| 许可证 | **Apache-2.0**（可商用、可改、可自部署） |
| 技术栈 | Python 3.11–3.14 + Node.js 20.9+ |
| 官网 / 论文 | <https://deeptutor.info> ／ [arXiv](https://arxiv.org/abs/2604.26962) |
| 数据 | 知识库、聊天记录都存在**你自己的机器**上（`data/user/`），不上传云端 |

论文标题是 *DeepTutor: Towards Agentic Personalized Tutoring*，核心是把**带引用的讲解**、**难度校准的出题**和**学习者记忆**拼成一个框架，并提出了评测基准 TutorBench（论文称个性化指标平均提升 10.8%）。看论文比看宣传语更能判断它适不适合你。

### 它能做什么

- **知识库问答（RAG）**：把 PDF / DOCX / PPTX / EPUB 丢进去，基于你自己的资料回答，带出处
- **引导式学习**：不是直接给答案，而是按掌握度出题、追进度
- **出题与测评**：选择题/填空/问答，可导出
- **Book 引擎**：把一堆资料编译成一本可读的"活书"
- **记忆与多智能体**：跨会话记住你学到哪，复杂任务拆给多个 agent
- **多端**：桌面客户端（macOS / Windows 安装包）、Web 界面、CLI

### 三种装法（按省事程度排序）

**① 桌面版（最省事，连 Python 都不用装）**

到 [Releases](https://github.com/HKUDS/DeepTutor/releases/latest) 下载对应安装包：

| 你的电脑 | 下载 |
|---|---|
| Mac（Apple Silicon） | `Open-DeepTutor-MacOS-Apple-Silicon.dmg` |
| Mac（Intel） | `Open-DeepTutor-MacOS-Intel.dmg` |
| Windows x64 | `Open-DeepTutor-Windows-Setup.exe` |

> Windows 预览版未签名，SmartScreen 会拦一下，选"仍要运行"。

**② pip 安装（自己控制环境）**

```bash
python -m pip install -U "deeptutor[full]"   # 装 Web 应用 + CLI
deeptutor start                              # 起服务，按提示配置模型
```

**③ Docker（部署到服务器/ NAS）**

```bash
docker run --rm --name deeptutor -p 8000:8000 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

### 用之前必须知道的三件事

1. **它本身不是模型**。DeepTutor 是"教学流程 + RAG + agent"的外壳，**要接自己的 LLM**（OpenAI/Claude/通义/本地 Ollama 都行）。没配模型 key 是跑不起来的。
2. **想完全免费 → 接本地模型**：先用 [Ollama](#一本地跑模型选一个引擎) 起一个 `qwen2.5:7b` 或更大，再把 DeepTutor 指向 `http://localhost:11434/v1`。这样从数据到推理全在自己的机器上。
3. **隐私边界**：资料存在本地，但**推理请求会发到你配置的模型服务商**。用云端 API 时，知识库检索出来的片段会随问题一起发出去；敏感材料请配本地模型。

---

## 四、GitHub 上的模型/数据集去哪找

- [huggingface/transformers](https://github.com/huggingface/transformers) —— 模型事实标准库
- [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) —— GGUF 量化模型生态入口
- [ollama/ollama](https://github.com/ollama/ollama) 的模型库 —— 直接 `ollama pull`，最省事

---

## 坑

1. **别把模型权重提交进 git**：一次 5 GB 的提交会永久留在大文件历史里，以后 clone 都痛苦。用 `.gitignore` + 发布到 Release / Hugging Face。
2. **n8n 的许可证不是标准开源**：内部用随便，但如果要把它打包进你卖的产品，必须先读 Sustainable Use License。
3. **本地模型 ≠ 云端模型**：3B 级别做不了复杂推理。要能力就得加显存，别指望小模型白嫖 GPT-4 的效果。
4. **端口别裸奔**：Ollama 的 11434、n8n 的 5678 默认无认证，暴露公网等于送人。绑定 `127.0.0.1` 或加反代认证。
