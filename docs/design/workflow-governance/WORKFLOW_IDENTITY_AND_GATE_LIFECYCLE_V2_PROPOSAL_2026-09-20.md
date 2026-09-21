# Workflow Identity & Capability Gate Lifecycle — Planner Proposal v2.1

- Date: 2026-09-20
- Status: DRAFT_FOR_CRITIC_REVIEW_R3
- Design topic: `workflow-identity-and-gate-lifecycle`
- Supersedes: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V1_PROPOSAL_2026-09-20.md`
- v1 Critic review: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V1_CRITIC_REVIEW_2026-09-20.md`
- v2 Critic review: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_CRITIC_REVIEW_2026-09-20.md`
- v2 reviewed proposal commit: `7a01c84c1c7f5a6419f62623cf8edc42199d33a4`
- v2 Critic review commit: `c8c349432b2f1343f87c73d6c39553abc874ae93`
- v1 review commit: `4ba429ebb510d6088f947468e624a1b043d19022`
- AI_Skills source inspected for v2.1: `main@c8c349432b2f1343f87c73d6c39553abc874ae93`
- Bridge source inspected: `YuukiAS/GPT_Codex_AI_Bridge_Kit main@afb2414b6fbe4b2b03292d3b1437d4dd22277fd0`
- Execution branch/worktree: NONE — design review only
- This document does not create a successor task, Reviewed Handoff task, branch, worktree, Goal, Kickoff, production change, paid review, or release authorization.

## 1. 结论

v2 的主架构不重做。上一轮 Critic 已明确关闭：

- `C-WIGL-01-SCOPE-PRECEDENCE`
- `C-WIGL-02-IMPACT-FALLBACK-BOUNDARY`
- `C-WIGL-03-IDENTITY-CUTOVER-COVERAGE`

本轮不重新打开这三项。

v2 Critic 新增的唯一 blocker 是 `C-WIGL-04-HUMAN-READABLE-WORKFLOW-LABEL`。重新核对用户要求与当前设计后，该 finding 合理，本版 `ACCEPT`，不提出 `REBUT`。

v2.1 只增加一个小澄清：**稳定的 technical task_key 与面向人的短名称是两个不同层次。** technical task_key 继续负责 branch/path/evidence 的稳定机器定位；Planner/Critic/Codex 在我们能够控制的 prompt、Goal、review/report heading 和普通交流中，默认使用简短、自然、低认知负担的人类名称，而不是反复展示 `cross-repo`、owner、状态名或长 contract。

其余 v2 已经被 Critic接受的架构全部保持：互斥 scope precedence、stable Gate taxonomy + growing regression bank、same-final-candidate、narrow vs broad/full fallback、G1–G7、legacy + semantic cutover、001–057 不迁移、同一 major objective 在 repair/review/integration 中保持同一个 task key、collision fail-closed、Bridge 只管 lexical syntax/compatibility/propagation、AI Skills Maintainer 管 AI_Skills scope semantics/regression maintenance/release closure、workflow-core 不成为第二个 parser、domain plugin 保留专业判断。

新文档目录布局 `docs/design/<task_key>/...` 等继续 `DEFERRED_NOT_IN_PRODUCTION_SCOPE`；本轮不改变文件组织。

## 2. 对 Critic blocker 的逐项处理

### C-WIGL-01-SCOPE-PRECEDENCE — ACCEPT

Critic 指出 v1 的 `cross-plugin` 与 `cross-repo` 会在 056 这种任务上重叠。重新读取当前 056 v0.3 Plan/Goal 后，这个 finding 成立：

- AI_Skills_Collection 是必要 mutable repo；
- GPT_Codex_AI_Bridge_Kit 也是必要 mutable repo；
- workflow-core / web-development / ai-skills-core 是 AI_Skills 内的 production owners；
- Bobbio、Lucerna、Mica、Asteria、SeminarArc、CUHK Date 等是 read-only reference，不属于 mutable scope。

因此 v2 不再用“primary objective”主观决定 scope，而使用 §5.2 的互斥 precedence。当前 056 的新式示例修正为：

```text
cross-repo--product-delivery-discipline
```

056 真实历史 identity `056_product_delivery_discipline` 不改名、不迁移。

### C-WIGL-02-IMPACT-FALLBACK-BOUNDARY — ACCEPT

Critic 指出 v1 的“如果 Planner 能解释 unaffected 就允许 canary”仍过于主观。这个 finding 成立。

v2 保留 risk-based selection，但把 release 运行分成明确的 `NARROW_RELEASE_SELECTION` 与 `BROAD_FULL_FALLBACK` 两种语义，并给出触发条件。任何 impact 无法可靠解释、shared/cross-cutting source 变化、新 failure 未归因、grader/eval semantics 变化、maturity promotion 等情况，不能走 narrow。

不新增 impact registry、dependency graph、数据库或 ledger。

### C-WIGL-03-IDENTITY-CUTOVER-COVERAGE — ACCEPT

Critic 指出 v1 G2 对 task-key propagation 写得过泛，可能出现主 creation 已支持 semantic key，但 text/visual review、generic validator 或某个 artifact consumer 仍只认 numeric key。

重新读取 Bridge 当前 source 后，这个 finding 成立。当前 numeric constraint 至少直接存在于：

- `ai_bridge_kit/reviewed_handoff.py`
- `ai_bridge_kit/cli.py`
- `scripts/validate_handoff_workspace.py`

因此 v2 直接强化 G1/G2/G4，不新建 gate。

### C-WIGL-04-HUMAN-READABLE-WORKFLOW-LABEL — ACCEPT

Critic 指出：v2 已经把 machine identity 从 0xx 改成更有语义的 task key，但如果 Planner/Critic/Codex 又把 `cross-repo--product-delivery-discipline` 当成普通 thread 名、报告标题和交流称呼反复展示，用户仍需要持续解析内部 scope token，等于把旧的数字负担换成另一种机器负担。

这个 finding 成立。v2.1 采用最小分层：

- **technical task_key**：稳定机器 locator；
- **human-readable short label**：普通用户交流和我们能控制的标题/heading 中的默认名称。

不新增 `display_name` 字段、schema、registry、title service 或状态。Bridge 完全不需要知道 human label。

详细规则见 §5.8。

## 3. 已验证的当前事实

### 3.1 Gate policy

当前 `PLUGIN_CAPABILITY_GATE_POLICY.md` 已明确：

- Gate 数量由独立用户能力决定，不以“越多越稳”为目标；
- 重复 Gate 应合并；
- release-critical Gate 必须绑定同一 final candidate；
- fresh/holdout 在曝光并用于修改后不再是 fresh；
- Critic 既要阻止 Gate 过简，也要阻止 Gate 过重。

v2 增加的是“成熟后如何维护 Gate / regression / release selection”的 lifecycle 规则，不建立第二套 eval framework。

### 3.2 056 当前真实 mutable boundary

当前 056 v0.3 Plan/Goal 明确：

```text
Mutable:
- YuukiAS/AI_Skills_Collection
  - workflow-core
  - web-development
  - ai-skills-core
