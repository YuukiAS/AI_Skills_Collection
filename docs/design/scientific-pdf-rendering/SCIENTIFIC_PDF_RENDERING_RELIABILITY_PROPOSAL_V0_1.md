# Scientific PDF Rendering Reliability — Planner Proposal

**Version:** v0.1  
**Status:** READY FOR INDEPENDENT CRITIC REVIEW / NOT EXECUTION AUTHORIZATION  
**Date:** 2026-09-21  
**Target repository:** `YuukiAS/AI_Skills_Collection`  
**Source branch/ref reviewed:** `main` at pre-package baseline `22fd8e5330cd669c19ba7edf3a523bdb27f84bb4`  
**Target skill/domain:** standalone `render-chinese-math-pdf` + bounded Research Authoring integration boundary  
**Task key:** `documents-media--scientific-pdf-rendering-reliability`  
**Planned execution branch:** `reviewed/documents-media--scientific-pdf-rendering-reliability`  
**Planned task-owned worktree:** `/tmp/ai-skills-documents-media-scientific-pdf-rendering-reliability`

This proposal is a Planner design package. It does not modify production skills, generated Marketplace payloads, profiles, versions, or runtime behavior. Only an independent Critic PASS on this exact package may make the later Goal/Kickoff execution-ready.

## 1. 结论先行

本轮不把 `render-chinese-math-pdf` 合并进 Research Authoring，也不立即改 canonical slug。它继续作为一个跨项目、跨上层产品复用的独立渲染 skill；这轮真正要修的是三件事：

1. **把 production renderer 从“文档里要求这样做”升级为 repo-owned、可验证、不可静默绕过的正常入口。**
2. **把“能生成 PDF”升级为“数学保真、字体一致、页面稳定、正式可读的科研/技术 PDF”。**
3. **让 Research Authoring 在合适的 profile/正常工作流中自动委托给这个 renderer，而不是要求用户手工点名 skill；但不在当前尚未收口的 Research Authoring 总体重构前，擅自把 renderer 变成第四个 Marketplace 用户入口。**

canonical slug `render-chinese-math-pdf` 在本轮保持不变。其 description / trigger 可以扩大为“Markdown/LaTeX 科研技术 PDF 渲染，特别保证 CJK 与数学”，但 rename/migration 只在这轮真实能力稳定后另行评估。

## 2. 已验证的真实问题

当前 `docs/skill-todos/render-chinese-math-pdf.md` 已记录四类真实失败：

- 用户明确让 Codex 调用 skill，最终产物仍由 HeadlessChrome/Skia 生成，违反当前 skill 自己声明的 `Markdown -> Pandoc -> XeLaTeX -> PDF` 默认路线；
- 第一版 PDF 的公式结构已经损坏，但现有 validator 仍没有 source-to-render math fidelity 检查；
- 同一报告的重渲染从 A4 / 17 页漂移到 US Letter / 24 页，用户没有要求改变页面身份；
- 即使真正使用 XeLaTeX、canonical 字体和数学字体，生成模板仍可通过 `\\small`、`\\footnotesize`、`\\section*` 与启发式 `tableline` 分类把普通正文缩小，导致技术正确但视觉不统一。

当前 source 也证明“规则已写但未落实”：

- `SKILL.md` 已明确默认 renderer 为 Pandoc + XeLaTeX，禁止 Chromium 静默 fallback；
- `build_chinese_math_header.py` 已固定 TeX Gyre Termes / Termes Math / Noto Serif SC / Noto Sans SC；
- `validate_pdf_layout.py` 只检查页数、嵌入字体、CJK ToUnicode、文本提取、表格 survival 与第一页 preview，不验证 canonical font allowlist、数学结构、全页视觉一致性或页面身份稳定；
- production entry 仍指向 repo 外的 `render_resources/chinese_math_pdf/scripts/render_markdown_pdf.sh`，所以“skill source”与“真正执行逻辑”分离；
- `research-main` profile 当前没有安装 renderer，而 `presentation-desktop` 与 `server-research-baseline` 已安装；
- `research-reporting` 明确不实现低层 PDF/LaTeX mechanics，这个边界本身正确，但当前没有稳定的自动 handoff；
- `tests/test_codex_marketplace.py` 明确保护 renderer 不进入中央 Marketplace config，这说明历史架构有意把它保持为 support skill，而不是中央 plugin user entry。

## 3. 产品目标

正常用户不应再经历：

