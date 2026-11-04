# Codex：Phase A 静态证据准备（Asteria Blueprint / Atlas）

这是 Asteria Recovery + Frontend Design vNext 总路线的 Phase A 机械准备任务。  
本轮不是设计、不是审查、不是重新研究，也不是实现 Asteria。

先读取：
- `YuukiAS/AI_Skills_Collection@design/frontend-feedback-continuity-20261104`
  - `docs/design/frontend-design/ASTERIA_RECOVERY_FRONTEND_VNEXT_MASTER_PLAN_20261104.md`
  - `docs/design/frontend-design/PHASE_A_EVIDENCE_PACK_AND_REVIEW_QUEUE_20261104.md`
  - `docs/design/frontend-design/DESIGN_ASSURANCE_CLAUDE_ROLE_DECISION_20261104.md`

## 唯一目标

在 Mac mini 本地生成一个 Claude Stage 1 可以直接读取的**静态证据目录**。Claude 后续不得为了理解历史启动 Obsidian、浏览器、Figma 或网页预览。

本轮只做文件定位、静态图片整理、PDF 指定页渲染、联系表和 manifest。

## 输入仓库

### Blueprint

必须使用：

`YuukiAS/Asteria-Blueprint@archive/asteria-blueprint-version-gallery-20261103`

主要输入：
- `docs/design/version-gallery/manifest.json`
- `docs/design/version-gallery/VERSION_CATALOG.md`
- `docs/design/version-gallery/assets/sources/ChatGPT_Asteria-BluePrint-裁决_20261103-1638.pdf`
- `docs/design/version-gallery/versions/**`

不得修改该归档分支。

### Atlas

必须使用：

`YuukiAS/Asteria-Atlas@archive/atlas-visual-history`

主要输入：
- `visual-history/assets/contact-sheet.png`
- `visual-history/source/CATALOG.json`
- `visual-history/source/THREAD_TIMELINE_ZH.md`
- `visual-history/source/ChatGPT_建立文献地图架构_20261103-1749.pdf`
- `visual-history/assets/**`

不得修改该归档分支。

## 本地输出

创建或重建：

`/Users/yuukias/Code/Asteria-Phase-A-Evidence/`

目录只保存可再生的静态证据，不作为新的产品事实源。

建议结构：

```text
Asteria-Phase-A-Evidence/
  README.md
  MANIFEST.json
  SHA256SUMS.txt
  blueprint/
    contact-sheet.png
    priority/
    pdf-pages/
  atlas/
    contact-sheet.png
    priority/
    pdf-pages/
  pro/
    initial-pro-summary.md
    gpt56-pro-summary.md
```

若实际用户名或 Code 根目录不同，只调整根目录，最终报告真实路径。

## 1. Blueprint 36 版 contact sheet

从 `manifest.json` 读取全部 36 个 version。

每个格子使用该 version 的 `cover`；cover 缺失时显示明确的 `NO RECOVERED IMAGE` 占位，不允许借用其他版本图片。

每格只显示：
- order；
- version_id；
- 历史 verdict。

不要把历史 verdict 改写成新的好坏判断。

生成一张可读的 `blueprint/contact-sheet.png`。优先 6×6；若字体过小，可采用纵向多行，但仍保持单张总览。

不得启动浏览器重新截图；只使用归档中现有图片。

## 2. Priority 静态图复制

从 Phase A review queue 的“优先审阅”集合中，对每个版本复制一张最有代表性的现有静态图到本地 `priority/`。

Blueprint 优先集合：

```text
01-asteria-v2-concepts
05-showcase-r2-gpt56
06-showcase-r2-gpt6
09-evolution-pro-a
10-evolution-pro-b
11-next-pro-a
12-next-pro-b
13-blueprint-blind-pro-a
14-blueprint-blind-pro-b
18-system-direction-1
19-system-direction-2
20-system-direction-3
25-workbench-r1-1
26-workbench-r1-2
27-workbench-r1-3
28-workbench-r1-4
36-gpt6pro-total-redesign
```