- YuukiAS/GPT_Codex_AI_Bridge_Kit

Read-only product references:
- Bobbio
- Lucerna
- Mica-for-ChatGPT
- Asteria
- SeminarArc
- CUHK Date
- others listed by the frozen Plan
```

所以按 v2 precedence，056 是 `cross-repo`，不是 `cross-plugin`。

### 3.3 Bridge 当前 task-key enforcement

Bridge 当前 `reviewed_handoff.py` 使用：

```python
TASK_KEY_RE = re.compile(r"^\d+_[A-Za-z0-9]+(?:_[A-Za-z0-9]+){0,2}$")
```

并在 canonical `init_task()` 中拒绝非 numeric key。

`ai_bridge_kit/cli.py` 与 `scripts/validate_handoff_workspace.py` 也有同类 numeric validation。Reviewed Handoff 又把同一 `task_key` 传播到 task/result directory、CURRENT/PLAN/RESULT/REVIEW/FINAL_REPORT、branch、text review 与 visual review evidence identity。

因此 semantic key 必须由 Bridge canonical lexical/compatibility path 支持；AI_Skills 不能局部 fork 一套 parser 冒充完成。

## 4. Capability Gate lifecycle

### 4.1 三个概念只作为 policy semantics

继续区分：

**Capability Gate taxonomy**

相对稳定的用户能力声明与独立 failure semantics。Gate 的职责是回答“产品必须证明哪一类不同的用户能力”。

**Regression bank**

Gate 下持续积累的已知真实 failure、should-change / should-not-change pair、代表性 artifact、deterministic checks 与合法 edge case。它随着真实使用增长。

**Release selection**

某个 final candidate 本轮实际需要跑到什么深度。它只决定验证深度，不改变 Gate obligation，也不能把旧 candidate PASS 拼接成新 candidate PASS。

这三个名称不创建新文件类型、schema、registry、database、state 或 ledger。

### 4.2 新 failure 默认进入 regression bank

新真实 failure 到来时，Planner/Maintainer 先回答：

> 它破坏的是哪个现有用户能力 claim？

若现有 Gate 已能准确表达相同 capability、相同 evidence semantics 与相同 PASS/FAIL 含义，则新增为该 Gate 的 regression case，而不是新增顶层 Gate。

只有同时满足以下条件才新增 Gate：

1. 是真实 user-visible capability / failure class；
2. 放入现有 Gate 会改变或模糊该 Gate 的 capability claim；
3. 需要 materially different evidence 或 materially different failure verdict；
4. 产品正常入口实际声称或必须声称该能力。

因此“又发现一个公式损坏例子”通常只是 technical-fidelity Gate 的新 regression；“产品首次新增 editable PPTX 输出能力”则可能需要独立 editability/export Gate。

### 4.3 Gate 不允许无限扩成 miscellaneous bucket

stable taxonomy 不等于禁止 split。

如果新 case 被塞进某个 Gate 后出现任一情况：

- Gate claim 必须扩大才能容纳它；
- 需要不同的正常入口或 artifact；
- evidence type 明显不同；
- PASS/FAIL 语义不同；
- 一个 Gate 内的两个风险可独立失败且相互不能替代；

Planner 必须评估 split/new gate，而不是为了保持 Gate 数不变把一切都塞进旧 Gate。

### 4.4 merge / split / retirement

Gate 可重构，但不能为了 release 更容易而删除 obligation。

任何 merge/split/retirement 必须经过 versioned Planner/Critic design review，并明确：

- 旧 capability claim；
- 新 destination Gate；
- 重要 regression cases/obligations 的去向；
- 是否真的退休某项 product claim；
- 为什么这不是降低验收标准。

历史 PASS/FAIL 原样保留，不回写历史。

如果 product claim 仍存在，就必须有新 Gate/剩余 Gate 承接它；如果 claim 被正式退休，proposal/changelog 必须明确记录产品边界变化。

## 5. Semantic workflow identity

### 5.1 Bridge lexical grammar 与 AI_Skills semantic scope 分开

Bridge 只拥有 **lexical syntax、legacy compatibility、identity propagation**。

Bridge 的 semantic task-key lexical form建议为：

```text
<scope-token>--<goal-token>
```

其中两个 token 都是 lowercase kebab-case；Bridge 不读取 AI_Skills registry，不判断某个 plugin slug 是否 canonical，也不决定 `cross-plugin` 与 `cross-repo` 业务含义。

实现时应由一个 canonical Bridge validator/helper（或等价 single authority）被 Reviewed Handoff creation、generic workspace validation 及其他 task-key consumers 复用，避免继续复制多份 regex。

AI_Skills policy / AI Skills Maintainer 在 Bridge lexical-valid 的前提下，进一步要求 AI_Skills 新 workflow 的 scope token 必须符合 §5.2。

### 5.2 AI_Skills scope 的互斥 precedence

先计算当前 frozen objective **实际需要写入的 mutable canonical repositories**。Read-only reference/evidence repos 不计入。

按以下顺序决定 scope，命中后停止：

1. **多于一个 mutable canonical repo**
   -> `cross-repo`

2. **恰好一个 mutable repo，且它是 AI_Skills_Collection，并且 production scope 修改多个中央 plugin**
   -> `cross-plugin`

3. **恰好一个 mutable repo，且 production scope 只修改一个中央 plugin**
   -> `plugin-<canonical-plugin-slug>`

4. **恰好一个 mutable repo，目标为 repo-wide / maintenance / infrastructure / docs-control 类工作，而不是一个或多个中央 plugin 的 production capability refinement**
   -> `repo`

补充边界：

- 只因为使用 `workflow-core` / `ai-skills-core` 作为 companion，不自动把一个单插件任务升级成 `cross-plugin`；只有多个中央 plugin 的 production behavior 本身都在修改范围内才算多个 plugin。
- generated parity、repository release metadata、plugin changelog 等单插件 release 所需的 repo-local support changes 不把 `plugin-<slug>` 升级成 `repo`。
- read-only Bobbio/CUHK Date 等 evidence source 不把任务升级成 `cross-repo`。
- 如果同一个 frozen objective 必须写 AI_Skills 与 Bridge，则无论 AI_Skills 内涉及几个 plugin，都优先是 `cross-repo`。

### 5.3 示例

单插件：

```text
plugin-writing-style--release-convergence
plugin-presentations--visual-quality-hardening
```

单 AI_Skills repo、多 production plugin：

```text
cross-plugin--shared-routing-hardening
```

repo-wide、非 plugin production scope：

```text
repo--workflow-identity-rework
```

多 mutable repo：

```text
cross-repo--product-delivery-discipline
cross-repo--repo-agents-hygiene
```

当前 056 如果今天新建，将使用：

```text
cross-repo--product-delivery-discipline
```

其 frozen Plan 仍必须明确记录：

```text
AI_Skills plugin ownership:
- workflow-core
- web-development
- ai-skills-core

