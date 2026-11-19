# 精选工具（按功能归位，来源见「来源」列）

能直接拿来干活的东西。不按第几期排，按它能干什么排。

| 项目 | 仓库 | 许可证 | 干什么 | 来源 |
|---|---|---|---|---|
| **Concat** | [jub0t/Concat](https://github.com/jub0t/Concat) | **AGPL-3.0** | 剪映的开源平替：本地优先的跨平台剪辑器，带 JSON-RPC + MCP，能被 AI agent 脚本化驱动 | 抖音 |
| **IT-Tools** | [CorentinTh/it-tools](https://github.com/CorentinTh/it-tools) | GPL-3.0 | 80+ 个纯前端小工具：时间戳、Base64、JWT、二维码、正则…数据不出浏览器 | 本仓库 · 工具篇 |
| **CyberChef** | [gchq/CyberChef](https://github.com/gchq/CyberChef) | Apache-2.0 | 英国 GCHQ 的数据瑞士军刀：编码解码、加解密、取证分析，可拖成流水线 | 本仓库 · 工具篇 |
| **Stirling-PDF** | [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | MIT | 自托管 PDF 全家桶：合并、拆分、OCR、转 Office、加水印 | 本仓库 · 工具篇 |
| **DBX** | [t8y2/dbx](https://github.com/t8y2/dbx) | Apache-2.0 | 25 MB 轻量跨平台数据库客户端，支持 100+ 种数据库 | 133 |
| **Scrapling** | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | BSD-3-Clause | 现代化 Python 爬虫框架：自适应选择器、反爬处理、并发抓取 | 138 |
| **agent-desktop** | [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | Apache-2.0 | 让 AI 通过 CLI 操作桌面应用的 computer-use 工具（走 macOS 无障碍 API + MCP） | 137 |
| **gods-eye-view** | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | **NOASSERTION** | 浏览器里的 3D 地球观测台，数据来自真实公开源 | 130 |

## 用之前要知道的

- **Concat 官网/下载**：<https://concat.standalones.org>
- **Concat 是 AGPL-3.0**：自己剪片没事；但如果你把它包进产品、或对外提供剪辑服务，就要按 AGPL 开源你的修改。
- **它自己标了 Beta**（README 第一行就是 `Beta:`）：重要项目别把素材库押在它上面，先把工程导出备份。
- **它有 voice-cloning 相关能力**：克隆他人声音必须拿到授权，冒充/诈骗是违法的，平台也会封。
- **gods-eye-view 的许可证是 NOASSERTION**：GitHub 认不出，商用前必须自己读 LICENSE；它聚合的公开卫星/摄像头数据**各源有自己的条款**，二次分发前逐条确认，也别拿来做追踪个人的事。
- **DBX 连生产库请用只读账号**；确认它把凭据存在哪（本地加密还是明文）。
- **Scrapling 能力越强越要自律**：先看目标站 `robots.txt` 与用户协议、限速，别把人家打挂。
- **agent-desktop 等于把桌面控制权交给模型**：先在虚拟机或小号环境试。
- IT-Tools 是 **GPL-3.0**：自己用没事，改了分发要开源。

## 在线即用 vs 自托管

- 纯前端（IT-Tools、CyberChef）→ 数据不出本机，最安全
- 需要后端（Stirling-PDF、DBX、Scrapling）→ 自托管时记得加认证，别裸奔到公网

## 相关章节

[README.md](README.md) —— 工具的部署方式与选型判断
