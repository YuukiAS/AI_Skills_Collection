# Slurm Workflows：通用作业取消保护正式设计提案 v0.3

- 日期：2026-10-13
- 角色：AI Research Stack 独立 Planner；等待另一线程 Critic 审查
- 目标：YuukiAS/AI_Skills_Collection，当前 main 基线 34e47fe6d0dc06d57ee1e6e37c0ff0f2fdfefc1b
- 目标对象：skills/tools/hpc/slurm-workflows/，现行独立 Skill 0.4；下一个候选 0.5（不是已获批准的版本）
- 任务标识：hpc--slurm-cancel-human-confirmation
- 权限：设计文档修订，无生产实现、无 Codex Goal/Kickoff、无服务器配置变更、无 Slurm 写操作
- 审查前状态：DESIGN_ONLY / CRITIC_PENDING / EXECUTION_NOT_AUTHORIZED

## 1. 最重要的用户结果

用户不负责审核长提示词里是否藏有会取消几天甚至一周才取得的计算作业的命令。任务/竞速/提交授权，不包含受保护作业的取消授权。用户在每个服务器自主指定受保护分区；还可选择跨服务器保护 GPU 型号。本次用户已明确表达个人保护要求：任何 H100 作业被代理主动取消或主动释放前必须取得本人针对该目标的二次同意。这是用户级偏好，必须在经过本人确认的本地策略中落实；不能写死在公共 Skill。

正常使用时，查询、日志查看、可接受的提交和监控不应反复询问；只有将要取消受保护作业时，给用户一张简短且不可藏在长 Goal 中的独立请求。当前没有可信本人审批通道，或无法保证代理执行权限受控时：不允许代理执行取消，保留作业并提供用户自行执行的短指令。不得将提示词、钩子已配置、自动审核同意、模拟测试通过或技能被加载冒充强制安全。

## 2. 已核实来源和 v0.2 的真实缺口

当前中央 Skill 0.4 的 SKILL.md 允许排队替换与双路竞速输家取消；slurm_routing.py 的 widening_plan、bounded_duplicate_race_decision、bounded_replacement_decision 只返回决策，不是全部外部命令的强制拦截器。DII 的 AGENTS.md 已批准特定 H100/A100 竞速，并写有赢家运行时取消另一作业的行为；这不是新取消的本人授权。CARE 的 slurm-routing-partition 和若干实际 Python 监控脚本可直接调用 scancel，绕过中央 Skill 的调用纪律。

Slurm 官方 scancel 文档允许作业编号、数组、作业步骤及筛选条件匹配多作业；混合 GPU 分区不等于固定 GPU 型号。salloc 文档明确指出控制程序结束会释放分配、SIGHUP 可提前释放。必须按“本次动作真正影响哪些作业/分配”而非只扫描 scancel 文本判断。

OpenAI 现行 Codex Hooks 文档确认 PreToolUse 在受支持的工具调用前可以 deny，但 permissionDecision: ask 尚未实现，并且不支持的字段可能令钩子失败后仍继续执行。工具覆盖存在特例；钩子由可信部署加载，不会因普通 Skill 安装就成为不可绕过的安全边界。因此 v0.2 关于“最强安全”的措辞只能升级为可验证执行条件，不能作为既成实现能力。

仓库 Issue #96 实时状态为 CLOSED / DONE，覆盖 0.4 竞速许可和 DII 适配；中央 TODO 仍留有“#96 open”等过时措辞。不能重开 #96 冒充 0.5 取消防护任务已完成。此轮应建立独立维护跟踪（按现有看板规则，且用户可读文本先经 Clear Writing），不自动重写已完成历史记录。

先前 v0.2 存在当前聊天附件，但未提交到 GitHub；上一位 Critic 不能访问全文，其 REVISE 是“缺可审对象 + 已辨识风险”，不是全文审过 v0.2 后给出的正式否决。本文件是替代 v0.2 的完整新版本，不要求 Critic 另外取得 v0.2。

## 3. 保护对象、默认权限与信任模型

