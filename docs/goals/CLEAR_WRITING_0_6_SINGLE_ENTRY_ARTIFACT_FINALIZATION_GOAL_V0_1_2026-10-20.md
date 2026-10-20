# Goal：Clear Writing 0.6 单入口与最终产物绑定

版本：v0.1
日期：2026-10-20
状态：DRAFT_PENDING_EXECUTION_READY_CRITIC
任务：`clear-writing--single-entry-artifact-finalization`
仓库：`YuukiAS/AI_Skills_Collection`
分支：`design/clear-writing--single-entry-artifact-finalization`
设计 authority：`docs/design/clear-writing/CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_PROPOSAL_V0_1_2026-10-20.md@3eefc626b86566113125a06fc6046a2bec1eafb2`
执行计划：`docs/design/clear-writing/CLEAR_WRITING_0_6_EXECUTION_READY_PLAN_V0_1_2026-10-20.md`
跟踪：Issue `#13`

> 本 Goal 只有在同一独立 Critic 对完整 execution-ready package 给出 `PASS / READY_FOR_CODEX=YES`，并且用户随后发送批准后的 Kickoff 后才可执行。

## 目标

把当前 ChatGPT Personal Plugin 的 Clear Writing 从“六个并列 Skill 由宿主继续猜路线”改成“一个显式可选的 `clear-writing` 总入口”，同时保持六项专业写作能力的 canonical source 和 Codex Marketplace 直接入口不变。

普通用户最终只需要选择一次 **Clear Writing**。总入口必须识别本轮实际交付对象，分别执行正确的已有写作路线，并且对正式支持的 GitHub 外部文档做到：完整读取 -> 终审候选 -> 写入 -> 回读 -> 逐对象准确报告状态。

## 必须实现的用户结果

1. ChatGPT Personal Plugin 只有一个可发现顶层 Skill：`clear-writing`。
2. 用户不需要知道 `response-clarity`、`scientific-rewrite`、`chinese-prose` 等内部 route。
3. 同一请求可以同时存在聊天回复与外部文档，两者必须分别处理、分别验收。
4. 正式中文长技术/科研材料需要结构重写时，按保真 -> 结构重写 -> 中文终审完成，不能只改善聊天总结。
5. GitHub 外部文档只有在 read/write/readback 与候选逐字一致后才能声称完成。
6. exact-only JSON/YAML/code/command/raw log 不被改写；mixed 输出只处理自然语言。
7. 六项 canonical writing Skill 与 `codex-writing-style` profile 继续直接可用，Research Authoring、Presentations、统计与科研图等领域 owner 不被接管。
8. 若 skills-only normal entry 无法稳定完成 G3 外部文档链，0.6 release path 立即停止；不继续堆提示词规则，也不让 Executor 自行设计 MCP。

## 正式外部 surface 边界

0.6 只把 **GitHub repository UTF-8 text file** 纳入已证明的 external-artifact finalization claim。

Google Drive、本地用户文件、Notion 或其他 surface 不由本版本的 GitHub Gate 推断为支持。它们需要各自真实 Gate 后才能加入正式 claim。

## source 与构建

ChatGPT adapter canonical source：

`packaging/chatgpt/writing-style/clear-writing/SKILL.md`

确定性 builder：

`scripts/build_clear_writing_chatgpt_wrapper.py`

六项专业 route canonical source 保持：

`skills/writing/core/{writing-fidelity,response-clarity,product-ui-copy,scientific-prose,scientific-rewrite,chinese-prose}/`

Personal wrapper 中只生成 route references，不手工维护第二份专业规则正文。完整细节、输出路径、hash parity 和 fail-closed 条件见 execution-ready Plan。

## required gates

必须由同一最终 candidate 满足：

- `CW06-G1`：Personal Plugin identity、单入口、双 manifest、old-path deletion、Plugin Creator / runtime 回读；
- `CW06-G2`：普通聊天、正式中文文档、长文结构重写、英文科研、UI、exact-only、mixed、必要长答和短答；
- `CW06-G3`：真实 Reader Guide known regression，同一请求完成聊天说明 + GitHub 文档全文读写回读；
- `CW06-G4`：source/final 保真、权限和状态边界；
- `CW06-G5`：canonical/generated parity、Codex 六 Skill、profile 和下游兼容；
- `CW06-G6`：final candidate 冻结后的一个真正 fresh 长技术文档完整任务，独立 Critic 直接读 source 全文和 final artifact 全文。

不得用 helper、schema、receipt、hash、Skill 自述或聊天回复质量替代 G3/G6。

## 实施与停止

执行顺序严格为：只读包装现实探针 -> implementation -> deterministic/parity -> known regression -> CI -> final candidate freeze -> Personal Plugin 0.6.0 update -> G1 -> G2 -> G3 -> G4/G5 final identity复核 -> Critic final-evaluation preflight -> G6 -> final review -> release closure。

每个 Web/fresh task 默认一个 model answer；只允许无模型输出的基础设施失败按同一输入最多重试一次。产品失败不 retry，不挑赢家，不换题。

如果 G3 失败：立即停止，不发布 0.6，不新增同义规则，回 Planner。后续只能重新提案为收窄 claim、已有 connector 的更受控工作流，或单独 App/MCP finalizer。

## 版本与发布

成功 closure 时：

```text
Repository bump decision: PATCH
Affected plugins:
- writing-style: 0.5 -> 0.6
- all other central plugins: NO_BUMP
Personal Plugin: 0.5.0 -> 0.6.0
Maturity: NO CHANGE
```

Repository 三段版本必须在 release 时按 current `origin/release` late-bind。

更新 `docs/plugin-changelogs/writing-style.md`；检查 README。若不需要更新，记录 `README checked: no update required`。若 README 有读者可见修改，必须真实调用已安装 Clear Writing 审校，不能用读 `SKILL.md` 代替。

Issue #13 继续复用且保持 open；0.6 完成不自动关闭原有 statistical-modeling / scientific-visualization adaptation。

## 禁止

本 Goal 不授权：

- 新 MCP / App /外部模型 /后台服务 /数据库 /状态机；
- 修改 Project setting；
- 扩大 Clear Writing 到领域判断；
- 用 temporary duplicate personal plugin 逃避真实 identity；
- 多次 reroll 到成功；
- G3 失败后继续修改 prompt 并把旧 Gate 当有效；
- fresh 样本失败后追加第二个样本；
- 未经 Critic PASS + 用户 Kickoff 就开始实现。
