# 文件

- [GitHub API 通道与凭据（gh_auth 与各脚本客户端）](github-api-transport.md) - 说明仓库所有出网行为共用的底座：只经 Python 标准库 urllib 访问 api.github.com、resolve_token 的环境变量优先两级凭据顺序与不落盘原则、统一请求头与 API 版本，以及四个调用方各自不同的重试与限流策略。