> “先让 Codex 渲染 → 公式坏 → 用户指出 → 改成 XeLaTeX → 字号又乱 → 用户继续指出”。

目标用户体验是：

> 用户给出 Markdown/LaTeX 或让 Research Authoring 产出报告并要求 PDF → 系统一次选择正确 renderer → 公式/表格/字体/页面身份通过可观察 QA → 完整 render 经实际视觉检查后才交付。

本轮完成后应新增这些真实能力：

- 独立 renderer 能处理中文、英文或中英混合的科研/技术 Markdown/LaTeX，只要任务是“生成正式 PDF”，用户不必知道内部 engine；
- CJK/math 仍是重点保证，但 skill 不再因为输入是英文科研 note 就错误地退回 generic/browser route；
- PDF 的默认页面与排版 profile 是单一、可追踪、稳定的，不会因 retry 静默从 A4 变 Letter；
- 普通正文不会因为“看起来像表格”就被自动缩成 `\\footnotesize`；
- 数学是否在 source → Pandoc AST → generated TeX → final PDF 之间存活，有直接证据，不只靠“pdftotext 能抽出一些字符”；
- Research Authoring 的 `research-main` profile 自动带 renderer，`research-reporting` 在用户要求 PDF 时明确委托给 renderer；若 standalone Marketplace plugin 环境没有 companion renderer，则 fail closed 并说明缺哪个 companion，而不是私自走 Chromium。

## 4. 不做什么

本轮明确不做：

- 不 rename `render-chinese-math-pdf` canonical slug；
- 不新增第 11 个中央 plugin；
- 不把 renderer 合并进 `research-writing` source tree；
- 不把 renderer 作为 Research Authoring 第四个 Marketplace 用户入口；
- 不重做整个 `RESEARCH_WRITING_PRODUCTION_REDESIGN_PLAN_V0_2_2026-09-07.md`；
- 不修改 Clear Writing 的语言能力；
- 不让 Presentations 承担本轮主 owner；
- 不引入 Typst/Quarto 作为新的 production dependency；
- 不下载新的字体 corpus；
- 不新增 schema、ledger、persistent state 或新的 workflow；
- 不启用 paid API / Terra；
- 不把 synthetic fixture PASS 当正式完成。

## 5. 五遍预检

### 5.1 Product

用户消费的是最终 PDF，而不是 `pandoc` exit code。成功必须同时包含：

- 正确的 production engine；
- 数学/表格/文本语义存活；
- 稳定的纸张与页面几何；
- 中英数公式字体视觉协调；
- 没有因错误分类把普通内容缩小；
- 完整文档实际 render 可读；
- Research Authoring handoff 不要求用户手工点名 renderer。

### 5.2 Reality

当前 skill 已有可复用资产，不需要推倒重来：

- bundle-local TeX Gyre + Noto 字体；
- XeLaTeX 环境 probe；
- header builder；
- PDF text/font/table validator；
- trigger eval；
- source/profile installer；
- 现成的 PDF page-to-image helper 能力在通用 `pdf` skill 中存在。

真正缺的是 repo-owned production orchestration、semantic block handling、math fidelity evidence 与视觉 acceptance。

### 5.3 Alternatives

#### A. 维持现状，只继续加 prompt/checklist

**不采用。** 四个真实 failure 已证明规则存在但 consumer/runtime 仍能绕过。继续写同义文字不能保证执行路径。

#### B. 把 renderer 彻底并入 Research Authoring

**本轮不采用。** renderer 同时被 presentation/server workflows 使用，属于共享 artifact capability；而 Research Authoring 总体 redesign 尚未最终冻结。合并会把文档语义 owner 与文件渲染 owner 混回一起。

#### C. 直接改成 Quarto

**REFERENCE_ONLY。** Quarto 的 PDF 配置成熟，明确支持 `mainfont`、`mathfont`、`CJKmainfont`、`fontsize`、`papersize`、`geometry`、`linestretch`，并默认使用 KOMA-Script 强调 typography。这证明“排版 profile 应由声明式文档配置管理”是成熟路线。但当前 repo 已有 Pandoc/XeLaTeX + bundled fonts + tests；为了这批 failure 引入新 runtime 依赖会扩大 blast radius，且不能直接解决现有 skill invocation 未消费 production path 的根因。  
Reference: https://quarto.org/docs/reference/formats/pdf.html ; https://quarto.org/docs/output-formats/pdf-basics

#### D. 迁移 Typst

