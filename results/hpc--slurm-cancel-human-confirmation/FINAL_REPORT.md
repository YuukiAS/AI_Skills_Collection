# Final Report

## What this task solved

本轮把“允许提交任务或进行竞速”与“允许取消已经取得的受保护 Slurm 作业”明确拆开。中央 slurm-workflows 现在有一个 Stage A 离线候选，可以根据真实集群身份、精确作业集合、当前状态、本轮所有权和用户私有保护策略，判断某个取消请求应当允许进入后续受控路径、必须重新向本人确认，还是直接拒绝。

这解决的是此前最危险的语义缺口：长 Goal、历史竞速许可或自动审批不能再被当成取消已有受保护作业的本人授权。

## What changed

主要改动位于现有 slurm-workflows，而不是新建一套控制系统：

- skills/tools/hpc/slurm-workflows/scripts/slurm_routing.py 增加受保护取消的纯决策、短确认请求和确认表示校验。
- scripts/skills.py 扩展现有私有 local override，支持取消策略版本、确认状态、受保护分区和受保护加速器，同时不把这些私有值写入公共生成摘要。
- skills/tools/hpc/slurm-workflows/SKILL.md 增加取消保护的正常使用规则，明确 Stage A 决策不能自行授权真实取消。
- tests/test_slurm_workflows.py 增加 G1/G2/G4 与正常安装入口的确定性回归。
- results/hpc--slurm-cancel-human-confirmation/ 保存 ER-02 隔离证据、验证记录和 DII/CARE 只读消费者清单。

没有新增 daemon、数据库、Bridge Kit 控制面或新的顶级 Slurm Plugin/Profile。

## New capabilities / behavior

当前候选可以：

- 区分当前轮次自有且不受保护的精确目标、需要本人当次确认的受保护/旧目标，以及信息不全或明确禁止的目标。
- 按每个集群分别使用私有 protected_partitions，并与个人 protected_accelerators、站点保护规则取并集。
- 对数组元素和多目标集合要求先展开精确 JobId；无法确认完整目标集合时拒绝。
- 为需要确认的目标生成一条短请求，包含集群、精确目标、状态、分区/加速器事实以及资源或排队位置损失，并默认保留作业。
- 识别并拒绝长 Goal、旧 race opt-in、auto_review、Hook、模型回执和 scancel --interactive 等伪人工确认来源。
- 在目标状态、策略版本或目标集合发生变化时使旧确认表示失效。
- 保持确认表示与真正执行权限分离；即使确认表示合法，Stage A 也不会产生真实取消权限。

Longleaf 的 htzhulab 全分区保护和个人 H100 保护仍是未来部署时的用户私有策略，不是公共源码常量。

## Deliberately not adopted / unchanged

本轮有意没有：

- 运行或测试任何真实 sbatch、salloc、srun、scancel、Slurm API mutation、kill/signal 或 allocation-holder 终止。
- 在当前宿主环境伪造一个“安全假 Slurm”来绕过 ER-02。因为真实 mutation 二进制可见且进程共享宿主 PID namespace，危险回放按合同停止。
- 安装生产 Hook、改变 Codex Host Policy、SSH 凭据、服务器权限或 Slurm 配置。
- 修改 DII/CARE。其当前竞速和直接 scancel 入口只做了只读盘点，留给后续独立适配。
- 修改 Bridge Kit。
- 提升 slurm-workflows 版本、仓库版本、发布正式 0.5 或合入 main。
- 修复与本任务无关的 VERSION/Marketplace/presentations/palette 既有基线问题。

## Example usage

未来在完成后续部署与权限验证后，用户可以得到类似以下行为：

- “取消我刚才这个普通测试作业”：系统先核实集群、精确 JobId、本轮所有权和保护集合。只有事实完整且确认为本轮自有、未受保护目标时，才可能进入受控取消路径。
- “这个排了一周的作业别动”：旧作业或受保护作业不会因为已有任务授权而自动取消，只会产生一条针对当前精确目标的短确认请求，默认选择保留。
- “服务器 A 的 premium 分区要保护，服务器 B 不保护”：两个集群的同名分区分别按各自私有策略判断，不跨集群混用。
- Longleaf 后续部署时，可以在私有策略中把 htzhulab 整个分区列为受保护，并另外把个人 H100 列为受保护加速器；这两条规则取并集。

当前 Stage A 仍不会真的替用户执行这些受保护取消动作。

## Regression and remaining limitations

定向验证通过：

- python -m unittest tests.test_slurm_workflows：19 tests PASS。
- python -m unittest tests.test_skill_update：11 tests PASS。
- python scripts/skills.py validate：PASS。
- python scripts/skills.py audit --all：PASS。
- git diff --check：PASS。
- task-local Reviewed Handoff preflight：PASS。

全仓 unittest discovery 的 6 个失败和 1 个错误属于既有 VERSION/Marketplace/presentations/palette 基线，相关失败路径没有被本任务 diff 修改。

最大的剩余限制是 ER-02：当前运行环境不能证明与真实 Slurm、SSH 和宿主 PID/holder 完全隔离，所以所有危险模拟被正确跳过。Reviewer 因此只批准“中央离线候选”的 claim，不批准“真实不可绕过防护已上线”。

DII/CARE 仍未适配；Longleaf 私有策略、可信真人授权来源、真实执行边界、生产部署、版本提升、release 和 main integration 均仍需后续独立授权与验证。

## Technical appendix

- task: hpc--slurm-cancel-human-confirmation
- base commit: 58ee18cd3e68df77c35b314c5cf9b0e83a985423
- implementation commit: acf8bf29681b404a3c107d25ade527ad1dfe0b89
- review branch tip before Reviewer transaction: 30b15750f34e3422fa36dfe2f570caadf0e41636
- Reviewer decision: PASS, round 1
- CI required: false
- real Slurm mutation: NO
- version decision: repository NONE; slurm-workflows NO_BUMP; central plugins NO_BUMP; Bridge Kit NO_CHANGE
- evidence:
  - results/hpc--slurm-cancel-human-confirmation/VALIDATION_EVIDENCE.md
  - results/hpc--slurm-cancel-human-confirmation/ER_02_ISOLATION_EVIDENCE.md
  - results/hpc--slurm-cancel-human-confirmation/CONSUMER_INVENTORY.md
- scope boundary: Stage A offline central candidate only; no production deployment or consumer adaptation.
