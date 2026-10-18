# Project Instructions Editor 0.2 — Bounded Implementation Plan v0.2

Status: DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW  
Repository: `YuukiAS/AI_Skills_Collection`  
Target: standalone Skill `project-instructions-editor`  
Task key: `project-instructions-editor--0.2-baseline-diff-contract`  
Source ref: `main`  
Planner observed main: `6da342a0103fc1f9ce003baa58ace5b23e748270`  
Supersedes: `PROJECT_INSTRUCTIONS_EDITOR_0_2_IMPLEMENTATION_PLAN_V0_1_2026-10-18.md`  
Reviewed product design: `CHAT_ONLY / PIE 0.2 Planner Proposal v0.1`  
Product-design Critic result: `PASS` (reported by the user; no repo review file exists for that chat-only review)  
Planned execution branch: `reviewed/project-instructions-editor--0.2-baseline-diff-contract`  
Planned worktree: `../AI_Skills_Collection-project-instructions-editor--0.2-baseline-diff-contract`

## 0. Critic finding disposition

Prior execution-ready Critic result:

```text
CRITIC_RESULT=REVISE
BLOCKER=PIE02-ER1
REVIEW_OBJECT=PIE_0_2_IMPLEMENTATION_PACKAGE_V0_1
```

Planner disposition:

```text
PIE02-ER1=ACCEPT
```

The prior package allowed public-safe / fixture G1 evidence to be reported as final `G1=PASS` even though the same Goal prohibited live private-wrapper mutation and deferred real ChatGPT Web / Project normal-entry verification. That could reproduce the exact class of failure seen during PIE 0.1 development: internal evidence appears green while the real Web entry still fails.

v0.2 keeps the same four Gate families and changes only G1 evidence semantics:

- implementation-stage public-safe / fixture G1 is development / pre-final diagnostic evidence only;
- final release G1 PASS requires the later approved live Web acceptance on exact `FINAL_CANDIDATE_COMMIT=C`;
- that same live acceptance first proves missing-baseline normal entry, then supplies the complete baseline and real edit request to produce the live G4 artifact;
- no fifth Gate, new workflow, new runtime dependency, or new product behavior is introduced.

G2/G3, the G4 pre-final packet, final-candidate discipline, PIE 0.1 should-not-change set, baseline/diff product contract, Clear Writing boundary, tracking, version/release boundary, and authorization envelope are unchanged.

## 1. 目标

PIE 0.2 是对已发布 PIE 0.1 的兼容增强，不重做产品架构。

本轮只增加五件用户可观察行为：

1. 任何当前 ChatGPT Project setting 的分析、压缩、修改、重组、同步或重置，在进入 PIE 编辑逻辑前，都必须取得用户在当前任务中明确提供的完整当前 Project setting 原文。
2. 用户明确声明当前 setting 为空时，将该声明视为完整空基线并继续支持 greenfield。
3. 每次真实修改都先交付人类可读 Markdown 修改预览：局部修改默认 `~~旧~~**新**`，大规模替换允许提升到整句、整段或整节粒度。
4. 每次真实修改同时交付完整、干净、可直接使用的新 Project setting。
5. 修改预览与干净结果必须来自同一个用户基线 (B) 和同一个真实修改 (E)，满足 (E(B)=C)。diff 只是审阅层，不得成为第二套语义编辑器。

## 2. PIE 0.1 必须原样保留的能力

以下均属于 0.1 已有产品合同，本轮不得弱化、重写成另一种机制或重新包装成 0.2 新功能：

- preservation-sensitive / greenfield / explicit reset；
- bounded edit 默认优先于整份重写；
- semantic ownership 与 effective Project enforcement placement 分离；
- canonical source locator / bridge；
- protected absence；
- no-op；
- instruction budget / headroom；
- mandatory/optional、trigger、authority、permission、authorization、safety、privacy、distribution、evidence/completion strength、role ownership、uncertainty、current/future status、exact identifiers、明确用户纠正/删除等语义不变量；
- complete replacement 的 mandatory final consistency pass；
- 正常运行不依赖 MCP finalizer、外部 model/provider、额外 API billing、sibling Skill、数据库、ledger、watcher 或第二状态机；
- C11 reader-layer failure 继续作为历史失败证据，不重新解释为 PASS。