定义一次“破坏性释放”为由代理主动发起、足以使 Slurm 作业终止/被撤销，或使用户持有的分配非自然提前释放的行为。包括整个作业/数组/组件取消、会造成作业或控制进程终止的信号、终止 salloc 持有进程或 tmux/session、以及经其他命令或脚本间接产生的同等结果。普通独立 srun 步骤自然结束、Slurm 时间限制自然到期、调度器自身抢占或非代理人类操作不视为代理主动取消；不得为了“保护”阻塞每次步骤正常退出。

区分三层：

1. 决策层（通用 Skill 及纯函数）：读取可信作业事实和用户策略，得出 ALLOW_THIS_OWNED_UNPROTECTED_CANCEL / REQUIRE_FRESH_HUMAN / DENY_UNKNOWN_OR_FORBIDDEN。此层不能自行声称阻止 shell 执行。
2. 辅助早期拦截（Codex PreToolUse）：在正常工具入口对明显危险命令发出有效 deny，为用户提供早期警告和阻止。它不是强制执行边界；需验证已加载、可信、匹配覆盖，且其失败、超时、意外格式不会被当作成功阻断。
3. 可信执行边界（必要条件）：限制代理实际能发出的 Slurm 取消与间接释放动作，使得只有经过本人独立授权的执行入口能对受保护目标生效。必须在真实部署证明代理无法从同一身份的任意 shell、SSH、Python、Slurm API 或 holder 进程控制绕过。若做不到，代理取消路径一律不启用，且不得宣传“强制二次确认已生效”。

当代理和用户共用同一不受限 Unix 账户、且代理可以任意运行 shell/SSH/Python 时，纯 Python 决策器、PATH 包装、shell alias、钩子、脚本注释或文件权限通常都不足以提供不可绕过保证；即使要求代理“不调用”，也只是行为约束。不得把同一 UID 下由模型可改写的配置文件或模型可生成的审批回执视为可信授权。

### 3.1 可交付的两种运行方式

- 安全人工方式（默认可用方案，需显式说明限制）：任何 Slurm 取消和主动释放都不属于代理获准执行动作；Skill 生成一条简短请求，由用户在独立于代理的终端亲自完成。Codex 钩子/本地执行规则尽可能提前 deny，并对已知运行脚本增加取消调用守卫。但只要模型仍拥有未经隔离的同账户任意命令权限，这种模式仍不能宣称“技术上无法绕过”，需在正式验收中如实披露并拒绝强制保护的发布宣称。
- 受控代理方式（仅条件满足后开启）：基于目标站点真实可用且经批准的限制执行身份、远端受限入口或等效权限隔离，让代理的运行环境不能直接取消受保护作业，也不能修改授权来源。唯一可取消的受控入口按实时事实判断并消耗本人一次性许可。优先复用站点现成权限/远端接口，不默认发明长期服务、数据库或守护进程；若需站点管理员支持或修改凭据/SSH/Slurm 权限，先独立授权和 Critic 审核，不在本轮暗中实施。

两种方式均不能仅靠 PreToolUse approve/deny 的文本证明受控；同一部署是否满足强制条件由真实入口验收决定。目标安全承诺是“不会在模型可独立控制的路径下取消受保护作业”，而非“模型会记得先问”。

## 4. 每台服务器独立选择保护范围

用户保护策略由用户控制的本地私有配置决定，不在中央源码硬编码 UNC、CUHK、Longleaf、htzhulab、H100 等 site/GPU 常量。用户可以逐集群指定 protected_partitions，并另外设置 protected_accelerators（个人可选跨站点 GPU 型号保护）。用户本轮要求的 H100 应在受控配置首次部署时转成用户确认的个人规则；现在没有现场配置写入证据，不得称已启用。

可信执行端根据 Slurm 当前作业和站点元数据识别集群，不能仅相信提示词里的 hostname/site_id。必须处理同名分区在两个不同集群、同一分区混合 GPU、job 位于候选多分区、作业数组元素、异构作业、作业 steps、多集群以及筛选器批量命中。RUNNING 查已分配 GPU 与真实分区；PENDING 查请求的 GRES/TRES/分区候选；若类型仍不能证实且可能命中保护，默认拒绝代理取消。不得根据 htzhulab 名字猜测 H100，也不得因看不到 GPU 字段推断为非 H100。

