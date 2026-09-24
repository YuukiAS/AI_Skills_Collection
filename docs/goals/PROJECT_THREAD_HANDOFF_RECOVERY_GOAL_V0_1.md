# Project Thread Handoff Recovery — Canonical Goal v0.1

Task key：`science-communication--project-thread-handoff-recovery`  
Human label：Project Thread Handoff V0.2 same-Project recovery refinement  
Status：AWAITING_EXECUTION_READY_CRITIC  
Approved design：`docs/design/PROJECT_THREAD_HANDOFF_V5_RECOVERY_PROPOSAL_2026-09-24.md` V5  
Approved design commit：`df0ca1ab809cf53b0d14901782bbf1a0d8a70642`  
Implementation Plan：`docs/design/PROJECT_THREAD_HANDOFF_RECOVERY_IMPLEMENTATION_PLAN_V0_1_2026-09-24.md` v0.1  
Kickoff：`docs/operations/prompts/PROJECT_THREAD_HANDOFF_RECOVERY_KICKOFF_V0_1.md` v0.1

只有独立 Critic 对 V5 Proposal + Plan + Goal + Kickoff 同版给出 `READY_FOR_CODEX=YES`，
且用户实际发送 approved Kickoff 后，implementation才被授权。

## 1. Required user capability

升级现有 standalone Skill `Project Thread Handoff` 到 v0.2，并保持一个 Skill、两个 explicit mode：

- Mode A：当前长 thread显式调用 -> exactly one copy-ready initialization Prompt -> stop。
- Mode B：同 Project新 thread显式 recovery -> identifiable target old conversation -> semantic continuation state
  -> hydrate当前新 thread；若同一 invocation要求 continue Y，则 recovery后同一回复继续 Y。

## 2. Frozen execution identity

Exact task key：
`science-communication--project-thread-handoff-recovery`

Exact branch：
`reviewed/science-communication--project-thread-handoff-recovery`

Exact worktree：
`../AI_Skills_Collection-science-communication-project-thread-handoff-recovery`

不得改用其他 branch、`/tmp` clone、第二个 worktree或 dirty main。

若 Host/sandbox拒绝 exact sibling worktree creation：

- 不绕过；
- 输出 `NEEDS_HUMAN_WORKTREE_BOOTSTRAP` + one exact command；
- 用户 sandbox外创建后 same-task resume。

## 3. Required source scope

允许：

```text
skills/science/communication/project-thread-handoff/SKILL.md
skills/science/communication/project-thread-handoff/agents/openai.yaml
skills/science/communication/project-thread-handoff/evals/trigger_queries.json
tests/test_project_thread_handoff_contract.py
tests/fixtures/project_thread_handoff/
docs/operations/prompts/PROJECT_THREAD_HANDOFF_CHATGPT_PLUGIN_UPDATE.md
tests/test_standalone_skill_baselines.py
VERSION / README.md / CHANGELOG.md
existing generated parity files
results/science-communication--project-thread-handoff-recovery/**
```

Canonical icon `skills/science/communication/project-thread-handoff/assets/app-facing.svg` bytes必须不变。
不修改中央 Plugin production source。

## 4. Non-substitutable semantics

必须保持：

1. standalone Skill；
2. explicit-only；
3. `agents/openai.yaml -> policy.allow_implicit_invocation=false`；
4. Mode A exactly one Prompt；
5. Mode B hydrate current new thread；
6. latest explicit user/frozen decision > assistant brainstorming；
7. thread-only delta；
8. entity-role；
9. canonical facts回 current source；
10. no repo-write behavior；
11. no MCP/database/CURRENT/history/transcript exporter/browser extension/external API；
12. no second Recovery Skill；
13. no Bridge Kit dependency；
14. no global Plugin Creator redesign。

## 5. PTH-06 target provenance

Strong Mode B recovery必须让 route-changing claims归因到 identifiable target past chat。

合法 evidence：

- target old chat in Memory Sources / Sources；
- identifiable target conversation source card/title/link；
- equivalent formal past-chat provenance。

不能替代：

- generic Saved Memory；
- profile summary；
- unsourced semantic recall；
- model prior knowledge；
- 无法归因到 target conversation 的 remembered context。

至少 latest decision/correction、route status、entity role、thread-only delta、open question、next step、
accepted proposal必须 target-chat-backed。

## 6. Strong / limited behavior

Strong：关键 decisions有 target-chat backing -> 可以声明 target old conversation continuation state recovered。

Limited：unsourced recall只能做 attribution-unverified summary，不能成为 authoritative decision/thread-only delta，
不能冒充 quote。