## 3. 当前真实生产基线

当前 `main`：

- repository `VERSION=5.4.5`；
- `project-instructions-editor` source version = `0.1`；
- runtime subtree 仍只有 `SKILL.md`、`agents/openai.yaml`、`references/editor-contract.md`、`evals/trigger_queries.json`、`assets/app-facing.svg`；
- `tests/test_project_instructions_editor_contract.py` 仍显式验证 0.1 合同以及“无 runtime scripts”；
- `tests/test_standalone_skill_baselines.py` 仍期望 PIE `0.1`；
- `README.md` 仍展示 PIE `0.1`；
- `CHANGELOG.md -> Unreleased` 仍记录 PIE 0.1 的首次集成。

当前正式 `release` ref：

- ref = `39e2f20c53a07936f8dc5a289f3af41a83943b75`；
- `VERSION=5.4.5`；
- 不包含 `skills/core/codex-system/project-instructions-editor/SKILL.md`。

因此本轮不能预先宣称未来 repository release 一定是 PATCH。若正式发布时 `release` 仍不包含 PIE，则把 PIE 正式加入 release 可能属于 repository-level 新能力；若此前已有正式 release 纳入 PIE 0.1，则 0.2 的兼容增强通常才是 PATCH。最终 repository bump 必须在 release closure 时重新比较真实 `release` baseline 并按 `PLUGIN_VERSIONING_AND_CHANGELOGS.md` 判断。

本 implementation task 本身不推进 `release` ref：

```text
Repository bump decision: NONE
Affected standalone skill:
- project-instructions-editor: 0.1 -> 0.2 candidate
Affected central plugins:
- all: NO_BUMP
```

## 4. 输入硬门

0.2 必须把 baseline gate 放在 PIE 编辑推理之前。允许先做的只有“这是不是 Project setting 编辑任务”的路由判断。

### 4.1 缺完整当前原文

如果用户没有在当前任务中明确提供完整当前 Project setting 原文，立即停止编辑分析，只输出：

> 请提供当前完整 Project setting 原文。PIE 不会根据 Project 上下文、Memory、历史聊天、仓库文件、部分 instructions 或模型推断重建当前 setting。

此时不得：

- 测试自己是否“知道” setting；
- 根据 Project context、Memory、历史聊天、old candidate、summary、部分 system/project instructions 或模型知识拼 baseline；
- 先做压缩、重组、语义审计、canonical sync 或 diff；
- 询问“是否愿意提供”。

明显含有 `[…]`、省略提示、局部摘录声明或其他自我标记为不完整的文本，不得冒充完整 baseline。

### 4.2 收到完整当前原文

先输出：

> 已收到当前完整 Project setting 原文；本轮以该原文作为唯一当前 baseline。

随后才进入 0.1 的 edit-mode、targeted history、canonical source、budget、ownership/enforcement、bounded/full/no-op 等逻辑。

### 4.3 greenfield

用户明确说明“当前 Project setting 为空”即构成完整空 baseline。随后继续按 0.1 greenfield 合同创建完整初始 setting。

### 4.4 explicit reset

explicit reset 仍要求用户提供完整当前 baseline。该 baseline 只承担可信输入和 B→C diff provenance；用户明确 reset 后，不恢复旧 Project-setting semantics 的 preservation obligation。system/workspace/repo authority、安全、隐私、权限和当前用户其他有效要求继续生效。

若用户明确说明 UI 中 setting 在本轮又发生变化，则旧 baseline 失效，下一次实际编辑前必须重新取得完整原文。

## 5. 候选与 diff 的单一真相链

运行顺序固定为：

```text
用户完整 baseline B
-> PIE 0.1 semantic editing
-> clean candidate C
-> PIE 0.1 mandatory final replacement consistency pass
-> derive temporary edit relation E from B -> C
-> render human-readable Markdown preview R from E
-> deliver R + clean C
```

