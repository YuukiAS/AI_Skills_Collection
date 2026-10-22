# 历史交接：2026-10-20 的 v0.2 候选

> 本文件以下内容只保留历史，不能用于当前 live update。旧 079bd798 候选已失效。
> 当前唯一批准包为 `48c42f89d23ba168e2d2045034a7f7117c2e0448`；
> 新实现进度和精确恢复点见 `v0.4/PLANNER_HANDOFF.md`。新版 FINAL_CANDIDATE 尚未冻结。

任务和分支不变：`clear-writing--single-entry-artifact-finalization` /
`design/clear-writing--single-entry-artifact-finalization`。
权威执行包仍为 `d7b810d194ead881303aaca9c2e4f1d59a97c1f1` 中的 Plan / Goal / Runbook / Kickoff v0.2。
本文件只定位实际产物，不修订 Gate 或授权。

## 候选与证据

- 最终身份：`candidate/FINAL_CANDIDATE.json`。
- 完整构建回执、文件映射和 hashes：`wrapper/BUILD_RECEIPT.json`。
- 独立实施审查：`review/IMPLEMENTATION_REVIEW.md`。
- 13 组原始输入、完整实际输出、首次运行记录：`known-regression/`。
- 最新本地验证与 required GitHub CI：`validation/`。
- README 的真实 installed Clear Writing 检查：`README_REVIEW.md`。
- GitHub 可读的 ZIP 文本分发：`transport/MANIFEST.json`、`transport/part-000.b64` 至 `transport/part-037.b64`。

按 transport manifest 顺序拼接纯 base64，验证每片与合并值的 SHA-256，再严格解码。
重建 ZIP 必须为 170866 bytes，SHA-256 必须为
`e4c451841583cb6e1ae4212f8d8559b93ef4272f66d687d3f6762f6114a73dc6`。
已实际重建校验：29 个文件，一个顶层 `skills/clear-writing/SKILL.md`，六项 route 及支持文件完整。
分片只包含公开仓库候选 payload，不包含账户 ID、凭据、私有链接或私人材料；无需用户手工上传 ZIP。

## 唯一下一阶段

由批准 Runbook 指定的长期 ChatGPT Planner 在原账户使用既有 Plugin Creator / GitHub connector 执行。
先做尚未完成的当前账户 P0 只读回读，不把本地缓存当作账户证据。
核对 live Clear Writing 仍为 0.5.0、USER/PRIVATE、同一插件身份与冻结旧文件集合，保存真实旧 archive 和 current release identity。

在任何 live update 前，以保存的真实 0.5.0 archive 和本候选 ZIP 调用同一提交中的
`scripts/build_clear_writing_chatgpt_wrapper.py prepare-restore`，生成并验证 forward-restore 0.6.1 archive、
`RESTORE_06_ONLY_PATHS.json` 与 `RESTORE_DELETE_PATHS.json`；不得把仓库/缓存的 0.5 文件冒充账户旧 release。
正向更新的冻结删除路径见 `wrapper/UPDATE_DELETE_PATHS.json`，必须与 live 旧 file list 对照，不临场重算迁移范围。

随后严格按原 Runbook 更新**现有**插件、逐文件回读并顺序执行 G1-G5。
G3 必须真实通过 ChatGPT Web GitHub connector 完成完整文件读取、完整终审候选、带 expected blob 的写入、全文回读一致。
本地回放和清楚的聊天回复均不能代替 G3。
模型仍为冻结的 `GPT-5.6 Sol`；不得换模型、换样本、追加工具或重跑产品失败。

只有 G1-G5 全 PASS 后，原独立 Critic 才可冻结唯一 fresh G6 输入。
再按原合同完成 G6、完整最终产物审查和 release closure。
G6 尚未选择或消费；没有提前使用 Reader Guide 调参。

## 当前未完成边界

尚未更新 Personal Plugin，未运行真实 G1-G6，未修改正式 release/main，未发布 0.6。
当前正式基线仍为 `fd79c4be54fc50bd66d9a51bbc1e681f361f6a77` / repository 5.5.1 / writing-style 0.5。
本地候选通过不等于整个用户 Goal 完成；不写 DONE，不伪造账户或 Web 证据。
Issue #13 保持 open / DOING，原有 #73/#49 下游接入仍 pending。

如 live mutation 后发生原合同规定的终止性产品失败或耗尽的基础设施失败，执行原 forward-restore 合同，
恢复已验证 0.5 行为并放弃中央 0.6 发布；不把未经验收的 0.6 留在正式个人插件中。