Atlas 优先集合：

```text
V01 V02 V03 V04 V05 V06 V07 V08 V10
```

Atlas 图片来源必须从 `CATALOG.json` 的已有 assets 中选；不启动 Obsidian补图。

文件名需保留 version id，例如：
`V05__01-domain-overview.png`。

## 3. PDF 关键页静态渲染

使用 `pdftoppm`、PyMuPDF 或等价本地工具，只渲染以下页；禁止 OCR，禁止整本重新渲染。

Blueprint：

```text
172 176 196 198 203 207 227 230
```

Atlas：

```text
138 139 165 180 181 198 199 208
```

每页 150–180 DPI PNG 即可。文件名固定：
`p0172.png`、`p0138.png` 等。

这些页用于让 Claude 同时看到关键历史画面与邻近用户反馈上下文，不代表只有这些页具有事实权威。Stage 1 后续若出现具体争议，才按页追加。

## 4. 两位 Pro 摘要

不要重新研究。

直接从以下已提交报告提取/复制执行摘要：

第一位 Pro：
`YuukiAS/Asteria-Blueprint@research/claude-handoff-initial-pro-20261104`
`docs/research/claude-handoff-20261104/initial-pro/EXECUTIVE_SUMMARY_ZH.md`

GPT-5.6 Pro：
`YuukiAS/Asteria-Blueprint@research/claude-independent-pdf-gate-gpt56-20261104`
`docs/research/claude-handoff-20261104/gpt56/EXECUTIVE_DECISION_ZH.md`

保存到本地 `pro/`。原文复制，不重写结论。

## 5. MANIFEST

`MANIFEST.json` 至少记录每个本地文件：
- project；
- version_id / pdf_page / report；
- original repo；
- original branch/ref；
- original relative path；
- local relative path；
- sha256；
- evidence_type；
- historical_verdict；
- user_decision：固定为 `OPEN`，不得自行填写。

`README.md` 只解释：
- 这是 Phase A 可再生静态证据；
- 真实权威仍在原仓库与原始 PDF；
- Claude Stage 1 应优先看 contact sheet + priority + 指定 PDF 页；
- Claude 不应启动 GUI 应用重新采集。

## 6. 验证

必须确认：
- 36 个 Blueprint version 都在 contact sheet 有位置；
- Atlas 原 contact sheet 成功复制；
- 17 个 Blueprint priority 版本都有图；没有图则明确列为缺失；
- 9 个 Atlas priority 版本都有图；没有图则明确列为缺失；
- Blueprint 8 个 PDF 页全部存在；
- Atlas 8 个 PDF 页全部存在；
- 两份 Pro 摘要存在；
- 所有 manifest 路径真实可读；
- SHA256 与生成后的实际文件一致。

## 严格禁止

- 不启动 Obsidian；
- 不启动浏览器或 Playwright；
- 不打开 Figma；
- 不调用 Claude；
- 不重新做 Deep Research；
- 不修改任何 Asteria 产品设计；
- 不改变历史 verdict；
- 不把候选标成用户 `KEEP`；
- 不修改两个 archive 分支；
- 不提交大批重复二进制到 GitHub；
- 不创建新的工作流、数据库、插件或管理系统。

## 最终只汇报

```text
PHASE_A_STATIC_PACK = PASS | BLOCKED
LOCAL_ROOT = ...
BLUEPRINT_CONTACT_SHEET = ...
BLUEPRINT_PRIORITY = <n>/<17>
ATLAS_CONTACT_SHEET = ...
ATLAS_PRIORITY = <n>/<9>
BLUEPRINT_PDF_PAGES = <n>/8
ATLAS_PDF_PAGES = <n>/8
PRO_SUMMARIES = <n>/2
MANIFEST = ...
GUI_APPS_LAUNCHED = NO
PRODUCT_REPOS_MODIFIED = NO
BLOCKERS = ...
```