关键边界：

- 先决定语义和干净候选，再生成 diff；不得为了 diff 好看反过来改 C。
- E/R 只存在于当前回答，不持久化，不形成 ledger、history service 或状态机。
- preview 中声称删除的内容必须真实存在于 B。
- preview 中新增的内容必须真实出现在 C。
- B→C 的所有实质修改必须在 preview 中可见；未修改章节可以省略，但不能“精选”一部分改动后声称是完整修改预览。
- C 中未授权、未修改的旧规则不得无故丢失。
- preview 与 C 不一致时，重新生成 preview；不得修改已经通过 semantic/final consistency 的 C 去迎合错误 preview。

no-op 不制造空 diff，也不重复输出一份完全相同的 setting；按 0.1 no-op 合同说明“不需要修改”及原因即可。

## 6. Markdown 修改预览合同

### 6.1 局部修改

默认：

`原文~~旧部分~~**新部分**原文`

只标真正变化的字符、词、短语或句子，未改部分保持普通文本。

### 6.2 少量相邻句子

仍优先保持正常段落顺序，用删除线和粗体直接表示替换，只要用户能从左到右迅速看出“原来是什么 → 现在是什么”。

### 6.3 大规模替换

当字符级 inline 标记明显降低可读性时，允许提升粒度：

- 旧整句 / 旧整段 / 旧整节整体删除线；
- 对应的新整句 / 新整段 / 新整节整体粗体。

不固定字符阈值。判断标准是“用户最快看出修改前后差异”。

### 6.4 省略与移动

- 未修改章节可以完全省略。
- 为定位而跨过未改内容时可用 `[…]`。
- 移动已有内容必须在旧位置显示删除、在新位置显示新增；不能把结构移动伪装成“没有变化”。

### 6.5 禁止格式

- 不使用 Git `+/-` diff；
- 不使用 code diff block；
- 不添加“删除：”“新增：”等机器标签；
- 不为了最细字符 diff 牺牲可读性。

## 7. 生产源码的最小修改范围

预计 production-owned 修改仅限：

1. `skills/core/codex-system/project-instructions-editor/SKILL.md`
   - version `0.1 -> 0.2`；
   - description 删除 “even if the live setting is missing” 语义，改为用户提供完整 baseline / 明确空 baseline 的正常入口；
   - baseline gate 前置；
   - 固定缺基线回复和 baseline receipt；
   - explicit reset 的 baseline-provenance 语义；
   - diff + clean final 双层交付；
   - preview 与 clean candidate 的同源一致性；
   - 保留 0.1 final consistency、protected absence、no-op、ownership/enforcement 等现有合同。

2. `skills/core/codex-system/project-instructions-editor/references/editor-contract.md`
   - 将 0.2 输入门、diff 展示、B/E/C 一致性和 failure handling 写成稳定详细合同；
   - 删除与新硬门冲突的“缺 baseline 仍先给 bounded advice/clause”语义；
   - 不复制 Clear Writing 规则，不加入 C11 finalizer 路线。

3. `skills/core/codex-system/project-instructions-editor/evals/trigger_queries.json`
   - 增加“不提供 baseline 的自然 Project-setting 编辑请求”正例，验证应路由进 PIE 后由 baseline gate 停止；
   - 保留明确空 setting 的 greenfield、提供 baseline 的 reset/sync/compress；
   - 保留 near-miss owner 边界。

4. `skills/core/codex-system/project-instructions-editor/agents/openai.yaml`
   - 仅在需要时同步 short description/default prompt 到“用户提供完整 current baseline”的 0.2 合同；
   - 保持 `allow_implicit_invocation: true`；
   - 不把 Clear Writing 或外部 finalizer 加为依赖。

禁止新增 `scripts/`、runtime helper、database、ledger、AST service 或外部 diff service。

## 8. 测试与仓库同步范围

### 8.1 确定性合同测试

更新 `tests/test_project_instructions_editor_contract.py`，至少验证：