supporting mutable repo:
- GPT_Codex_AI_Bridge_Kit

read-only references:
- Bobbio
- Lucerna
- Mica
- Asteria
- SeminarArc
- CUHK Date
...
```

task key 不负责把所有 owner 塞进名字。

### 5.4 task key 不编码的内容

继续不编码：

- creation sequence；
- date；
- current state；
- priority；
- review round；
- candidate version；
- every plugin；
- every repo；
- recovery/integration stage。

这些信息已有 Plan/CURRENT/history owner。

### 5.5 legacy + semantic cutover

Bridge 需要区分：

```text
LEGACY_TASK_KEY
= existing numeric form

SEMANTIC_TASK_KEY
= new lexical <scope-token>--<goal-token>
```

Cutover 后：

- canonical **new task creation** 只接受 semantic key；
- generic workspace validation 与 existing-workspace validation 同时接受 legacy + semantic；
- 001–057 以及其他现存 numeric task/branch/result/evidence 完全不 rename、不 migrate；
- repair / review / CI recovery / evidence correction / integration 继续复用原 task key；
- historical PASS/FAIL 不重写。

重要限制：在不新增 registry/creation ledger 的前提下，generic validator 不应该试图根据文件时间猜“这个 numeric task 是旧的还是刚手写出来的”。因此：

- canonical creation API/CLI 必须拒绝新的 numeric key；
- validator 为历史兼容继续接受结构合法的 legacy numeric key；
- out-of-band 手工伪造 numeric task 不属于受支持的新 task creation path；
- 不为区分“旧 numeric / 新 numeric”新增 timestamp registry 或 migration database。

### 5.6 collision

Semantic key collision 默认 fail-closed。

如果已有 task/result/branch identity 表明同 key 已属于另一个 objective：

- 不自动加 UUID；
- 不自动加 date；
- 不自动加 sequence；
- 不创建 successor 逃避冲突。

Planner 先判断：

- 若其实是旧 objective 的 repair/review/integration -> 继续同 key；
- 若确实是不同 closed objective -> 用有实际语义的 goal disambiguation，例如更具体 capability/component/release target。

只有真实长期使用证明语义 disambiguation 仍频繁冲突，才另提 uniqueness 机制。

### 5.7 文档目录组织

v1 的：

```text
docs/design/<task_key>/...
docs/goals/<task_key>/...
docs/operations/prompts/<task_key>/...
```

本轮 **DEFERRED / OUT OF IMPLEMENTATION SCOPE**。

理由：

- 它不是用户本轮核心问题；
- semantic key cutover 已经涉及 branch/path identity；
- 同时引入第二种文档布局会制造额外链接和 prompt churn；
- 当前没有真实证据证明 semantic key 生效后仍需要目录迁移。

首轮 semantic-key implementation 保持现有 docs locations；旧文件完全不迁移。

### 5.8 Technical task_key 与面向人的短名称

#### 5.8.1 两层身份

**technical task_key** 只承担稳定机器定位，不承担“给用户起一个最好读的名字”。

它用于：

```text
reviewed/<task_key>
automation/reviewed_handoff/tasks/<task_key>/
results/<task_key>/
CURRENT / PLAN / RESULT / REVIEW / FINAL_REPORT 中必要的 technical locator
text-review / visual-review manifest 与 evidence identity
其他必须精确绑定 task identity 的技术位置
```

例如：

```text
cross-repo--product-delivery-discipline
```

这个字符串适合 branch/path/evidence 定位，但**不是普通 thread title，也不应在用户可见正文里反复充当工作名称**。

**面向人的短名称**只是可控文字表面的命名约定，不是新的机器身份。

它用于我们能够控制的：

- Planner / Critic prompt 标题与开头；
- Canonical Goal 的人类可读标题；
- review / report heading；
- Codex kickoff/repair/resume prompt 中给用户看的工作名；
- 普通聊天、交接说明和状态解释。

不新增：

- `display_name` schema field；
- task registry；
- title registry/service；
- database/ledger；
- 第二个 identity mapping 系统。

技术 locator 需要时可以在正文首次或附录中给一次；之后默认使用人类短名称。

#### 5.8.2 人类短名称的选择原则

优先顺序是：**用户一眼能知道“在改什么/交付什么” > 内部 scope 精确度 > 历史编号。**

单插件正式 release 且 target version 已冻结时，优先直接使用 display name + version：

```text
Clear Writing 0.4
Presentations 0.3
```

版本尚未冻结，或当前阶段不是正式 release target 时，用简单目标：

```text
Clear Writing 发布收口
Presentations 视觉质量完善
```

跨 plugin / cross-repo 工作使用简单结果导向名称，必要时加一个短 scope hint：

```text
开发交付流程完善（AI_Skills + Bridge）
仓库 AGENTS 整理
```

不要把：

```text
cross-repo--product-delivery-discipline
cross-plugin--shared-routing-hardening
```

当作普通用户 thread 名或整篇报告里反复出现的主称呼。

#### 5.8.3 历史 0xx 的过渡称呼

001–057 仍完全不 rename/migrate。

过渡期为了让用户把新称呼与旧上下文对上，可以写：

```text
开发交付流程完善（原 056）
仓库 AGENTS 整理（原 057）
```

“原 056”只是临时定位提示，不是长期 primary label。普通交流稳定后应优先使用短名称。

#### 5.8.4 version 与 technical task_key

版本号**不是**所有 technical task_key 的强制组成部分。

默认仍可以使用：

```text
plugin-writing-style--release-convergence
```

只有当：

1. release target 已经冻结；并且
2. version 是区分两个真实、独立 workflow 最自然的语义；并且
3. 不会把候选版本/未冻结版本误写成稳定 identity；

才允许把版本用于 goal token 的 semantic disambiguation，例如：

```text
plugin-writing-style--release-0-4
```

这不是 collision 自动后缀机制。仍禁止为了唯一性自动追加 UUID、date、sequence 或流水号。

若 collision 实际代表同一个 objective 的 repair/review/integration，继续复用原 task key；若确属不同 objective，优先用真实 capability/component/release target 做语义化区分。

#### 5.8.5 可控表面边界

本规则只约束 repository/workflow **实际能够控制的文字表面**：

- prompts；
- Goal；
- review/report headings；
- Codex/Planner/Critic 交接文字；
- 普通用户交流。

它**不声称** repository、AGENTS 或 workflow 可以控制 ChatGPT/Codex 客户端自动生成的 conversation title、sidebar title 或其他平台 UI 自动命名。

如果客户端自动标题与建议短名称不同，不算本 workflow implementation failure；但我们自己生成的 prompt/report 不应主动把 raw task_key 变成人类主标题。


## 6. Release regression selection：明确 narrow 与 broad/full fallback

### 6.1 不变的硬约束

无论 narrow 还是 broad/full：

- 所有 release-critical Gate 都必须有**同一 final candidate 的直接 evidence**；
- 旧 candidate PASS 不得替代当前 candidate；
- fresh 被查看并用于修改后转成 regression，不再叫 fresh；
- Gate obligation 不因本轮 selection depth 变浅而消失；
- paid/manual review 不按 Gate 数机械倍增；
- 不固定 fresh/manual/paid 样本数。

### 6.2 所有 release 都先跑 applicable cheap deterministic bank

在进入 narrow/broad 判断前，final candidate 必须通过**全部 applicable cheap deterministic known regressions**。

`applicable` 的含义是：该 regression 对当前 product route/runtime/平台仍有定义且可以在当前候选上合法运行。若省略，必须能解释：

- product capability 已正式退休；或
- regression fixture 已失效且有等价/更强 replacement；或
- 当前平台/route 明确不适用。

“测试很多”“预计不受影响”“跑起来麻烦”不是省略理由。

这仍然是 policy/Plan 说明，不新增 regression registry/database。

### 6.3 NARROW_RELEASE_SELECTION 的合法条件

只有同时满足以下条件才可 narrow：

1. 变更可以从 source/consumer/normal-entry 路径解释为局部；
2. 不修改 §6.4 的 cross-cutting/shared surfaces；
3. affected Gate 可以清楚列出，且不存在 unresolved multi-gate impact；
4. applicable cheap deterministic known-regression bank 全部 PASS；
5. affected/high-risk Gate 做足代表性 artifact/qualitative evidence；
6. 所有其他 release-critical Gate 仍有同一 final candidate 的 direct canary/evidence；
7. 没有 grader/eval semantics 变化使旧标准失去可比性；
8. 不是 maturity promotion。

这里的 canary 不能只是“文件存在 / schema PASS”；必须是该 Gate 正常入口下能直接观察 capability 仍成立的证据。

### 6.4 BROAD_FULL_FALLBACK 的强制触发条件

出现任一项，禁止 narrow，必须回退 broad/full release matrix：

1. **shared generation / prompt assembly**
   - 修改多个 Gate 共用的生成 prompt、assembly、postprocessor、shared rendering/generation logic；
2. **model / runtime / provider / router**
   - 更换或实质修改模型、agent/runtime、provider、路由/dispatch/selection 机制；
3. **normal entry / install / invocation**
   - 修改安装、Marketplace/profile exposure、plugin identity、invocation、trigger、session loading、normal-entry routing；
4. **shared layer consumed by multiple release-critical Gates**
   - 修改一个明确被多个 Gate 消费的 shared parser、shared renderer、shared validator/transformer、shared orchestration/assembly layer；
5. **impact 无法可靠追踪**
   - source/consumer dependency 不清、存在 dynamic routing/implicit consumer、无法说明哪些 Gate 真正隔离；
6. **新 failure 尚未明确归因**
   - root cause 未定，或同一 failure 可能跨多个 Gate / shared layer；
7. **grader / eval semantics 实质变化**
   - rubric、grader、evaluation harness、artifact interpretation 或 PASS/FAIL 定义发生变化，使旧 evidence 与新标准不可直接比较；
8. **maturity promotion**
   - 准备将 plugin 提升长期 maturity/status，例如从 baseline 到 alpha、alpha 到 stable；
9. **Critic/Planner 已有具体证据表明本轮影响跨 Gate**
   - 不能因为 diff 小就仍按 narrow 处理。

### 6.5 broad/full 的含义

`BROAD_FULL_FALLBACK` 不等于“每一个历史 qualitative/paid case 都重新人工审一次”。

它至少要求：

- 全部 applicable cheap deterministic known-regression bank；
- 每一个 release-critical Gate 都有 representative normal-entry evidence；
- qualitative/artifact Gate 有风险相称的完整 artifact/qualitative coverage；
- 当前变更涉及的 shared/cross-cutting route 有直接 integration/normal-entry evidence；
- generalization-sensitive capability 在当前 frozen Plan 判断需要 fresh 时使用 fresh；
- maturity promotion 必须有 broad release-critical coverage，并服从 `PLUGIN_MATURITY.md` 的真实任务/用户验收要求。

不固定每个 Gate 的 fresh/manual/paid 数量。是否需要 paid review仍由 frozen acceptance/risk 与 paid policy决定。

### 6.6 grader/eval semantics 变化的特殊处理

如果 grader/rubric/eval harness 发生实质变化：

- 旧 product artifact / regression 仍可作为历史 evidence；
- 但不能直接把旧 PASS 当作新 grader 下的 current proof；
- 先用开发期已知 good/bad / should-change / should-not-change 例子校准新 semantics；
- 再对 final candidate 做当前标准下的 release evidence；
- 不为了保持 fresh 身份改写旧评审结论。

## 7. Ownership

### 7.1 Canonical policy authority

`docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md` 继续是 Gate lifecycle 的 canonical policy authority。

AI Skills Maintainer **消费和执行**该 policy，而不是拥有一个平行 Gate 体系。

### 7.2 AI Skills Maintainer

负责：

- AI_Skills scope semantics；
- regression case intake / dedup / mapping；
- source/generated parity；
- plugin/version/changelog/release closure；
- 判断新 failure 应进入 existing Gate regression 还是需要 Planner 重新审 Gate taxonomy；
- 应用 narrow/broad release decision 的 maintenance closure；
- 在 AI_Skills 可控文字表面执行 human-readable short-label 命名约定，但不创建新的 display-name 数据模型。

不负责专业领域正确性。

### 7.3 Target domain plugin

负责：

- Gate 的专业 capability claim；
- regression case 在写作、PPT、统计、影像、生信等领域是否专业正确；
- 用户 artifact/domain quality 的专业判断。

### 7.4 workflow-core

负责：

- AI_Skills frozen Plan 如何写 affected Gate / release selection；
- same-final-candidate execution semantics；
- narrow 条件与 broad/full fallback 的执行语义；
- failure attribution 后怎样决定继续 narrow 或升级 broad。

不实现第二个 task-key parser，不拥有 plugin domain semantics。

### 7.5 Bridge Kit Reviewed Handoff

只负责：

- task-key lexical syntax；
- semantic-vs-legacy compatibility；
- canonical task creation；
- generic validation consumption；
- task key 在 task/result/branch/review evidence 的无损 propagation。

Bridge 不：

- 读取 AI_Skills registry 来验证 plugin slug；
- 判断任务应该叫 cross-plugin 还是 cross-repo；
- 管 AI_Skills Gate lifecycle；
- 新增 Reviewed Handoff state/controller/watcher；
- 存储、解析或生成 human-readable workflow label。

## 8. Capability Gate Matrix v2

不新增 G8。G1/G2/G4 已按 Critic 要求强化。

| Gate | Capability / claim | Normal entry / direct evidence | Failure | Final-candidate / regression boundary |
| --- | --- | --- | --- | --- |
| **G1 Semantic creation & lexical identity** | 新 Reviewed Handoff task 能通过 canonical Bridge creation 使用 semantic key，且 cutover 后 canonical creation 拒绝 numeric new key | canonical task creation + canonical lexical validator；semantic valid/invalid/collision cases | 仍要求 numeric；semantic 只能手工造文件；collision 静默覆盖；canonical create 仍接受新 numeric | exact Bridge final candidate；不改变 task state graph |
| **G2 Identity propagation** | 同一 semantic task key 无损传播到所有现有 normal-entry identity surfaces | 同一 semantic task 覆盖：`automation/reviewed_handoff/tasks/<task_key>/`、`results/<task_key>/`、`reviewed/<task_key>`、CURRENT/PLAN/RESULT/REVIEW/FINAL_REPORT、text-review manifest/evidence、visual-review manifest/evidence，以及当前 task-bound Planner/Reviewer/Executor path consumers | 任一 surface reject/truncate/remap/mismatch；helper PASS 但 review evidence 路径失败 | exact Bridge final candidate；不新增 parallel identity/parser |
| **G3 Scope clarity** | AI_Skills semantic scope 按 mutable canonical repo count -> plugin scope 的互斥 precedence 决定 | representative cases：single plugin；one-repo multi-plugin；repo-wide non-plugin；multi-mutable-repo；multiple read-only refs not counted；056 -> `cross-repo` | 同一 topology 可因措辞被叫 cross-plugin/cross-repo；read-only ref 错误升级 scope | AI_Skills policy/Maintainer final candidate；Bridge 不判断 semantic ownership |
| **G4 Legacy coexistence & cutover** | 001–057 等 legacy task 不迁移且继续合法；semantic task 可同时存在；cutover 后只禁止新的 numeric canonical creation | 同一 workspace/fixture 中至少一个 legacy numbered task + 一个 semantic task；generic workspace validation 双格式；canonical creation semantic-only；历史 branch/result/review identity 仍可读 | validator 迫使历史迁移；legacy 与 semantic 冲突；新 numeric canonical creation 成功；历史 evidence 失效 | existing numeric history should-not-change；无 migration |
| **G5 Gate lifecycle** | 新真实 failure 默认进入正确 existing Gate 的 regression bank；真正新 capability 才新增 Gate；merge/split/retirement 不丢 obligation | 用 056 post-probe “不新增 G9/G10”作为 existing-gate case，再用真正新增 capability 的 contrasting case；检查 obligation mapping | 每个 failure 都长 Gate；或为省 release 删除 Gate/历史 obligation；Gate 变 miscellaneous bucket | AI_Skills policy final candidate |
| **G6 Release regression safety** | mature plugin 可风险分层验证，但 narrow 只有在 isolation 可解释时合法；cross-cutting/uncertain/maturity promotion 强制 broad/full fallback | 至少验证：合法 isolated narrow；shared prompt/runtime/router 等 fallback；unresolved failure fallback；grader semantics change；maturity promotion；same-final-candidate direct evidence | affected 判断靠主观感觉；shared change 仍只跑 weak canary；old-candidate evidence 拼接；cheap bank 未过仍 narrow | workflow-core + Maintainer final candidate；不固定 fresh/manual/paid 样本数 |
| **G7 No governance bloat** | 本重构不创造第二套 workflow/control/eval infrastructure | source diff + small-task normal workflow replay | 新 registry/ledger/database/controller/watcher/state machine/display_name schema/title service；workflow-core 第二 parser；AI Skills parser fork；小 patch 被迫跑无关 expensive matrix | Bridge + AI_Skills should-not-change |

### 8.1 G1/G2/G4 的 mandatory acceptance surface

未来 implementation Plan 不能把以下任一项省略成“covered generically”：

```text
canonical Reviewed Handoff task creation
generic workspace validation
automation/reviewed_handoff/tasks/<task_key>/
results/<task_key>/
reviewed/<task_key>
CURRENT
PLAN
RESULT
REVIEW
FINAL_REPORT
text-review manifest
text-review evidence
visual-review manifest
visual-review evidence
legacy numbered + semantic coexistence
new numeric canonical creation rejection
```

测试可以复用 fixture，但最终结论必须证明这些真实 consumer，而不是只证明一个 regex helper。

## 9. Cutover 与历史边界

保持：

- 001–057 不 rename；
- 055/056/057 的 active/history task key 不变；
- 不搬 task/result directories；
- 不改 branch identity；
- 不改 text/visual evidence identity；
- 不重写历史 PASS/FAIL；
- 不为了 semantic key 创建 successor；
- repair/review/integration 沿用同 key；
- numeric order 不表示 priority/dependency/completion order；
- semantic key cutover 只影响未来 canonical new-task creation。
- human-readable short label 不改变任何历史 task_key；过渡期可用“<短名称>（原 056）”这类自然定位。

## 10. 文件组织决定

`docs/design/<task_key>/...` 等 task-local grouping：

```text
DISPOSITION = DEFERRED_NOT_IN_PRODUCTION_SCOPE
```

本轮不改 docs layout，不迁历史文件，也不把新的文档目录约定加入未来 execution Goal/Kickoff。v2.1 的 human-readable short label 只是现有可控文字表面的命名约定，不要求新的文件层级。

若 semantic keys 真正投入使用后仍有明确的文档发现困难，再基于真实失败单独评估，不预先加复杂度。

## 11. 外部研究复核

本轮没有重新设计外部方法，只针对 blocker 重新核对两条关键实践。

### Anthropic — capability vs regression

Anthropic 2026 的 agent-eval guidance 明确区分 capability/quality eval 与 regression eval，并指出接近饱和的 capability eval 可以“graduate”成持续 regression suite；真实用户/生产 failure 应持续转为 eval cases。

采用：支持“Gate taxonomy 稳定、regression bank 增长”。

不采用：不照搬其 eval harness/团队组织，也不规定固定 trial 数。

Source:
https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

### Microsoft — Test Impact Analysis safe fallback

Microsoft TIA 明确采用 impacted test selection；当 change/scenario 无法可靠理解时，安全回退到运行全量测试，并允许周期性 full run。

采用：只借鉴“impact 可解释才 narrow；impact 不可解释就 full fallback”的安全原则。

不采用：AI plugin 的 prompt/runtime/model 影响不能等同于 managed-code dependency graph，因此本方案不建依赖数据库，也不把 Microsoft 的自动 impact algorithm 移植进来。

Source:
https://learn.microsoft.com/en-us/azure/devops/pipelines/test/test-impact-analysis

这两项复核强化了 C-WIGL-02 的修订，但没有改变 v1 的总体架构。

## 12. Alternatives / red-team 仍保持

继续拒绝：

- 保留 0xx 只靠 title 解释；
- 日期/timestamp 替代 semantic identity；
- UUID/sequence 作为默认 suffix；
- GitHub Issue 作为 canonical task source；
- ACTIVE_WORK registry/dashboard；
- AI_Skills 自己 fork Bridge parser；
- 把所有 mutable/read-only repo/plugin 都塞进 task key；
- 每个 failure 新增 Gate；
- 每次 release 把所有历史 paid/manual case 全部重跑。

关键 red-team 防线：

- scope 由 precedence 决定，不由“primary objective”措辞决定；
- technical task_key 不等于 human-facing title；普通用户不需要反复解析 scope token；
- collision fail-closed；
- impact 不清 -> broad/full；
- same-final-candidate 永远保留；
- Gate restructure 必须保留 obligation mapping；
- semantic cutover 不迁历史；
- Bridge lexical / AI_Skills semantics 分权；
- 不新增控制体系。

## 13. 未来执行顺序（仅供 Critic 审设计，不是授权）

只有 v2.1 获得明确 Critic PASS 后，Planner 才进入 execution-package planning。

未来 execution package 才可分别设计：

### Phase A — Bridge lexical/cutover support

- one canonical lexical validator/helper；
- legacy-validation + semantic-validation；
- canonical new creation semantic-only；
- propagation tests across G1/G2/G4 surfaces；
- no history migration；
- no state-machine change。

### Phase B — AI_Skills policy/consumer alignment

- amend `PLUGIN_CAPABILITY_GATE_POLICY.md` lifecycle/fallback rules；
- minimum necessary AI Skills Maintainer / workflow-core consumer alignment；
- AI_Skills scope precedence；
- Gate lifecycle/release-selection examples/tests；
- no second parser；
- controlled human-readable naming convention for prompts/Goal/review/report headings, with no display_name schema/registry；
- no docs-layout migration。

### Phase C — normal-entry verification

- isolated semantic creation；
- legacy + semantic coexistence；
- propagation through task/result/branch/all review evidence surfaces；
- narrow-selection example + mandatory broad/full fallback examples；
- no paid review unless a later frozen execution package separately justifies and receives authorization.

本 v2.1 不准备 executable Goal/Kickoff，也不授权上述实施。

## 14. Critic v2.1 复核重点

上一轮三个 blocker 已正式关闭，本轮不得重新打开：

```text
C-WIGL-01-SCOPE-PRECEDENCE = CLOSED
C-WIGL-02-IMPACT-FALLBACK-BOUNDARY = CLOSED
C-WIGL-03-IDENTITY-CUTOVER-COVERAGE = CLOSED
```

Critic 只需要复核：

### C-WIGL-04-HUMAN-READABLE-WORKFLOW-LABEL

检查 §5.8 是否完成最小闭环：

1. technical task_key 只用于稳定机器 locator；
2. human-readable short label 是普通 thread/prompt/Goal/review/report heading 与交流的默认名称；
3. 没有新增 `display_name` schema、registry、title service 或第二 identity mapping system；
4. 单插件 frozen release 可以优先显示 `Clear Writing 0.4` / `Presentations 0.3`；
5. version 未冻结时使用简单目标，如 `Clear Writing 发布收口`；
6. 当前 056 的技术 key 示例仍为 `cross-repo--product-delivery-discipline`，而普通人类名称使用 `开发交付流程完善（AI_Skills + Bridge）`；
7. 历史 056 不 rename，过渡交流可写 `开发交付流程完善（原 056）`；
8. version 不是所有 task_key 的强制组成部分，只可在 frozen release target 确实是最自然语义 disambiguator 时进入 goal token；
9. collision 仍不自动追加 UUID/date/sequence；
10. 规则只覆盖 workflow 能控制的文字表面，不承诺控制 ChatGPT/Codex 客户端自动 conversation title。

同时检查这个小修改是否意外破坏已接受的 semantic key、legacy compatibility、scope precedence、Gate lifecycle、release fallback 或 ownership 边界。

若 C-WIGL-04 关闭且没有由 v2.1 新增的具体回归，应对 v2.1 design 收敛为 PASS，并允许 Planner 下一轮进入 execution-package planning。PASS 仍不授权 Codex、branch/worktree、production 修改、paid API、merge/release，也不代表客户端 UI title 已可控。

