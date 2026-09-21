# 056 交付工作流可靠性基线 — v6 有界修订

- 日期：2026-09-21
- Package version：v0.4
- Historical technical task key：056_product_delivery_discipline
- Human-readable name：交付工作流可靠性基线（Delivery Workflow Reliability Baseline）
- Primary repository：YuukiAS/AI_Skills_Collection
- Current AI_Skills source：main@72f163330ea5a21637df95f08289e2c4739d2bd9
- Current Bridge source：YuukiAS/GPT_Codex_AI_Bridge_Kit main@9d2da9f485f26ca51842a1909a276cb44f73351a
- Architecture authority：PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md + post-probe addendum
- Disposition：V6_BOUNDED_AMENDMENT
- Status：DRAFT_FOR_INDEPENDENT_CRITIC_REVIEW

## 1. 结论

056 不应变成一个永远吸收后续事故的长期 mega-task，也没有证据需要建立 successor architecture owner。它仍然是一次 bounded implementation task，但人类可读名称应从 “Product Delivery Discipline” 改为“交付工作流可靠性基线”。

这个名字比旧名更准确：本轮真正要建立的是复杂任务从 source、执行、Human Gate、恢复、验证、actual surface 到 acceptance 的可靠基线，而不是一次性的“纪律文本”。“基线”同时明确它有可关闭的完成边界；未来 Lucerna、CUHK Date、Mica、Server/HPC 等暴露的新 failure 继续进入 workflow-core / Frontend Design / AI Skills Maintainer / Bridge 的 regression bank 与 TODO，由 Gate lifecycle 判断是否是既有能力回归或新的 bounded refinement，不继续无限扩张 056。

长期 owner 是 production capability，不是 task 056：

- workflow-core：任务执行、Human Gate eligibility、acceptance/evidence/recovery semantics；
- Frontend Design：canonical design、design-system、actual-surface convergence；
- AI Skills Maintainer：AI_Skills 中规则/生成层/安装身份/consumer path 的维护闭环；
- Bridge Kit：host transport、wait/resume、Persistent Run 等跨 repo runtime capability；
- domain plugin：专业判断；
- repo AGENTS：项目独有 invariant / locator。

因此三种路线中选择 A，而不是 B/C：056 做完后关闭；统一语义由上述正式 owner 持续维护。

## 2. 名称与技术身份

比较过三个候选：

1. 交付工作流可靠性基线；
2. 可靠交付与人工门控工作流；
3. 复杂任务交付与恢复机制。

选择“交付工作流可靠性基线”。第二个名字过度突出 Human Gate，弱化 W1/W3/W5、Frontend 和 consumer diagnosis；第三个名字又弱化 acceptance / actual-surface / delivery。

technical key 继续保留 056_product_delivery_discipline。当前 Gate-lifecycle / identity 规则已经明确：task key 是技术 locator，人类标题与 machine key 分离；历史 numbered key 继续兼容。没有收益足以抵消迁移 branches/results/references/history 的成本，因此：

- 不迁移 historical task key；
- 不批量重命名旧 056 文件路径；
- 新增的 amendment / Critic prompt 可以使用新的 human-readable label；
- 后续真正的新 task 才遵循 semantic task-key 规则。

## 3. 最新 main 对 v0.3 的实质影响

v0.3 的 source/version 假设已经失效，不是只换 SHA：

### AI_Skills

当前 production baseline 已是：

- Repository / CLI：5.0.6；
- workflow-core：0.2；
- ai-skills-core：0.3；
- web-development：0.1。

刚完成的“工作流命名与插件回归机制完善”已经把 semantic task identity、human label separation、Gate lifecycle、regression bank、narrow-vs-broad/full fallback、same-final-candidate 规则接入 production，并完成真实 candidate plugin replay 与 production smoke。

这部分不能由 056 重复实现。056 必须把这些能力列为 should-not-change baseline。

但当前 workflow-core 0.2 仍没有实现原 v6 的 W1-W5 delivery/Human-Gate contract；web-development 0.1 仍未接入原 v6 的 F-A/F-B/F-C production wiring；AI Skills Maintainer 0.3 已经覆盖一部分 regression/consumer diagnosis 原则，但尚未完整实现 v6 G8 所要求的 installed/generated/invocation/task-entry/session/normal-entry diagnosis 闭环。因此 056 仍有真实 production work。

### Bridge

当前 production source version 已是 0.8.4。0.8.4 已完成 semantic task-key compatibility；0.8.1 已有 upfront authorization preflight；0.8.0 已有 Persistent Run。

但 Host source / templates / tests 仍管理 default_mode_request_user_input=true，Default required-human-input 的 fail-closed transcript semantics 仍是 056 未完成工作。因此旧 0.8.4 candidate slot 已被消费；本轮若形成兼容 Bridge candidate，应为 0.8.5，而不是重用 0.8.4。

## 4. 最近问题逐项归类

