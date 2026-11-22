<!-- OPENWIKI:START -->

## OpenWiki

This repository has a generated `openwiki/` evidence index. It is optional just-in-time context, not required startup reading.

- Do not enumerate, preload, or search wikis at task start. Use retrieval when the user asks for it, when unfamiliar architecture or dependency behavior materially affects the task, or when source inspection leaves an important uncertainty. Stop once the question is grounded.
- When those conditions apply and OpenWiki retrieval tools are available, use `openwiki_search` for just-in-time context and `openwiki_read` for the relevant complete sections. If search returns `workspace_required`, ask which listed workspace to use and retry with its ID.
- Use `openwiki_list_workspaces` or `openwiki_list_wikis` when workspace membership itself needs to be discovered.
- If the retrieval tools are unavailable, read `openwiki/quickstart.md` and follow its links to the relevant pages.
- Treat source code and tests as authoritative. A brief's unknowns and review items are verification gaps, not automatic requirements.
- Prefer the narrowest quiet validation that proves the changed behavior. Preserve complete failure output.

Use the repository's documented maintenance process to refresh generated pages after source changes. Check its configuration and completed runs before relying on automatic updates. Do not hand-edit generated OpenWiki pages unless explicitly asked; prefer updating source code/docs and letting OpenWiki regenerate.

<!-- OPENWIKI:END -->

<!-- DSH-LOCAL:START -->
## 在本机 DeepSeek Harness（DSH）里怎么用这个知识库

- 本机 DSH **没有** `openwiki_search` / `openwiki_read` 这些工具；上面第 8–10 行说的是别的 coding agent。DSH 里直接读文件：先读 `openwiki/quickstart.md`，再顺着链接进具体页面。
- 面板入口在 DSH 左下角「📚 openwiki知识库」，选中本仓库工作区后点「刷新」即可看到整棵树；「知识卡片」Tab 是按文件溯源的知识点。
- 生成/更新也在面板里点「生成」；`~/.openwiki/.env` 已配好模型（openai-compatible / deepseek-flash）。
- 页面是生成物：改内容请改源码或文档再重新生成，不要手改 `openwiki/*.md`。
<!-- DSH-LOCAL:END -->