**REVIEWED_NOT_ADOPTED for this round。** Typst 原生输出 PDF、支持 OpenType math 与字体 fallback，长期值得保留为替代路线；但迁移会改变 Markdown/LaTeX compatibility、公式输入与现有资源链，当前没有证据证明 XeLaTeX 本身是根因。  
Reference: https://typst.app/docs/reference/pdf/ ; https://typst.app/docs/reference/math/ ; https://typst.app/docs/reference/text/text

#### E. 保留 Pandoc/XeLaTeX，但把 template/defaults/AST 正式化

**采用。** Pandoc 官方已经提供 defaults files、templates 与 AST filters；Lua filter 可直接识别 `Header`、`Para`、`Table`、`Math` 等真实语义节点，不需要发明 `tableline` 这种字符串启发式。  
Reference: https://pandoc.org/MANUAL.html ; https://pandoc.org/filters.html ; https://pandoc.org/lua-filters.html

字体协调优先使用 fontspec 的标准 scale 机制（如 `Scale=MatchLowercase` / `MatchAveragecase`）做候选，并以真实 render 判断，而不是手工猜视觉倍率。  
Reference: https://ctan.org/pkg/fontspec ; https://tug.ctan.org/macros/unicodetex/latex/fontspec/fontspec.pdf

### 5.4 Red Team

重点防这些假修复：

1. 新 wrapper 存在，但 Codex 仍直接运行旧 host script；
2. wrapper 自报 XeLaTeX，最终 PDF 实际还是 Chrome/Skia；
3. math node 数没丢，但 glyph/render 视觉仍坏；
4. exact font allowlist 通过，但 CJK 与 Latin apparent size 明显失衡；
5. 为避免表格 overflow，普通段落仍被错误缩小；
6. 每个页面单独可读，但整份 20+ 页 PDF density、heading rhythm、title/TOC 重复仍不正式；
7. A4/11pt 等只写在文档，没有真正成为 production defaults；
8. retry 只因 formula repair 就改变 papersize/margins/numbering；
9. research-main profile 安装了 renderer，但 research-reporting 仍不调用；
10. standalone Research Authoring 缺 renderer 时静默 fallback 到 browser；
11. 为了通过 fixture 写 test-specific hardcode；
12. 修改 shared renderer 后把 Presentations 现有 Beamer route 弄坏；
13. 为解决视觉一致性强行让中文、英文、数学使用同一个 font file；
14. broad/full release gate 用 unittest/CI 冒充完整 artifact 视觉质量；
15. fresh/independent review 首次发生在不可恢复的最后一步。

### 5.5 Execution

执行应是一次 bounded refinement，不拆 successor：

`repo-owned renderer -> declarative style profile -> semantic AST handling -> validator hardening -> Research Authoring/profile handoff -> regression/full render review -> version/changelog/release closure`

如果 implementation 暴露 XeLaTeX 本身无法达到正式文档质量，再回 Planner/Critic 讨论 Typst/Quarto，不允许 Executor自行迁移。

## 6. 目标架构

### 6.1 Canonical production entry 归 repo

新增一个 repo-owned renderer entry，例如：

`skills/tools/documents-media/render-chinese-math-pdf/scripts/render_scientific_pdf.py`

它成为 canonical Markdown/LaTeX → PDF orchestration entry；repo 外 `render_resources/chinese_math_pdf` 只保留 **fonts / texmf / host-local resources**，不再拥有 canonical business logic。

默认 Markdown route：

`Markdown -> Pandoc reader -> Pandoc AST -> optional bounded semantic Lua filter -> LaTeX -> XeLaTeX -> PDF -> QA`

禁止自动 Chromium fallback。Chromium helper继续保留为显式 diagnostic route。

### 6.2 单一 declarative formal-note profile

不要让每个任务自己拼模板。新增一个 repo-owned Pandoc defaults/template profile，职责仅限：

- default paper identity；
- body font size / line spacing；
- margins；
- title metadata；
- section numbering policy；
- table/figure baseline；
- font header。

建议 v0.1 default：

- paper: A4；
- body: 11pt；
- margins: 25mm baseline；
- line spacing: 约 1.15；
- auto TOC: off；
- auto section numbering: off，除非 source/user 明确请求；
- body paragraphs: 不因 heuristic block class 改字号；
- true table/caption/footnote 才允许语义上不同字号；
- actual table 如正常尺寸 overflow，允许 bounded table-only repair；不得把普通 prose 自动降为 `\\footnotesize`；
- source/user/project metadata 可覆盖 default，但 rerender 必须保持同一 resolved profile，除非请求本身改变。

