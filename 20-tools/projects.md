# 精选工具（按功能归位，来源见「来源」列）

能直接拿来干活的东西。不按第几期排，按它能干什么排。

| 项目 | 仓库 | 许可证 | 干什么 | 来源 |
|---|---|---|---|---|
| **ai-goofish-monitor** | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | MIT | 闲鱼多任务监控与智能分析：Playwright + AI 盯商品，带后台 UI（只读，不改平台操作） | 抖音 |
| **RustDesk** | [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | AGPL-3.0 | 开源远程桌面，可自建中继服务器，替代 TeamViewer/向日葵 | 小白神器 |
| **LocalSend** | [localsend/localsend](https://github.com/localsend/localsend) | Apache-2.0 | 跨平台 AirDrop 替代：手机↔电脑互传，同一个局域网直连 | 小白神器 |
| **Mole** | [tw93/Mole](https://github.com/tw93/Mole) | GPL-3.0 | 开源 Mac/PC 清理工具，命令行删缓存、找大文件 | 小白神器 |
| **Motrix** | [agalwood/Motrix](https://github.com/agalwood/Motrix) | NOASSERTION | 全能下载器（HTTP/BT/磁力），替代迅雷 | 小白神器 |
| **Univer** | [dream-num/univer](https://github.com/dream-num/univer) | Apache-2.0 | 开源 AI 办公套件：表格/文档/幻灯片的 SDK，AI 可直接调用 | 86 |
| **Sure** | [we-promise/sure](https://github.com/we-promise/sure) | AGPL-3.0 | 开源个人记账理财 App，自带 AI 助手 | 86 |
| **agent-browser** | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Apache-2.0 | Vercel 给 AI 做的浏览器自动化 CLI，能把跑通的网页流程存下来重放 | 73 |
| **Concat** | [jub0t/Concat](https://github.com/jub0t/Concat) | **AGPL-3.0** | 剪映的开源平替：本地优先的跨平台剪辑器，带 JSON-RPC + MCP，能被 AI agent 脚本化驱动 | 抖音 |
| **IT-Tools** | [CorentinTh/it-tools](https://github.com/CorentinTh/it-tools) | GPL-3.0 | 80+ 个纯前端小工具：时间戳、Base64、JWT、二维码、正则…数据不出浏览器 | 本仓库 · 工具篇 |
| **CyberChef** | [gchq/CyberChef](https://github.com/gchq/CyberChef) | Apache-2.0 | 英国 GCHQ 的数据瑞士军刀：编码解码、加解密、取证分析，可拖成流水线 | 本仓库 · 工具篇 |
| **Stirling-PDF** | [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | MIT | 自托管 PDF 全家桶：合并、拆分、OCR、转 Office、加水印 | 本仓库 · 工具篇 |
| **DBX** | [t8y2/dbx](https://github.com/t8y2/dbx) | Apache-2.0 | 25 MB 轻量跨平台数据库客户端，支持 100+ 种数据库 | 133 |
| **Scrapling** | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | BSD-3-Clause | 现代化 Python 爬虫框架：自适应选择器、反爬处理、并发抓取 | 138 |
| **agent-desktop** | [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | Apache-2.0 | 让 AI 通过 CLI 操作桌面应用的 computer-use 工具（走 macOS 无障碍 API + MCP） | 137 |
| **gods-eye-view** | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | **NOASSERTION** | 浏览器里的 3D 地球观测台，数据来自真实公开源 | 130 |

## 「会员能停了」这五个（本仓库的对应关系）

| 你以前付的费用 | 开源替代 | 在这个仓库的哪 |
|---|---|---|
| TeamViewer / 向日葵会员 | **RustDesk** | 本页表格 |
| 各种传输助手/网盘 | **LocalSend** | 本页表格 |
| PDF 编辑/转换订阅 | **Stirling-PDF** | 本页表格 |
| 清理软件订阅 | **Mole** | 本页表格 |
| 迅雷会员 | **Motrix** | 本页表格 |

## 闲鱼自动化：高风险项目不放这里

同类的「闲鱼超级管家」（自动发货/评价/擦亮/过滑块）**放在 [60-others](../60-others/README.md)**，那里写了完整的风险拆解——它对抗平台风控，封号是常态，不适合和常规工具并列推荐。

本页只留只读的 **ai-goofish-monitor**（监控/选品，不改平台操作）。

## 用之前要知道的

- **RustDesk 是 AGPL-3.0**：自建服务器给自己用没问题，但对外提供远程桌面服务要按 AGPL 开源修改；没自建中继时走官方服务器，速度和稳定性受限。
- **Motrix 的许可证 GitHub 识别不出（NOASSERTION）**：商用前自己读 LICENSE。
- **Mole 是 GPL-3.0 的命令行工具**：删除类操作**先用 `--dry-run` 或预览模式**跑一遍，别一上来就清。
- **LocalSend 只在同一局域网直连**：跨网段用不了，这是设计如此（不经服务器）。
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
