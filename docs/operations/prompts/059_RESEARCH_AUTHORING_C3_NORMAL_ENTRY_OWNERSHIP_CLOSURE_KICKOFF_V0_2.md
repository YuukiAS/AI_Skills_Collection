# 059 Research Authoring C3 正常入口所有权收口 — Kickoff Draft v0.2

状态：DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW / NOT_AUTHORIZED  
日期：2026-10-06

只有独立 Critic 对本执行包给出 execution-ready PASS，并逐字批准本 Kickoff 后，用户实际发送批准正文，才形成实现授权。

## Bound objects

Repair Proposal：

docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_PROPOSAL_V0_1_2026-10-06.md  
@ b4820e49e3473959010afe5fa1e9f92bc0f4844f

Implementation Plan：

docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_IMPLEMENTATION_PLAN_V0_2_2026-10-07.md  
@ 04272c05c59ec90ee068b0d5da8d7a02beee3afa

Canonical Goal：

docs/goals/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_GOAL_V0_2.md  
@ 539ed6114dc861b129b6808b3b9a57c2763b7242

Capability Gate impact：

docs/design/059_RESEARCH_AUTHORING_C3_CAPABILITY_GATE_IMPACT_V0_2_2026-10-07.md  
@ 164051ebde003354e1303a086214a109c8f595bf

Prior execution-ready Critic review：

docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_EXECUTION_READY_CRITIC_REVIEW_V0_1_2026-10-07.md  
@ 75df537cd5f167e9df8afae9670a993cef137b58

This v0.2 only closes blocker RA-C3ER1; the main repair architecture and authorization ceiling are unchanged.

ChatGPT Plugin offline preparation：

docs/operations/059_RESEARCH_AUTHORING_C3_CHATGPT_PLUGIN_PREPARATION_V0_1.md  
@ 6320925c0b3a08f480d56f69908c40edd3b6d03e

## Kickoff正文

继续同一个 059 task，不开 successor，不重做架构。

Repository：

YuukiAS/AI_Skills_Collection

Task：

research-authoring--formal-production-authoring

Branch：

work/research-authoring--formal-production-authoring

Worktree：

/overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring

Permanent failed candidate：

C2=ac501d988f00cb6672fec105ae5fd51a0679cae0

C2 G1 FAIL必须永久保留，不能追认成PASS。

开始前：

1. 在 exact worktree 核实 repository/origin/branch/dirty ownership，并 fetch origin main；
2. 读取 current AGENTS.md、workflow-core、ai-skills-core、Research Authoring 当前 source，以及上述 Critic failure authority 和本执行包；
3. 不修改 candidate_plugin_replay shared infrastructure；
4. 不修改 Bridge Kit；
5. 不启动 final G1-G4。

## 允许的 production source修改

Research Authoring：

- skills/writing/research/research-authoring-core/SKILL.md
- skills/writing/research/research-reporting/SKILL.md
- skills/writing/research/paper-workflow-orchestrator/SKILL.md
- skills/writing/research/latex-paper-authoring/SKILL.md

Renderer：

- skills/tools/documents-media/render-chinese-math-pdf/SKILL.md

Profiles/routing：

- profiles/research-main.json
- profiles/codex-research-writing.json
- scripts/codex_marketplace_config.json

Tests：

- tests/test_research_writing_routing.py
- tests/test_render_chinese_math_pdf.py
- directly required existing Marketplace/version parity tests only.

Release-candidate docs/metadata as required by current repository policy：

- docs/plugin-changelogs/research-writing.md
- docs/skill-todos/render-chinese-math-pdf.md
- root CHANGELOG Unreleased candidate entry
- README standalone renderer version/card only if renderer candidate version changes
- source/generated registry/catalog/provenance/version parity produced by current generators.

README changes require actual Clear Writing review before commit.

## 必须实现的所有权机制

不要再加一层 G1专用禁止句。

实现：

~~~text
Research Authoring canonical owner/handoff boundary
+ renderer discovery/trigger boundary
+ research-main / codex-research-writing profile routing authority
~~~