这些 exact defaults 在已知 regression development 中可以做一次有证据的微调；进入 pre-final Critic 前必须冻结，不能在 final candidate 间继续漂移。

### 6.3 语义块由 Pandoc AST 决定

不再根据抽取文本行形状定义 `tableline`、`listline` 等排版语义。

优先使用：

- `Header`
- `Para`
- `BulletList/OrderedList`
- `Table`
- `Math`
- `CodeBlock`
- `Figure`
- `BlockQuote`

Lua filter 只在 Pandoc 默认 writer 不能满足明确需求时使用，并且只处理 AST 节点，不重新发明字符串 parser。

### 6.4 标题与编号冲突必须 fail/warn，不静默叠加

- YAML `title` 是 title metadata；
- H1 默认是 section，不重复提升为 title；
- auto numbering 默认关闭；
- 如果 source 已有手工 `1.` / `2.` heading 且又请求 auto numbering，renderer 应显式报告 conflict 或要求一个明确策略，不能产出 `2.1 1. ...`。

### 6.5 字体是“协调系统”，不是“一个字体文件”

默认仍保留：

- Latin: TeX Gyre Termes；
- Math: TeX Gyre Termes Math；
- CJK serif: Noto Serif SC；
- CJK sans/mono fallback: Noto Sans SC。

但加入 fontspec scale/metrics-based harmonization，验证 apparent size / weight / baseline，而不是要求一个 font file 覆盖所有 script。默认 route 的 `pdffonts` 应拒绝意外 Liberation / DejaVu / Droid fallback；显式 project-owned template route可以使用别的字体，但必须可追踪，不得被误判成 canonical default PASS。

### 6.6 Math fidelity 分成 deterministic 与 visual 两层

Deterministic：

- 用 Pandoc JSON/AST 统计并定位 source `Math` nodes；
- 生成 LaTeX 后确认对应 math nodes 未被转换成普通 prose/code；
- known regression fixture覆盖 inline/display math、hat/subscript/superscript、sum/integral/gradient、Greek、matrix、`\\mathbb`、长公式、中文邻接公式；
- 编译错误直接 fail。

Visual：

- equation/table-heavy page 必须 raster；
- final candidate 必须观察实际公式页面，不接受只有 `pdftotext` 证据。

不引入 OCR 作为常规 math validator。

### 6.7 全文 render QA，而非第一页 QA

对完整 PDF：

- `pdfinfo`；
- `pdffonts`；
- `pdftotext -layout`；
- all-page PNG / validation montage；
- overflow/bounding-box check 可复用通用 PDF skill 的成熟 helper，而不是再造低配版本；
- qualitative review直接看完整 montage，并在需要时打开高风险页。

长文可根据页数生成分块 montage，但不能只检查第一页。

### 6.8 Research Authoring 只做 handoff，不吞并 renderer

本轮修改 `research-reporting` 的 boundary/workflow：

- Markdown-only request：正常停止于 Markdown；
- 用户明确要求 PDF / final formal PDF：document semantics 冻结后委托 `render-chinese-math-pdf`；
- renderer 未安装：报告 companion dependency，不自行写另一套模板，不静默 browser fallback；
- renderer 只处理 artifact mechanics，不重新决定科学结构、claim/evidence、表格语义。

`research-main` profile 加入 renderer，保证 source-profile 正常科研工作流无需用户手工安装。

**本轮不修改 `scripts/codex_marketplace_config.json` 的 skill membership。** 现有“renderer 不进入中央 Marketplace source set”的 test 保留。只因 `research-reporting` production source发生 user-visible handoff 改进，正式 release 时 Research Authoring plugin version需要按版本政策推进。

## 7. 预计 production 修改范围

允许的主要 source：

- `skills/tools/documents-media/render-chinese-math-pdf/**`
- `skills/writing/research/research-reporting/SKILL.md`
- `profiles/research-main.json`
- `tests/test_render_chinese_math_pdf.py`
- `tests/test_research_writing_routing.py`
- 必要的 profile/Marketplace/version parity tests
- `scripts/codex_marketplace_config.json` **仅允许 Research Authoring version bump，不允许把 renderer 加入 plugin skill membership**
- generated registry/catalog/Marketplace layer，只能由现有 generator生成
- `docs/skill-todos/render-chinese-math-pdf.md`
- `docs/plugin-todos/research-writing.md`
- `docs/plugin-changelogs/research-writing.md`
- `CHANGELOG.md`
- `README.md`（closure 显式检查；若 research-writing version/capability发生变化则同步）
- task/result evidence path