- version = `0.2`；
- description 与 0.2 baseline gate 一致，不再承诺 missing baseline 下继续编辑；
- 冻结的缺基线回复逐字存在；
- baseline receipt 逐字存在；
- greenfield explicit-empty 与 explicit reset baseline 语义都存在；
- Markdown preview 合同含删除线/粗体、局部替换和大块替换原则；
- clean full setting 是每次真实修改的交付物；
- preview/clean final 绑定同一 B→C 修改；
- no-op 不被强制制造假 diff；
- 0.1 protected absence、ownership/enforcement、semantic invariants、formal runtime route 等保护仍在；
- rejected C7-C11 / external-finalizer mechanisms 仍不是 runtime dependency；
- runtime subtree 仍无 scripts。

更新 `tests/test_standalone_skill_baselines.py`，使 PIE expected standalone version 为 `0.2`。

可以在测试代码中使用 Python 标准库 `difflib` 对冻结回归产物做 B→C 辅助核对，但它只属于测试/证据层，不进入 Skill runtime，也不能替代独立 Reviewer 对完整 Markdown preview 与 clean final 的定性审查。

### 8.2 生成层与文档

生产源码完成后使用现有 generator：

```text
python scripts/skills.py registry --write
python scripts/skills.py catalog --write
python scripts/audit_skill_provenance.py --write
python scripts/skills.py validate
```

standalone PIE 不得被错误加入 central Marketplace topology。

README 因 standalone version 与能力描述变化需要更新为 v0.2。按 `AGENTS.md`，任何 README 修改前必须真实调用当前安装的 Clear Writing（`writing-style`）检查受影响读者区域。这个调用只服务仓库 README，可见文案检查；它不是 PIE 0.2 runtime dependency。若执行环境无法真实调用 Clear Writing，不得伪造调用，也不得完成 README/final-candidate closure。

`CHANGELOG.md -> Unreleased` 应记录 PIE `0.1 -> 0.2` 的用户可观察变化，并把本 implementation task 的 repository bump 明确为 `NONE`。正式 repository release 类型留到 release preflight 根据当时 `release` baseline 决定。

## 9. Capability Gate Matrix

继续使用 0.1 的四个 Gate family，不新增第五 Gate。

### G1 — Normal entry / routing boundary

G1 family remains one Gate, but it has two evidence stages.

**Development / pre-final evidence** during implementation:

- public-safe / fixture requests may show that an unnamed Project-setting edit request routes toward PIE behavior;
- missing-baseline fixtures must return only the frozen request and no edit analysis;
- near-miss tasks must remain with ordinary prose, writing fidelity, scientific rewrite, AI_Skills maintenance, workflow/control, or global Custom Instructions owners.

This evidence may be recorded only as:

```text
G1_DEVELOPMENT_EVIDENCE=PASS | FAIL
```

It must not be reported as final `G1=PASS`.

**Final live release evidence** is deferred until the separately approved real ChatGPT Web acceptance. It must use exact `FINAL_CANDIDATE_COMMIT=C` loaded into the existing PRIVATE / USER-scope PIE wrapper. In a fresh real ChatGPT Web / Project entry:

1. send a natural Project-setting edit request without naming PIE and without supplying a baseline;
2. observe only the frozen exact missing-baseline message, with no analysis or edit attempt;
3. only then provide the complete baseline B plus the real edit request and continue to the live R + clean C artifact used for G4 review.

Only step 1–2 on the exact live candidate can establish:

```text
G1_FINAL_LIVE=PASS
```

Until then:

```text
G1_FINAL_LIVE=PENDING
```

Failure includes:

- fixture/development evidence being promoted to final G1 PASS;
- forced invocation substituted for real normal entry;
- live entry first analyzes or edits before requesting the baseline;
- live entry uses Project context / Memory / history to reconstruct the baseline;
- near-miss routing regresses.

### G2 — Core Project editing semantics

覆盖至少以下冻结任务族：

- user-supplied preservation-sensitive baseline + 小型 inline diff；
- user explicitly says setting empty -> greenfield；
- user-supplied baseline + explicit reset；
- 大段/整节重写触发更粗粒度 Markdown preview；
- no-op；
- existing 0.1 locator/budget/ownership/enforcement behavior。

