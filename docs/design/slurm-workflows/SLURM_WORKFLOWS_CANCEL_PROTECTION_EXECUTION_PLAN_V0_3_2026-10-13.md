# Slurm 作业取消保护：v0.3 执行方案（待独立执行就绪审查）

- 任务：hpc--slurm-cancel-human-confirmation
- 目标：YuukiAS/AI_Skills_Collection，独立技能 slurm-workflows 0.4；0.5 仅为候选
- 方案依据：docs/design/slurm-workflows/SLURM_WORKFLOWS_CANCEL_PROTECTION_PROPOSAL_V0_3_2026-10-13.md，提交 a92dc4729e9c5bd2740c5d1bd967daa40f13e8d3
- 权威：用户在 2026-10-13 本次消息转述独立 Critic 已对 v0.3 设计方向 PASS；审查原文尚未归档，不能冒充正式审查文件或执行许可
- 当前状态：EXECUTION_READY_REVIEW_PENDING；EXECUTION_NOT_AUTHORIZED；REAL_SLURM_MUTATION=NO
- 冻结执行身份：R=`/overflow/htzhu/mingcheng_new/AI_Skills_Collection`；W=`/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-cancel-human-confirmation`；branch=`reviewed/hpc--slurm-cancel-human-confirmation`。只读定位已完成，实际 branch/worktree 尚未创建，仍待 execution-ready PASS + 用户短 Kickoff 授权
- 当前允许写入：本仓库 Plan、Goal 草案、Kickoff 草案及内部技能 TODO，不修改任何生产技能、服务器、真实 Slurm 状态、DII/CARE 源码

## ER-01：执行身份与工作树已完成只读定位

用户已选择并只读核实实际 Longleaf Codex 工作目录。当前事实：

- 主仓库绝对路径 R：/overflow/htzhu/mingcheng_new/AI_Skills_Collection
- Git 顶层：与 R 完全一致
- origin：https://github.com/YuukiAS/AI_Skills_Collection.git
- 只读核实时工作树：clean
- 只读核实时本地 HEAD：1c59199f88c7527f2bd853e606f20146134fda47
- 同一时刻 GitHub main：1c59199f88c7527f2bd853e606f20146134fda47
- 冻结任务键：hpc--slurm-cancel-human-confirmation
- 唯一执行分支：reviewed/hpc--slurm-cancel-human-confirmation
- Bridge Kit 按正式源码唯一派生工作树 W：/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-cancel-human-confirmation
- W：未注册、路径不存在
- 同名本地分支：不存在
- 同名 remote-tracking 分支：不存在
- 实际 ai-bridge：/users/a/e/aereinh/bin/ai-bridge
- ai-bridge --version 在该安装中不是受支持 CLI 形式并以 2 退出；这不冒充版本已确认。正式 reviewed-handoff task bootstrap --help 可读，故能力存在性只以当前正式入口及后续实际 preflight 为准。
- 旧审执行包提交 2adc1be81ed6e2eada398c07397dc31a8723f01c 可读，四份 v0.3 文件与该提交一致。
- 这轮定位未执行写操作、Git 同步、bootstrap、测试或任何 Slurm 操作。

因此 ER-01 的“路径未知/冲突未知”已经关闭。**这仍不等于当前已经授权创建分支、工作树或开始编码。** 当前 Plan 的执行身份冻结为上述 R/W/branch，任何替换目录、替换分支、同名路径占用或 repo/origin 漂移都必须 fail closed。

正式初始化若以后经 execution-ready Critic PASS 且用户发送批准后的短 Kickoff，只允许以下受限顺序：

1. 在 R 中执行安全同步 git fetch origin main，读取 refs/remotes/origin/main。Kickoff 必须绑定 Critic 报告中的准确 APPROVED_COMMIT；若同步后的 origin/main != APPROVED_COMMIT，立即停止，不 bootstrap、不采用更新后的 main。这样避免在批准后悄悄吸收新的主分支变化。
2. 再次只读确认 R、origin、clean 状态、W 未占用、同名 local/remote branch 不存在、四份批准文件与 APPROVED_COMMIT 一致。任何不一致停止。
3. 仅调用当前正式 Bridge 入口：
   ai-bridge reviewed-handoff task bootstrap --task-key hpc--slurm-cancel-human-confirmation --expected-repo YuukiAS/AI_Skills_Collection --expected-base-commit "$APPROVED_COMMIT" --objective "Implement the approved v0.3 Slurm protected-cancellation Stage A only; no real Slurm or remote deployment."
   该命令只能由 Bridge 自己派生固定 branch/W；不得手工 git branch、git worktree add、换目录或修改 Git 配置作为 fallback。