### Persistent Run 长期可靠性

Disposition：BRIDGE_ONLY_FOLLOWUP。

056 只保留两个上层 invariant：长期执行不能因 Codex/SSH 生命周期结束被判失败；session/job/PID/heartbeat/checkpoint 只证明运行状态，不证明 Goal 完成。这两点已经由 Bridge Persistent Run 与 v6 evidence semantics 覆盖。

以下属于 Bridge Persistent Run 独立能力，不并入本轮：

- tmux discovery / preflight；
- 数小时 / overnight durability；
- 真实 SSH disconnect / reconnect；
- stale session reconciliation；
- checkpoint/resume；
- duplicate-launch protection 的长期行为；
- progress / ETA reporting。

近期 50 分钟真实 H100 run 是有价值的 basic behavior evidence，但不足以支持上述 durability claim。login PATH 找不到 tmux、最后使用 allocation node user-space copy 的事实应进入 Bridge 后续 preflight/durability refinement。当前不为此创建 successor task。

### 普通复杂任务 bounded kickoff

Disposition：DEFER_AFTER_056_WORKFLOW_CORE。

最新 source 已经解决了两层中的大部分：

- Planner/Critic v1.4 要求 execution-ready package 自带完整 Kickoff Draft；
- Bridge 0.8.1 Codex startup preflight 已明确：repo Goal/Plan 只是 frozen scope，不是 current-user authorization；当前消息已授权同一 frozen effect 时不得重复问。

当前残余缺口是“不经过 Planner/Critic 的普通复杂 workflow task”还没有统一自动渲染 copy-ready bounded kickoff。这是 workflow-core task-authoring UX / handoff refinement，不是 056 正确性的 blocker。本轮 056 自己已经有完整 Kickoff Draft，因此不需要为了修普通 task authoring 再扩大 v6。

### Human Gate 前 least-privilege equivalent recovery

Disposition：ABSORB_IN_056_NOW。

这是本轮唯一新增的实质 amendment，但不新增 W/G。

现有 W2 已经声称：只有真正 HUMAN_ONLY 才能问用户；AGENT_RESOLVABLE 由 Executor 解决。CUHK Date 暴露的是 W2 eligibility 定义还不够完整：权限不足可能只是 Executor 自己选了一个更重的实现路线，而不是 frozen Goal 本身缺权限。

v0.4 在 W2 内增加以下规则：

1. 在因 credential scope / provider permission / paid resource / environment mutation 准备进入 Human Gate 前，先判断该权限是 frozen Goal 所必需，还是当前实现路线才需要；
2. 对已经知道、已经授权的可行路线做 bounded equivalence check，不要求无限搜索新 provider；
3. 如果存在 lower-privilege route，并且它在 security/privacy、product behavior、evidence quality、quality bar、provider/data/purpose boundary 上与 frozen completion contract 真正等价，则自动选择该路线继续；
4. degraded/manual/fallback 不能因为省权限就被称为 equivalent；
5. route switch 若改变 provider/account/data/security/product semantics，仍进入 Human Gate / Planner；
6. blocker report 必须区分 credential missing/expired/revoked 与“credential 只对某个可选实现路线权限不足”。

这属于 W2/G1 已声明能力的 production regression closure，不是新 capability；G1 增加两个 regression case 即可，不新增 G9。

### task-local prohibitions expiry

Disposition：DEFER_AFTER_056_WORKFLOW_CORE。

这是 instruction lifetime / scope precedence 问题。它与 Human Gate 有交集，但 root cause 不是“依赖能否由 agent 解决”，而是历史 task-local restriction 被错误提升为 durable repository constraint。最新 semantic task identity 工作解决了 locator/label，不等于解决 instruction lifetime。它应作为后续小 workflow-core refinement，而不是继续扩大 056。

### acceptance-artifact packaging / comparison-review fidelity

Disposition：DEFER_AFTER_056_WORKFLOW_CORE。

v6 W1/W3/W4/W5 已覆盖 generic acceptance admission、evidence truth、repeat-failure circuit breaker、should-not-change；但“怎样生成可读、对齐、语义合法的 comparison artifact”横跨 workflow-core + research-writing + presentation/artifact rendering。056 不应把 domain semantic alignment 和 render layout 收进 workflow-core。本轮只保留现有 generic gates，完成 056 后再按真实残余缺口拆分 owner。

### 旧 TODO 的归宿

- workflow rules 与 Bridge runtime bug 分离：SUPERSEDED / ALREADY_SOLVED，当前 AGENTS、Maintainer、Bridge boundaries 已明确；
- real-task-driven Reviewed Handoff bounded batches：SUPERSEDED / ALREADY_SOLVED，当前 Maintainer 与 Review round contract 已有 bounded batch / no endless successor semantics；
- Review admission / Human Gate / delivery closure：ABSORB_IN_056_NOW，它就是原 v6 的主要 production scope。

## 5. Gate lifecycle 处理

