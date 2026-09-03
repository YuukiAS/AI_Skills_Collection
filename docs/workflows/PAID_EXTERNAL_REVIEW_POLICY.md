# Paid External Review Policy

本文件约束 AI_Skills_Collection 中所有会产生真实 API 费用的外部模型 review。它同时约束 GPT Planner、Codex Executor、Reviewer、GitHub Actions 和后续维护任务。

## 1. 默认架构

正常 plugin / skill 的生成、理解、规划、中间推理、自审和局部修复，默认由当前 host model（例如当前 Codex）完成，不额外调用付费模型。

本地 deterministic tooling 只负责机械、可验证的检查，例如 schema / manifest / hash / source-span identity、数字/公式/引用/路径/formal identifier 的 exact fidelity、render/file existence/generated parity、privacy boundary，以及 paid-review budget preflight / reservation / receipt。

外部付费模型只在“独立性本身提供了 host model 无法自证的新增证据”时使用，默认只允许 final candidate / final render QA。

因此默认禁止把外部 API 用于 Document Map、argument segmentation、Meaning Card、planning、正文 generation/rewrite、每个 unit 的常规 semantic self-audit、ordinary targeted repair、assembly/coherence 中间检查，或仅为了让多个 stage 看起来独立而拆成多次付费 model call。不得通过换更便宜的外部模型维持一个本来就不该存在的 per-stage API pipeline。

## 2. GPT Planner 必须先证明付费 API 的必要性

任何 Plan 只要包含一个 paid external model call，就必须显式回答：

1. 为什么 host model 自己完成该阶段不够？
2. 为什么 deterministic check 不够？
3. 付费调用增加的独立证据是什么？
4. 为什么必须现在调用，而不能只审 final candidate/final render？
5. 最多几次付费调用？
6. 单次 worst-case 成本、task campaign 总预算是多少？
7. 失败后怎样停止，为什么不会形成自动 review/repair/review 循环？

回答不了任一项：不得把付费 API 写进 frozen Plan。

## 3. 默认付费边界

AI_Skills Reviewed Handoff 默认 external reviewer 是 `gpt-5.6-terra`，仅用于独立 final QA。released plugin 默认 Terra OFF，正常 plugin production behavior 不依赖 Terra。

默认 task campaign：

```text
model: gpt-5.6-terra
max paid review calls: 2
campaign reserved-cost hard ceiling: USD 0.50
per-call worst-case ceiling: USD 0.25
automatic paid retries: 0
service tier: default
reasoning effort: low
max output tokens: 4096
paid tools: none
prompt cache: explicit mode with no cache breakpoints
```

任何超出默认值的 Plan 都必须由用户明确批准成本边界；Planner/Executor 不能自行扩大。同一 task 的 retry、GitHub rerun、Codex restart、换机器或 checkout 都不得重置 campaign budget。

## 4. 运行前预算：只用 persistent worst-case reservation

运行时安全判断只使用 task-local persistent reservation，不使用“今天花了多少”、Dashboard day bucket、Organization Costs API 或其他异步账单统计作为放行条件。

每次 paid request 前必须：

1. 构造即将真实发送的完整 request；
2. 对同一 request 调 `POST /v1/responses/input_tokens`；图片输入必须包含在真实 request 中；
3. 验证 model / service tier / reasoning / tools / prompt-cache 配置与已审计价格合同一致；
4. 使用已验证价格和 `max_output_tokens` 计算 `worst_case_cost_usd`；
5. 检查 `reserved_cost_usd + worst_case_cost_usd <= campaign_budget_usd`；
6. 检查 paid call count 仍在上限；
7. 在发送模型请求前持久化 reservation；
8. 只有 reservation 成功后才允许 `POST /v1/responses`。

reservation 一旦发生，不因为请求失败、实际输出较短、retry、workflow rerun 或进程重启而自动返还。reservation 是安全保险丝，不是事后报表。

当前 Terra 价格基线（reviewed 2026-09-03，官方 model docs）：

```text
input: USD 2 / 1M tokens
cached input: USD 0.20 / 1M tokens
output: USD 12 / 1M tokens
cache write: 1.25x uncached input price
```