4. 核对 bootstrap 只创建目标 branch、W 以及首份 automation/reviewed_handoff/tasks/hpc--slurm-cancel-human-confirmation/REQUEST.md / CURRENT.json。首次提交只能包含这两份元数据。
5. 首次远端分支创建只能走：
   ai-bridge reviewed-handoff task publish-first --task-key hpc--slurm-cancel-human-confirmation --expected-repo YuukiAS/AI_Skills_Collection
   不允许 raw git push -u、force、其它 remote/branch 或夹带源码。首次发布成功并回读远端身份后，后续阶段 A 普通非强制同分支发布只能使用 Host Policy 已批准的同分支受限入口。
6. **bootstrap/publish-first 不是代码实现完成条件。** 它们只建立已批准任务身份。随后 Stage A 仅在同一个 W/branch 内执行，且仍受 ER-02 的危险模拟隔离门、G1–G6 以及所有真实 Slurm/远端禁止项约束。

Critic 若批准本轮执行包，应把 APPROVED_COMMIT 精确绑定到本轮最终包提交；用户实际发送 approved Kickoff 才授权上述 Git 初始化 + Stage A 离线实现。设计 PASS、此前只读定位 PASS、Critic 文本本身均不自动授权执行。

## ER-02：危险离线模拟前的系统隔离先决条件（G3 已有验收，不新增 Gate）

任何会模拟 scancel、远端调用、Python/shell 子进程取消、作业数组/批量取消、模拟 signal、终止 salloc/tmux holder 的回放，必须**先对实际将运行被测子进程的同一个执行沙箱**完成可审计的隔离证明，不能只检查 PATH、替换模拟命令、设置 DRY_RUN、引用代码注释或根据提示词承诺。危险回放绝不在普通生产 UID/宿主 shell 中直接运行。

隔离应复用实际可验证的成熟容器、隔离虚拟机或可信离线执行器，不创建新服务。预检必须证明被测进程：没有真实 Slurm 控制器、调度器 API、MUNGE 或 Slurm Unix socket；没有任何生产 SSH 私钥、SSH agent、凭据/令牌、认证环境变量或挂载；没有连接真实服务器的网络出口、主机网络、代理、隧道或继承的可用通信 socket；没有宿主 PID/信号权限、主机进程空间或操作现有 allocation holder 的途径；没有特权模式、宿主控制 socket、宿主敏感目录/GPU/生产作业路径的可写挂载。检查实际隔离配置、挂载、网络/进程命名空间、有效权限及实际执行子进程身份；只能在隔离环境内建立假 Slurm、假远端接口和自建的模拟 holder。既不向生产地址作危险探针，也不调用宿主真实 scancel/kill。

**先取证再运行**：证据完整、范围与即将执行的子进程一致时才允许对应危险回放。任何隔离功能缺失、不确定或执行子进程可能继承真实认证/网络/PID 权限，就停止全部涉及取消、模拟远端、信号或 holder 的危险回放；不通过更换命令格式、移除失败检查、直接改宿主 PATH 或在服务器上“简单试一下”继续。仍可开展不触发模拟取消/信号/网络子进程的纯函数与静态检查，记录 G3 模拟执行部分因隔离不足而未验收，返回 Planner/独立 Critic。G1—G6 六项含义、原始验收标准及 DII/CARE 范围均不改；隔离沙箱 PASS 也不构成真实 Longleaf 执行权限隔离或真实发布 PASS。

## 一、最重要的交付意义

用户不应通过逐行阅读长 Goal 来发现其中隐藏的取消 H100 命令。受保护作业取消必须由用户本人就当前精确作业再次明确同意；旧任务、历史竞速授权及 Codex 自动审核均不是人类确认。本次设计保持 v0.3，不重新发明架构。