禁止顺手修改：

- Clear Writing production source；
- Presentations production source；
- Bridge Kit；
- workflow-core / ai-skills-core architecture；
- Host Policy；
- unrelated profiles；
- private project research content。

## 8. Capability Gate Matrix

| Gate | Capability / claim | Why distinct | Normal entry | Required evidence | Failure | Regression boundary | Final candidate |
|---|---|---|---|---|---|---|---|
| G1 Production route identity | 普通 PDF render 请求真实走 repo-owned Pandoc+XeLaTeX route | 防“调用 skill 但没消费 production path” | “把这份 Markdown 渲染成正式 PDF” | canonical entry command + actual PDF；无 Chrome/Skia；missing XeLaTeX 时 fail closed | browser fallback、host-only script成为唯一逻辑、fake PASS | 保留显式 Chromium diagnostic | YES |
| G2 Source/math/font fidelity | source math/table/text 不被破坏，canonical default font chain真实生效 | 语义正确不同于 engine identity | mixed CJK/English/math fixture | Pandoc AST math inventory + generated TeX + actual PDF + canonical font check + equation page render | math node丢失、raw math、wrong fallback fonts、glyph failure | 现有中文提取/table survival继续通过 | YES |
| G3 Formal typography & semantic blocks | 正文层级、字号、页面 density、跨 script texture 正式且一致 | “不坏”不等于“正式可读” | complete research/technical note | all-page render；Para/Table/Header语义；pseudo-table prose不缩小；独立定性 review | `tableline` 类误判、正文 footnotesize、title/TOC/numbering重复、明显字体纹理割裂 | 真表格/脚注仍可用合理小字号 | YES |
| G4 Stable document identity | retry 不静默改变 paper/margin/numbering/profile | 对应真实 A4→Letter 漂移 | same source repeated render + bounded formula repair | resolved profile一致；page size/margins/numbering stable；deterministic repeated output at semantic level | 无请求却改变 A4/Letter、margin、auto numbering | explicit user/project override仍允许改变 | YES |
| G5 Research Authoring handoff | Research Authoring profile用户不需手工点 renderer；plugin-only 缺 companion 时诚实阻断 | integration 与 standalone core不同 | “整理成给老师看的报告并输出 PDF” | `research-main` clean install含 renderer；research-reporting明确 delegate；正常 replay实际使用 canonical renderer | 仍手工点名；另写模板；缺 skill时 browser fallback | Markdown-only report不被强制 PDF | YES |
| G6 Input diversity & compatibility | renderer不只针对一份私有失败，也不抢 generic PDF manipulation | 防 fixture hardcode / trigger过窄 | English technical note + mixed CJK/math note + explicit diagnostic | trigger eval + complete renders + generic existing-PDF tasks仍归 `pdf` | 英文 note不能正式渲染；generic PDF extract误触 renderer | `pdf` skill现有边界保持 | YES |
| G7 Broad/full release integrity | profile/shared skill改动没有破坏 Marketplace、Presentations、installer、generated parity | policy要求 profile/shared behavior用 broad/full gate | full repo release path | targeted tests → full unittest → skills validate/audit → generator check/path report → research-main + presentation-desktop/server smoke；same final candidate | 不同 commit 拼 evidence、generated drift、presentation profile regression | ten-plugin topology、presentations plugin version/source不变 | YES |

### Gate lifecycle / regression bank

四个已知 TODO failure 不新建四个 gate：

- Chromium bypass → G1；
- math/font validator miss → G2；
- A4/Letter drift → G4；
- XeLaTeX 成功但 typography 不统一 → G3。

Research Authoring handoff 是不同 normal entry / owner boundary，因此独立 G5。G6覆盖 generalization/should-not-change，G7覆盖 shared/profile/release blast radius。

执行顺序：cheap deterministic regression bank → known complete renders → full repo/profile smoke → pre-final Critic whole-artifact review → frozen final candidate gates。无 paid gate。

## 9. 真实 artifact / reviewer 计划

已知用户提供的 2026-09-19/20 PDFs 是 development regression，不得再称 fresh。

开发期必须至少有：

1. known math-corruption structure fixture；
2. known pseudo-table / typography regression fixture；
3. complete mixed Chinese/English/math research-note fixture；
4. English-only technical-note fixture；
5. should-not-change generic PDF task。

