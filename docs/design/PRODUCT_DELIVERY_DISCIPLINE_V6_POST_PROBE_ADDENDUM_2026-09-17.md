# Product Delivery Discipline v6 — Post-Probe Planner Addendum

状态：`DRAFT_FOR_SHORT_CRITIC_REVIEW`  
日期：2026-09-17  
任务：`056_product_delivery_discipline`  
基础方案：`docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md`  
性质：这是 v6 Critic PASS 后、capability probe 完成后的 Planner 解释与证据增补。**不新增顶级 capability，不修改 production skill/plugin、Bridge Kit production 或任何项目 AGENTS，也不冻结 implementation Plan/Goal/Kickoff。**

## 1. 为什么需要这个 addendum

独立 Critic 已对 v6 架构给出 PASS，并允许先执行 persistent-user-input capability probe；但明确指出 probe 结果仍会决定 W2 的最终 transport，因此当时不能冻结 implementation Plan。

probe 已完成。同时，Lucerna/Bridge Kit 与 CUHK Date 的最新真实开发又暴露出两类新的用户成本：

1. Executor 在已有本地 canonical repo/clone 可以复用时绕去 `/tmp` 新 clone、再尝试改 remote，浪费时间并触发额外审批；
2. CUHK Date Questionnaire V4 出现“测试很多、实现结构齐全，但用户随手操作就发现基础能力未闭环”的一组真实失败，包括 catalog breadth、locale token leakage、mock-only provider、真实输入序列、material product branches、fallback 冒充 primary capability、hosted config 未消费真实 backend capability，以及 rewrite 退化已接受 interaction。

这两类证据都可以落入 v6 已批准的小架构；不需要新增 W6/W7 或新的状态机。

## 2. Persistent prompt probe：已验证事实

用户提供的 probe result 记录：

```text
CODEX_CLI_VERSION = codex-cli 0.142.0
COLLABORATION_MODE = DEFAULT
DEFAULT_MODE_REQUEST_USER_INPUT_FEATURE = ENABLED
NATIVE_TOOL_AVAILABLE = YES
ELAPSED_SECONDS = 114
NATIVE_AUTO_RESOLVED = YES
EMPTY_OR_DEFAULT_ANSWER_RETURNED = YES
NATIVE_150S_PENDING = FAIL
TERMINAL_BLOCKED_EMITTED = NO
AUTOMATIC_RETRY_OBSERVED = NO
TRACKED_WORKFLOW_STATE_CHANGED = NO
FALLBACK_TYPE = DURABLE_TRANSCRIPT_WAIT_RESUME
FALLBACK_RESUME = PASS
NATIVE_DEFAULT_PERSISTENT_PROMPT = FAIL
```

因此，在当前实际安装版本上，Default-mode native `request_user_input` **不能满足用户要求的“持续显示、未回答就绝不继续”语义**。本轮不能再把 feature flag enabled、tool available 或 `auto_resolution_ms=None` 当作 no-expiry 证据。

## 3. 当前 upstream source：config.toml 不能把 Default prompt 变成 persistent

本轮重新核对当前 `openai/codex` main source（检查时 commit `8ace915aced81ed841e34fa069b2e489c324731c`）：

- `codex-rs/core/src/tools/handlers/request_user_input.rs` 直接构造：

```rust
is_blocking: mode == ModeKind::Plan,
auto_resolution_ms: None,
```

即 blocking 由 collaboration mode 决定，不读取一个 user-configurable timeout/blocking setting。

- `features.default_mode_request_user_input` 只是 under-development feature，用来让 Default mode 暴露该 tool；它不是“always wait”开关。
- 当前 config schema 能找到 `default_mode_request_user_input: boolean`，但没有 `[tools.request_user_input] timeout_enabled/timeout_ms/on_timeout` 之类 production setting。
- 当前 TUI source 对 `is_blocking=false` 使用固定 60s hidden grace + 60s visible countdown；`is_blocking=true` 或用户手工 snooze 才禁用 auto-resolution。
- 当前 Default collaboration instruction 明确区分：`request_user_input` 只用于 optional question；若 explicit user input 真的是继续执行的必要条件，应直接发送一条 concise plain-text question，而不是使用该 tool。
- open issue #43759、#37472、#34455、#29702、#28969 仍在请求 Default-mode always-wait / configurable timeout；#43759 甚至报告较新的 Desktop build + CLI 0.153.4 仍没有 persistent global setting。因此仅升级 CLI/App 目前也没有已验证依据可解决本问题。

### 结论

**当前没有受支持的 `config.toml` 参数能把 Default-mode native `request_user_input` 改成 indefinite blocking。**

三个现实替代：

