# 01 · 免费商用素材：图标、字体、插画、头像

视频里第一类"白嫖"就是**素材**：GitHub 上有一批许可证干净的图标库、字体库、插画库，质量比很多付费站还高，而且**可以商用**。

本目录已经真的下载了一批进仓库（见根目录 `MANIFEST.json` 里的 SHA-256 校验），你可以直接用，也可以按下面的清单自己扩。

---

## 已经下载进仓库的

| 素材 | 数量 | 许可证 | 目录 | 上游 |
|------|------|--------|------|------|
| Tabler Icons（线性 UI 图标） | 106 个 SVG | MIT | `icons/tabler/` | [tabler/tabler-icons](https://github.com/tabler/tabler-icons) |
| Lucide（Feather 的社区续作） | 94 个 SVG | ISC | `icons/lucide/` | [lucide-icons/lucide](https://github.com/lucide-icons/lucide) |
| JetBrains Mono（可变字重，写代码用） | 1 个 TTF | OFL-1.1 | `fonts/` | [google/fonts](https://github.com/google/fonts) |
| Inter（可变字重，界面/正文用） | 1 个 TTF | OFL-1.1 | `fonts/` | [google/fonts](https://github.com/google/fonts) |

许可证原文在 `LICENSES/`。**MIT / ISC 只要求保留版权声明，OFL 允许商用和嵌入，但字体文件本身不能单独售卖。**

### 用法示例

```html
<!-- 图标：直接当 <img> 用 -->
<img src="10-resources/assets/icons/tabler/home.svg" width="16" alt="home">

<!-- 字体：拷到项目里，注意路径里 [] 要 URL 编码 -->
<style>
  @font-face {
    font-family: "Inter";
    src: url("10-resources/assets/fonts/Inter%5Bopsz,wght%5D.ttf") format("truetype");
    font-weight: 100 900;
  }
</style>
```

> 注意：可变字体的文件名带方括号 `Inter[opsz,wght].ttf`，在 CSS/URL 里必须写成 `%5B` `%5D`，否则 404。

---

## 还能去哪找（按许可证挑，别只看脸）

### 图标

| 仓库 | 说明 | 许可证 |
|------|------|--------|
| [tabler/tabler-icons](https://github.com/tabler/tabler-icons) | 5800+ 线性图标，风格统一，最推荐打底 | MIT |
| [lucide-icons/lucide](https://github.com/lucide-icons/lucide) | Feather 的社区续作，1500+ | ISC |
| [feathericons/feather](https://github.com/feathericons/feather) | 极简鼻祖，只有 280 个但干净 | MIT |
| [simple-icons/simple-icons](https://github.com/simple-icons/simple-icons) | 品牌/logo 图标（GitHub、微信…） | CC0-1.0 |
| [iconify/iconify](https://github.com/iconify/iconify) | 150+ 图标集的统一入口，可只取 SVG | MIT |
| [ionic-team/ionicons](https://github.com/ionic-team/ionicons) | 移动端风格，1300+ | MIT |

### 字体

| 仓库 | 说明 | 许可证 |
|------|------|--------|
| [google/fonts](https://github.com/google/fonts) | Google Fonts 官方源，3000+ 字体 | OFL / Apache-2.0 |
| [adobe-fonts/source-han-sans](https://github.com/adobe-fonts/source-han-sans) | 思源黑体，中文字体首选 | OFL-1.1 |
| [lxgw/LxgwWenKai](https://github.com/lxgw/LxgwWenKai) | 霞鹜文楷，中文开源楷体 | OFL-1.1 |

> 中文字体动辄 10–20 MB，不适合塞进代码仓库。建议用 `pyftsubset` 按需裁剪：

```bash
pip install fonttools brotli
pyftsubset SourceHanSansSC-Regular.otf \
  --text-file=常用字.txt --flavor=woff2 --output-file=subset.woff2
```

### 插画 / 头像

| 仓库 | 说明 | 许可证 |
|------|------|--------|
| [dicebear/dicebear](https://github.com/dicebear/dicebear) | 头像生成器，26 种风格，可 API 可离线 | 各风格不同，多数 CC0 / MIT |
| [microsoft/fluentui-emoji](https://github.com/microsoft/fluentui-emoji) | 微软 Fluent 表情，4000+ | MIT |
| [twemoji/twemoji → jdecked/twemoji](https://github.com/jdecked/twemoji) | Twitter 表情，风格统一（原仓库已迁移） | CC-BY 4.0（图形）/ MIT（代码） |

---

## 三个必须在动手前确认的事

1. **看 `LICENSE` 文件本身，不看 README 的一句话**。README 常写"free to use"，但可能只免费个人使用。
2. **区分"代码许可证"和"素材许可证"**：很多项目代码 MIT，但图标/插画另有许可（甚至只许非商用）。
3. **保留署名**：MIT / ISC / CC-BY 都要求保留版权声明。最稳的做法是把你用到的素材的 `LICENSE` 一起放进你的项目 `THIRD-PARTY-NOTICES.md`。

---

## 自己扩充素材库

```bash
# 只下图标，会自动更新 MANIFEST.json
python scripts/fetch_assets.py --only icons

# 想加别的图标：改 scripts/fetch_assets.py 里的 ICON_NAMES 列表即可
```

下载走 `api.github.com`，不需要 `git clone` 大仓库（tabler 全仓 1.1 GB，我们只取需要的几百个文件）。
