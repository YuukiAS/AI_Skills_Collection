---
schema: AI_BRIDGE_REVIEWED_FINAL_REPORT_V1
task_key: 029_reviewed_handoff_visual_contract_adaptation
final_decision: PASS
---

# 029 Final Report — Reviewed Handoff Visual Contract Consumer Adaptation

## What this task solved

029 关闭了 AI_Skills_Collection Visual Review consumer 与 Bridge Kit task-local Reviewed Handoff visual contract 之间的真实接线缺口。此前普通 push 在没有 repository-level manifest/output vars 时可能显示 workflow success，但 live Terra 实际没有运行；以后视觉型 task 可以依赖自身 tracked CURRENT 与 task-local manifest/evidence path，由 push workflow 自动发现唯一待审目标。

## What changed

新增 deterministic resolver `scripts/resolve_reviewed_handoff_visual_target.py`，并改造 `.github/workflows/ai-bridge-visual-review.yml`：普通 push 通过 resolver 解析 task-local visual target，显式 `workflow_dispatch` 仍保留为恢复/调试入口。Bridge Kit visual-review extra 固定到支持当前 contract 的稳定 revision。相应 consumer 行为与恢复方式记录在 `docs/AI_BRIDGE_VISUAL_REVIEW.md`，并增加 targeted regression tests。

## New capabilities / behavior

push-mode 现在具有确定性的三态行为：没有待审 task 时正常 no-op；恰好一个合法 task 时自动获得该 task 的 manifest/output path；多个合法 task 或 identity/path 非法时 fail closed。已有 evidence 只有在 manifest SHA、task key 与 implementation commit 都匹配时才被视为 fresh，因此同一视觉 identity 不会被重复调用。

真实 GitHub Actions 已验证当前 0-task 路径：run `32932425821` 中 resolver 明确返回 `eligible_count=0`，随后 Terra 与 writeback 按设计跳过；这与旧版“缺固定 vars 后静默 skip”不同。下一项真实 Stage 3 视觉 recovery 将自然验证 1-task 的 live Terra/writeback 路径。

## Example usage

后续视觉型 Reviewed Handoff task 由 Planner 在 CURRENT 中声明 `visual_review_required=true`，并提供 repository-relative task-local `visual_review_manifest_path` 与 `visual_review_evidence_path`。Codex 生成并提交真实 render/manifest 后，正常 CI 完成并进入视觉证据等待阶段；push-mode Visual Review workflow 自动解析唯一 pending task，使用 GitHub secret 运行 Terra 并把 `VISUAL_REVIEW.json` 写回。用户不再需要为正常路径手工执行 `gh workflow run`。

## Regression and remaining limitations

029 没有修改 Reviewed Handoff state machine、角色 authority、review 次数、Terra reviewer semantics、027 页面、Stage 2 gold 或 canonical CUHK layout。显式 manual dispatch 仍可用。

当前唯一保留的非阻断限制是：029 本身不是视觉业务 task，因此没有为了测试而额外制造一次付费 1-task Terra 调用。该分支已经有 deterministic regression；下一项真实 Stage 3 visual-maturity recovery 将提供生产级端到端证据。如果届时出现新的 consumer failure，应作为新的可复现 production issue 处理，而不是回退到 repository-level 固定 manifest vars。

## Technical appendix

- implementation commit: `9f067118efe528241e45c425555a6061fa342d41`
- handoff CI tip: `ea562e09cd5dfb347c84e7c1de95051c1d5cf21c`
- `Codex Marketplace` run: `32932425818`, success
- `AI Bridge Visual Review` run: `32932425821`, success
- targeted resolver/workflow regression: 11 tests passed
- full unittest suite reported by Executor: 133 tests passed; real `Codex Marketplace` CI test step passed
- skills/marketplace/Reviewed Handoff validation: passed
- Stage 3 remains not passed; 027 retains historical two-round `REVISE / REVIEW_LIMIT` result
