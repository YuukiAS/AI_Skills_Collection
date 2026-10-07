# 059 Research Authoring C3 integrated owner-chain recovery — Critic Review v0.1

日期：2026-10-07  
角色：独立 Critic  
审查阶段：EXECUTION_READY_REVIEW_AFTER_C3_DEVELOPMENT_FAIL  
Task：`research-authoring--formal-production-authoring`

## 结论

```text
RESULT=REVISE
RA-C3DEV1_RECOVERY_DESIGN=REVISE
READY_FOR_CODEX=NO

C2_G1_FAIL=PERMANENT
04a17a904ce522cb4a517cb33f22e062f2bcbc09=FAILED_PROVISIONAL_DEVELOPMENT_ATTEMPT

P2=NOT_CREATED
C3_FINAL_CANDIDATE_COMMIT=NOT_ADMITTED

FINAL_GATES_AUTHORIZED=NO
LIVE_PLUGIN_UPDATE_AUTHORIZED=NO
PAID_API_AUTHORIZED=NO
MAIN_MERGE_RELEASE_AUTHORIZED=NO

BLOCKERS=RA-C3DEV1
NEXT_HANDOFF=PLANNER
```

本 recovery 的主方向成立：`allow_implicit_invocation=false` 是当前 OpenAI/Codex 支持的真实 machine-consumed Skill policy；把 `research-main` 的 artifact delegates 做成 profile-scoped explicit-only，比继续加 description/routing wording 更直接命中 DEV-04/DEV-05 的失败机制。

当前只剩一个同一 blocker 内的覆盖缺口：计划把 `latex-paper-authoring` 从 research-main 的 implicit Skill Routing 中移除并改为 explicit-only，但 profile routing contract 和 P2 regression matrix 没有给它的 **direct existing-LaTeX compile/debug/source-hygiene 模式** 留出明确 normal entry，也没有运行时验证这个原有能力没有被新 policy 切断。

不需要重开主架构，不需要改 Bridge/shared replay，也不需要新增 Gate。

## 已通过部分

### 1. OpenAI/Codex policy 机制成立

当前官方 Skill 文档说明：

- model 先看到 Skill metadata；
-完整 Skill instructions 在匹配/显式调用后读取；
- `agents/openai.yaml` 支持：
  `policy.allow_implicit_invocation=false`；
- false 时 Skill 不进入默认模型上下文，但仍保持 enabled，可显式调用。

当前 Codex source 的 `SkillMetadata::allows_implicit_invocation()` 也把该字段解释为 implicit visibility policy，而不是 disable。

因此 Planner 选择“profile-installed local copy + destination-local `agents/openai.yaml` policy”作为结构性 recovery 有真实平台依据。

同时，pinned `codex-cli 0.153.4` 是否与 current main完全一致仍不能凭文档推断；v0.3 在 P2 前安排 task-local runtime preflight，并在失败时 STOP，不用 wording fallback。这个处理正确。

### 2. generic pdf 的处理现在合理

DEV-05 已经证明 generic `pdf` 在 integrated new-manuscript route中实际被读取，因此不能继续当纯理论风险。

但证据仍是 `research-main` surface-specific。先把 research-main 安装的 local copy变成 explicit-only，同时保持 canonical global `pdf` 不变，是比全局收窄更小的 repair。

P2 matrix还要求 existing-PDF操作通过 explicit generic pdf delegate工作；如果 same-name global copy仍绕过 local policy，必须 STOP。当前不需要提前扩大到 global generic pdf。

### 3. renderer 的处理合理

04a17 renderer metadata已经写明它不应先拥有科研文档 authoring，但 DEV-04仍然先读 renderer。

因此继续加强 renderer wording没有新的因果价值。

把 research-main 的 renderer local copy改成 explicit-only，并让 finalized-source render-only在 profile route中显式进入 renderer，是更直接的 enforcement。

### 4. current-runtime preflight 足够作为 P2 admission

preflight要求同时证明：

- destination policy写入；
- implicit selection消失；
- explicit/local path仍可用；
- same-name global/user Skill不被修改；
- manifest-bounded install/cleanup。

如果这五项失败就不形成 P2，足以避免把“current main文档语义”未经验证地投射到 pinned runtime。

### 5. shared installer 扩展的范围仍可接受

`explicit_only_skills` 是一个 optional profile field，不引入 daemon/router/database/state machine。

它要求：

- field只引用 profile primary skills；
-普通 profiles保持现有行为；
- policy Skill必须 local copy；
- source不被修改；
- sidecar字段安全 merge；
- manifest记录实际 mode/override；
- reinstall/prune继续 manifest-bounded。

这是对现有 profile installer 的小扩展，不是第二套路由框架。

### 6. Bridge / authorization

已读取最新 Bridge Kit `main` `050c786d7480a00b924aa6f2b0c4542eae4b1e3f` 的 `AGENTS.md` 及 Reviewed Handoff branch/worktree/Kickoff约束。

当前 Kickoff仍绑定 exact repository / task / branch / worktree，并且只允许 bounded source/tests/evidence与 ordinary non-force publish；没有借 recovery扩大 Bridge、branch、remote、force/destructive Git权限。

Bridge不需要修改。

## RA-C3DEV1 — explicit-only LaTeX delegate 缺少 direct-mode normal entry 与回归

### requirement

Recovery Proposal与 Plan明确保留 `latex-paper-authoring` 两种模式：

1. **direct existing-LaTeX mode**：
   existing source compile/debug、template repair、bibliography/build troubleshooting、existing-source render/build，可以 compile；