必须区分两种部署承诺：

1. 人工模式：技能拒绝代理自行取消，基于可信只读事实产生独立简短请求，让用户从代理无法操纵的终端亲自执行。可以验收正常使用流程、识别和指令层防护；若代理仍拥有同一 Unix 身份下任意 shell/SSH/Python/API 权限，则不得自称不可绕过。
2. 受控代理模式：仅当经真实部署验证，代理的所有有效执行路径均无法绕过受控取消入口、无法读取或改写本人确认来源，且不能通过持有者信号释放交互式分配时，才允许它凭一次性本人许可取消受保护作业。不能证明则禁用，不以钩子或模拟测试宣称强制安全。

现行 Bridge Kit 主机规范使用 approvals_reviewer = "auto_review"；其命令审批不足以证明用户本人的同意。远程基础设施存在过 SSH 强制命令，但它只证明某些连接已受限，不证明 Longleaf 的 Slurm 同 UID 权限受控。当前没有目标机隔离的真实证据。

## 二、实施边界比较与选择

- 只添加技能说明或长提示词：不能强制拦截，拒绝。
- 仅使用 Codex PreToolUse：可提前 deny，但 permissionDecision: "ask" 尚不支持；钩子失败或未加载可能继续，脚本内部间接取消也可能不经钩子。仅作为早期辅助拦截。
- 全局对所有命令人工审核：阻碍日常查询、训练和正常开发，且自动审核不等于本人，拒绝。
- 同一 Unix UID 的 PATH 包装、alias、仅包装 scancel：绝对路径、SSH、Python 子进程、API、同 UID 信号/持有者能绕过，不构成强制防线。
- 现有受限远端入口、限制身份或站点管理员支持的权限隔离：可能可信，但必须逐一核查真实 UID、其他密钥/密码、PTY/转发、计算节点 shell、允许提交脚本的命令权、Slurm API、同 UID 持有者进程。站点支持与否未知，不能预设。
- 用户独立终端亲自取消：默认可用退路，但在不受限代理凭据仍存在时只属于行为层防护，不能宣称硬隔离。

选择：在原有 slurm-workflows 内实现单一纯取消决策及短确认建议，可选钩子为辅助；受控取消模式必须有站点级独立证据才能开启。若必须新增服务、修改远端身份或存在不可消除的绕过，停止并重新取得 Critic 与用户批准。不新增顶级 Skill/Plugin/数据库/长期控制进程，不改 Bridge Kit。

## 三、固定产品行为

通用源码不写死 Longleaf、UNC、htzhulab、H100 或任何分区。每台服务器的真实集群身份必须由可信调度器数据及用户私有、经本人确认的配置识别。保护取并集：站点强制禁止规则、用户指定 protected_partitions、个人 protected_accelerators。用户已经指定 Longleaf 的 htzhulab 分区无论 GPU 型号都受保护，个人 H100 也始终需要本人确认；两项规则是待真实安装时用户核准的个人配置，尚未部署，不可说已经生效。

检查目标不能只看一个 scancel 字符串。必须覆盖精确 JobId、数组父编号/元素、异构作业、批量选择器、排队多分区候选、请求 GRES/TRES、运行时实际分配 GPU 和分区、Slurm 状态与本轮生命周期所有权。混合分区不能凭分区名猜 H100。缺失策略、集群身份、GPU、目标范围、数组展开或作业状态时一律不允许代理取消；明确配置空保护集合与没有配置不同。

唯一决策可为：
- ALLOW_OWNED_UNPROTECTED：本轮实际拥有、状态可安全替换、事实完整且无保护/禁令、真实执行路径获授权的非保护作业。
- REQUIRE_FRESH_HUMAN：保护命中或用户/其他任务拥有的既有作业，短独立确认；无可信审批渠道则仅交用户本人执行。
- DENY_UNKNOWN_OR_FORBIDDEN：站点禁止、身份/状态/策略/受影响目标不确定、未经核实的权限边界，直接拒绝。

