# 下一步安全执行边界

结论：继续同一 Goal 下的有界证据修复，由 Executor 处理。Reviewer 没有要求改变架构、范围、版本或 production source，因此不应仅因新增证据要求而重新规划产品、申请扩大权限或停止整个任务。使用当前正常的 workspace-write 执行能力，限定为 replay fixtures 和 tracked gate evidence 的修复。

## 固定候选与允许范围

- 从现有本地冻结 Plan、验收门槛、当前任务状态和本轮 Reviewer 意见确认具体缺口；核对 review target 是否对应当前最终候选。旧轮次意见不能触发新一轮修复。
- 在执行前记录最终候选的 commit、production payload/artifact hash、版本和实际加载路径；这些身份必须保持不变。若证据修复产生新的提交，分别记录证据提交与受保护的 production candidate，不能将两者混为新的产品候选。
- 只修复失真的 fixture、错误的回放输入/定位或证据记录，并通过既有本地正常入口重新运行受影响的 gate。不得改验收标准、削弱断言、替换失败案例以追逐 PASS，或用 mock/smoke 代替冻结计划要求的真实路径证据。
- 当前任务禁止联网；不执行 fetch、push、远端 review、在线 replay 或其他网络操作。可完成的本地工作继续，依赖网络的门槛明确留待后续，不把本地结果写成远端已验收。

## 必须补齐的证据

1. 建立逐项对应关系：Reviewer 要求 → 冻结 Plan 中的验收门槛 → 现有缺口 → fixture 修复 → 重跑命令、结果和证据路径。不能从当前简短输入推断具体缺失 gate 的名称或数量。
2. 说明 fixture 原来为何不能代表目标情形、修复后为何忠实；保留原失败/缺失证据与修复后结果，区分测试夹具问题和产品缺陷。
3. 每项新证据绑定同一个最终候选，记录实际 consumer/loading path、fixture 身份、运行环境、命令、退出状态和原始日志。历史 PASS 只有在候选身份及适用性均可核实时才可引用，不拼接不同候选的 PASS。
4. 按影响范围重跑缺失或失效的 gate，并提供相邻已接受行为未改变的回归证据。若共享 fixture 影响多个 gate，应覆盖这些 gate；无需凭空创造新的固定 gate 数量。
5. 核查修复 diff 与候选 hash，证明 production source、payload、版本和 release identity 未变；记录未运行、失败或在离线条件下无法取得的证据及其对验收的影响。

## 不可越过的边界

不使用 paid API；不修改 production Marketplace；不修改 Bridge/Host Policy；不合并 main、不发布、不 bump version；不改变生产候选。所有本次交付文件只写入 outputs。

如果可信回放证明修复必须触及 production source，或者 Reviewer 要求实质改变方法、范围、验收标准或候选身份，则停止该项依赖操作，保留证据并使用现有 NEEDS_GPT_PLANNER/STOP 路由。不得以“补证据”为名改变产品，也不把可由 Executor 解决的 fixture 问题升级为人工授权问题。

## 交接与完成语义

只有同一最终候选的全部适用证据门槛闭合，才可请求本轮验收复审；本地证据补齐并不等于整个 release Goal 完成。需要外部 Reviewer 的阶段保留既有合法状态和明确 next_action，不伪造审批、发布或终态完成。

本次实际完成的是执行边界文档。输入未提供具体 Plan、候选 hash、Reviewer 明细或运行结果，因此这里没有宣称已修复 fixture、已重跑 gate 或已达成 release Goal。