若缺失关键 decision会改变 route：bounded source identification -> 仍无 provenance则 fail closed ->
最多一次必要 clarification -> 不猜 route。

## 7. Cross-Project boundary

Mode B只接受 target same-Project conversation evidence作为 authority。

default-memory可能暴露 Project外 context，因此 Project membership本身不是 provenance。

不要求用户改 project-only memory，不做另一个私有 Project live leakage test，不主动跨 Project补洞。

## 8. Capability Gates

只允许 G1/G2/G3。

### G1 — Distribution / Explicit Invocation / Visual Identity

同一 final candidate证明：

- Skill v0.2 source/generated parity；
- explicit-only；
- existing PRIVATE / USER-scope skills-only personal wrapper identity preserved；
- no MCP；
- canonical icon reused且 bundled icon byte-equivalent；
- target Pro regular Chat explicit invocation。

### G2 — Current-Thread Handoff Regression

同一 final candidate在 target Pro regular Chat长 thread运行 Mode A，证明 current context、authority/recency、
entity role、thread-only delta、locator、exactly one Prompt、no second confirmation、no repo write、
DII/CARE representative semantics与no hardcode。

### G3 — Same-Project Recovery / Generalization + Provenance

同一 final candidate在 `AI Research Stack` Project新 thread恢复真实 Bridge/SSH old conversation；
用户不重贴完整回答。

恢复至少包括：Bridge Kit不依赖 SSH；SSH是 publisher compatibility/safety相关 transport；WSL GitHub SSH
identity未配置不等于 Bridge failure；不应只为 gate修改 HTTPS环境；问题属于 compatibility
acceptance/evidence而非 Bridge runtime dependency。

Strong PASS额外要求 target Bridge/SSH old conversation作为 identifiable past-chat provenance出现，
generic Memory/profile/unsourced recall不能替代；key claim无 provenance -> G3 strong PASS = NO。

Final claim仅：

`target-conversation-backed semantic recovery verified; no observed cross-project substitution`

不声称 absolute isolation/raw transcript/transcript-level fidelity。

## 9. Existing wrapper / icon

现有 regular Chat distribution是 existing PRIVATE / USER-scope / skills-only personal Plugin wrapper。

V0.2只允许更新该 existing identity：

- no create-new fallback；
- bundle exact final candidate canonical Skill；
- no MCP/connector/database/app/state/external API；
- bundled canonical icon byte-equivalent；
- composerIcon/logo优先 canonical icon；
- target明确不支持 SVG时才 deterministic conversion，no redesign。

Public repo不写 private Plugin ID/URL/current version/release id。Identity不唯一时最多一次最小用户选择。

## 10. Same-final-candidate acceptance

用户介入前完成 implementation/tests/generated parity/public-safe regressions/version/docs/icon check/candidate
freeze/commit/push/remote verify/wrapper-update handoff准备。

一次 target session完成：

1. update existing wrapper to exact final candidate；
2. G1；
3. Mode A G2；
4. Mode B Bridge/SSH G3；
5. target-source provenance observation。

Work/Codex不能替代 regular Chat。

## 11. Version

Standalone Skill：`0.1 -> 0.2`  
Repository：`5.1.0 -> 5.1.1 PATCH`  
Central Plugins：全部 `NO_BUMP`

Private wrapper：执行时读取 current private version/release id后 compatible increment。

若 kickoff-time `origin/main:VERSION != 5.1.0`，记录 `VERSION_DRIFT`并回 Planner。

## 12. Privacy

不得提交 old thread全文、full private recovery output、unrelated Memory Sources、private Plugin ID/URL 或
Project transcript dump。只保存 minimal redacted provenance/criterion receipts。

## 13. Authorized implementation boundary after approved Kickoff

允许 exact branch/worktree、冻结 source/tests/fixtures/generated/version/README/changelog/results edits、
deterministic tests、package/hash generation、public OpenAI docs read、ordinary task-owned commits 与 exact
reviewed branch ordinary non-force push。

不授权 main merge/tag/release/publish、paid API、新 Plugin、MCP/database/external API、Bridge Kit write、
target research repo write、destructive/force Git或 unrelated private-data upload。

Personal Plugin existing-wrapper update属于 final target-surface acceptance；平台所需用户确认必须走正常产品确认。

## 14. Completion

用户 target acceptance前最多：

`FINAL_CANDIDATE_READY_FOR_TARGET_ACCEPTANCE=YES`

G1/G2/G3未对同一 final candidate全部 PASS：

`PROJECT_THREAD_HANDOFF_V0_2_READY != YES`

总体 ready还需 independent final review + separate authorized integration/release closure，且 main integrated
canonical Skill bytes必须与 accepted candidate一致。
