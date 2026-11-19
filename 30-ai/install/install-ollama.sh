#!/usr/bin/env bash
# 安装 Ollama 并拉一个中文可用的小模型。
# 用法：bash install/install-ollama.sh [模型名]
set -euo pipefail

MODEL="${1:-qwen2.5:3b}"

echo "==> 检查平台"
case "$(uname -s)" in
  Linux*)  OS=linux ;;
  Darwin*) OS=mac ;;
  MINGW*|MSYS*|CYGWIN*) OS=windows ;;
  *) echo "未识别的系统：$(uname -s)"; exit 1 ;;
esac

if [ "$OS" = "windows" ]; then
  cat <<'EOF'
Windows 请手动安装（脚本不代下 exe）：
  1. 打开 https://ollama.com/download 下载 OllamaSetup.exe
  2. 双击安装，安装完托盘会出现 Ollama 图标
  3. 重新打开 Git Bash，执行：ollama pull qwen2.5:3b
EOF
  exit 0
fi

if command -v ollama >/dev/null 2>&1; then
  echo "==> Ollama 已安装：$(ollama --version 2>&1 | head -n1)"
else
  echo "==> 安装 Ollama"
  curl -fsSL https://ollama.com/install.sh | sh
fi

echo "==> 拉取模型 $MODEL（首次约 2 GB，耐心等）"
ollama pull "$MODEL"

echo "==> 试跑一句"
ollama run "$MODEL" "用一句话说明你已经在本机跑起来了。"

cat <<EOF

完成。常用命令：
  ollama list                     # 已安装的模型
  ollama run $MODEL               # 交互对话
  ollama serve                    # 只起 API 服务（127.0.0.1:11434）
  ollama rm $MODEL                # 删除模型

OpenAI 兼容端点：http://localhost:11434/v1
EOF
