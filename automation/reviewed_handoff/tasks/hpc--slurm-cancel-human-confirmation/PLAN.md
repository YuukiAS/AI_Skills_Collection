---
schema: AI_BRIDGE_REVIEWED_PLAN_V2
task_key: hpc--slurm-cancel-human-confirmation
decision: PLAN_FROZEN
---

# Reviewed Handoff Plan

## Objective and value

实现已经通过独立设计审查和执行就绪审查的 Slurm Workflows v0.3 Stage A 离线候选：让通用 slurm-workflows 把“任务/竞速授权”和“取消受保护作业的本人当次授权”严格分开，并对未知目标默认拒绝；同时保留正常查询、提交、监控和计算步骤生命周期。

本轮解决的真实失败是：长 Codex Goal 曾把资源清理/竞速语义扩大成对已有 H100 分配的取消，用户并未针对该作业单独同意。Stage A 只把这一安全语义落实到中央 Skill 的确定性决策、配置接口和离线回归，不交付 Longleaf 生产部署。

## Frozen decisions

- 权威设计与执行合同固定为 task base commit 58ee18cd3e68df77c35b314c5cf9b0e83a985423 中的四份 v0.3 文件：
  - docs/design/slurm-workflows/SLURM_WORKFLOWS_CANCEL_PROTECTION_PROPOSAL_V0_3_2026-10-13.md
  - docs/design/slurm-workflows/SLURM_WORKFLOWS_CANCEL_PROTECTION_EXECUTION_PLAN_V0_3_2026-10-13.md
  - docs/goals/hpc--slurm-cancel-human-confirmation-goal-draft-v0_3.md
  - docs/design/slurm-workflows/SLURM_WORKFLOWS_CANCEL_PROTECTION_KICKOFF_DRAFT_V0_3_2026-10-13.md
- 执行身份固定：
  - repo: YuukiAS/AI_Skills_Collection
  - branch: reviewed/hpc--slurm-cancel-human-confirmation
  - R: /overflow/htzhu/mingcheng_new/AI_Skills_Collection
  - W: /overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-cancel-human-confirmation
  Executor 不得换目录、分支或工作树。
- 产品仍是现有通用独立 Skill slurm-workflows；不得新增顶级 Slurm Plugin/Profile、后台服务、数据库、控制面或 Bridge Kit 机制。
- 公共源码不得硬编码 Longleaf、UNC、htzhulab、H100 等站点值。用户每集群 protected_partitions、个人 protected_accelerators 与站点不可覆盖禁令取并集；Longleaf htzhulab 全分区保护和个人 H100 保护是用户私有部署要求，不进入公共常量。
- 取消判断保持三类：ALLOW_OWNED_UNPROTECTED、REQUIRE_FRESH_HUMAN、DENY_UNKNOWN_OR_FORBIDDEN。未知集群、策略、JobId、数组/批量集合、GPU 或状态不能按“不受保护”放行。
- 任务/竞速许可、历史 Goal、auto_review、Hook 返回、模型生成回执和 scancel --interactive 都不能代替本人针对当前精确目标的确认。
- 保护对象不仅是 scancel 文本，还包括等价 Slurm API、批量/数组取消，以及代理主动通过 kill、signal、tmux/session 终止导致 salloc allocation 提前释放。普通 srun 步骤自然结束不属于取消整个 allocation。
- Codex PreToolUse 只允许作为辅助提前拒绝；不得把 Hook、PATH 包装、alias、提示词或同 UID 可改写文件冒充不可绕过执行边界。
- ER-02 是危险模拟的强制前置条件：模拟取消、远端调用、Python/shell 子进程取消、批量取消、signal 或 holder 终止，只能在同一被测进程已经证明没有真实 Slurm、生产 SSH/凭据、真实远端网络、宿主 PID/holder、特权宿主控制入口和生产写挂载的隔离环境运行。仅 PATH fake、DRY_RUN 或提示词声明不算隔离。
- Stage A 严禁任何真实 sbatch/salloc/srun/scancel、mutating scontrol、真实 kill/pkill/tmux holder 终止、H100/htzhulab 操作、服务器/SSH/凭据/private override/Codex Host Policy/生产 Hook 变更、DII/CARE 写入、Bridge Kit 修改或付费操作。
- DII 和 CARE 本轮只读核查当前实际消费者，形成“必须适配 / 必须停用 / 历史参考”清单；不修改消费者仓库。
- 维护跟踪保持现状：新 skill TODO 已记录；独立 Issue 仍等待可真实调用的 Clear Writing 入口，不复用已关闭 #96，不因 Stage A 自动标记 Project DONE。
- 本轮版本决定：Repository bump decision = NONE；slurm-workflows = NO_BUMP；中央 Plugins 全部 NO_BUMP。Stage A 不改 VERSION、正式 Skill 版本或正式发布 README。