2. **Research Authoring delegate mode**：
   只负责 source/package，不能直接生产 final PDF，随后交给 renderer。

同时 P2会把 `latex-paper-authoring` 从 research-main 的 ordinary implicit Skill Routing中移除，改成 explicit-only。

因此 research-main 必须同时有清楚、可消费的路由入口，让 ordinary existing-LaTeX compile/debug请求还能显式进入 `latex-paper-authoring`。

### direct evidence

当前 v0.3 `research-main` proposed routing只列：

- new/substantial report + PDF；
- new/substantial manuscript + PDF；
- finalized-source render-only -> explicit renderer；
- existing-PDF -> explicit generic pdf。

没有：

```text
existing LaTeX source + compile/debug/template/build/source-hygiene
-> explicit latex-paper-authoring
```

与此同时，managed AGENTS设计又要求 explicit-only delegates：

- 不出现在 ordinary Skill Routing descriptions；
- 只有 profile routing notes到达 delegate stage时才读取。

因此把 `latex-paper-authoring` 隐藏以后，当前 package没有定义它在 direct existing-LaTeX模式下的 profile stage。

Development matrix的新增 should-not-change同样缺这一条：

- DEV-06/07只验证 research-main finalized-source render-only能显式到 renderer；
- DEV-08只验证 research-main existing-PDF能显式到 generic pdf；
- DEV-05验证的是 Research Authoring delegate mode。

没有一个 subrun证明：

```text
research-main
+ existing LaTeX source
+ compile/debug/template/build request
-> explicit latex-paper-authoring
-> compile/debug remains allowed
-> renderer/Research Authoring不错误接管
```

### causal risk

这个 recovery正通过 machine policy把三个 artifact Skills从 implicit catalog里拿掉。

如果只验证 Research Authoring delegate mode，而不验证 LaTeX direct mode，可能把原本正常的 existing-LaTeX编译/调试入口一起切断。

这会造成一个新的 user-visible regression：

```text
修复“新 manuscript PDF 被 LaTeX 提前编译”
->
research-main 下真正的 existing-LaTeX compile/debug 也找不到 owner
```

这不是为了“更保险”多加测试，而是被本次 production mechanism直接影响的 should-not-change场景。

### minimum closure

不改 recovery主架构，不新增 Gate，不新增 case family。

只需在同一 v0.3 package做两项很小的同步：

1. **research-main routing contract补 direct LaTeX stage**

例如语义为：

```text
existing LaTeX source where the main task is compile/debug,
template/source-hygiene, bibliography/build troubleshooting,
or existing-source build
-> explicitly load latex-paper-authoring
-> compilation/debug allowed
```

并继续与：

```text
finalized source render-only
-> explicit render-chinese-math-pdf
```

区分。

对于新建/实质修改 manuscript，无论是否最终要 PDF，仍保持 Research Authoring first；需要 LaTeX source/package时才显式进入 LaTeX delegate。

2. **把 direct-mode回归折进现有 development matrix**

建议并入 DEV-07 或 DEV-08，不创建 DEV-12：

```text
research-main existing-LaTeX compile/debug subrun
-> managed AGENTS明确提供 direct LaTeX delegate route
-> latex-paper-authoring actual read > 0
-> compile/debug allowed
-> no premature Research Authoring rewrite
-> no generic pdf owner
-> renderer only if the user task later becomes render-only/final artifact
```

保持 natural request，不写内部 Skill名。

同步 Plan / Goal / Kickoff / Gate impact / package描述后，再交 Critic复核。

Owner：Planner。

## README Clear Writing

当前 package已经把之前缺失的 README Clear Writing durable evidence补进 P2前置合同：

- exact README hash；
-自然 review request；
- installed `writing-style` consumption trace；
- decision/patch。

如果无需改文案，允许记录 no-change结果。

该部分已关闭，不新增 blocker。

## Gate / candidate boundary

```text
ADD_G5=NO
G1_G4_TAXONOMY_CHANGED=NO

04A17_DEVELOPMENT_EVIDENCE=REGRESSION_ONLY
P2_PREFLIGHT=DEVELOPMENT_ONLY
P2_FULL_11_CASE_MATRIX=DEVELOPMENT_ONLY

FINAL_GATES_NOT_STARTED=YES
```

P2仍必须完整重跑原11类开发场景，不能拼接04a17的 PASS。

本次补充的 existing-LaTeX direct-mode验证是现有 case内 should-not-change subrun，不是 G5，也不增加 final Gate taxonomy。

## Maintenance tracking

Issue #99仍是旧的 early-C0 reader-facing状态，与当前 C2 permanent FAIL / C3 recovery不一致。

按照仓库规则，Issue实质改写必须先真实调用 Clear Writing。本 Critic不绕过该约束。

下一次合法 maintenance mutation应同步当前 recovery状态并保持 Project lifecycle为 `DOING`；该 tracking drift不阻断本 execution package的技术复核。

## 当前边界

```text
RA-C3ER1=CLOSED
RA-C3DEV1=OPEN

READY_FOR_CODEX=NO
P2=NOT_CREATED
C3_FINAL_CANDIDATE_COMMIT=NOT_ADMITTED

FINAL_GATES_AUTHORIZED=NO
LIVE_PLUGIN_UPDATE_AUTHORIZED=NO
PAID_API_AUTHORIZED=NO
MAIN_MERGE_RELEASE_AUTHORIZED=NO
```