1. **全任务切 Plan mode**：native blocking 更接近所需语义，但把“工作方式”和“是否等待用户”绑在一起，且需要改变正常 implementation mode；不采用为全局默认。
2. **fork/patch Codex Desktop/CLI source**：技术上可把 Default 的 `is_blocking` 改成 true 或新增 config，但需要维护自定义 Desktop/App/CLI、跟随 upstream 更新，属于高维护 unsupported fork；不作为 056 主路线。
3. **Default mode 使用 durable transcript wait/resume**：符合当前 upstream Default instruction；probe 已证明同 thread transcript resume 能恢复一次；这是当前最小、成熟、可解释的 fallback。采用为主路线候选。

## 4. W2 transport 的 Planner 建议

v6 顶级架构不变，W2 的 transport branch 建议从 `PROBE_REQUIRED` 收敛为：

```text
Default-mode HUMAN_ONLY gate
-> 不依赖 native request_user_input 的 non-blocking question card
-> 发送一条清楚、单步的 plain-text user question
-> 写/保留当前 resume point
-> 当前 dependent execution 结束并保持 recoverable waiting
-> 用户未回复：什么都不继续，不 polling，不 timeout，不 terminal BLOCKED
-> 用户在同一 thread 明确回复
-> 重读 resume point / current task state
-> exact-once resume
```

这项能力名称应诚实写成：

`DURABLE_TRANSCRIPT_WAIT_RESUME`

而不是 `NATIVE_PERSISTENT_PROMPT`。

### Bridge Kit config 候选

为了避免 Default mode 继续偶发使用会 auto-resolve 的 `request_user_input`，implementation 阶段优先评审一个很小的 Bridge Kit host-policy change：

```toml
[features]
default_mode_request_user_input = false
```

理由：

- Plan mode 的 native `request_user_input` 不依赖该 flag；
- Default upstream instruction 本来就要求真正必需输入时 direct plain-text question；
- 关闭 tool 比“工具仍存在但要求 agent 永远记得不要误用”更 fail-closed；
- optional questions 在 Default mode 本来也应优先合理假设而不是打断用户。

但这是 **implementation candidate，不是本 addendum 自行批准的 production change**。Critic 需要审它是否会破坏当前合法场景；实施时还要 normal-entry replay：Default required human gate 应使用 transcript wait/resume，Plan-mode合法问答保持正常。

如果 Critic 不接受关闭 flag，次选是保留 flag 但在 workflow/host rule 中禁止它用于 `HUMAN_ONLY` gate；这比关闭 flag 更依赖模型遵守文本规则，风险较高。

## 5. 新问题 A：已有本地 repo 却绕去临时 clone

最新 Bridge Kit 开发反馈显示：Executor 因 canonical checkout 有一项无关 `.gitignore` dirty change，就在 `/tmp` 新 clone；发现 local clone 的 origin 指向另一本地 checkout 后又尝试 `git remote set-url`，触发授权拦截；用户随后明确指出机器上本来已有合适 clone，应先找并 pull。

这不是 Bridge Kit 产品 bug，也不需要新增 Lite 第 7 条或 workflow W6。它属于 **Verified Workflow 已有 Source Discovery / dirty-tree protection 的 enforcement 缺口**。

后续 refinement 应补一个小的 source-resolution contract：

1. task 指向已知 repo 时，先定位本机已有 canonical checkout / worktree / clone；
2. 核对其 branch/ref/origin/dirty state；
3. unrelated dirty file 要保护，但**不能仅因 dirty 就默认抛弃 canonical repo**；
4. 需要 isolation 时，优先从已验证 canonical repo 创建 clean worktree，或使用机器上已经存在的正确 clone；
5. 只有确实没有可用本地 source 时才 network clone；
6. 不通过“local clone -> 再 remap remote”制造额外 provenance/授权风险；修改 Git remote 仍是独立高影响动作，不能用 ordinary push 授权替代；
7. local existing implementation / mature helper / canonical repo 应优先复用，不为方便重新造临时低信息副本。

这属于现有 source discovery 的 refinement，不进入 v6 新 capability 计数。

建议增加一个 workflow regression scenario：

```text
existing canonical local repo + unrelated dirty file + task needs clean implementation surface
=> preserve dirty file
=> discover existing worktrees/clones
=> use canonical local source / clean worktree
=> no redundant clone
=> no remote remap
```

## 6. 新问题 B：CUHK Date data-backed / localized consumer flow

当前 main 已新增：

`docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_CUHK_DATE_REAL_FEEDBACK_2026-09-17.md`

该反馈的核心判断正确：**不增加新 W capability，把缺口强化进 W1/W3/W5 与 Frontend F-B/F-C。**

### 6.1 W1 — Acceptance Review Admission / Vertical Closure 增补

当 frozen claim 本身包含 breadth / variants / locales / hosted lifecycle 时，`real target behavior` 不能只用一个 happy path 表示；按目标风险加入小型 representative coverage：