本人确认只显示真实集群、JobId/元素、当前状态、分区/GPU、资源或排队位置损失、保留与确认取消两个操作。默认保留，超时、拒绝、失联不执行。可信受控模式以后若经许可启用，授权必须由代理不可写来源产生，一次消费，绑定站点、目标集合、动作、策略版本、状态约束和短时效；执行前复验目标，PENDING 转 RUNNING 或集合改变就作废。不能将旧 Goal、auto_review、scancel --interactive 的标准输入或模型生成确认视作本人。

取消包含 scancel、变相 Slurm API、批量取消以及代理主动 kill/signal/tmux 退出使 salloc holder 提前释放的情形。普通 srun 计算步骤自然完成、已授权提交、只读 sinfo/squeue/sacct/scontrol show、日志与监控不能无端被阻断。若历史竞速要求自动取消受保护输家，无人值守竞速不得启动；已存在作业保留，不用取消“清理”或静默改科学预算。

## 四、批准后才允许执行的范围与阶段

阶段 A（须先完成 ER-01 的真实路径冻结与本人批准，危险模拟须完成 ER-02 的同一进程隔离证明）：在经审查和授权的本仓库任务工作树中，复用 scripts/slurm_routing.py 的既有能力，增加唯一确定性判断与本地保护策略解析、只读目标解析、短确认展示、故障默认拒绝以及可选前置钩子；严格分离判定与实际执行。危险动作全部使用隔离假 Slurm、无生产凭据模拟进程。实现完整负例及正常使用回归，记录安装/权限未证实部分，停止在离线产物和独立实现复核前。不调用真实 sbatch/salloc/srun/scancel、mutating scontrol、kill、tmux 终止、真实 SSH/密钥或服务器部署。

阶段 B（不在当前 Kickoff 授权内）：在新的 bounded 只读取证批准后，核对每个目标环境的真实 Codex 版本、钩子信任/加载、Slurm 账号、备用认证和 SSH 入口、计算节点权限、interactive holder 归属与私有策略写权限；无法证明硬隔离则不启动代理取消。任何远端凭据、权限、钩子安装、真实危险探针须单独 Critic 与用户许可；不能从 A 自动继续。

阶段 C（不在当前 Kickoff 授权内）：中央候选经独立审查并具备发布资格后，按独立批准的消费者适配包修改 DII 的项目级竞速许可用法及实际安装技能、CARE 的 slurm-routing-partition 及仍可达的直接 scancel watcher。已归档历史 watcher 不机械重构，但仍可达而未适配的入口不允许在受保护环境执行。消费方实际安装、加载与新会话正常调用通过后才完成维护看板闭环；不能由中央单测直接标记 DONE。

必须复核的消费者源码包括 DII/AGENTS.md 与 CARE/.agents/skills/slurm-routing-partition/SKILL.md，以及 CARE/scripts/route_B_round04/watch_B1_race.py、scripts/evaluation/watch_care_srr_cascade_formal_race.py、watch_srr_v3_m7_routing.py、watch_srr_v3_m8_myops_race.py、scripts/target_domain_gap_closure/monitor_interactive_takeover.py。消费者阶段涉及其他仓库的写入仍需新授权，不能隐含在本任务长提示词。

## 五、同一候选的六项能力验收

G1 配置与作业识别：两个集群同名分区、混合 GPU、PENDING/RUNNING、多个候选 partition、job array/异构/批量目标；用户私有保护并集及未知拒绝。模拟只证明判定，目标机身份须另验。

G2 本人确认：旧竞速许可、长 Goal、auto_review、钩子 ask、伪造回执、超时与失联均不能批准；短请求一次对应一个明确目标/集合，状态或策略改变失效；无取消时不打扰。

G3 不可绕过：真实 Codex 普通入口与经验证受限执行身份，模拟执行测试涵盖 Python subprocess、绝对路径、shell、SSH、Slurm API、批量/数组、tmux/salloc holder、钩子异常和备用认证；任一路径能在未确认时释放受保护分配即强制保护 FAIL。假 Slurm 通过不等于真实权限隔离通过。

G4 状态安全：执行前复验目标集合、JobId/数组与依赖，PENDING→RUNNING 及不明取消结果保持原作业，不在旧作业仍活动时重提或暗中双跑。

G5 原有能力与消费者：正常 read/submit/monitor/计算步骤结束持续可用；真实当前 DII/CARE 入口与技能安装版本一致；非保护本轮自有作业的自动取消只在受限代理模式有证据时宣称可用。人工模式不得拼装成完整 G5 PASS。

