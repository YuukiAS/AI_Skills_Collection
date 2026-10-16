---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: hpc--slurm-cancel-human-confirmation
review_round: 1
decision: PASS
implementation_commit: acf8bf29681b404a3c107d25ade527ad1dfe0b89
---

# GPT Review

## Decision

PASS。

本次结论只覆盖冻结的 Stage A 离线候选，不覆盖真实 Longleaf/H100 部署、可信人工授权通道、不可绕过的真实取消执行器、DII/CARE 适配、正式 slurm-workflows 0.5 发布或 main 集成。

Positive completion 已在冻结范围内观察到：

- 正常安装路径中新增了确定性的受保护取消分类核心，输出固定为 ALLOW_OWNED_UNPROTECTED / REQUIRE_FRESH_HUMAN / DENY_UNKNOWN_OR_FORBIDDEN，并且所有结果都保持 execution_authorized=false。
- 私有取消策略通过现有 local override 机制表达；protected_partitions、protected_accelerators 与站点保护取并集，公共生成摘要不暴露这些私有值。
- 目标事实不完整、集群身份不可信、策略缺失、目标集合未展开、JobId 非精确、状态/加速器/所有权未知时均 fail closed。
- 受保护目标和旧/非本轮拥有目标只能生成短、精确目标绑定的本人确认请求；长 Goal、旧竞速授权、auto_review、Hook、模型回执、scancel --interactive 等均不能成为可信确认来源。
- 状态、目标集合、策略版本变化会使确认表示失效；即使确认表示结构有效，也不产生执行权限。
- DII/CARE 真实取消入口已形成只读清单且保持未修改；Reviewer 复核时 DII 当前 main 与清单提交一致，CARE 当前 main 虽已前进，但清单中列出的六个消费者文件 blob 均未变化。
- RESULT 对 Stage A 最大声明范围进行了正确限制，没有把测试、模拟或配置存在解释成 Longleaf/H100 已部署。

冻结的 non-substitutable semantics 没有被弱化。公共源码没有硬编码 Longleaf、htzhulab 或 H100；旧竞速许可没有被升级为取消许可；UNKNOWN 没有被解释为安全；正常查询、路由、竞速资格、sticky/persistent、doctor 和普通 srun 生命周期没有被改成全局人工审批。

G1：PASS。源码和定向回归覆盖跨集群同名分区、保护分区/加速器并集、多候选分区、精确数组元素、批量精确目标集合、PENDING/RUNNING 绑定及未知事实拒绝。异构组件使用精确 JobId 语法并进入同一目标绑定；范围表达式如 4200_[1-4] 被拒绝，必须先展开。

G2：PASS。确认请求默认 retain；确认表示要求独立真人来源、验证身份、精确目标集合、动作、策略版本、状态绑定、短时效和单次使用语义，并始终保持 execution_authorized=false。

G3：按冻结 Plan 的 fail-closed 分支满足 Stage A。ER_02_ISOLATION_EVIDENCE.md 证明当前执行进程可见真实 scancel/salloc/ssh 且共享宿主 PID namespace，因此环境不满足危险模拟隔离条件。Executor 没有运行 fake/real scancel、SSH/API、批量取消、signal、tmux 或 allocation-holder 回放，并明确记录 BLOCKED_BY_ISOLATION。这里不构成真实不可绕过性 PASS，也不要求本轮补做真实 Slurm 测试。

G4：PASS。目标、状态、策略和所有权进入绑定摘要；PENDING→RUNNING、策略变化、目标集合变化均使旧确认失效；旧/不确定作业的替换路径继续 fail closed。

G5：PASS，限中央离线候选。目标 Slurm 测试、skill 安装路径、skill update、validate/audit 均通过；消费者清单独立复核有效。DII/CARE 仍明确未适配，不被冒充为完成。

G6：PASS，限声明真实性。Repository/Skill 均 NO_BUMP，未安装生产 Hook，未部署 Longleaf，未触碰真实 Slurm，未修改消费者，也未宣称正式 0.5 已发布。

全仓 unittest discovery 的 6 个失败和 1 个错误位于既有 VERSION/Marketplace/presentations/palette 基线；base..implementation diff 未修改这些对应源/测试/生成表面，定向 Slurm 与 skill 更新验证均通过，因此不构成本任务回归 blocker。AI Skills Maintainer 的 bounded plugin replay 因 WRITE_ISOLATION_NOT_ENFORCEABLE 在子执行前 fail closed，未使用 raw fallback；本 Stage A 不以该失败扩大维护或发布声明。

PROCESS PASS：YES。
PRODUCT / ARTIFACT PASS：YES，仅指冻结的 Stage A 中央离线候选及其受限 claim scope。
REAL_SLURM_MUTATION：NO。

## Blocking findings

无。

## Non-blocking notes

- G3 的真实执行不可绕过性仍未证明；这属于冻结 Plan 明确保留给后续独立授权阶段的限制，不是 Stage A 修复项。
- DII/CARE 的实际消费者适配、Longleaf 私有策略写入、可信本人审批来源、生产 Hook/执行边界、版本提升、release 与 main integration 均仍在本轮范围外。
- 全仓既有 VERSION/Marketplace/presentations/palette 基线失败应由其各自 owner 处理，不应在本任务中顺手修复。
