# 056 交付工作流可靠性基线 — Execution Package Review v0.5

- Review object：`v0.5 exact-worktree authorization amendment`
- Historical task key：`056_product_delivery_discipline`
- Human-readable name：交付工作流可靠性基线
- Review stage：`EXECUTION_READY_PACKAGE_REVIEW_AFTER_C056_E3`
- Prior reviewed package：`v0.4 @ 2df53f24964673fbf79cb3bcdab63b6dfd5ee4c4`
- Prior Critic result：`REVISE`，chat-only；无 Critic repo commit
- Stable blocker：`C056-E3-EXACT-WORKTREE-AUTHORIZATION`
- AI_Skills production/evidence baseline：`main@72f163330ea5a21637df95f08289e2c4739d2bd9`
- Bridge source locator：`main@9d2da9f485f26ca51842a1909a276cb44f73351a`
- Amendment：`docs/design/056_DELIVERY_WORKFLOW_RELIABILITY_BASELINE_V6_AMENDMENT_2026-09-21.md`（unchanged）
- Plan：`docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_IMPLEMENTATION_PLAN.md` v0.5
- Goal：`docs/goals/056_PRODUCT_DELIVERY_DISCIPLINE_GOAL.md` v0.5
- Kickoff：`docs/operations/prompts/056_PRODUCT_DELIVERY_DISCIPLINE_KICKOFF.md` v0.5
- Status：`AWAITING_INDEPENDENT_CRITIC_RECHECK`

## 1. 本轮 review scope

v0.4 独立 Critic 已接受并关闭/放行以下内容，除非 latest source 出现新的直接语义证据，本轮不得重开：

- human-readable name“交付工作流可靠性基线”；
- historical key `056_product_delivery_discipline` 保留；
- 056 是 bounded baseline task，不是 evergreen program；
- `V6_BOUNDED_AMENDMENT`；
- least-privilege equivalent recovery 吸收到 W2/G1，不新增 W6/G9；
- Persistent Run durability / ordinary bounded kickoff renderer / task-local prohibition expiry / acceptance packaging 的 defer owner；
- G1-G8、Source Discovery not G9、BROAD_FULL_FALLBACK、cheap deterministic first、same-final-candidate；
- Repository 5.0.6 -> 5.0.7 PATCH；
- workflow-core 0.2 -> 0.3；
- web-development 0.1 -> 0.2；
- ai-skills-core 0.3 -> 0.4 仅限 residual diagnosis，或 kickoff-time direct evidence 支持 NO_BUMP；
- Bridge 0.8.4 -> 0.8.5；
- `C056-E1` closed；
- `C056-E2` closed by Critic Role Contract v1.4 generic reporting rule。

本轮只复核 `C056-E3` 是否关闭，以及 v0.5 locator amendment 是否直接引入新的 scope/authorization/recovery regression。

## 2. Prior blocker C056-E3

### Requirement

AI_Skills 当前 AGENTS 要求：使用 `reviewed/<task_key>` + task-owned worktree 时，Goal/Kickoff 必须把 exact branch 和 exact worktree 绑定为 current-user-visible authorization。

### v0.4 defect

v0.4 Kickoff 已冻结 exact branch，但只写“创建对应 task-owned worktree”；Plan 中 worktree basename 只是“建议继续使用”。因此到 worktree creation 时仍可能再次索权，或留下 Executor临场选择路径的解释空间。

## 3. v0.5 closure

v0.5 在 Plan、Goal、Kickoff 三者一致冻结：

### AI_Skills_Collection

Exact branch：

`reviewed/056_product_delivery_discipline`

Exact worktree locator：

`../AI_Skills_Collection-056-product-delivery-discipline`

解析基准：verified canonical AI_Skills checkout root。

### GPT_Codex_AI_Bridge_Kit

Exact branch：

`reviewed/056_product_delivery_discipline`

Exact worktree locator：

`../GPT_Codex_AI_Bridge_Kit-056-product-delivery-discipline`

解析基准：verified canonical Bridge checkout root。

两个 locator 都明确规定：

- relative path 不是相对任意 shell cwd，而是相对 verified canonical checkout root；
- 只能解析为 canonical root 的父目录下 exact basename sibling；
- 不允许临场换路径、第二个 worktree 或 `/tmp` clone；
- locator 已存在时只在 repo identity + exact branch 都匹配时复用；
- locator 被占用或 identity 不匹配时停止，不自动换位置。

Kickoff 开头将这两个 exact branch/worktree pair 写成用户若发送即明确授权的 frozen effect，并明确后续到达同一 worktree/branch creation effect 时不得重复询问。

## 4. Unchanged authorization boundary

v0.5 不新增任何其他授权。

仍禁止：

- remote remap / pushurl rewrite；
- force push；
- main merge / release / tag / publish / deploy；
- product repo write；
- real `CODEX_HOME` / Host install；
- paid API/Terra；
- Persistent Run refinement；
- new provider/account/credential purpose；
- out-of-scope side effects。

same frozen effect no-repeat 与 genuinely new scope fresh gate 保持不变。

## 5. Version / architecture impact

`ARCHITECTURE_CHANGE=NO`

`GATE_CHANGE=NO`

`LEAST_PRIV_SEMANTICS_CHANGE=NO`

`VERSION_ROUTE_CHANGE=NO`

`DEFER_DISPOSITION_CHANGE=NO`

`AMENDMENT_DOC_CHANGE=NO`

Package version 从 v0.4 -> v0.5 只是因为 Critic 要求“不要静默修改旧 review object”，需要形成新的完整 execution package identity。

## 6. Source drift

AI_Skills latest main 在本轮开始时仍是 v0.4 package commit `2df53f24964673fbf79cb3bcdab63b6dfd5ee4c4`；Bridge latest main 仍是 `9d2da9f485f26ca51842a1909a276cb44f73351a`。没有新的 production/version semantic drift。

后续如果仅 docs/evidence SHA advance，不重开 architecture；只有 production/version/release/frozen semantics overlap 才返回 Planner/Critic。

## 7. Critic expected output

优先复核旧 blocker：

`C056-E3-EXACT-WORKTREE-AUTHORIZATION`

检查：

1. Plan / Goal / Kickoff 的两个 exact branch + exact worktree locator 是否逐项一致；
2. relative locator 是否被 canonical-root resolution 唯一化；
3. Kickoff 是否已经形成足够 current-user-visible bounded authorization；
4. occupied/mismatched locator 是否 fail closed；
5. 是否仍有“对应 worktree”“建议继续使用”等开放措辞；
6. 本次 amendment 是否意外扩大 Git/provider/Host/paid/product scope。

如果仍 REVISE，只能提出由本次 locator amendment 或 latest direct semantic evidence 引起的真实 blocker，并按 Critic Role Contract 自动附完整 Planner prompt。

如果 PASS：

- 因 056 major round历史上已有 REVISE，先给用户可读 closure explanation；
- 明确 `C056-E3=CLOSED`；
- 不重开已接受的 architecture/Gate/version/defer/C056-E1/E2；
- 输出 approved package paths + commit；
- `READY_FOR_CODEX=YES`；
- `NEXT_HANDOFF=CODEX`；
- 逐字输出 v0.5 approved Kickoff。

PASS 仍不执行 056，也不授权 main merge/release/paid/real Host。