保护判定取并集：个人 GPU 保护、当前站点用户指定分区、站点/管理员硬性限制；硬性禁止即使用户确认也不能被覆盖。缺配置、未确认保护范围、未知集群/作业/GPU/批量覆盖、策略版本不明或读取失败时，拒绝代理取消。显式的空保护列表与缺失配置不同；即使站点列表为空，个人 H100 保护仍生效。普通“任务获批”“竞速获批”不会修改这个集合。

策略更改本身必须由本人在可信通道确认，改变某站点策略不能顺手清空别的站点；执行身份无法改写策略才可能声称具有强制性。保留必要的策略版本和站点标识供每次决策绑定；不把私人用户名、账号、节点或策略内容提交到公共库。

## 5. 作业权属与取消决策

旧作业优先：在当前运行任务之前已存在的作业、别的任务/用户/项目管理的作业、当前运行未明确创建/拥有生命周期的作业，不会因为“非受保护分区”就自动获得取消权；需本次针对目标的明示授权或用户自行操作。即使是本轮创建的作业，命中受保护范围也必须重新取得本次本人同意。

正常自动取消仅限于同时满足：确认为同一受控执行轮次创建并具有取消职责；可信元数据已解析为确定的具体目标；该目标不命中任何保护规则/站点禁止；取消符合已有安全替换合同（例如仅 PENDING 镜像）；受控执行入口已通过绕过回归。否则返回 REQUIRE_FRESH_HUMAN 或 DENY；不允许把状态 UNKNOWN 解析成安全的“非保护”。

任何批量过滤、数组父编号、多目标选择器、作业名称/分区/用户过滤，都必须先展开所有会被影响的精确作业，再分别检查；一项不明或需要保护时禁止整批代理取消。允许人工独立决定，但不允许由一次确认暗中扩大选择器所指的集合。对真实作业使用 Slurm 只读接口进行核对；没有权限或证据不能为了推进而猜测。

## 6. 二次人工确认：仅一条短请求，不藏在 Goal

“二次确认”指原有任务许可之外的、取消前的本人当次确认，不代表需要两轮新的长对话。用户只看到：集群、精确 JobId（必要时数组元素/组件）、分区/GPU、当前状态、取消会失去的资源或排队位置，以及两个动作：保留 / 确认取消这个作业。不含论文说明、执行计划或大段 shell。默认保留；拒绝、超时、没有响应、连接失效均不执行。

人工确认不能由模型代答、Codex 自动审查、普通 PermissionRequest 交由 auto_review 批准、长 Goal 的确认语句、此前 standing opt-in、scancel --interactive 的标准输入等替代。现有 PreToolUse 不支持 permissionDecision: ask；不能伪造为 Codex 原生人类弹窗已可用。没有能够验证真人来源的审批通道时，不由代理执行，只交付人类终端命令。

受控代理方式如实际具备独立审批源：许可要精确绑定站点、JobId/数组元素集合、取消动作、保护匹配、用户本人身份、策略版本、实时状态约束和短时效；只能消费一次，不能保存为长期“以后均同意”的授权。执行前重新核验同一真实目标；状态从 PENDING 变 RUNNING、目标新增、策略更改或身份不符即许可失效。具备站点验证的状态条件时使用 state-conditioned cancellation；否则不能可靠约束竞态时转为人工执行。确认记录不能由代理写入同一共享目录冒充本人。

## 7. 对钩子、脚本和交互式会话的落地合同

