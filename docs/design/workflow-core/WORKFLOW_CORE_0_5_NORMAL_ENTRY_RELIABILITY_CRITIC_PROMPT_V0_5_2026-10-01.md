# workflow-core 0.5 — Design Re-review Prompt v0.5

你继续作为 AI Research Stack 的独立 Critic thread，对 `workflow-core / Verified Workflow 0.5` 做新的 DESIGN_REVIEW。

这不是 execution-ready review。上一套 Reviewed Handoff execution package 已被 Planner 明确判定为路线错误并废弃；本轮先重新审 architecture，不得启动 Codex implementation。

## Active Design Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: `workflow-core`
- design_topic_or_task_key: `workflow-core--normal-entry-reliability`
- source_branch_or_ref: `main`
- review_stage: `DESIGN_REVIEW_R5`
- reviewed proposal: `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_5_2026-10-01.md`
- proposal commit: `7c5a04a1142bdcbbd707f9c998b1a9ce64df66e1`
- prior approved design: `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_4_2026-10-01.md`
- superseded execution package commit: `c7fb7488d3847855609d86fb0307bfeea824e078`
- implementation state: `NOT STARTED`
- execution branch/worktree: `NONE / NOT AUTHORIZED`

V0.5 Proposal explicitly supersedes the V0.1/V0.2 Plan/Goal/Kickoff packages. Do not审那些旧 package 是否还能修；它们已经 `SUPERSEDED / NOT EXECUTABLE`。

## 必须重新读取

