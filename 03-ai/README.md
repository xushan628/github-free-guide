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

## 三、GitHub 上的模型/数据集去哪找

- [huggingface/transformers](https://github.com/huggingface/transformers) —— 模型事实标准库
- [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) —— GGUF 量化模型生态入口
- [ollama/ollama](https://github.com/ollama/ollama) 的模型库 —— 直接 `ollama pull`，最省事

---

## 坑

1. **别把模型权重提交进 git**：一次 5 GB 的提交会永久留在大文件历史里，以后 clone 都痛苦。用 `.gitignore` + 发布到 Release / Hugging Face。
2. **n8n 的许可证不是标准开源**：内部用随便，但如果要把它打包进你卖的产品，必须先读 Sustainable Use License。
3. **本地模型 ≠ 云端模型**：3B 级别做不了复杂推理。要能力就得加显存，别指望小模型白嫖 GPT-4 的效果。
4. **端口别裸奔**：Ollama 的 11434、n8n 的 5678 默认无认证，暴露公网等于送人。绑定 `127.0.0.1` 或加反代认证。