- Codex PreToolUse 只做提前阻断/可见反馈：验证真实 Codex 版本/安装/信任状态；处理 deny 与损坏 JSON、超时、抛异常、未启动、未加载、不同工具路径的行为。禁止使用 ask 作为人工确认。钩子坏了仍放行时，受控取消边界必须独立阻止危险操作，不能退回“让模型遵守规定”。
- 统一纯决策入口可放在现有 slurm-workflows 脚本族中，供钩子、受控取消执行器、消费者脚本使用相同规则；不自动变成新的后台服务。只读计划/检查与真正执行明确分层，不能让一个 helper 的 allow 布尔值冒充已经获得操作授权。
- 既有 CARE Python subprocess scancel、shell 包装、远端 ssh -c、直接 /usr/bin/scancel、批量选择器和 Slurm API 不仅需要源码适配，还要用真实执行边界中的隔离模拟路径验证，避免脚本内部发出 scancel 时被钩子漏检。
- 对 salloc holder 的保护采用“受保护持有进程的所有权/生命周期边界”：Codex 的退出、SSH 掉线、后台清理、kill/pkill、tmux kill-session、向 holder 发 SIGHUP、结束持有命令，不得释放已获取的受保护 allocation。普通 srun 步骤结束不等于关闭 salloc。若当前环境的 holder 本身依赖代理终端，则不能宣称安全，必须保留运行、禁止代理终止，待获批准的独立持有方式再改。
- 改提示词、脚本或项目规则只能提高正常路径遵守程度；不允许将其单独视为真实权限隔离。任何未受控旧脚本如果仍可在生产身份运行并取消受保护作业，则强制保护验收失败；不得靠仅测试新封装器绕开。

## 8. 不应被破坏的正常科研工作

保持只读 sinfo/squeue/sacct/scontrol show、监控、日志检查、数据处理和已经获准的普通提交。不要全局将 Codex 审批改成人工，也不要把安全问题扩张到独立的资源预算/实验方案。对未受保护、当前轮次明确持有的可替换作业，受控执行方式可按已有 state-safe 条件自动取消。

如果竞速/双路镜像一开始就依赖“赢了立即取消另一个受保护作业”，不得因历史竞速 opt-in 而自动安排这种无人值守方案。优先单作业或无需取消的安全调度方案；如果竞速已在运行，则保留已有作业、暂停自动清理并向用户说明成本与选择，不暗中干预。持续 allocation 或 H100 正在运行时，停止/重启 Codex 推理只应停止推理，不应触碰 Slurm 作业/holder。

## 9. 改动归属与消费者适配

唯一通用产品归属：AI_Skills_Collection 现有独立 slurm-workflows，不新增 Slurm Plugin、Profile、控制数据库或 Bridge Kit 通用取消服务。实施候选需包括：Skill/现有 helper 的统一决策、用户本地配置/安装说明、必要的可选钩子分发、真实执行端授权边界和测试。正式加载层与源码、生成的站点参考应保持一致，不把个人站点配置写入仓库。

主要已知消费者：DII（仓库级 0.4 技能及 standing race opt-in）和 CARE（独立旧 slurm-routing-partition Skill 与多个直接调用 scancel 的脚本）。先按当前生产入口识别仍在执行的脚本，不以仓库中每个历史 watcher 一律升级为大重构；不可验证或未适配的旧入口要显式标为不允许在受保护环境执行。历史 Issue #96 是 0.4 的完成记录，不作为新功能的完成证据。v0.5 中央完成后才按维护看板完成消费者适配并决定 DONE。

## 10. 现实替代比较与选择

A. 只改长提示词/AGENTS：不能阻止隐藏取消，拒绝。
B. 只装 PreToolUse 钩子：支持早期 deny，但 ask 不支持、失败可能继续、间接命令难以覆盖；拒绝为唯一防线，保留为辅助。
C. 全局要求每条命令人工审核：打断普通科研，并不能证明脚本内部不取消；拒绝。
D. 共享 UID 下 PATH alias/包装器：可改善正常路径，但任意 SSH/绝对路径/脚本绕过；不称强制隔离。
E. 通用决策 + 明确的个人策略 + 仅在有可信限制的取消入口里代理执行；否则人工直接取消：首选。先复用现有受限执行能力，不默认新增持久服务。站点若不允许权限隔离，承认无法提供强制代理取消能力，而不是降级成一个虚假的 PASS。

## 11. 验收能力矩阵（按同一正式候选）

