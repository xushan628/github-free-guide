# 05 · GitHub Pages：零成本托管个人网站 / 博客 / 文档

本仓库就是活例子：`docs/` 目录下的单文件站点，通过 Pages 部署后即可访问
`https://<用户名>.github.io/github-free-guide/`。

---

## 免费额度

| 项目 | 限制 |
|------|------|
| 站点大小 | 1 GB |
| 月流量（软限制） | 100 GB |
| 构建次数 | 10 次/小时（软限制） |
| 支持的仓库 | 公开仓库免费；私有仓库需 Pro/Team/Enterprise 才能用 Pages |
| 自定义域名 | 支持，含 HTTPS（Let's Encrypt 自动签发） |
| 后端 | **不支持**。只能放静态文件（HTML/CSS/JS/图片/WASM） |

> "软限制"的意思：超了不会立刻断你，但持续超会被限流。图片多的站一定要压图。

---

## 三种部署方式，按需选

### 方式 A：直接从分支部署（最简单，本仓库用的就是它）

1. 仓库 → `Settings` → `Pages`
2. `Source` 选 **Deploy from a branch**
3. `Branch` 选 `main`，目录选 **`/docs`**（或 `/ (root)`）
4. 保存，等 30–60 秒

之后每次 `git push` 到 `main`，站点自动更新（有 1–2 分钟缓存延迟）。

### 方式 B：用 Actions 构建部署（站点需要编译时用这个）

适合 Vite / Next（静态导出）/ VitePress / MkDocs 这类要 `npm run build` 的框架。

```yaml
name: Deploy Pages
on:
  push:
    branches: [main]
permissions:
  contents: read
  pages: write
  id-token: write
concurrency:
  group: pages
  cancel-in-progress: true
jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20, cache: npm }
      - run: npm ci && npm run build
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with: { path: dist }
      - id: deployment
        uses: actions/deploy-pages@v4
```

然后在 `Settings → Pages → Source` 选 **GitHub Actions**。

### 方式 C：用现成主题（不想自己写页面）

| 主题/框架 | 适合 | 说明 |
|-----------|------|------|
| [squidfunk/mkdocs-material](https://github.com/squidfunk/mkdocs-material) | 文档站 | Markdown 写，搜得到，本仓库这种技术文档最合适 |
| [cotes2020/jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) | 个人博客 | 自带归档、标签、暗色模式 |
| [docsifyjs/docsify](https://github.com/docsifyjs/docsify) | 极简文档 | 一个 `index.html` 搞定，不用构建 |
| [jekyll/jekyll](https://github.com/jekyll/jekyll) | 传统博客 | GitHub 原生支持，无需 workflow |

---

## 自定义域名（可选）

1. 域名 DNS 加一条 `CNAME` 记录指向 `<用户名>.github.io`
2. 仓库 `Settings → Pages → Custom domain` 填你的域名
3. 勾选 `Enforce HTTPS`（先等证书签发，一般几分钟）

> 仓库根目录会生成 `CNAME` 文件，**别删**，否则下次部署会丢域名。

---

## 坑

1. **路径大小写敏感**：本地 Windows 不区分大小写，Pages 区分。`Images/Logo.png` 写成 `images/logo.png` 就是 404。
2. **绝对路径写死 `/` 后会 404**：项目站点的根是 `/<仓库名>/`，不是 `/`。用相对路径最稳。
3. **`docs/` 和根目录二选一**：选了 `/docs` 就不能同时用根目录，否则以为改了没生效。
4. **私有仓库不能白嫖 Pages**：Free 计划下私有仓库的 Pages 不可用。
5. **构建 10 次/小时**：一小时内反复 push 会排队甚至失败，别把 Pages 当预览服务器刷。
6. **别用它跑需要后端的东西**：表单提交、登录、数据库都不行，得接第三方（如 Formspree）或换 Vercel/Cloudflare。
