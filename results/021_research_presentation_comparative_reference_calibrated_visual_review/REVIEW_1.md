---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 021_research_presentation_comparative_reference_calibrated_visual_review
review_round: 1
decision: PASS
implementation_commit: 6037c6280ec6d9db46e78292ec5013b28f98d9f8
---

# GPT Review

## Decision

`PASS`。

021 的目标不是证明当前候选已经达到成熟科研汇报质量，而是建立可信的“候选 vs 真实 inspected reference”匿名相对视觉审查机制。当前实现满足冻结 Plan：两个 case 都真实包含 020 的三个候选和两个 inspected reference renders；reference pixels 真实进入 Terra；reviewer 看不到作者、机构、RRL/SRC、candidate strategy 或 generated/reference 身份；每个 immutable case identity 只运行了一次 live `gpt-5.6-terra`；解码报告保留了 no-winner 语义；required CI 已通过。

更重要的是，这次相对审查第一次给出了对长期产品真正有用的负面证据：统计公式页三个 generated candidates 全部低于成熟 reference bar；医学影像 case 也没有任何 item 达到成熟组会 / strong conference-talk level。因此 021 可以作为“评价机制 PASS”关闭，但绝不能把候选质量或整个 Presentation Program 判 PASS。

当前 handoff tip `b0c786c1647f34b4bd0bef18ce4dda999e799791` 的 `reviewed-handoff/ci-summary=success`，指向 GitHub Actions run `32635425215`。

## Independent review

### 1. Terra-visible 输入确实匿名，而不是口头声明 blind review

统计 case 的 `visual_inputs.json` 使用统一的 `item_A` 至 `item_E`、匿名 runtime 路径和共同 page-job 描述。可见 manifest 没有 RRL/SRC、作者、机构、candidate strategy、generated/reference/gold/baseline 标签；rubric 也明确要求只根据 pixels 和共同 page job 判断。

真实 identity 只保存在内部 `review_identity_map.json`。这满足“reviewer 不知道谁是 reference、谁是 generated”的冻结要求。

### 2. 真正送审的是 reference pixels，而不是 composition metadata

Executor 的 materialization path 会从既有 public source 恢复指定 inspected page，使用 runtime renderer 得到 PNG，并同时记录：

- inspected source identity；
- 019 canonical render SHA；
- 本次实际 reviewer-input SHA；
- page number；
- materialization method；
- rights/public-safe note。

因此 019 canonical render 与本次 review input 不被错误地强制视为同一字节 identity，真正参与 Terra 判断的是 actual input SHA。外部 reference screenshots/pages 没有提交进长期 source corpus。

### 3. Comparative rubric 已经从“有没有错”变成“与成熟参考相比差多少”

统计 rubric 明确要求逐 item 检查 composition、whitespace、typography hierarchy、scientific-object prominence、equation treatment、annotation/caption integration、visual specificity、AI-template fingerprints 与 projection readability，并且特别要求：最强 item 也不能自动视为足够好，可以合法得出 no item reaches mature bar。

这与上一轮 absolute Terra QA 的关键区别已经真实落实。

### 4. 统计 case 给出了清晰的 reference bar

解码后，RRL-028 是唯一被 Terra 判为 mature / projection-ready 的 item。三个 generated candidates 全部 `REVISE`。

其中 reference-faithful candidate 是 generated 中最好的一版，但仍存在两个明显差距：

- equation contrast / legibility 不够强；
- annotation 没有直接与数学对象形成成熟的视觉整合。

这说明 020 的 source geometry transfer 虽然成立，但“几何像 reference”并不等于“公式页的视觉完成度像 reference”。下一步应该修 candidate visual treatment，而不是继续增加 reference metadata。

### 5. 医学影像 case 合法保留了 no-winner

医学影像 case 中五个匿名 items 全部 `REVISE`。generated reference-faithful candidate 的布局与 hierarchy 相对最好，但 synthetic/demo-like image evidence 让其仍低于成熟科研汇报水平；另一候选也存在 image comparison 太小、页面偏 sparse 等问题。

这里没有因为 generated candidate 相对排名第一就强行晋级。该结果正是 021 设计 no-winner 语义的目的。

同时需要区分两个问题：

- composition / image prominence / hierarchy 等属于 candidate renderer 可修问题；
- synthetic fixture-like evidence 属于当前 regression content 的上限，不能靠继续“美化 synthetic phantom”解决。后续真实 holdout 必须使用真实科研材料。

### 6. 范围边界保持

021 没有修改 020 candidate geometry 来迎合 reviewer，没有修改 Bridge Kit core，没有提交外部 reference pixels，没有锁定 deck-wide design system，也没有偷跑真实 statistical / medical-imaging holdout。

因此当前 comparative result 可以被当成可信的独立诊断，而不是训练集内自我修图后的结果。

## CI

current handoff tip `b0c786c1647f34b4bd0bef18ce4dda999e799791` 的 `reviewed-handoff/ci-summary=success`，GitHub Actions run `32635425215` 成功。

Executor 记录的 comparative validator、Presentation targeted tests、全库 116 tests、skills validation、Codex marketplace validation、Reviewed Handoff validation 与 `git diff --check` 均通过。

## Final assessment

021 冻结范围内没有剩余 blocker，可以关闭。

但 comparative evidence 明确否定“现在已经可以锁 design system 或开始最终 one-shot holdout”的判断。下一 bounded task 应优先修 **candidate visual finish / scientific-object treatment**，至少关闭统计公式页的 equation contrast + direct annotation 差距，以及医学影像候选的 image prominence / panel integration 问题；同时不得试图把 synthetic medical fixture 本身包装成成熟真实科研证据。

只有 repaired candidates 在新的 immutable comparative review identity 下接近真实 reference bar，才进入 deck-wide design-system locking / generation integration。

长期 `PROGRAM_MATURE=false`，`REFERENCE_CALIBRATED_ONE_SHOT_QUALITY` 仍未完成。
