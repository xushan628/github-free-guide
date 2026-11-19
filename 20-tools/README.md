# 02 · 在线轻工具：格式转换、PDF、图片、编码

这类仓库的价值在于：**打开浏览器就能用，或者一条 Docker 命令就能私有化部署**。不用装客户端、不上传文件到陌生服务器（自部署时），而且全部开源可审计。

---

## 推荐清单

### 一站式工具箱（最推荐先试这两个）

| 项目 | 能干什么 | 许可证 | 部署难度 |
|------|---------|--------|---------|
| [CorentinTh/it-tools](https://github.com/CorentinTh/it-tools) | 80+ 个前端小工具：时间戳、Base64、JWT、哈希、二维码、正则、颜色、单位换算、crontab、URL 编解码…… 纯前端，数据不出浏览器 | GPL-3.0 | 极低（Docker / 静态托管） |
| [gchq/CyberChef](https://github.com/gchq/CyberChef) | 英国 GCHQ 出品的"数据瑞士军刀"：编码解码、加解密、取证分析，可拖拽组合成流水线 | Apache-2.0 | 极低（单 HTML 也能跑） |

### 文档 / PDF

| 项目 | 能干什么 | 许可证 |
|------|---------|--------|
| [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | 自托管 PDF 全家桶：合并、拆分、压缩、OCR、转 Office、加水印、签名 | MIT（含部分第三方条款） |
| [mozilla/pdf.js](https://github.com/mozilla/pdf.js) | 浏览器里的 PDF 渲染器（几乎所有在线预览都基于它） | Apache-2.0 |

### 图片 / 媒体

| 项目 | 能干什么 | 许可证 |
|------|---------|--------|
| [jgraph/drawio](https://github.com/jgraph/drawio) | 在线画流程图 / 架构图 / UML，可离线自部署（drawio-desktop 同源） | Apache-2.0 |
| [image-rs/image](https://github.com/image-rs/image) | Rust 图片编解码库，命令行批量转格式的底座 | MIT / Apache-2.0 |
| [mermaid-js/mermaid](https://github.com/mermaid-js/mermaid) | 用文本画图（流程图、时序图、甘特图），GitHub Markdown 原生支持 | MIT |

### 编码 / 开发辅助

| 项目 | 能干什么 | 许可证 |
|------|---------|--------|
| [httpie/cli](https://github.com/httpie/cli) | 比 curl 好用的 API 调试命令行 | BSD-3-Clause |
| [hoppscotch/hoppscotch](https://github.com/hoppscotch/hoppscotch) | 开源版 Postman，可自部署 | MIT |
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | 1400+ 免费 API 清单（做小工具找数据源用） | MIT |

---

## 最快的三条上手路径

**路径 A：Docker 一把梭（本机）**

```bash
# IT-Tools：浏览器打开 http://localhost:8080
docker run -d --name it-tools -p 8080:80 corentinth/it-tools:latest

# Stirling-PDF：浏览器打开 http://localhost:8081
docker run -d --name stirling-pdf -p 8081:8080 \
  -v ./pdf-data:/configs stirlingtools/stirling-pdf:latest
```

**路径 B：部署到 GitHub Pages（纯前端工具）**

IT-Tools 是纯静态应用，`npm run build` 后把 `dist/` 推到 `gh-pages` 分支即可，完全不花钱。步骤见 [40-ship/pages](../40-ship/pages/README.md)。

**路径 C：直接用在线实例**

不想自己部署时，很多项目有官方 demo（仓库首页的 About 里有链接）。**但涉及隐私数据（合同、身份证、Token）时，一定自部署或用纯前端工具**——纯前端工具的数据不会离开你的浏览器。

---

## 选型判断：三个问题

1. **是纯前端吗？** 纯前端（IT-Tools、CyberChef）→ 数据不出本机，最安全。
2. **需要后端吗？** 需要（Stirling-PDF、Hoppscotch）→ 自部署时别忘了改默认密码、把服务关在内网。
3. **许可证是什么？** GPL-3.0（IT-Tools）会传染：你改了它的代码并分发，就必须开源。自己内部用不受限。

---

## 坑

- **别用来路不明的在线转换站**：上传的 PDF/图片会被留存。自部署或纯前端是唯一稳妥解。
- **Docker `latest` 标签不等于最新安全版**：生产用固定 tag，并定期 `docker pull` 更新。
- **不要把工具部署到公开的 0.0.0.0:8080 就完事**：Stirling-PDF 有默认无认证模式，暴露公网等于把硬盘交出去。