| Gate | 本项独立证明的能力 | 正常入口 / 直接证据 | 失败及应保留能力 |
|---|---|---|---|
| G1 配置和作业识别 | 服务器逐个配置、个人 GPU 保护并集、未知拒绝 | 两个站点同名分区；混合 GPU；PENDING 多分区；作业数组及多目标展开，经安装后的 Skill/可信读取路径 | 只凭分区名猜 H100、缺失策略放行；只读查询仍正常 |
| G2 本人授权 | 长 Goal 不能静默批准，单个目标短确认与失效 | 真实用户受控批准路径或明确人工终端转交；测试旧竞速许可、auto_review、超时、伪造回执、PENDING→RUNNING | 模型或自动审查能批准、旧同意重复使用；无需取消时不弹窗 |
| G3 执行不可绕过性 | 实际执行端确实能挡住危险 Slurm 变更 | 真实 Codex 普通入口 + 隔离假 Slurm/受限模拟环境，覆盖直接、Python、shell、ssh、API、数组/批量与 holder 终止；验证钩子缺失、失败、超时 | 只要任一路径仍能直接取消受保护目标，强制保护 FAIL；普通科研命令仍可运行 |
| G4 Slurm 状态安全 | 不误伤排队转运行、数组/依赖和已有作业 | 实时状态快照/执行前复验及 site-confirmed 状态约束；结果未知时拒绝 | 旧 JobId 改变、用户未许可作业被取消、双份工作静默执行均 FAIL |
| G5 既有功能与消费者 | 非保护作业、普通 Slurm 生命周期可正常使用 | DII/CARE 已知生产入口与正式安装技能使用同一最终候选；受保护竞速降级为不自动启动；只读/合法提交/自有非保护取消正常 | 只测 helper、误把正常 srun 结束视为 cancel、全局人工审核、旧 watcher 漏检均 FAIL |
| G6 发布真实性 | 当前环境究竟能承诺哪个防护等级 | 真实目标安装身份、钩子信任与加载、受限权限核对、代表性的完整工作流；由独立 Reviewer 实际审风险证据 | 模拟 PASS 或钩子配置存在冒充强制能力；不能证明执行受限时标记未部署，不发布强制防护声明 |

G1 是目标真实性，G2 是人工授权来源，G3 是强制执行边界，G4 是调度竞态，G5 是正常使用兼容，G6 是正式候选身份；各自验证对象不同。先运行确定性无副作用回归，再做最终候选的正常入口演练。所有危险命令使用隔离假 Slurm、无生产认证能力的环境执行；不调用真实 sbatch/salloc/scancel，也不结束现有 tmux/SSH/H100 作业。部署验证可只读核对配置与权限；任何未来需要修改远端权限/SSH/服务的探针先另行授权。严禁用模拟脚本的 PASS 宣称真实 HPC 强制安全已上线。

## 12. 实施前置条件、停止条件和失败恢复

只有新的 Critic 对本 v0.3 的设计给 PASS，Planner 才能准备同版 Plan/Goal/Kickoff 交独立 execution-ready Critic；审查通过也不等于授权真实部署。初始实现范围以中心 Skill、测试和授权安全的演示环境为界，禁止在用户现有 H100 allocation 上测试。若不能证明实际执行隔离，保持取消能力不开放，继续普通只读/计算任务，并如实报告因同账户 shell 暴露造成的残余风险；不能为了通过验收把标准降为“钩子已安装”。

真正需要用户参与的只有：部署时首次确定每台站点的保护范围，以及每次准备取消受保护作业的独立短确认。不得让用户阅读长 Goal、通用策略全文或多次审查重复给相同授权。若需要站点管理员/额外身份、改变生产权限或费用，先获得用户对具体范围的单独授权。无该能力时仍保持已有作业，不能让 Executor 改用 kill/退出 holder 规避。

## 13. 版本、追踪和不变范围

设计文件本身无版本号提升：Repository bump decision = NONE；slurm-workflows = NO_BUMP；所有中央 Plugins = NO_BUMP；Bridge Kit = NO_CHANGE。只有正式用户可见功能完成、同一最终候选正常入口安全回归通过且独立审查后，才考虑 Skill 0.4 → 0.5、仓库按当时版本下一个补丁发布。现在 5.4.4 是事实基线，不能预先宣称 5.4.5 已发布。

新问题属于新的作业取消保护能力/事故回归，不是 Issue #96 的延续发布。跟踪应在 docs/skill-todos/slurm-workflows.md 和独立 maintenance-track Issue 建立，并在 Project 中同步真实状态；但用户可读 Issue 受 Clear Writing 实际调用要求约束，当前只读/设计修订不以虚假的 Board DONE 冒充完成。若审查线程无法操作 Project，应提供准确的待同步动作给后续有权限的维护线程，不要求用户人工维护看板。