GPT-5.6 还存在长上下文分档价格；任何 request 如果进入已验证价格表之外的区间，必须 fail closed。当前 reviewer request 应通过预算/TPM 边界远低于该阈值，不得依赖“应该不会超过”而忽略检查。

为了让 preflight 与实际账单口径稳定，review request 默认使用 `prompt_cache_options.mode=explicit` 且不设置 cache breakpoint，避免 implicit cache-write 产生额外计费。如果成功 response 仍报告非零 `cache_write_tokens`，则标记 `ACCOUNTING_UNVERIFIED`，同一 campaign 不得再发下一次 paid request，直到计费逻辑被重新核实。

## 5. 每轮实际花销：只用 response usage 计算 task-local actual cost

每个成功的 `/v1/responses` 必须读取并持久化：

```text
response_id
usage.input_tokens
usage.input_tokens_details.cached_tokens
usage.input_tokens_details.cache_write_tokens
usage.output_tokens
usage.output_tokens_details.reasoning_tokens
```

`usage.output_tokens` 已包含 reasoning tokens，因此 reasoning tokens 只作为诊断字段，不能再次加价。

在默认禁用 cache-write 的合同下，若 `cache_write_tokens=0`，actual model cost 按官方 usage 计算：

```text
uncached_input_tokens = input_tokens - cached_tokens
actual_model_cost_usd =
  uncached_input_tokens * 2 / 1_000_000
  + cached_tokens * 0.20 / 1_000_000
  + output_tokens * 12 / 1_000_000
```

receipt 必须同时保留两套数字：

```text
reserved_worst_case_cost_usd   # safety gate，不返还
actual_model_cost_usd           # 本次真实 model usage 的成本核算
campaign_reserved_cost_usd
campaign_actual_model_cost_usd
```

实际成本只用于 task accounting / 用户报告，不反向释放 reservation。不得为了“算得更准”把 Organization Admin API key、Costs API 或 day bucket 引入 CI。

Live migration smoke 之前必须先用 repository secret 在 GitHub Actions 内验证 `POST /v1/responses/input_tokens` 可用，且该检查只能调用 input-token endpoint，不得继续调用 `POST /v1/responses`。Implementation rule: only call input-token endpoint during this permission smoke. 如果新 project-scoped key 因缺少 `Responses=Write` 或其他 authorization / permission 问题失败，必须 fail closed 并报告非 secret 的 HTTP status、OpenAI error code/type/message/param；不得自动扩大 model capability 或改用旧 key。

## 6. Text Review

Text Review 默认只看需要独立判断的最终 candidate，加上 audience 与 frozen review questions/rubric。除非 fidelity review 明确需要 source-aware comparison，否则 reader-style QA 不上传 source 原文、intermediate drafts、Meaning Cards、internal self-audit 或 repo workflow log。

## 7. Visual Review

Terra 的 image modality 在本项目中只用于 image input review，不用于 image generation。Visual Review 允许发送 final render / selected final comparison images 给 Terra，然后只接收文本 review 结果。

默认：

- no image generation；
- no web search / file search / computer use / code interpreter / hosted shell 等额外 paid tool；
- 图片必须进入同一个 `/responses/input_tokens` preflight；
- `images/min` 是平台吞吐上限，不是本仓库预算；真正保险丝仍是 request token preflight + task campaign reservation。

如果一套 deck/figure batch 无法在单次 `$0.25` worst-case ceiling 内完成合理 final review，应由 Planner/用户重新决定 review strategy；不得自动扩大预算。

## 8. Trigger 与 retry

付费 review workflow 必须 explicit/manual invocation。普通 `push`、普通 CI、manifest commit、evidence writeback 不得自动调用 Terra。

默认自动 paid retry = 0。`credit_balance_exhausted`、`project_spend_limit_exceeded`、`organization_spend_limit_exceeded`、`organization_usage_limit_exceeded` 和其他明确 billing/insufficient-quota error 必须立即停止，绝不 backoff。

真正 transient rate-limit error 即使未来允许 retry，也必须消耗同一 campaign 的 paid-call slot 与 reservation；不得产生新预算。

## 9. 多插件并行：开发并行，paid review 使用 repo-wide execution slot

