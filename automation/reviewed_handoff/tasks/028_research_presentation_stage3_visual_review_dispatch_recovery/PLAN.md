---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 028_research_presentation_stage3_visual_review_dispatch_recovery
decision: PLAN_FROZEN
---

# 028 Research Presentation Stage 3 Visual-Review Dispatch Recovery — Plan

## Frozen decisions

028 是 027 的控制面 recovery，不是新的 Presentation 业务阶段，也不是 027 的第三次计划修订。它只执行 027 Plan revision 1 已经冻结但本轮 Executor 未真正完成的显式 GitHub Actions `workflow_dispatch`，以产生返修后像素对应的新 Terra evidence。

027 的业务实现、REVIEW_1、当前六张 rendered pixels、mature-talk 质量门槛与第二轮 review 额度全部保持不变。缺少视觉 evidence 不得算作 027 REVIEW_2 失败。

## Frozen objective

在不修改 027 页面或布局实现的前提下，获得并验证一份与当前 027 `visual_inputs.json` identity 一致的真实 task-local Terra item/page-level evidence，然后把控制权交还 Scheduled GPT Reviewer 继续 027。

## Required reading

Executor 至少读取：

- `automation/reviewed_handoff/schema.json`
- `automation/reviewed_handoff/prompts/CODEX_EXECUTOR.md`
- `automation/reviewed_handoff/tasks/RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md`
- `automation/reviewed_handoff/tasks/RESEARCH_PRESENTATION_CURRENT_ROUND.md`
- 027 REQUEST / PLAN（尤其 Plan revision 1）/ CURRENT / RESULT / REVIEW_1
- `results/027_research_presentation_executable_cuhk_scientific_layout_system/visual_review/visual_inputs.json`
- 当前旧 `VISUAL_REVIEW.json`
- `.github/workflows/ai-bridge-visual-review.yml`

## Known evidence before execution

当前可信事实：

- 027 implementation commit：`7dadb5e027013253c23025a847bae5d3e3039bd7`；
- handoff commit：`44ddd5b627f3325ae756603ffcef1fbca6d4cc70`；
- Codex Marketplace push run `32820700167`：completed / success；
- AI Bridge Visual Review push run `32820700238`：top-level success，但真实 log 显示 manifest/output path 为空，live visual review 被 skip，evidence commit 被 skip；
- 当前 027 PDF SHA：`b2dace9cb16a32ab832275a8d1c2c9c7c665015dd76bf94525543cf47b4cf194`；
- 当前六张主要内容页 PNG SHA：
  - slide 2: `508d5842483139f703c646efdd1c117eed7323e8d5214c78c29302cf974ad491`
  - slide 3: `15f35966635192b0b07818394d5402a98a40e247c2abc376434e92332b604437`
  - slide 4: `f7631db19453fca82efddcb8afab1a5b8c024221d9080ba5359a6377d5de77a9`
  - slide 5: `3ae702392aa81f62881f3d1533c269fe07ed99f0c9eb4e619d8338656cbca7e7`
  - slide 6: `61db6033b6868a06ba05becd3cd82279df87dd61657571c985ade84003a87421`
  - slide 7: `09859b9a192bd1657bedbf59cc648cfaa492478b40bbb98b0ef466ca2d6481cb`。

现有 `VISUAL_REVIEW.json` 绑定的是返修前旧 SHA，因此严格视为 stale。

## Implementation scope

### 1. Do not regenerate or edit Stage 3 pixels

先 `git fetch` 并 fast-forward 到最新 `origin/main`。确认 027 当前 `visual_inputs.json` 仍绑定上述六个新 SHA，且对应 PNG 文件存在。若 identity 已因其他合法提交改变，停止并交回 Planner，不得自行选一套像素继续。

不得重新生成 PDF/PNG，不得修改 Stage 3 generator、TeX、layout、gold、CUHK theme 或 027 Planner/Reviewer-owned files。

### 2. Explicitly dispatch the task-local visual review

必须使用 workflow_dispatch，而不是依赖 push 自动触发：