最终放行前 Critic 必须实际看到 final candidate 的完整 PDF render/montage，而不是只看 test log。若私有原始报告不可安全进入 repo，则不复制到公开路径；可以用 repo-safe regression fixture + private/exports 中已获授权且可访问的完整 artifact。若 pre-final 时 Critic拿不到私有完整 render，则该私有 artifact不能被声称已独立审查，但不因此阻止使用公开/仓库可达的完整 representative artifact。

不要求 Terra 或 paid external review。

## 10. 版本、README、发布

若本轮按 Proposal 实现并形成正式 release：

Repository bump decision: **PATCH**  
Planned: `5.0.6 -> 5.0.7`  
Reason: compatible rendering/profile/research-authoring improvement，不增加中央 plugin 数，不改变 repository-level contract。

Affected plugins:

- `research-writing`: `0.1 -> 0.2`
  - Reason: `research-reporting` 获得 user-visible、source-authoritative PDF handoff contract，并通过 normal profile replay。
- `presentations`: **NO_BUMP**
  - Reason: 本轮不改 Presentations plugin source/Marketplace payload；只要求 shared renderer improvement 不破坏其已有 companion behavior。
- 其他中央 plugin: **NO_BUMP**。

Standalone skill 无独立 plugin version。

README checked:
- research-writing version 必须同步；
- 若人类可见能力描述因正式 PDF handoff 需要调整，同一 release更新；
- 若最终 Critic要求不发布 plugin behavior change，则记录 `README checked: no update required`。

Maturity：**不自动改变**。一次 renderer release 不能把 Research Authoring 从 `unclassified` 提升到 alpha/stable。

## 11. 恢复与停止条件

如果出现以下情况，Executor停止扩 scope并回 Planner：

- repo-owned Pandoc/XeLaTeX route 在代表性完整任务上无法达到可接受 typography；
- 需要 Typst/Quarto 才能解决根因；
- renderer 必须进入 Research Authoring Marketplace payload 才能实现正常入口；
- 需要改变 Presentations production source；
- 需要新字体/受限资源/网络下载；
- 需要 private source 新授权；
- 需要 paid model；
- exact default profile被证据证明不适合且要改变产品语义；
- Research Authoring redesign v0.2 的未决架构与本 handoff产生实质冲突。

普通 code bug、test failure、LaTeX package path问题、fixture调整在 frozen scope 内由 Executor自行修复，不回用户逐条验收。

## 12. 外部研究采用结论

- **Pandoc defaults/templates：ADOPT。** 用成熟声明式配置替代任务内模板拼装。
- **Pandoc AST/Lua filters：SELECTIVELY_ADOPT。** 只解决真实 block semantics，不造复杂转换框架。
- **fontspec scaling：SELECTIVELY_ADOPT / REAL-RENDER VALIDATED。** 只在实际视觉改善时进入 final。
- **Quarto：REFERENCE_ONLY。** 采用其“PDF typography 参数是正式配置”的思想，不引入 runtime dependency。
- **Typst：REVIEWED_NOT_ADOPTED。** 保留为 XeLaTeX 路线被真实证据否定后的后续替代，不并行实现两套。
- **自研字符串 block classifier：REJECT。**

## 13. Critic 需要重点攻击的地方

1. standalone skill继续独立、只通过 profile/handoff集成，是否过于保守？是否真的能满足“Research Authoring 正常入口不用用户点 skill”？
2. 不把 renderer 直接加入 Research Authoring Marketplace payload，是否留下 plugin-only 场景的能力缺口，还是合理的 fail-closed boundary？
3. repo-owned renderer + Pandoc defaults + semantic AST 是否足够简单，还是仍然过重？
4. A4/11pt/25mm/1.15 作为 default baseline 是否应冻结，还是只应冻结“稳定 profile机制”而不冻结 exact values？
5. G2 math fidelity 是否足够直接，是否会被“AST没丢但最终公式视觉错”钻空子？
6. G3 qualitative review 是否有直接 artifact evidence，而不是机械指标代理？
7. G7 broad/full gate是否过重/过简？
8. research-writing `0.1 -> 0.2` 与 repository `5.0.7` release决策是否符合现行 version policy？
9. 是否需要把 Presentations 视为 affected plugin bump，还是 NO_BUMP + should-not-change gate足够？
10. rename 延后是否合理，或 canonical slug 已严重误导到值得本轮一起迁移？

