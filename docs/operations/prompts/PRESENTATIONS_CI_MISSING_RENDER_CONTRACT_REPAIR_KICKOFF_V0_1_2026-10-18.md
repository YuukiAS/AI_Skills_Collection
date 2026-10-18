修复 Presentations 当前的 CI missing-render contract，不要扩大范围。

仓库：`YuukiAS/AI_Skills_Collection`
任务：`presentations--ci-missing-render-contract-repair`
分支：`reviewed/presentations--ci-missing-render-contract-repair`

先读取并严格执行：
- `docs/design/presentations/PRESENTATIONS_CI_MISSING_RENDER_CONTRACT_REPAIR_V0_1_2026-10-18.md`
- `docs/goals/PRESENTATIONS_CI_MISSING_RENDER_CONTRACT_REPAIR_GOAL_V0_1_2026-10-18.md`
- 当前 task 的 REQUEST / PLAN / CURRENT
- 本 package 的独立 Critic PASS

已知根因是 `f717d28...` 引入 canonical font-resource typed state 后，generator、validator/test 的 missing-render 语义没有同步。

只允许：
1. 无 TeX engine 时 primary compile status 正确返回 `BLOCKED_MISSING_TEX_ENGINE`；
2. `--allow-missing-render` 仅新增接受 `BLOCKED_MISSING_CANONICAL_FONT_RESOURCE` 这一 typed environmental state；
3. 增加/修正对应 regression tests；
4. 通过正式 generator 更新 generated mirrors。

严格模式仍必须对缺失 TeX/font fail closed。不得 skip/delete tests，不得把 source/token/font-policy defect 加进 allowlist，不得安装私有 font bundle 来绕开状态 bug，不得改 Clear Writing。

完成后跑 focused tests、full tests、Marketplace write/check、generated parity、git diff check 和 required GitHub CI。全部 PASS 后提交/push并交独立 Reviewer。