- catalog/search：真实 corpus breadth + representative known items；
- material product branches：代表性 branch matrix；
- locale support：有限 enum/control 的 reachable locale coverage；
- provider-backed feature：configured target environment 的 capability presence；
- persisted/uploaded state：必要时检查 action -> navigation -> refresh/re-entry -> same authoritative state。

同时明确：

> fallback/recovery 只能证明 recoverability；除非 Goal 明确接受为等价结果，否则不能证明 primary capability complete。

因此 `自由文本兜底`、`needs_review`、`Needs setup` 等可以是诚实 fallback，但不能让对应 primary claim 进入 acceptance-ready。

### 6.2 W3 — Verification / Evidence Fidelity 增补

- external/provider claim：mock adapter test 证明 adapter；hosted capability 需要安全、bounded 的 real configured provider evidence；
- controlled interaction：当 intermediate state 会被代码转换时，验证真实 sequence，而不仅 final value schema。例如 `1 -> 17 -> 178`、paste、backspace/replace、blur/commit；
- material branch：source counts/type-level support 不能替代普通 product entry 的代表性 branch replay。

### 6.3 W5 — Change Impact / Should-not-change 增补

rewrite/refactor 不得把已被用户接受或已经真实工作的 structured interaction 静默降级成低质量 generic fallback。

例如已有“兴趣大类 -> 具体标签”的成熟 interaction，schema/UI rewrite 不能未经明确产品决策退化成自由文本 list。

### 6.4 Frontend F-B/F-C 增补

localized consumer UI 的有限 enum/token 应有 deterministic completeness：

- supported locale 必须覆盖 reachable finite values；
- internal enum identifier 不能作为 production fallback；
- proper noun/acronym 可以 narrow allowlist；
- actual-surface convergence 还要找 untranslated/internal token 与跨 branch UI 不一致。

这不是要求所有项目实现 i18n；只在 frozen objective 声称多个 locale 时触发。

## 7. Capability Gate Matrix 的增补场景

不新增 G9/G10；把以下场景并入现有 gates：

### G1/W2 Human gate

- `HUMAN_ONLY secret` -> durable transcript question -> wait -> same-goal resume；
- `AGENT_RESOLVABLE local repo/source issue` -> 不 prompt 用户；
- `UNSUPPORTED_WITH_EVIDENCE` -> truthful close，不让用户“配置一下试试”。

### G2/W1 Acceptance Admission

CUHK-Date-like candidate：build/tests 绿，但同时存在 demo catalog、material branch 未覆盖、fallback-only primary feature、hosted config 未消费真实 backend capability -> `READY_FOR_USER_REVIEW=NO`。

### G4/W3 Faithful regression

final-value test 绿但真实 keystroke sequence 失败 -> gate 必须 FAIL；mock provider test 绿但 configured staging provider 未工作 -> hosted claim 不能 PASS。

### G7 Non-overreach

small docs/server/nonvisual fix 不触发 locale/catalog/provider/branch matrix；只有 frozen claim 真包含这些维度才触发。

### Source-discovery regression（现有 workflow source discovery，不新增 capability）

existing canonical repo + unrelated dirty state -> reuse local source/worktree；不重复 clone/remap remote。

## 8. 仍然不做什么

- 不新增 W6/W7；
- 不新增 Lite 条数；
- 不因为 CUHK Date 写一个通用“所有表单都跑全矩阵”的 checklist；
- 不把 Programme、GeoNames、YuNet、TMDB/OpenLibrary 等项目细节写进通用 plugin；
- 不 patch/fork Codex Desktop 作为默认路线；
- 不新增 watcher、polling daemon、Persistent Run、Control、ledger 或第二状态机；
- 不把 durable transcript fallback 冒充 native persistent prompt；
- 不在这个 addendum 修改 Bridge Kit config 或任何 production source。

## 9. Planner 当前建议与下一步

Planner 当前建议：

1. **保持 v6 已 PASS 的 6 Lite + 5 workflow + 3 Frontend + 1 maintainer 架构不变**；
2. W2 transport 选择 `DURABLE_TRANSCRIPT_WAIT_RESUME`；
3. implementation Plan 中评审并优先采用 `default_mode_request_user_input=false` 作为 fail-closed host config，避免 Default mode 再误用 auto-resolving native card；
4. 将 local-repo reuse 作为现有 Source Discovery 的 enforcement 修复；
5. 将 CUHK Date 的 8 类真实失败分别并入 W1/W3/W5/F-B/F-C，不新增 capability；
6. 在冻结 implementation Plan 前，让独立 Critic 对本 addendum 做一次**短的 post-probe review**，重点审 transport choice、关闭 feature flag 的副作用，以及新 evidence 是否真的只是已有 capability refinement。

`NEXT_HANDOFF = CRITIC_POST_PROBE_SHORT_REVIEW`