### Renderer discovery

render-chinese-math-pdf 应直接匹配：

- 已定稿 Markdown/LaTeX 的 render-only；
- 已有明确 document-owner downstream handoff；
- 已进入 renderer阶段后的 PDF QA。

不得仅因为：

“用户最终想要 PDF”

就先于 Research Authoring 接管一个仍在创建/重写/组织科研报告或论文的请求。

### Research Authoring

Canonical core必须明确：

~~~text
renderer globally installed/discoverable
!=
renderer admitted for the current Research Authoring task
~~~

Standalone/authoring-only：
source/package + complete handoff后 STOP。

research-main：
Research Authoring先稳定 source/handoff，再 renderer，再 Research Authoring final scientific QA。

render-only：
从一开始路由给 renderer，不进入完整 Research Authoring planning。

### Manuscript / LaTeX

新建或实质修改 manuscript：
Research Authoring core/paper first。

latex-paper-authoring 可以管理 source/package，但不能因为可编译就提前成为 Research Authoring final artifact owner。

真正 existing-LaTeX compile/debug/render-only任务继续允许直接走 LaTeX/renderer正常路径。

### Profiles

research-main：
继续安装 renderer，明确 report + manuscript 的 authoring -> handoff -> renderer -> final scientific QA 顺序，并保留 render-only直接 renderer。

codex-research-writing：
继续不安装 renderer；明确它是 authoring/source profile，formal PDF停在 handoff，完整生产使用 research-main。

## 明确不改

除非开发矩阵产生新的直接证据并返回 Planner/Critic：

- skills/tools/documents-media/pdf/SKILL.md
- renderer scripts / Pandoc/XeLaTeX / font / PDF QA implementation
- Clear Writing production behavior
- Presentations
- Statistical Modeling
- Bridge Kit
- candidate_plugin_replay
- live Research Authoring Plugin

generic pdf Skill必须作为 development negative owner检查，不能因为不改它就不测它。

## Source-first generated parity

只改 source，随后通过 current generators产生 generated output。

禁止手改：