失败：

- greenfield 被 baseline gate 错误阻塞；
- reset 绕过用户 baseline；
- 真实修改缺 preview 或缺完整 clean final；
- preview 粒度机械到不可读；
- 0.1 核心编辑能力回归。

### G3 — Fidelity / authority / should-not-change

至少冻结以下回归：

1. baseline 中不存在某句，但 old chat / Memory-like summary / stale candidate 中存在：preview 不得声称删除该句；
2. 小修改后完整 C 必须保留所有未授权旧规则；
3. mandatory/optional、authorization、安全、隐私、evidence strength、role ownership、exact identifier 不漂移；
4. protected absence 与 explicit deletion/correction 保持 0.1 行为；
5. 对每个冻结产物同时保存 B、用户请求、preview R、clean C；用独立 B→C 文本差异辅助检查 R 是否覆盖真实变化，并由 Reviewer 直接判断 `E(B)=C` 的语义一致性。

机械字符串测试不能单独给 G3 PASS。

### G4 — Representative complete task + qualitative final artifact

Implementation prepares a complete public-safe pre-final packet from exact `FINAL_CANDIDATE_COMMIT=C`:

```text
full user request
+ user-supplied complete B
+ required canonical source
-> readable Markdown preview R
+ complete clean C
```

This packet is development / pre-final evidence and does not itself establish the final live G4 PASS.

After independent pre-final review and separate user authorization, the real ChatGPT Web acceptance uses the same exact C loaded into the existing PRIVATE / USER-scope PIE wrapper. The same live acceptance that establishes final G1 then continues by supplying the complete B and real requested delta, producing the actual live R + clean C artifact for G4 qualitative review.

The independent Reviewer must be able to see the full live user request, B, necessary current source, R, C, and candidate identity, and directly judge:

- whether the preview lets a human understand before→after quickly;
- whether every actual B→C change is reviewable;
- whether C completely preserves unchanged rules;
- whether PIE 0.1 semantic invariants remain intact;
- whether C is directly usable as the new Project setting.

The real Web acceptance must reuse the existing PRIVATE / USER-scope `project-instructions-editor` wrapper; it must not create a second capability source. Wrapper mutation remains outside this implementation Goal and requires the later approved live-acceptance stage.

## 10. Gate 执行纪律

执行顺序：

1. cheap deterministic tests / regression bank；
2. 开发期运行 G1 development/pre-final diagnostics 与 G2/G3 replay；
3. freeze `FINAL_CANDIDATE_COMMIT=C`；
4. 从 C 重跑 `G1_DEVELOPMENT_EVIDENCE`、G2、G3；其中只有 G2/G3 可在 implementation stage 形成 Gate PASS，G1 final live 仍保持 PENDING；
5. 从 C 生成 G4 完整 pre-final packet；
6. independent pre-final / implementation review；
7. 只有获得后续明确授权时，把 exact C 更新到现有 PRIVATE / USER-scope PIE wrapper；
8. 在真实 ChatGPT Web / Project 正常入口先运行无 baseline 的自然请求；只有 exact missing-baseline behavior 成立时，记录 `G1_FINAL_LIVE=PASS`；
9. 在同一获批 live acceptance 中随后提供完整 B + 真实修改请求，产生 live R + clean C，并提交 G4 定性审查；
10. independent G4 adjudication 与最终 release closure 另行进行。

implementation package 结束时不得写 `G1=PASS`。在 live acceptance 前，G1 的唯一合法最终状态是 `G1_FINAL_LIVE=PENDING`。

所有 release claim 必须来自同一个 C。C 之后的 evidence-only commit 记为 E；若任何 candidate-owned 文件在 C 后变化，旧 Gate evidence 失效，并按 blast radius 重跑。

不固定样本数量；优先使用 0.1 既有回归加本轮新增 baseline/diff failures。不得无限追加样本、挑赢家或把开发样本伪装成 fresh evidence。

## 11. 实现分支与范围