多个 plugin task 的 Codex development、local tests、deterministic CI 可以并行。每个 task 使用独立 campaign ledger：

```text
results/<task_key>/paid_review_budget.json
```

因此不同 task 的 `$0.50` budget 互不串账。

但 AI_Skills_Collection 内真正调用 Terra 的 paid review 默认一次只执行一个，避免多个 final review 同时争用同一个 OpenAI Project 的 100k TPM。

这不是要求实现一个新的 FIFO queue service。正确语义是 **pre-dispatch slot check + GitHub concurrency mutex**：

1. Executor/dispatcher 在 dispatch 前检查本 repository 的 paid Text/Visual review workflow 是否已有 `queued` / `in_progress` / 等价 active run；
2. 如果已有 active paid review：不 dispatch，不 reserve，不消费 paid call count；保持当前 workflow state 合法等待，并在 next action / RESULT 中记录 `waiting_paid_review_slot`；
3. slot 空闲时才 dispatch；
4. Text/Visual paid workflows 共同使用 repository-wide concurrency group，例如 `ai-bridge-paid-review-${{ github.repository }}`、`cancel-in-progress: false`，仅作为 race mutex；
5. 不把 GitHub concurrency 的 pending run 当 FIFO queue，也不允许主动积压一串 pending paid workflows；GitHub concurrency 不保证 FIFO，不能承担业务队列语义；
6. 极小概率 race 导致一个 pending run 被取消/替换时，若其 paid request 尚未开始、未 reserve，则视为 scheduling deferral，不是 task failure，也不消耗 review/repair/cost budget；后续正常 Executor/scheduler check 再尝试。

不要为此新增数据库、长期 worker、daemon、独立 queue service 或新的 Reviewed Handoff state。当前迁移只保证 **AI_Skills_Collection repo 内** 的 paid review 串行；不同 repository 共享同一 OpenAI Project 时仍由 Project 10 RPM / 100k TPM / monthly hard limit 做外层保护。除非以后真实出现跨 repo contention，不提前构建全局 queue。

## 10. Project / secret contract

外部平台配置由用户在 OpenAI API Project 管理，不由 repo 自动修改。预期：

```text
project: AI_Research_Review
allowed model: gpt-5.6-terra only
project override: 10 RPM
project override: 100,000 TPM
monthly project spend: USD 10 hard limit
```

这些只是最后一道保险，不替代 task-local `$0.50` fuse。

AI_Skills 的 secret 名称继续分开：

```text
OPENAI_REVIEW_API_KEY
OPENAI_VISUAL_REVIEW_API_KEY
```

两者可以属于同一个 `AI_Research_Review` project，但不得互相 fallback。Secret value 不得打印、commit、写入 artifact 或要求用户粘贴到聊天中。

## 11. Artifact review 语义

External Terra PASS 只是独立 review evidence，不拥有产品最终裁决权。用户明确拒绝真实 artifact 时，以用户反馈为准。未调用 Terra 也不等于 review 缺失：如果 frozen acceptance 不需要独立 external review，host review + deterministic checks + human artifact gate 可以是正确路径。

## 12. CI 生命周期

允许 ordinary push 自动运行的 workflow 必须同时满足：zero paid API、cheap、strongly path-scoped、failure 与 changed area 直接相关、read-only、不跑全库 heavyweight matrix。

Codex Marketplace full matrix、release smoke、Windows sparse checkout、Linux/Windows editable install smoke、以及任何 paid review 都是 explicit gate，不是每个 commit 的默认仪式。`ci_required=true` 的语义是 implementation candidate frozen 后显式 dispatch full CI，PASS 后再进入 Reviewer/integration。

## 13. 迁移原则

active production path 最终必须满足：

- paid workflows manual-only；
- text/visual secret 不互相 fallback；
- Terra-only final QA；
- persistent task budget + actual-cost receipt；
- no paid retry loop；
- repo-wide paid-review slot，不伪装成 FIFO queue；
- Text Review 和 Visual Review 都仍可真实运行；
- 普通 Codex/plugin generation 不产生额外 API 账单。

如果旧 workflow 与本政策冲突，先迁移 workflow，再启动依赖它的新高成本 task。不得一边知道成本保护尚未完成，一边继续 live paid replay。
