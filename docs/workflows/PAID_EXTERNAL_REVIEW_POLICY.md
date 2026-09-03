# Paid External Review Policy

本文件约束 AI_Skills_Collection 中所有会产生真实 API 费用的外部模型 review。它同时约束 GPT Planner、Codex Executor、Reviewer、GitHub Actions 和任何后续维护任务。

## 1. 默认架构

正常 plugin / skill 的生成、理解、规划、中间推理、自审和局部修复，默认由当前 host model（例如当前 Codex）完成，不额外调用付费模型。

本地 deterministic tooling 负责机械、可验证的检查，例如：

- schema / manifest / hash / source-span identity；
- 数字、公式、引用、路径、formal identifier 等 exact fidelity；
- render / file existence / generated parity；
- privacy boundary 与 no-plaintext-in-Git；
- paid-review budget preflight / reservation / receipt。

外部付费模型只在“独立性本身提供了 host model 无法自证的价值”时使用，默认只允许 final candidate / final render QA。

因此默认禁止把外部 API 用于：

- Document Map、argument segmentation、Meaning Card、planning；
- 正文 generation / rewrite；
- 每个 unit 的常规 semantic self-audit；
- ordinary targeted repair；
- assembly / coherence 的常规中间检查；
- 为了让多个 stage 看起来独立而把同一个任务拆成多次付费 model call；
- 用更便宜的外部模型维持一个本来就不该存在的 per-stage API pipeline。

如果 host model + deterministic checks 已足够完成该阶段，Planner 不得仅以“独立 reviewer 更稳”为理由增加付费调用。

## 2. GPT Planner 必须先证明付费 API 的必要性

任何 Plan 只要包含一个付费 external model call，就必须显式回答：

1. 为什么 host model 自己完成该阶段不够？
2. 为什么 deterministic check 不够？
3. 付费调用增加的独立证据是什么？
4. 为什么这个调用必须发生在现在，而不能只审 final candidate / final render？
5. 最多几次付费调用？
6. 单次 worst-case 成本、task campaign 总预算是多少？
7. 失败后怎样停止，为什么不会形成自动 review/repair/review 循环？

回答不了任一项：不允许把付费 API 写进 frozen Plan。

用户没有明确要求“每个 stage 都找独立模型”时，不得自行设计 per-stage paid review architecture。

## 3. 默认付费边界

AI_Skills Reviewed Handoff 的默认外部 reviewer 是 `gpt-5.6-terra`，仅用于独立 final QA。正常 plugin production behavior 不依赖 Terra，released plugin 默认 Terra OFF。

默认 task campaign：

```text
model: gpt-5.6-terra
max paid review calls: 2
campaign reserved-cost hard ceiling: USD 0.50
per-call worst-case ceiling: USD 0.25
automatic paid retries: 0
reasoning effort: low unless the frozen final-review rubric genuinely requires more
max output tokens: 4000 unless a lower cap is sufficient
paid tools: none
```

任何超出上述默认值的 Plan 都必须由用户明确批准成本边界；Planner/Executor 不能自行扩大。

同一 task 的 retry、GitHub rerun、重新启动 Codex、重新运行 workflow、换机器或换 branch checkout 都不得重置 campaign budget。

## 4. 运行前预算：只用 persistent worst-case reservation

运行时安全判断只使用 task-local persistent reservation，不使用“今天花了多少”、Dashboard 日 bucket、Organization Costs API 或其他异步账单统计作为放行条件。

每次 paid request 前必须：

1. 构造即将真实发送的完整 request；
2. 对该完整 request 做 input-token preflight；图片输入也必须包含在同一真实 request 的 token 统计里；
3. 使用当前允许模型的已验证价格和该请求的 `max_output_tokens`，按 uncached input 的最坏情况计算 `worst_case_cost_usd`；
4. 检查 `reserved_cost_usd + worst_case_cost_usd <= campaign_budget_usd`；
5. 检查 paid call count 仍在上限内；
6. 在发送请求前持久化 reservation；
7. 只有 reservation 成功后才允许发送请求。

reservation 一旦发生，不因为请求失败、实际输出较短、retry、workflow rerun 或进程重启而自动返还。这样预算是保险丝，不是事后报表。

当前 Terra 价格基线（2026-09-03，官方 model docs）：

```text
input: USD 2 / 1M tokens
cached input: USD 0.20 / 1M tokens
output: USD 12 / 1M tokens
```

preflight 必须按 uncached input 计算，不提前假设 cache discount。若模型 ID、价格或计费口径未知/已变更，fail closed，不发送付费 QA，直到价格配置重新核实。

官方 Responses API 提供 `POST /responses/input_tokens` 用于对完整 request 做 input-token count；review implementation 应优先使用这一真实 request preflight，而不是凭字符数猜测。若当前 SDK/transport 无法可靠计算包含图片的真实输入成本，visual paid review 必须停在 preflight，不得以猜测值继续。