## 14. 对 Critic 已指出问题的逐项处置

R1-01：文件不可读——将 v0.3 完整、可直接定位的文件置入 AI_Skills_Collection 的 docs/design/slurm-workflows/；Critic 不再依赖聊天附件，v0.2 不需要并读。
R1-02：只靠钩子不安全——钩子仅早期 deny；另设可信执行能力条件，且钩子失败不允许降级放行危险动作。
R1-03：技能可能不被调用、Python 内部可取消——统一决策逻辑供正式执行入口消费；强制能力以权限隔离和真实脚本回放验收，而非模型记忆。
R1-04：作业身份不能按单个分区猜——以真正 Slurm 目标、跨分区/GPU、数组和批量展开按并集判断，未知拒绝。
R1-05：确认可能被自动审核代答——本人本次短确认不通过 auto_review/ask/scancel -i；无可信本人通道则仅人工终端操作。
R1-06：间接释放交互式分配——覆盖 salloc holder、SIGHUP、tmux/SSH 生命周期，并明确正常 srun 步骤结束不视为取消。
R1-07：别过度阻塞——只对危险释放加限制，保持查询、日志、提交和正常步骤生命周期；保护竞速重新判断启动资格。
R1-08：历史状态不能误认完成——Issue #96 已关闭，0.4 消费适配历史已结束，本轮 0.5 必须单独跟踪和验收。

这些条目是 Planner 的 ACCEPT 和提案修订，不代表 Critic 已接受或关闭任一阻塞项。

## 15. 可独立定位的依据

本次仓库基线：

- https://github.com/YuukiAS/AI_Skills_Collection/blob/34e47fe6d0dc06d57ee1e6e37c0ff0f2fdfefc1b/skills/tools/hpc/slurm-workflows/SKILL.md
- https://github.com/YuukiAS/AI_Skills_Collection/blob/34e47fe6d0dc06d57ee1e6e37c0ff0f2fdfefc1b/skills/tools/hpc/slurm-workflows/scripts/slurm_routing.py
- https://github.com/YuukiAS/AI_Skills_Collection/blob/34e47fe6d0dc06d57ee1e6e37c0ff0f2fdfefc1b/tests/test_slurm_workflows.py
- https://github.com/YuukiAS/AI_Skills_Collection/blob/main/docs/workflows/PLANNER_ROLE_CONTRACT.md
- https://github.com/YuukiAS/AI_Skills_Collection/blob/main/docs/workflows/CRITIC_ROLE_CONTRACT.md
- https://github.com/YuukiAS/AI_Skills_Collection/blob/main/docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md
- https://github.com/YuukiAS/AI_Skills_Collection/blob/main/docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
- https://github.com/YuukiAS/AI_Skills_Collection/issues/96 （关闭；仅旧 0.4 范围）
- https://github.com/YuukiAS/Distributed_Imaging_Inference/blob/main/AGENTS.md
- https://github.com/YuukiAS/CARE_Challenge/blob/main/.agents/skills/slurm-routing-partition/SKILL.md
- https://github.com/YuukiAS/CARE_Challenge/blob/main/scripts/route_B_round04/watch_B1_race.py
- https://github.com/YuukiAS/CARE_Challenge/blob/main/scripts/target_domain_gap_closure/monitor_interactive_takeover.py

官方运行机制（核对 2026-10-13）：

- https://learn.chatgpt.com/docs/hooks （PreToolUse 的 deny、ask 尚不支持、钩子覆盖例外）
- https://github.com/openai/codex/blob/main/codex-rs/hooks/src/events/pre_tool_use.rs （当前解析和失败行为）
- https://slurm.schedmd.com/scancel.html （作业、数组、批量选择器、状态条件、普通交互提示不是可信用户证明）
- https://slurm.schedmd.com/salloc.html （控制程序退出和 SIGHUP 可释放分配）

**本文件不声称当前服务器已经采用任何执行防护；没有运行过真实 Slurm 修改。**
