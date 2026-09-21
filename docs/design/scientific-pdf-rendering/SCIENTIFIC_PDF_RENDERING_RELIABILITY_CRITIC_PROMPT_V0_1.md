# Scientific PDF Rendering Reliability — Critic Handoff v0.1

把下面内容发送给独立 Critic thread。此文件只是 handoff prompt；被审 execution package 固定在 commit `9530e7b74d4312b990fa5b97a27f2d3dfaf65c4f`。

---

你是 AI Research Stack 的独立 Critic thread。现在审查一个新的 AI_Skills_Collection execution-ready package；不要实现代码，不要代 Planner 修改 Proposal，不要创建 branch/worktree，不要启动 paid API 或 automation。

## Active Review Context

target_repo: `YuukiAS/AI_Skills_Collection`  
target_plugin_or_domain: standalone `render-chinese-math-pdf` + bounded `research-writing` / Research Authoring integration  
design_topic_or_task_key: `documents-media--scientific-pdf-rendering-reliability`  
source_branch_or_ref: `main`  
review_stage: `EXECUTION_READY`  
package_commit: `9530e7b74d4312b990fa5b97a27f2d3dfaf65c4f`  
pre-package_main: `22fd8e5330cd669c19ba7edf3a523bdb27f84bb4`  
planned_execution_branch: `reviewed/documents-media--scientific-pdf-rendering-reliability`  
planned_execution_worktree: `/tmp/ai-skills-documents-media-scientific-pdf-rendering-reliability`

Proposal v0.1:
`docs/design/scientific-pdf-rendering/SCIENTIFIC_PDF_RENDERING_RELIABILITY_PROPOSAL_V0_1.md`

Canonical Goal v0.1:
`docs/goals/SCIENTIFIC_PDF_RENDERING_RELIABILITY_GOAL_V0_1.md`

Kickoff Draft v0.1:
`docs/operations/prompts/SCIENTIFIC_PDF_RENDERING_RELIABILITY_KICKOFF_V0_1.md`

这个 package 从 pre-package main 到 package commit 只有以上 Proposal / Goal / Kickoff 三个新增 docs 文件，没有 production source 变化。

## 强制读取