本轮不新增 W6/W7/G9/G10。

least-privilege failure 映射到：

- W2：Human Gate eligibility / equivalent-route recovery；
- G1：normal-entry regression；
- W4：同类重复索权发生后触发 repeat-failure diagnosis；
- G8：如果文本规则已存在但 consumer 仍重复问，转 production-consumption diagnosis。

Persistent Run durability 有不同 normal entry、owner、evidence 和 failure semantics，因此留 Bridge 独立后续是正确 split；bounded kickoff 的普通 task authoring也不是当前 G1 release blocker。

## 6. v6 architecture disposition

ARCHITECTURE_DISPOSITION = V6_BOUNDED_AMENDMENT。

没有 v7，原因是：

- Lite L1-L6 不变；
- workflow-core 仍是 W1-W5；
- Frontend 仍是 F-A/F-B/F-C；
- Maintainer 仍是一项 production-consumption diagnosis；
- Bridge owner 边界不变；
- G1-G8 数量和职责不变；
- least privilege 是 W2/G1 coverage clarification + regression；
- source/version refresh 不构成 architecture redesign。

## 7. 版本 disposition

按当前 version policy，只有完成 production behavior change、回放与 regression 并准备形成 release 时才 bump。当前 planning commit 不改任何 version source。

预期 candidate：

~~~text
AI_Skills repository: 5.0.6 -> 5.0.7 PATCH
workflow-core:        0.2 -> 0.3
web-development:      0.1 -> 0.2
ai-skills-core:       0.3 -> 0.4

Bridge Kit:           0.8.4 -> 0.8.5
~~~

理由：

- workflow-core 会形成 W1-W5 + W2 least-privilege 的新 user-visible production behavior batch；
- web-development 原 F-A/F-B/F-C wiring 仍未完成；
- ai-skills-core 只做 v6 residual consumer-diagnosis closure，不重复 0.3 已完成的 Gate lifecycle / task identity；
- Repository 是兼容增强，默认 PATCH；
- Bridge 是现有 Host/Human-Gate behavior hardening，不是新的独立顶层 capability，因此留在 0.8.x patch line。

若 Executor 发现当前 main 已经完整覆盖某一拟改 plugin，则必须先证明 normal-entry behavior 已经满足对应 Gate，再将该 plugin 改为 NO_BUMP；不得为了沿用旧计划机械 bump。

## 8. 外部现实核查

本轮针对三个关键假设做了窄核查：

1. 当前 openai/codex Default collaboration guidance 明确：request_user_input 只用于 optional question，不能用于 permission request；真正必须显式用户输入才能继续时，应发一条 concise plain-text question。当前 handler 仍把 is_blocking 绑定到 Plan mode。这个事实继续支持 056 的 durable transcript wait/resume，而不支持把 Default native card 当无限等待。
2. AWS IAM 官方最佳实践仍是只授予完成任务所需的最小权限。它支持“不要为了某个可选实现路线先扩大 credential scope”的安全方向，但不替代本项目自己的 equivalence contract。
3. tmux 官方文档确认 client detach 后 session/program 继续运行，并提供 attach / attach-or-create 语义；它只支持“disconnect survival”这一层，不证明 overnight correctness、checkpoint semantics 或科学 Goal completion。这进一步支持把 Persistent Run durability 留给 Bridge 独立验证。

参考：
- https://github.com/openai/codex/blob/main/codex-rs/collaboration-mode-templates/templates/default.md
- https://github.com/openai/codex/blob/main/codex-rs/core/src/tools/handlers/request_user_input.rs
- https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html
- https://github.com/tmux/tmux/wiki/Getting-Started

## 9. 为什么不会过重，也不会过简

不会过重：只吸收一个直接击穿 056 核心 claim 的 least-privilege regression；不新增 Gate、不改 Persistent Run、不实现普通 kickoff renderer、不处理 acceptance artifact semantic/layout、不做 task-local expiry。

不会过简：如果 least-privilege recovery 继续 defer，056 即使 G1 证明 HUMAN_ONLY/AGENT_RESOLVABLE 分类存在，真实任务仍可能因为 Executor 自选高权限路线而错误向用户索权，直接违反“只有 genuine HUMAN_ONLY 才问用户”的正面目标。

## 10. 下一步

本轮改变了 Human Gate eligibility / recovery semantics，并刷新了 execution package 的 production/version baseline，因此旧 execution-ready review 不能直接沿用。

NEXT_HANDOFF = CRITIC。

Critic 只需审 v0.4 bounded amendment，不因后续 docs/evidence SHA 变化重开整套 v6。PASS 后，用户再发送被审过的 v0.4 Codex Kickoff；本 planning commit 本身不授权 execution。

README checked: no update required。本轮只改变 planning/review artifacts 与 TODO disposition，不改变已发布 plugin 名称、版本、能力描述、安装/调用方式、profile/Marketplace 暴露或用户入口。