execution-ready Critic PASS 后，用户发送 approved Kickoff 才授权 Codex 创建/使用：

```text
branch = reviewed/project-instructions-editor--0.2-baseline-diff-contract
worktree = ../AI_Skills_Collection-project-instructions-editor--0.2-baseline-diff-contract
```

允许修改的候选范围：

- 上述 PIE production source；
- PIE focused tests/evals；
- generated registry/catalog/provenance；
- README/CHANGELOG 中与 PIE 0.2 直接相关的条目；
- `results/project-instructions-editor--0.2-baseline-diff-contract/**` 证据；
- 已批准的 0.2 canonical TODO / tracking locator。

禁止：

- unrelated central Plugin behavior/version；
- Clear Writing production source；
- Bridge Kit；
- Project setting 实际写回；
- global Custom Instructions；
- external provider / paid API；
- force push/rebase/destructive mutation；
- 新 runtime service/helper/state store。

## 12. Tracking 与 Issue #93

Issue #93 是 PIE 0.1 的已完成 tracking Issue，不得重开或复用。

0.2 进入新的 tracking scope，应创建独立 Issue：

```text
title = Project Instructions Editor 0.2：真实基线与可审阅修改预览
labels =
  maintenance-track
  kind:enhancement
  scope:standalone-skill
  area:standalone-skill
Project Status = DOING
Project Area = standalone-skill
Resolution commit = blank
canonical source = docs/skill-todos/project-instructions-editor.md
tracking backlink = tracking: #<new issue number>
```

当前 Planner surface 无法真实调用 Clear Writing，因此依据 maintenance-board policy，不创建 reader-facing tracking Issue，也不假称 Project 已同步。执行前由具备真实 `writing-style` 调用和 GitHub mutation surface 的下一 maintenance action 机械完成；若只能创建 Issue/写 backlink 而不能改 Project fields，则完成合法部分并记录 exact pending Project mutation，不要求用户手工拖看板。

## 13. README / release 与 Clear Writing 边界

本轮明确不把 Clear Writing 接入 PIE 0.2 产品 runtime。未来 thin bridge 仍只是兼容位置，不是 release requirement。

但 AI_Skills 仓库自己的 README 写作规则仍独立生效：若 implementation 修改 README，必须真实调用 `writing-style`。这只是仓库维护流程，不得写入 PIE runtime contract，也不得作为用户使用 PIE 的依赖。

## 14. Failure handling

- 缺 user baseline：按冻结 exact message 停止 PIE editing。
- baseline 明显被用户声明为节选：继续请求完整原文。
- canonical source / budget / authority 在 baseline 已齐后仍缺：沿用 0.1 的局部 honest degradation，只阻止受影响 claim。
- preview 与 C 不一致：重建 preview，不修改 C。
- semantic final pass 失败：修 candidate，随后重新生成 preview。
- candidate-owned 文件在 C 后变化：失效旧 Gate evidence，按 blast radius 重跑。
- Clear Writing 不可用：README/final-candidate closure 不得伪造 PASS。
- tracking Project mutation 不可用：记录 exact pending mutation，不让用户手工维护。
- 正式 `release` baseline 变化：在 release closure 重新计算 repository bump，不在 implementation 中猜版本。

## 15. 完成边界

本 implementation Goal 完成只能证明：

- PIE 0.2 source candidate 实现冻结产品合同；
- 0.1 regression 保持；
- G1 development/pre-final evidence、G2/G3 PASS 与 G4 pre-final packet 达到独立 pre-final review 条件；final live G1 仍为 PENDING。

它不自动证明：

- G1 final live normal-entry acceptance 已通过；
- G4 real ChatGPT Web acceptance / qualitative adjudication 已通过；
- private wrapper 已更新；
- main 已集成；
- formal `release` ref 已推进；
- repository release version 已决定；
- Issue / Project 已最终 DONE。

下一步必须是独立 execution-ready Critic 对本 Plan、同版 Goal 和同版 Kickoff 的完整审查。Critic PASS 以前：

```text
READY_FOR_CODEX=NO
```