## 5. Text Review

Text Review 默认只看需要独立判断的最终 candidate，加上 audience 与 frozen review questions / rubric。

除非 fidelity review 本身明确需要 source-aware comparison，否则 reader-style QA 不应上传：

- source 原文；
- intermediate drafts；
- Meaning Cards；
- internal self-audit；
- repo workflow log。

一个 task 如果已经由 host model 完成 generation 和 self-audit，不得再把每个中间阶段逐个发送给 Terra。

## 6. Visual Review

Terra 的 Image modality 在本项目中只用于 image input review，不用于 image generation。

Visual Review 允许发送 final render / selected final comparison images 给 Terra，然后只接收文本 review 结果。默认：

- 不启用 image generation；
- 不启用 web search / file search / computer use 等额外付费 tool；
- 图片必须进入同一个 request preflight；
- `images/min` 是平台吞吐上限，不是本仓库的预算控制；真正的成本保险丝仍是 request token preflight + task campaign reservation。

如果一套 deck / figure batch 无法在单次 `$0.25` worst-case ceiling 内完成合理 final review，应先减少到真正需要独立审查的 final evidence，或由 Planner/用户重新决定 review strategy；不得自动扩大预算。

## 7. Trigger 与 retry

付费 review workflow 必须是显式、bounded 的 manual invocation。普通 `push`、普通 CI、manifest commit、evidence writeback 不得自动调用付费模型。

普通 push 可以做：

- manifest/schema validation；
- hash / identity validation；
- deterministic preflight；
- budget configuration validation；
- `SKIPPED / NOT_REQUIRED` resolution。

但不能调用 Terra。

默认自动 paid retry = 0。特别是以下 billing/quota errors 必须立即停止，绝不 backoff：

- `credit_balance_exhausted`；
- `project_spend_limit_exceeded`；
- `organization_spend_limit_exceeded`；
- `organization_usage_limit_exceeded`；
- 其他明确的 billing / insufficient quota 错误。

真正 transient rate-limit error 即使未来允许 retry，也必须消耗同一 campaign 的 paid-call slot 与 reservation；不得通过 retry 产生新预算。

## 8. Project / secret contract

当前外部平台安全配置由用户在 OpenAI API Project 管理，不由 repo 自动修改。预期配置是：

```text
project: AI_Research_Review
allowed model: gpt-5.6-terra only
project override: 10 RPM
project override: 100,000 TPM
monthly project spend: USD 10 hard limit
```

这些平台限制是最后一道保险，不替代 task-local `$0.50` campaign fuse。

AI_Skills 的 text / visual review secret 名称继续分开：

```text
OPENAI_REVIEW_API_KEY
OPENAI_VISUAL_REVIEW_API_KEY
```

两者可以指向同一个 `AI_Research_Review` project-scoped key，但 workflow 不得在一个 secret 缺失时偷偷 fallback 到另一个 secret。Secret value 不得打印、commit、写入 artifact 或要求用户粘贴到聊天中。

## 9. Artifact review 语义

External Terra PASS 只是独立 review evidence，不拥有产品最终裁决权。用户明确拒绝真实 artifact 时，以用户 artifact feedback 为准。

同样，未调用 Terra 不等于 review 缺失：如果 frozen acceptance 不需要独立 external review，host review + deterministic checks + human artifact gate 可以是正确路径。

不要为了让每个 task 看起来“review 更充分”而默认增加付费 API。

## 10. 迁移原则

历史 workflow 可以保留历史 evidence，但 active production path 必须逐步满足：

- paid workflows manual-only；
- text/visual secret 不互相 fallback；
- Terra-only final QA；
- persistent task budget；
- no paid retry loop；
- text 和 visual review 都仍可真实运行；
- 普通 Codex/plugin generation 不产生额外 API 账单。

如果旧 workflow 与本政策冲突，先迁移 workflow，再启动依赖它的新高成本 task。不得一边知道成本保护尚未完成，一边继续 live paid replay。

## 11. CI 生命周期

Paid review policy 与 CI 生命周期是同一个安全边界的一部分：普通 push 不应启动昂贵、全库、会写回 repository 或可能产生账单的工作。

允许 ordinary push 自动运行的 workflow 必须同时满足：

- zero paid API；
- cheap；
- strongly path-scoped；
- failure 与当前 changed area 直接相关；
- read-only，不 commit/push repository；
- 不运行全库 heavyweight matrix。

Codex Marketplace full matrix、release smoke、Windows sparse checkout、Linux/Windows editable install smoke、以及任何 Terra/OpenAI paid review 都是 explicit gate，不是每个 commit 的默认仪式。`ci_required=true` 的 Reviewed Handoff 语义是 implementation candidate frozen 后显式 dispatch task branch 的 full CI，PASS 后再进入 Reviewer / integration。