plugins/codex/plugins/**
.agents/plugins/marketplace.json
registry/catalog/domain/provenance generated files

按 Plan运行完整 deterministic validation。

## Version/candidate closure

这仍是同一个 Research Authoring 0.3 candidate。

~~~text
research-writing=0.3 candidate
repository VERSION=5.4.4 unchanged during bounded task
~~~

如果 renderer trigger behavior修改并准备进入 C3：

~~~text
render-chinese-math-pdf=0.3 candidate
~~~

不创建 Research Authoring 0.4。

正式 repository PATCH只允许在未来 final G1-G4全部通过后的 release closure决定；本 Kickoff不授权。

## Provisional product commit

所有 source/tests/generated/version/docs闭合并 deterministic validation PASS后，先形成：

C3_PROVISIONAL_PRODUCT_COMMIT=<P>

P不是C3。

P之后在完整开发矩阵结束前不得再改 candidate-owned product files。

任何 product edit都形成新的 P2，并使旧 development matrix evidence失效。

## 完整开发回归矩阵

必须在 exact P 上运行：

1. standalone report + formal PDF
   -> Research Authoring source + handoff
   -> renderer read=0
   -> PDF mechanics=0
   -> PDF artifact=0

2. standalone ordinary advisor report
   -> Research Authoring正常完成

3. standalone manuscript + formal PDF
   -> core/paper route
   -> source/package handoff
   -> renderer read=0
   -> final PDF mechanics=0

4. research-main report + formal PDF
   -> Research Authoring first
   -> explicit handoff
   -> renderer second
   -> real PDF + renderer QA
   -> Research Authoring final scientific QA

5. research-main manuscript + PDF
   -> core/paper first
   -> source/package
   -> handoff
   -> renderer
   -> real PDF + QA
   -> final scientific QA

6. render-only finalized Markdown
   -> renderer direct
   -> Research Authoring read=0
   -> real PDF + QA

7. render-only finalized LaTeX
   -> renderer direct
   -> Research Authoring planning=0
   -> real PDF + QA

8. neighboring owners：
   - PPT/Beamer
   - citation-only
   - ordinary research Q&A
   不被错误接管

9. global renderer反证：
   renderer真实全局可发现，
   standalone Research Authoring仍只能 handoff；
   不允许隐藏或卸载 renderer。

10. unrelated global Skill/plugin反证：
    至少一个无关真实全局能力保持可发现，
    但不改变 target owner。

11. codex-research-writing authoring-only profile：
    - 在 fresh task-local project 正常安装 exact P 的 `codex-research-writing` profile；
    - 必须由正常 profile install 真正写入 managed AGENTS routing notes；
    - generic `pdf` Skill保持安装/可见；
    - 当前机器若全局可见 `render-chinese-math-pdf`，不得隐藏或卸载；
    - 使用自然的“新建/实质修改 manuscript + formal PDF”请求，不添加 renderer/PDF command blacklist；
    - Research Authoring core/paper reads > 0；
    - manuscript source/package produced = YES；
    - complete downstream production handoff = YES；
    - generic `pdf` 不得成为新科研文档 artifact owner；
    - render-chinese-math-pdf execution = 0；
    - PDF mechanics commands = 0；
    - final PDF artifact = 0；
    - 必须保存 managed AGENTS locator/hash 及 routing notes 确实进入 normal consumer 的证据。

每个case必须保存：

- exact P；
- natural prompt；
- installed/available identities；
-实际 Skill path reads；
- command trace或明确 no-command evidence；
- output inventory；
- owner route；
- should-not-change结论。

静态字符串测试不能替代 runtime。

不得在开发 prompt中添加：

“不要 XeLaTeX”
“不要 pdftotext”
“不要 renderer”

等测试专用黑名单。

## C3 freeze

只有完整矩阵（包括 codex-research-writing authoring-only profile runtime case）全部 PASS：

C3_FINAL_CANDIDATE_COMMIT=<same P>

然后保存：

- C2 -> C3 product diff；
- exact source/generated/file hashes；
- complete development matrix manifest；
- C3 -> evidence HEAD candidate-owned no-drift proof。

如果矩阵失败，C3_CANDIDATE_READY=NO，不启动 final Gate。

## Offline ChatGPT wrapper

C3冻结后、pre-final前，按：

docs/operations/059_RESEARCH_AUTHORING_C3_CHATGPT_PLUGIN_PREPARATION_V0_1.md

准备：

- exact-C3 skills-only research-authoring archive；
- file/hash manifest；
- wrapper composition；
- same-C3 Clear Writing snapshots；
- future guarded-update input。

不调用 Plugin Creator。

不更新 live Plugin。

## 成功终态

本实现包若成功，只允许：

~~~text
C3_CANDIDATE_READY=YES
C3_FINAL_CANDIDATE_COMMIT=<P>
C3_DEVELOPMENT_MATRIX=PASS
C3_OFFLINE_WRAPPER_READY=YES
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=CRITIC
~~~

然后独立 Critic审 C2->C3 diff和完整开发矩阵。

Critic PASS后由 Planner另行冻结 C3 fresh pre-final G1-G4 packet。

## 本 Kickoff明确不授权

- live Plugin Creator / live Plugin update；
- final G1-G4 execution；
- G4 ChatGPT live run；
- paid API；
- main merge；
- release/tag/GitHub Release；
- Bridge Kit修改；
- generic pdf Skill修改；
- renderer engine/font/QA脚本修改；
- candidate_plugin_replay修改；
-新 workflow / successor task；
- daemon/watcher/database/routing service/state machine；
- force push/destructive Git。

允许 task branch ordinary non-force push。

如果现有 Skill metadata + canonical owner + profile routing在完整矩阵中仍无法同时满足 standalone、codex-research-writing authoring-only、research-main、render-only：

STOP。

明确报告平台/机制限制，返回 Planner/Critic，不继续叠加自然语言补丁。