首次开始本轮审查，必须实际读取最新 main 的：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/PLUGIN_MATURITY.md`

然后实际读取：

- 上述 Proposal / Goal / Kickoff exact package；
- `docs/skill-todos/render-chinese-math-pdf.md`
- `docs/plugin-todos/research-writing.md`
- `skills/tools/documents-media/render-chinese-math-pdf/SKILL.md`
- `skills/tools/documents-media/render-chinese-math-pdf/scripts/build_chinese_math_header.py`
- `skills/tools/documents-media/render-chinese-math-pdf/scripts/probe_pdf_render_env.py`
- `skills/tools/documents-media/render-chinese-math-pdf/scripts/validate_pdf_layout.py`
- `skills/tools/documents-media/render-chinese-math-pdf/references/portable-rendering.md`
- `skills/tools/documents-media/render-chinese-math-pdf/references/checklists.md`
- `tests/test_render_chinese_math_pdf.py`
- `skills/writing/research/research-reporting/SKILL.md`
- `profiles/research-main.json`
- `profiles/presentation-desktop.json`
- `profiles/server-research-baseline.json`
- `scripts/codex_marketplace_config.json`
- `tests/test_codex_marketplace.py`
- `tests/test_research_writing_routing.py`

还要把下面这份旧架构方案作为 context 读取，但不要把它当成已 PASS 的冻结合同：

- `docs/design/RESEARCH_WRITING_PRODUCTION_REDESIGN_PLAN_V0_2_2026-09-07.md`

如果你需要核实历史“renderer 作为 support skill 装入 profile”的事实，可读取：

- `results/004_current_library_acceptance/RESULT.md`
- `results/004_current_library_acceptance/PLANNER_REVIEW.md`

## 用户目标

用户真实痛点不是“能不能生成一个 PDF”，而是：

1. 明明让 Codex 调用了 `render-chinese-math-pdf`，公式仍可能坏，甚至实际产物走 Chromium/Skia；
2. 用户第二次明确提醒后公式才正确；
3. 公式修好后，整份科研 report 仍显得不正式：字体纹理、margin、页面密度、标题/目录/编号等不统一；
4. 即使真正用了 XeLaTeX + canonical fonts，自制模板仍会因为 `\\small` / `\\footnotesize` / `tableline` 分类把普通正文缩小；
5. 用户不希望每次自己发现问题、再告诉 Codex怎么返修；正常入口应一次完成并自行 QA。

用户已经同意 Planner 方向：优先把它保留为独立共享 skill，不急着 rename，也不直接吞进 Research Authoring；但要求现在由 Planner 正式准备方案并交 Critic 攻击，不代表该方向已经获批准。

## 本轮 Proposal 的核心判断

Planner 选择：

- 保留 `render-chinese-math-pdf` 为 standalone shared renderer；
- canonical slug 本轮不 rename；
- 不新增中央 plugin；
- 不把 renderer 变成 Research Authoring 第四个 Marketplace skill；
- 把 canonical renderer orchestration 从 host-local resource script 收回 repo source；
- 继续使用 Pandoc + XeLaTeX，改成 declarative defaults + Pandoc AST 语义，而不是 ad-hoc `tableline` classifier；
- 加强 math/font/page identity / full-document visual QA；
- `research-main` profile 安装 renderer；
- `research-reporting` 在用户明确请求正式 PDF 时委托 renderer；Markdown-only 请求保持不变；
- standalone Research Authoring plugin 环境若没有 renderer，则 fail closed，不静默 fallback；
- production behavior完成并通过同一 final candidate G1–G7 后，计划 `research-writing 0.1 -> 0.2`，repository `5.0.6 -> 5.0.7`；Presentations NO_BUMP。

## 必须独立核查的外部现实

按 Critic contract 做你自己的针对性网络核查，不要只接受 Planner 的外部资料结论。至少独立核实：

1. Pandoc 官方 defaults/templates/AST/Lua filter 是否足以支撑 Proposal 的 semantic rendering 方案；
2. fontspec 官方 scaling 能否作为跨字体视觉协调的候选，而不是手工猜 scale；
3. Quarto/Typst 是否存在更成熟、明显更简单的现实替代，足以推翻继续 Pandoc/XeLaTeX 的判断。

优先官方文档：
- https://pandoc.org/MANUAL.html
- https://pandoc.org/lua-filters.html
- https://quarto.org/docs/reference/formats/pdf.html
- https://quarto.org/docs/output-formats/pdf-basics
- https://typst.app/docs/reference/pdf/
- https://typst.app/docs/reference/text/text
- https://ctan.org/pkg/fontspec

记录你实际采用/不采用什么，以及原因。

## 重点攻击，不要只找“更保险”的问题

请重点判断以下真实风险：

1. **方向是否正确**：根因到底是 missing production entry + template/QA discipline，还是 Pandoc/XeLaTeX 本身已经不值得保留？
2. **standalone vs Research Authoring integration**：只通过 `research-main` profile + `research-reporting` delegation 是否足够？还是 plugin-only 用户会继续缺 renderer，使“正常 Research Authoring PDF”仍不成立？如果你认为需要把 renderer 作为 internal shared payload 带进 plugin，必须说明最小实现，而不是简单要求“合并 skill”。
3. **历史 test 是否被误当产品合同**：`test_render_and_slurm_are_not_central_marketplace_skills` 是应继续保护的产品边界，还是旧实现约束，不能阻止更正确的 integration？
4. **Proposal 是否过重**：repo-owned wrapper + defaults + optional Lua filter + math AST inventory + all-page montage 会不会做成新的小框架？哪些机制能删而不丢能力？
5. **Proposal 是否过简**：Math AST node 数保留是否仍可能让最终公式视觉损坏？字体 allowlist 是否可能机械 PASS 但整体 typography 仍差？
6. **默认 style**：A4 / 11pt / 25mm / ~1.15 是否应在 design stage 冻结，还是只冻结“一个稳定默认 profile + real-render calibration”，具体值留给实现期 bounded calibration？
7. **页面身份与项目模板**：default profile 怎样避免覆盖 venue/project-owned template？retry stability怎样定义才不会误阻止用户明确改格式？
8. **G1–G7**：是否覆盖 normal entry、core behavior、input diversity、output quality、fidelity、should-not-change、complete artifact、production integration、qualitative review；是否有重复 gate 可以合并？
9. **G7 broad/full**：本轮涉及 shared skill + profile + Research Authoring source，但没有改 Presentations source；当前 broad/full regression范围是否恰当？
10. **版本决策**：`research-writing 0.1 -> 0.2` 和 repo patch `5.0.7` 是否真的由 user-visible behavior change支持；renderer 本身没有独立 plugin version时如何诚实记录？
11. **rename**：延后 canonical slug migration是否合理，还是 current scope 已经明显超出名字导致 routing风险，必须本轮解决？
12. **与旧 Research Authoring redesign 的关系**：本轮 bounded handoff 是否会提前冻结旧 v0.2 redesign尚未正式 PASS 的 artifact-adapter边界？如果有冲突，给最小关闭条件，不要顺手重做整个 Research Authoring architecture。

## 私有 artifact 边界

Planner此前看过用户提供的真实 PDF，并把可公开的 failure summary记录进 TODO；完整私有/未公开科研内容没有提交公开 repo。

如果你在当前 Critic thread 无法访问那些完整 PDF：

- 不得声称亲自复审；
- 先判断 repo TODO + source 是否足以审 architecture；
- 只有缺少像素级证据会实际阻止 execution-ready判断时，才 REVISE 并提出最小补证要求；
- 不要为了“更保险”要求把私有论文全文上传公共 repo。

## 输出要求

对这个 exact v0.1 execution package 给：

- `PASS` 或 `REVISE`
- complexity verdict：是否过重 / 过简 / 合适
- 每个 blocker（如有）必须包含：
  - stable finding ID
  - 对应用户要求 / repo contract
  - 直接证据
  - 因果风险
  - 最小关闭条件
  - owner
- non-blocking notes 单独列出，不得混成 blocker。

不要因为纯 SHA locator、Critic review 自己导致 main多一个 docs commit、或已有 latest-main preflight可处理的无关 drift而机械 REVISE。只审 production/architecture/验收/权限/恢复的实质风险。

如果 PASS，必须同时审查 Proposal + Goal + Kickoff 三者一致，并按 `CRITIC_ROLE_CONTRACT.md §6.1` 输出：

`APPROVED_PROPOSAL_PATH=`  
`APPROVED_GOAL_PATH=`  
`APPROVED_KICKOFF_PATH=`  
`APPROVED_COMMIT=9530e7b74d4312b990fa5b97a27f2d3dfaf65c4f`  
`READY_FOR_CODEX=YES`

然后逐字给出已经审过的 Kickoff 正文，不能临场另写一个语义不同的新 prompt。

如果 REVISE，按 Critic contract 自动生成下一条可直接复制给 Planner 的完整 prompt；不要让用户自己打开 GitHub 拼 blocker。