## Positive completion

Stage A 的正向完成必须同时具备以下同一候选结果：

1. 现有 slurm-workflows 正常入口中存在一个通用、确定性的受保护取消决策核心，能消费站点身份、用户私有保护策略、精确作业/集合事实和本轮所有权，并得到上述三类决定；默认未知拒绝。
2. 受保护目标只产生简短、目标绑定的本人确认表示，不产生模型可自行伪造为“已同意”的长期回执；没有可信本人来源时不构建真实可执行取消能力。
3. 隔离环境中的确定性/模拟回归覆盖已批准的代表性直接与间接取消失败模式；ER-02 证明不足时对应危险回放不运行，并明确写成 BLOCKED_BY_ISOLATION，不得伪造 G3 PASS。
4. 既有路由、竞速资格判断、sticky resource、persistent capacity、站点上下文、正常只读查询、合法提交语义与普通 srun 生命周期无回归。
5. DII/CARE 当前可达的取消消费者形成可追溯只读清单，后续适配责任明确，但没有消费者生产修改。
6. RESULT.md 清楚区分离线算法/隔离模拟证据、尚未证明的真实权限隔离、未部署的 Longleaf 状态以及下一步所需最小授权。

Stage A 允许声明的最大范围是：中央 slurm-workflows 具有待独立 Reviewer 审核的通用离线取消保护候选，并且在已证明隔离的测试范围内 fail closed。不得声明 Longleaf/H100 强制保护已经上线、真实用户审批通道已经部署、DII/CARE 已适配或正式 0.5 已发布。

测试、文件存在、CI、Hook 配置或模拟 PASS 单独都不能构成上述完成。

## Non-substitutable semantics

- “本人当次确认”不可被长 Goal、历史竞速 opt-in、自动审批、模型自签名文本或 Hook 决定替代。
- 用户按服务器指定保护分区与个人加速器保护必须取并集；不能把分区保护缩成只保护某种 GPU，也不能把个人 H100 保护缩成只在某个分区生效。
- Longleaf htzhulab 无论实际 GPU 型号都需要本人确认；个人 H100 无论在哪个分区都需要本人确认；实现必须通过私有策略表达，不能写死公共 Skill。
- 真实目标不明时必须拒绝，不能把 UNKNOWN 解释为安全。
- 旧作业或非本轮拥有作业不能因“不在保护分区”自动获得代理取消权。
- 批量/数组/过滤器必须先展开真实受影响集合；一项未知或受保护就不能自动取消整批。
- PENDING→RUNNING、目标集合变化或策略版本变化会使此前确认失效。
- 危险模拟隔离是运行前事实门，不能通过 fake PATH、DRY_RUN、测试特判或换命令形式绕过。
- 普通科研能力必须继续低打扰；不得把修复扩大成所有命令人工审批或静默改变 GPU、分区或科学预算。
- Stage A 不允许真实 Slurm mutation，也不能用现有 H100 JobId 做任何测试。

## Implementation scope

允许修改范围仅限当前 reviewed branch/W 内与本 Stage A 直接相关的 AI_Skills_Collection 文件，优先复用现有结构：

- skills/tools/hpc/slurm-workflows/SKILL.md
- skills/tools/hpc/slurm-workflows/scripts/slurm_routing.py
- tests/test_slurm_workflows.py
- 现有 local override / site-context 的解析、模板、文档或生成层；若新增字段，必须沿用现有本地配置机制，不创建第二套 registry/state store
- 如确有必要，可在现有 skill/package 内增加小型纯决策/模拟辅助文件；不得新增 daemon/service/database
- 可选 Hook 只能作为现有能力的辅助分发/拒绝层，Stage A 不安装生产 Hook
- results/hpc--slurm-cancel-human-confirmation/ 下的 RESULT、测试/隔离证据和消费者只读清单

