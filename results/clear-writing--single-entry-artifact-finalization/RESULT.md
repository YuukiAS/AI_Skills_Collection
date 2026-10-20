# Clear Writing 0.6：本地实施与交接

任务：`clear-writing--single-entry-artifact-finalization`。
分支：`design/clear-writing--single-entry-artifact-finalization`。
批准执行包：`d7b810d194ead881303aaca9c2e4f1d59a97c1f1`。
候选代码：`079bd7987bb33d624d244feb415327d5cf2343d8`。

本轮完成 Codex 所属的本地包装实现、回归、验证与分发准备，不宣布整个 release Goal 完成。
后续账户阶段沿用原任务和批准 Runbook，由既有 ChatGPT Planner 执行，
不因 Codex 缺少 Plugin Creator 创建新架构或把本地工作标成产品失败。

## 实际实现

新增唯一 ChatGPT 总入口、确定性构建器与直接单测。
六项专业规则继续由 canonical source 拥有，正文和 profile 均未变化。
Codex Marketplace 保留六个直接入口；generated 层通过正式 generator 更新，只有候选版本变为 0.6。

Personal wrapper 0.6.0 包含 29 个文件、一个可发现 Skill，双 manifest 一致。
仅应用批准的两条 `CW06_ROUTE_PROJECTION_V1` 路径转换；其余专业正文逆变换、支持文件和图标均逐字节一致。
按 `CW06_DETERMINISTIC_ZIP_V1` 重复构建的 raw ZIP 相同：

`e4c451841583cb6e1ae4212f8d8559b93ef4272f66d687d3f6762f6114a73dc6`。

完整恢复工具已实现和机械验证；实际 live 0.5.0 archive 保存与 forward-restore 包构建仍须在 Phase C mutation 前完成，
本地测试数据不冒充真实账户快照。

## 真实验证

| 检查 | 结果 |
| --- | --- |
| 独立实施审查 | PASS；全部 findings 已关闭，明确允许冻结该候选 |
| wrapper focused tests | 18/18 PASS |
| 全仓单测 | 370/370 PASS |
| KR-WEB-01..09 | 9/9 本地完整产物 PASS，保留 03/08/09 正向深度 |
| should-not-change | 4/4 PASS；精确合同及 JSON 字节一致 |
| source / wrapper / generated parity | PASS；六项专业正文/profile 无改动 |
| Marketplace write/validate/check/path-report + second check | PASS；无 generated drift |
| skills validate / audit | PASS；156 active skills，18 profiles |
| README 当前 installed Clear Writing | PASS；完整 README 原样放行 |
| required GitHub CI | PASS；`39368960081`，四个 job，exact candidate head |
| 文本 transport 重建 | PASS；38 parts，170866 bytes，raw ZIP SHA 一致 |
| `git diff --check` | PASS |

完整 CI：[run 39368960081](https://github.com/YuukiAS/AI_Skills_Collection/actions/runs/39368960081)。
逐项审查、source-to-output 对照及原始运行身份见 `known-regression/` 和 `review/`。
回放在 f86c4d0d 上产生，后续只修构建/采集校验，专业 payload 和实际 ZIP 未变化；
保留原运行提交和第一次有效产物，不伪造新提交上重跑，也不 reroll。

## 版本与未完成边界

Repository bump decision: NONE (implementation candidate)
Reason: required live Gates 和最终完整产物审查未完成；PATCH 版本在正式发布阶段按 origin/release 后绑定。
Affected plugins:
- writing-style: 0.6 candidate only; formal 0.5 unchanged
- all other central plugins: NO_BUMP

正式 release 仍为 `fd79c4be54fc50bd66d9a51bbc1e681f361f6a77`，repository 5.5.1 / writing-style 0.5。
未更新 PRIVATE 插件，未运行 ChatGPT G1-G6，未选择 G6 fresh 输入，未把 Reader Guide 用于开发调参。
未修改其他插件产品行为、Bridge Kit、main 或 release ref，没有重跑旧 Web Gate/W2。
Issue #13 保持 open / DOING，Area writing-style，Resolution commit 空；#73/#49 接入仍 pending。
Issue 当前进度正文已由真实 installed Clear Writing 终审并写回，完整回读与审校候选一致，
原正文保留在明确标注的历史区。Project 的 DOING / writing-style / 空 Resolution commit 已实际回读确认，
不是 pending mutation 或口头声称同步；回执见 `validation/ISSUE_SYNC.json` 与 `validation/PROJECT_SYNC.json`。

## 下一步

独立实施审查 PASS 后已冻结最终身份，见 `review/IMPLEMENTATION_REVIEW.md`、`candidate/FINAL_CANDIDATE.json`。
现有 ChatGPT Planner 从同分支读取 `PHASE_C_HANDOFF.md` 与 transport，继续批准的 P0/恢复预备、
现有插件更新和 G1-G6。聊天回复清楚、本地哈希/测试或本地回放都不能替代真实 GitHub 文档的全文终审、写入与回读。
只有全部 required Gates 和最终完整产物审查通过，才允许正式发布 0.6。
