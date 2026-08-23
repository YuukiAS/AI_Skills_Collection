---
schema: AI_BRIDGE_REVIEWED_FINAL_REPORT_V1
task_key: 021_research_presentation_comparative_reference_calibrated_visual_review
final_decision: PASS
implementation_commit: 6037c6280ec6d9db46e78292ec5013b28f98d9f8
---

# 021 Research Presentation Comparative Reference-Calibrated Visual Review — Final Report

## 结论

021 已在第一轮独立审核中 PASS。它完成了新一轮 Presentation 质量链路中的第三个核心节点：系统现在不仅能从真实 inspected reference 提取构图并生成多个候选，还能把 generated candidates 与真实 reference renders 放进同一个匿名 Terra 视觉审查包，得到真正的相对质量差距。

这不是 candidate quality PASS。相反，本轮最重要的价值就是第一次得到可靠的负面结论：当前统计公式候选仍明显低于成熟 reference bar，医学影像 case 也没有任何 item 达到成熟组会 / strong conference-talk level。

## What this task solved

上一阶段已经证明 candidate geometry 真实受 reference composition 影响，但没有回答“这些候选到底好不好”。021 现在把评价问题从 absolute QA 改成 comparative QA：

```text
3 generated candidates
+
2 inspected reference renders
-> anonymous visual review
-> candidate-vs-reference quality gap
```

reviewer 不知道谁是 generated、谁是 reference，也看不到作者、机构、RRL/SRC 或 candidate strategy。

## What changed

仓库新增了：

- comparative visual-review preparation / validation scripts；
- consumer-side GitHub Actions workflow；
- statistical estimator/equation comparative case；
- medical-image comparison comparative case；
- per-case anonymous visual input manifests；
- per-case immutable review identity；
- internal identity maps；
- live Terra evidence；
- decoded comparative audit report；
- regression tests。

外部 reference pixels 只在 runtime materialize，没有被提交为长期 binary corpus。

## Reference identity handling

本轮明确区分：

- 019 canonical inspected-page render SHA；
- 本次 runtime renderer 真正送给 Terra 的 input SHA。

这样不会因为不同 renderer 的 PNG bytes 不同，就伪造 reference identity 相等。真正参与当前 visual review 的 pixels 由 actual reviewer-input SHA 绑定。

## Blind comparative review

两个 case 都使用匿名 `item_A` ... `item_E`。

Terra-visible manifest 不包含：

- RRL / SRC；
- author / institution；
- candidate strategy；
- generated / reference / gold / baseline 标签。

真实身份只保留在内部 identity map，review 完成后才解码。

每个 immutable case identity 只执行一次 live `gpt-5.6-terra`，没有重复刷新相同输入来追求更有利结果。

## Statistical result

统计 estimator/equation case 中：

- RRL-028 是唯一达到 mature / projection-ready bar 的 item；
- 三个 generated candidates 全部低于该 bar；
- generated 中 reference-faithful variant 最好，但仍有 equation contrast / legibility 不足与 annotation 没有直接整合数学对象的问题。

这说明 source-derived geometry 已经有效，但当前 candidate renderer 的公式处理与视觉完成度仍不够成熟。

## Medical-imaging result

医学影像 case 中所有 items 都被判为 `REVISE`。

Generated reference-faithful candidate 的布局和 hierarchy 相对最好，但仍受到两类限制：

- image prominence / panel integration 仍有改进空间；
- 当前 content 是 synthetic/demo-like fixture，本身不足以证明真实医学影像研究汇报的成熟视觉质量。

本轮没有强制 best-of-three winner，也没有把相对第一名误认为“已经够好”。

## Scope boundaries

021 没有：

- 修改 020 candidate geometry；
- 修改 Bridge Kit core；
- 把 reference pixels 提交进 repo；
- 锁定最终 deck-wide design system；
- 生成最终 PPTX / Beamer；
- 开始 statistical holdout；
- 开始 medical-imaging holdout；
- 宣告 `ONE_SHOT_QUALITY_PASS` 或 `PROGRAM_MATURE`。

## CI

最终 handoff tip `b0c786c1647f34b4bd0bef18ce4dda999e799791` 的 `reviewed-handoff/ci-summary=success`，GitHub Actions run `32635425215` 成功。

本任务的 comparative validator、targeted Presentation tests、全库 116 tests、skills validation、Codex marketplace validation、Reviewed Handoff validation 与 `git diff --check` 均通过。

## Regression and remaining limitations

当前链路已经成立：

```text
reference
-> composition
-> candidate
-> comparative review
```

但 comparative evidence 明确显示 candidate 视觉完成度还没有达到可以直接进入最终 design-system lock 的程度。

下一步应该修 candidate visual finish / scientific-object treatment，而不是继续扩 reference metadata。统计方向必须重点解决公式对比度、可读性和直接数学标注；医学影像方向必须提高 image prominence / panel integration，同时不能把 synthetic phantom 美化成“真实研究证据”。

真实医学影像质量最终仍必须由后续 real holdout 检验。

## 下一步

下一 bounded task 应做 **candidate visual finish repair**，在不破坏 019/020 已验证的 reference geometry transfer 和 compatibility gate 的前提下，改善公式页与影像页的 presentation-native rendering，并在新 immutable identity 下重新执行 comparative review。

只有 repaired candidates 已接近真实 reference bar，才进入 deck-wide design-system locking / generation integration。

长期 `PROGRAM_MATURE=false`，`REFERENCE_CALIBRATED_ONE_SHOT_QUALITY` 仍未完成。

## Technical appendix

- implementation commit: `6037c6280ec6d9db46e78292ec5013b28f98d9f8`
- final handoff tip: `b0c786c1647f34b4bd0bef18ce4dda999e799791`
- required CI: PASS
- GitHub Actions run: `32635425215`
- Planner review: `REVIEW_1 = PASS`

## New capabilities / behavior

021 added an internal comparative visual-review capability for research
presentation candidates. It can place three generated candidates and matched
inspected reference renders into the same anonymous Terra package, then decode
the blind relative findings after review. This capability is evidence
infrastructure only; it does not make the current generated candidates or the
long-term Presentation Program complete.

## Example usage

The task-owned evidence was produced by the consumer workflow and helper:

```bash
python skills/tools/documents-media/presentations/shared/scripts/prepare_comparative_visual_review.py
python skills/tools/documents-media/presentations/shared/scripts/validate_comparative_visual_review.py --require-review --require-bytes
```

For 021, the resulting evidence lives under:

`results/021_research_presentation_comparative_reference_calibrated_visual_review/visual_review/`