```bash
gh workflow run "AI Bridge Visual Review" \
  --ref main \
  -f manifest=results/027_research_presentation_executable_cuhk_scientific_layout_system/visual_review/visual_inputs.json \
  -f output=results/027_research_presentation_executable_cuhk_scientific_layout_system/visual_review/VISUAL_REVIEW.json
```

记录实际 dispatched run id、event type、head SHA 和时间。

### 3. Require a real live-review execution

等待 dispatched run 完成。不能只检查 workflow top-level `success`；必须检查 job/step/log，确认：

- event 是 `workflow_dispatch`；
- `OPENAI_API_KEY` secret 通路可用；
- manifest/output path 为上面的 027 task-local 路径；
- `ai-bridge visual-review run` 实际执行，而不是因为 missing secret/path 被 skip；
- writeback step 实际检查新 evidence；若产生 diff，应由 workflow 正常 commit/push。

如果第一次 run 因 GitHub 短暂取消/服务抖动失败，最多允许一次同参数重新 dispatch。若失败原因是权限、secret、workflow contract 或其他确定性配置问题，不得循环重试；保留真实 run/log 并交回 Planner。

### 4. Validate fresh evidence identity

GitHub Actions 写回后，`git fetch` 并只做 fast-forward 同步。新版 `VISUAL_REVIEW.json` 至少必须满足：

- `task_key` 为 027；
- `review_model` 为当前真实 Terra 模型（预期 `gpt-5.6-terra`）；
- 六个 `item_reviews` 均存在，对应 slide 2–7；
- review 中 images / input manifest 的六个 PNG SHA 与当前 `visual_inputs.json` 完全一致；
- PDF/build identity 与当前 027 manifest 没有冲突；
- `created_at` / evidence identity 明确晚于返修前旧 review；
- 不是复用旧 `review_identity=6e2e6dab29b0688cc0fde5fe6d68925c5043339fc07df522edb966dc11a44ca1`。

无论 item-level 结果是 PASS 还是 REVISE，只要 evidence 真实、完整、identity 正确，028 的证据恢复目标即可视为完成。页面质量判断属于 027 Scheduled GPT REVIEW_2，不属于 028 Executor。

### 5. Handoff

写 `results/028_research_presentation_stage3_visual_review_dispatch_recovery/RESULT.md`，只汇总：

- dispatched run id / event / conclusion；
- live review 是否真实执行；
- evidence writeback commit（若有）；
- 新 review identity；
- 六个 item ids 与对应 PNG SHA；
- item-level decisions 原样简短列出，但不得据此宣告 027 PASS；
- 若失败，精确记录失败点和恢复条件。

028 不需要修改 027 CURRENT。Scheduled GPT Reviewer 在后续运行中看到 fresh evidence 后自行恢复 027 的 CI/review 路由。

## Validation

至少验证：

- `git diff --check`；
- Reviewed Handoff repository validation；
- 027 manifest 与新 VISUAL_REVIEW identity 一致；
- 不存在 027 页面/业务代码的非预期 diff；
- 不存在对 027 PLAN/REVIEW_1/CURRENT 的 Executor 修改。

本 task 不新增业务代码，因此 `ci_required=false`。真实 GitHub visual-review run 本身就是本 recovery 的核心外部证据。

## Stop condition

满足以下条件立即停止：

1. workflow_dispatch 的 live visual review 真实执行；
2. 新 `VISUAL_REVIEW.json` 写回 main；
3. 六页 identity 与当前 027 manifest 一致；
4. 028 RESULT 已记录真实 evidence。

随后交回 Planner，不重新审页面，不启动 Stage 4。

## Acceptance and regression gates

Planner 只有在以下全部成立时才可 PASS 028：

1. 没有修改 027 Stage 3 页面/布局实现；
2. 没有消耗或伪造 027 REVIEW_2；
3. dispatched run 不是 push-mode skip，而是真实 workflow_dispatch live review；
4. 新 Terra evidence 与返修后六张 PNG identity 完全一致；
5. evidence 包含六个 item/page-level judgement；
6. 没有降低 027 frozen mature bar；
7. 没有开始 Stage 4/5。

028 PASS 只表示视觉证据通路恢复。之后必须回到 027 做第二轮独立审核；028 PASS 不能替代 027 PASS，也不触发 Stage 3 PASS notifier。