实现前先最小核查现有配置/生成入口，避免重复架构。若发现必须新增跨仓库控制面、远端身份、服务器权限或 Bridge Kit 能力，停止并转 Planner，不自行扩项。

DII/CARE 本轮仅允许 GitHub/源码只读；消费者修改留到后续独立授权阶段。

## Acceptance and regression gates

维持批准的 G1–G6，不增不减：

- G1 配置与作业识别：覆盖两个站点同名分区、混合 GPU、PENDING/RUNNING、多候选 partition、数组/异构/批量集合、私有保护并集和缺信息拒绝。只凭分区名猜 H100、缺策略放行均失败；正常只读能力保持。
- G2 本人授权：长 Goal、旧竞速、auto_review、Hook ask、伪造回执、超时/失联不得批准；短请求绑定精确目标，状态/策略/集合改变即失效；没有取消动作时不增加打扰。
- G3 执行不可绕过性：Stage A 只允许在 ER-02 已证明的隔离环境中回放 direct/absolute path/Python/shell/SSH fake endpoint/API/数组批量/holder 信号和 Hook 故障。隔离不足则禁止运行并记录 BLOCKED_BY_ISOLATION。Stage A 的模拟 PASS 不等于真实权限隔离 PASS。
- G4 状态与 JobId 安全：执行前复验目标集合、状态、数组/依赖；PENDING→RUNNING、旧 JobId、取消结果未知、旧作业未终止时不得误取消、重提或双跑。
- G5 既有能力与消费者：中央候选不得破坏 route/race/sticky/persistent/doctor/只读/合法提交/自然 srun；只读核查 DII/CARE 当前入口并暴露尚未适配的真实缺口。只测 helper 或遗漏旧可达 watcher均失败。
- G6 发布真实性：RESULT.md 和 Reviewer 必须如实限制 claim。Stage A 是 central offline candidate；真实授权来源、Longleaf 权限隔离、生产安装和消费者适配尚未完成时，不能发布“强制保护已上线”或正式 0.5 完成声明。

回归必须包括原事故语义“长 Goal 偷藏取消”、旧竞速授权、H100 跨分区、htzhulab 中非 H100、未知 GPU、批量扩大目标、PENDING→RUNNING、旧任务作业、Python/shell/SSH 间接取消、Hook 失效、holder 信号，以及正常 srun 步骤结束不被误拦。

Reviewer 必须读取冻结 PLAN、当前 diff、真实测试/隔离证据、RESULT.md 和消费者清单；不得用 Executor 自报、CI 或模拟数量代替能力判断。

## Natural-language usage / routing expectations

未来正常用户意图示例：

- “取消我刚才这个普通测试作业”：Skill 先核实集群、精确目标、本轮所有权和保护集合；只有确定属于本轮且不受保护时才可能自动取消。
- “这个排了一周的作业别动”：命中保护或旧作业语义时只能给出一条短确认请求，默认保留。
- “我在服务器 A 保护 premium 分区，在服务器 B 不保护它”：按集群分别读取私有配置，不把同名分区跨集群混用。
- Longleaf 实际部署时，用户私有策略会表达 htzhulab 全分区保护和个人 H100 保护；Stage A 不写入该生产配置，也不声称已经生效。

用户不需要重新阅读长 Goal 来寻找取消命令；真正的受保护取消必须单独出现为当前目标的短本人确认。

## Out of scope

- 任何真实 Slurm 提交、取消、释放、重排、mutation 或现有 H100/htzhulab 操作
- Longleaf 或其他服务器生产安装、真实 private override 写入、SSH/凭据/权限调整、真实受限身份部署
- 生产 Codex Hook/Host Policy 修改或部署
- DII/CARE 代码修改、安装、发布或真实竞速清理
- Bridge Kit 修改、Reviewed Handoff 架构调整或新增 Planner/Reviewer/控制层
- 新 daemon、service、database、registry 或长期资源控制面
- 付费外部模型/评审
- Repository/Skill 正式版本提升、正式 release、main integration
- 把 pending Clear Writing 的维护 Issue 当作本 Stage A 的完成证明
- Stage B/C 的真实权限核查、消费者适配和生产发布