从最新 `main` 实际读取：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`
- `docs/plugin-todos/workflow-core.md`
- `docs/plugin-changelogs/workflow-core.md`
- `skills/core/codex-system/codex-workflow-protocol/SKILL.md`
- `skills/core/codex-system/codex-workflow-protocol/references/escalation-rules.md`
- `skills/core/codex-system/codex-workflow-protocol/agents/openai.yaml`
- `skills/core/codex-system/codex-workflow-protocol/evals/trigger_queries.json`
- Proposal V0.4
- Proposal V0.5

Bridge Kit只做 owner-boundary / reality check，不设计、不修改。至少核实当前：

- `release` ref；
- `pyproject.toml` / package version；
- current `main`；
- `ai_bridge_kit/host.py` 中 `GIT_ASKPASS/SSH_ASKPASS` publisher preflight；
- release -> current main 的实际 diff surface；
- current main 是否已经有独立 Bridge execution-reliability proposal。

不要把 Bridge-side问题改写成 workflow-core production source要求。

## 本轮需要重新审的核心变化

### R5-1 — 是否应该废弃 Reviewed Handoff execution topology

Planner结论：

workflow-core 0.5 没有 Reviewed Handoff 的不可替代需求，应回到普通 bounded implementation：

```text
one ordinary task branch
-> source-first implementation
-> deterministic tests + known regressions
-> stable 0.4 qualification candidate
-> original failure + unrelated regression PASS
-> exactly-once 0.4 -> 0.5
-> repository next PATCH
-> regenerate
-> one final candidate
-> final candidate G1-G6 + broad CI
-> independent final-candidate Critic
-> release closure
```

请独立判断：

- 是否真的不需要 Reviewed task / CURRENT / PLAN_FROZEN / watcher / Scheduled Reviewer；
- 是否存在某个用户目标、证据、付费、私有artifact、不可逆风险或自动review需求，使 Reviewed Handoff仍不可替代；
- 如果不存在，不得为了“更规范”强迫保留重控制层；
- ordinary branch是否足以满足 source isolation、final-candidate identity和release closure。

### R5-2 — specialist-first 是否应扩展为 least-privilege normal-entry selection

Planner保留 V0.4 capability discovery，但增加：

> 在冻结目标允许的合法 route 中，优先选择能完成当前 effect 的最低权限 canonical/normal entry；repo-local workspace操作可完成时不主动要求更高权限。

同时 escalation前先判断 effect 是 required / optional / unknown；optional cleanup不应成为 approval blocker。

请检查：

- 这是workflow-core职责还是Host/Bridge职责；
- 是否会把“least privilege”写成过宽禁令；
- 是否保持 genuine required escalation的合法路径；
- 是否需要新permission registry/state（Planner主张不需要）。

### R5-3 — approval-aware privilege-non-increasing recovery

V0.4 六维等价保持：

1. frozen effect
2. professional quality
3. acceptance evidence strength
4. safety/privacy
5. artifact identity
6. current authorization scope

V0.5 额外要求 automatic recovery 的 privilege/authority surface不得扩大，除非 current user新增明确授权。

重点审：

- bounded publisher -> raw push 自动fallback应被拦；
- canonical wrapper -> unsandboxed/general shell 自动fallback应被拦；
- lower-privilege且六维等价 recovery仍应允许；
- privilege guard是否是必要的eligibility条件，而不是应机械增加成第七个state/schema字段；
- “route correction”与“fallback”区分是否可执行。

### R5-4 — approval rejection 四类归因

Planner冻结：

1. optional/non-required effect；
2. 错选高权限 route；
3. genuine authority boundary；
4. normal entry itself broken。

请攻击：

- 是否漏掉重要失败类；
- 是否足以覆盖用户真实事故；
- 是否会把安全拒绝错误解释成“选错route”然后继续绕过；
- normal-entry broken时是否正确fail closed并交回owner，而不是workflow-core接管底层实现。

### R5-5 — W4 approval-rejection circuit breaker

Planner要求：

同类 approval rejection连续出现，或同一bounded effect被拒后准备换同级/更高权限route重试，必须先停止approval-sensitive execution并做route reassessment。

只有真正新信息才允许再次尝试。

请检查：

- 是否能阻止blind escalation；
- 是否会误伤一次正常、明确授权后的合法重试；
- “换shell/python/raw wrapper”不算新信息是否合理；
- 是否与现有W4同根，还是Planner错误增加了新的状态机语义。

### R5-6 — effect-scoped evidence preservation

Planner要求：

如果 build/render/QA/local commit已经成功，publication后续失败只能阻塞publication effect；不能把local成果重新判FAIL，也不应重跑未受影响步骤。

请判断：

- 这是否应属于W3/W1；
- overall Goal required publication时仍必须 complete=NO；
- optional publication/cleanup时是否应允许总体目标不被阻塞；
- 是否存在“保留成果”导致过度声称完成的风险。

### R5-7 — G6 是否是真正必要的新 Gate

Planner只新增一个 G6，不复制 G1–G5：

```text
ordinary complex task
-> workflow-core actual implicit consumption
-> repo-local build/check uses workspace-write normal entry
-> optional cleanup does not trigger escalation
-> bounded/canonical publication route attempted
-> bounded publisher returns authority/transport blocker
-> completed local artifacts + local commit remain intact/valid
-> raw git push / broader privileged fallback NOT attempted
-> no second same-class escalated retry without new information
-> only publication effect remains blocked
```

要求 actual command/tool trace、artifact/commit identity before/after；不能靠source grep/self-report；fixture不得硬编码具体项目/用户名/Longleaf/ctex/scenario id。

请判断：

- G6是否确有不同failure semantics/evidence surface，值得独立Gate；
- 是否与G2/G3/G4高度重复；
- 如果保留，如何防止用mock/helper冒充normal entry；
- bounded publication failure在安全preflight处发生是否足够真实；
- 是否还需要approval rejection deterministic regression作为G3开发bank，而不把G6做成随机审批测试。

### R5-8 — G1–G5 变化是否最小

V0.5声称：

- G1不变；
- G2扩route selection；
- G3扩approval/recovery；
- G4保留capability-discovery integrated normal entry；
- G5保留broad regression并增加should-not-change；
- 只新增G6。

确认没有机械复制Gate，也没有借新事故重开 #7/#8/#9/#10 专属逻辑。

### R5-9 — release selection是否更简单且仍可信

Planner不再让0.4 candidate跑完整final campaign两次。

开发阶段：

```text
known regressions + targeted G1/G2/G3 + unrelated regression
-> stable 0.4 qualification candidate
```

只有qualification PASS后才 exactly-once bump。

然后 version-bumped final candidate：

```text
G1-G6 + broad CI
-> independent final-candidate Critic
-> release closure
```

请判断：

- 是否仍满足same-final-candidate release claim；
- 0.4 qualification是否足够证明“值得bump”，又没有重复完整final campaign；
- final Gate失败后的repair/rerun规则是否避免挑赢家；
- 当前没有paid/fresh one-shot holdout时，是否确实不需要额外mid-implementation control workflow。

### R5-10 — Bridge事实与ownership

请独立核实并纠正任何不准确之处：

- formal `release` ref当前是否为 `9dad0ba4bfa54e251f345091c5151ae991251ec9`；
-该ref是否为0.9.3；
- current main相对release是否只有docs/evidence/design changes而无runtime source变化；
- release `host.py`是否在sanitization前因ambient `GIT_ASKPASS/SSH_ASKPASS` fail closed；
- Bridge current main是否已有独立0.10.0 proposal。

即使这些成立，也只用于scope owner判定；不要把Bridge 0.10的实现设计塞进workflow-core review。

用户提供的 duplicate editable metadata是runtime evidence，不是repo可独立验证事实；Critic应保持这个证据边界。

## 外部独立核查

按Critic contract做少量官方核查，优先OpenAI：

- Codex sandbox/approval的低风险顺畅、高风险显式边界；
- Auto-review为何需要避免主agent把approval当障碍绕过；
- Skills如何定义workflow、stop/ask/incomplete-result handling。

Planner参考：

- https://openai.com/index/running-codex-safely/
- https://alignment.openai.com/auto-review
- https://developers.openai.com/plugins/concepts/skills
- https://developers.openai.com/plugins/build/skills

不要只复述Planner。

## Supersession boundary

以下execution package已废弃：

- Plan v0.1 / Goal v0.1 / Kickoff v0.1
- Plan v0.2 / Goal v0.2 / Kickoff v0.2
- package commit `c7fb7488d3847855609d86fb0307bfeea824e078`

Critic不得对它们给 `READY_FOR_CODEX=YES`。

本轮如果PASS，只批准V0.5设计方向。下一步回Planner重新制作**普通bounded implementation** execution package。

## Version / permission boundary

当前仍然：

```text
workflow-core = 0.4 / NO_BUMP
repository bump = NONE
implementation = NOT STARTED
execution branch/worktree = NONE / NOT AUTHORIZED
maturity = unchanged
paid API = NOT AUTHORIZED
```

## 输出要求

给出：

`RESULT = PASS` 或 `RESULT = REVISE`

若REVISE：

- 每个blocker给stable finding ID；
- requirement/source；
- direct evidence；
- causal risk；
- minimum closure condition；
- owner；
- 按Critic Role Contract自动附完整Planner返修prompt。

若PASS：

- 明确哪些V0.4设计继续保留、哪些被V0.5扩展；
- 明确Reviewed Handoff execution topology已被设计层废弃，原因是什么；
- 明确G6是否成立以及它证明什么真实用户行为；
- 明确Bridge follow-up仍由Bridge owner处理；
- PASS只批准V0.5设计，不批准implementation/version/release/branch/worktree/paid action；
- 下一步回Planner准备一个ordinary bounded implementation的Proposal/Plan + Canonical Goal + Kickoff Draft execution package；
- 不要启动Codex。