G6 发布真实性：同一最终候选、正常安装和新会话、真人授权来源、远端权限与 holder 证据、独立 Reviewer 实际审完整工作流；仅单测/CI、README/钩子存在、模拟 PASS 或任务报告不能证明 H100 真受保护。G3/G5/G6 不满足时禁止发布强制防护/Longleaf 已部署声明。

回归负例必须覆盖：“长 Goal 偷藏取消”、旧分区竞速、H100 跨分区、htzhulab 中非 H100、未知 GPU、JobId 扩大命中、旧作业、状态变化、脚本间接调用、钩子坏了仍放行、holder 被信号释放以及 srun 步骤自然完成。全部危险操作只对假调度器/模拟进程做；不使用任何现有 H100 JobId。

## 六、停止与恢复

任何来源不明、钩子不可用、权限无保障、未知 JobId 或审批无法真人核验，代理取消立即拒绝；现有 Slurm 作业、allocation、隧道、tmux holder 不改、不杀、不重提。离线回归发现正常查询/训练被阻止时修复兼容性，不把所有审批切成人工。若必须新增服务、权限或直接操作真实机器，停止阶段 A，回 Planner/独立 Critic；绝不换命令形式绕过禁止。

## 七、版本、Issue 与授权

当前 Repository 5.4.4、独立 Skill 0.4。文档阶段 Repository bump decision = NONE，slurm-workflows = NO_BUMP，中央 Plugins = NO_BUMP。若实现与真实验收完整成立，独立 Skill 候选 0.4→0.5；Repository 根据发布当时基线选下一 PATCH（仅基线仍 5.4.4 时为 5.4.5），中央 Plugins 不升级。README 检查和发布生成物按已有规则进行，不提前写死发版。

Issue #96 已完成并关闭，只属于 0.4 竞速适配。需要新 Issue“防止 AI 未经本人确认取消受保护 Slurm 作业”，以 maintenance-track 关联 docs/skill-todos/slurm-workflows.md 本次新反馈，并使 Project Status 为 DOING，锚点为 Plan/Goal/Kickoff 待 Critic、下一步执行就绪审查。当前工具无可真实调用的已安装 Clear Writing（writing-style）；维护看板要求读者可见 Issue 写入前必须调用它，故不能声称已创建或已同步。明确待执行操作：具备该能力的 AI Skills Maintainer 先调用 Clear Writing，再建立该 Issue，回填 source tracking: #真实编号，更新 Project DOING/Area=standalone-skill/执行锚点；不得要求用户手工维护。此状态标记 ISSUE_CREATE_PENDING_CLEAR_WRITING，非已完成。

本 Plan 及同版 Goal、Kickoff 均是待审草案，绝不包含部署、费用、远端账号/凭据、生产钩子安装、真实 Slurm 修改或 DII/CARE 源码写入的授权。Critic 的 execution-ready PASS 仍不代用户授权；只有用户实际发送**经审查的同一份**短 Kickoff 才能开始明确的离线阶段 A。禁止把用户原来设计方向的 PASS 当成执行 PASS。

## 八、独立可检索的资料

- 正式设计：https://github.com/YuukiAS/AI_Skills_Collection/blob/a92dc4729e9c5bd2740c5d1bd967daa40f13e8d3/docs/design/slurm-workflows/SLURM_WORKFLOWS_CANCEL_PROTECTION_PROPOSAL_V0_3_2026-10-13.md
- OpenAI Codex 安全和自动审批：https://openai.com/index/running-codex-safely/
- 执行前钩子 ask 未支持：https://github.com/openai/codex/issues/28437
- 执行前钩子异常风险：https://github.com/openai/codex/issues/41979
- Codex 执行命令规则：https://github.com/openai/codex/blob/main/codex-rs/execpolicy/README.md
- Slurm 分配持有者：https://slurm.schedmd.com/salloc.html
- Slurm 取消和批量/数组：https://slurm.schedmd.com/scancel.html
- OpenSSH 受限远端身份：https://man.openbsd.org/sshd.8
- 历史已关闭 Issue：https://github.com/YuukiAS/AI_Skills_Collection/issues/96
