# Slurm Workflows 0.5 候选：取消保护离线实施 Goal v0.3（草案，禁止直接执行）

任务：hpc--slurm-cancel-human-confirmation
目标仓库：YuukiAS/AI_Skills_Collection
设计权威：docs/design/slurm-workflows/SLURM_WORKFLOWS_CANCEL_PROTECTION_PROPOSAL_V0_3_2026-10-13.md（设计方向已据用户转交的 Critic PASS 获批）
执行范围来源：docs/design/slurm-workflows/SLURM_WORKFLOWS_CANCEL_PROTECTION_EXECUTION_PLAN_V0_3_2026-10-13.md
文档版本：v0.3，待 execution-ready Critic 独立审核
执行分支：尚未创建；后续依审查与授权按 Reviewed Handoff 合同采用 reviewed/hpc--slurm-cancel-human-confirmation
授权状态：DRAFT_ONLY。读取此文件、设计 PASS、CI 或 Critic 审查本身均不授权启动。

## 用户结果

禁止 AI 在长提示词、历史竞速许可、自动审批或钩子失效的情况下主动取消已取得的受保护 Slurm 作业。用户逐集群指定受保护分区，并可另设个人 GPU 保护；二者取并集。Longleaf 的 htzhulab 分区所有 GPU 和用户指定 H100 无论在哪个分区都必须在取消前取得本人当次确认，但通用源码不得写死任何具体站点或 GPU。危险操作不可被确定拦截的环境必须关闭代理取消功能，不能宣称已强制安全。

## 离线 Executor 必须交付

1. 保持 slurm-workflows 为通用独立 Skill，不新增顶级 Slurm Plugin、Profile、长期服务、控制数据库或 Bridge Kit 改动。研究目前 scripts/slurm_routing.py、SKILL.md、scripts/skills.py 对站点生成/安装的正规入口，在已有结构内实现**一个确定性的取消判断核心**。明确来源、状态、站点、政策版本、作业权属和可能影响的全部目标，决策为 ALLOW_OWNED_UNPROTECTED / REQUIRE_FRESH_HUMAN / DENY_UNKNOWN_OR_FORBIDDEN。未知、历史旧作业、站点硬禁一律 fail closed。
2. 用隔离模拟调度器验证用户策略：两个集群同名分区、用户指定不同保护分区、个人加速器保护、待取消 mixed GPU 分区、PENDING GRES/TRES、RUNNING 分配、多个 partition、数组元素/父编号、批量选择器、异构目标和权限缺失；不能仅根据分区名字推断 H100。公共代码/生成参考不泄漏用户私有站点配置。
3. 将本人确认作为独立短操作表示：实际集群、精确 JobId/数组、分区/GPU、状态、取消后失去的资源/排队、保留/确认取消。只生成请求，不生成可由模型伪造的审批回执。默认保留；拒绝、超时、状态或目标范围变化不取消。无可信本人来源时不构建可直接取消的代理能力。
4. 可选加入 Codex PreToolUse 的提前 deny，用独立的离线 Codex 正常入口验证加载与已知失效模式，绝不使用不支持的 permissionDecision: ask。钩子是辅助，不得因仅测试钩子或某种命令格式通过宣称不受限 shell/SSH 已不可绕过。
5. 所有潜在执行动作保持与 pure decision 分离。阶段 A 默认不提供可用真实服务器凭据的主动 cancel 路径；未经站点权限审查不开放受保护取消或任意真实取消。测试只能调用隔离 fake Slurm/模拟持有者。所有脚本必须能在 hook 崩溃/未加载、subprocess 调 scancel 时保持“未获强制能力”的真实报告。
6. 只读检查 DII 当前 AGENTS/安装技能与 CARE 正式 slurm-routing-partition 和直接 scancel 脚本。核实哪些是当前正常使用消费者，编制必须改、必须停用、仅历史参考三类列表；使中央测试覆盖代表性的直接 Python/shell/SSH 及 salloc holder 负例。不修改 DII/CARE 代码，不提交消费者正式发布。
7. 确保已有 route、竞速、sticky 资源、persistent capacity、站点隔离、doctor、正常安装、只读查询、已获授权普通提交与自然 srun 步骤完成不退化；不全局打开人工审核，不静默改 GPU、分区或科学训练预算。
8. 将 G1–G6 六项能力门按 Plan 逐项记录测试输入、实际入口、明确失败、应保持场景和**同一最终候选**的直接证据。分开标记离线算法、模拟执行、真实权限隔离、实际消费者与正式发布身份，不得拼接成伪 PASS。
9. 产出版本决策、受影响文件、原失败回放、负例、合法场景、不应改变范围、部署前无法证明事项及安全停止路径的完整 RESULT。任何准备提升版本或发布的动作只在所有必需验收和后续授权有效时进行；本阶段不修改 VERSION、正式 Skill 版本、README 发布版本或对外声称生产防护生效。

## 明确禁止

- 不运行真实 sbatch、salloc、srun、scancel、mutating scontrol、远端 kill/pkill/killall、tmux kill-session、主动终止任何 allocation holder。
- 不创建、取消、释放、重排、刷新用户任何真实作业；尤其不接触 H100 和 Longleaf htzhulab allocation。
- 不修改服务器/Slurm、真实站点 private overrides、SSH keys/authorized_keys、凭据、Codex 主机全局设置、正式钩子安装、BWG/隧道或 Bridge Kit。
- 不修改 DII/CARE 正式源码或消费环境；不部署、不进行真站点危险探针、不启动付费实验、不偷偷新增 daemon/数据库/跨仓库维护入口。
- 不绕过 shell/SSH 限制，不将自动审批、任务启动授权或长 Goal 当作作业取消授权。
- 不创建或复用已关闭的 #96 作为本轮发布证明，不擅自将 Project 改为 DONE。

## 验收及停止条件

G1 正确识别站点/目标/保护范围；G2 人工授权不可冒充；G3 真实强制执行边界的证据缺失时主动禁用并准确标记 NOT_VERIFIED；G4 取消重检防止 PENDING 转 RUNNING 等误伤；G5 已有能力与 DII/CARE 必需适配证据缺口不被掩盖；G6 正式安装和发布证据不得伪造。离线阶段只允许证明其中可在模拟环境验证的子集。

若发现共享同一 UID 的任意 shell、备用 SSH 认证、Slurm API 或持有者终止仍可以绕过，停止强制发布路线并记录真实缺口，不通过给 PATH 增加包装器冒充解决。缺失站点证据不阻碍安全离线代码研发，但不得让 Codex 顺势部署、自动关闭 Issue 或安排新 GPU job。

## 交接与最终产物

在目标任务工作树内提交所有正式变更及可复现离线测试，生成 task 结果、manifest、实际使用的文件路径/源码身份、消费者待适配清单及明确下一轮审核对象。独立 Reviewer 能直接看源代码、真正执行回放、完整日志和失败证据。未经后续 Critic/用户许可不得集成、对外发布或触碰生产。Central implementation complete 后仍须实际适配 DII/CARE 并按 AI Skills Maintenance Board 才能 DONE。

当前维护事项仍待由具有真实 Clear Writing 入口的维护者创建独立 Issue 并关联技能 TODO；无法创建不得伪造 Issue ID 或要求用户手工维护。

最终交付必须明确答复：哪些保护只在模拟环境成立、哪些真实服务器尚未隔离、如何在没有取消权限时继续正常科研、下一步仅需要哪个有界授权。绝不能把模拟 PASS 写成 Longleaf H100 安全已启用。
