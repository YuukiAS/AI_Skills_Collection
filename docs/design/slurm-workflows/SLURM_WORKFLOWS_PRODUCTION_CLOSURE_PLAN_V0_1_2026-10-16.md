# Slurm Workflows：受保护取消生产收口 Plan v0.1

- 日期：2026-10-16
- task：`hpc--slurm-cancel-production-closure`
- owner：`YuukiAS/AI_Skills_Collection` standalone `slurm-workflows`
- 上游已通过 Stage A：`reviewed/hpc--slurm-cancel-human-confirmation`
- Stage A implementation：`acf8bf29681b404a3c107d25ade527ad1dfe0b89`
- Stage A Reviewer PASS tip：`b672b408151915118d08aa200b59f4ab0bdda256`
- 当前仓库 main 版本：5.4.4
- 当前状态：PRODUCTION_CLOSURE_DESIGN / CRITIC_PENDING / NO_PRODUCTION_MUTATION

## 1. 目标与实际新增能力

本轮不重新设计 Stage A。目标是把已经通过独立 Reviewer 的中央离线候选真正变成**Longleaf 正常使用路径上的安全取消能力**，并关闭 DII/CARE 已知直接取消入口。

用户结果固定为：

1. Longleaf 私有策略明确保护整个 `htzhulab` 分区，以及所有 H100 作业；两类保护取并集。
2. 代理遇到受保护目标、旧作业或非当前轮次拥有的作业时，**永远不自行执行取消**，只生成一条精确目标的短请求；真正取消由用户在独立终端亲自完成。
3. Long Goal、历史竞速授权、`auto_review`、Hook 返回值不能替代本人确认。
4. 当前轮次自有、精确展开且确定不受保护的作业，仍可通过受控安全入口自动取消，避免把所有 Slurm 管理变成人工。
5. Codex 正常命令入口禁止直接 `scancel`；DII/CARE 已知自动取消路径改用同一个中央安全入口。
6. 当前共享 UID 仍不能证明绝对不可绕过，因此最终只声明“生产正常入口保护已启用”；不声明同 UID 任意 Python/Slurm API 已被操作系统层彻底隔离。

这比继续研究独立审批服务或新控制面更快，也与 Stage A 已批准的 fail-closed 语义一致。

## 2. 现实路线比较

### A. 只部署 Stage A Skill / AGENTS

不能阻止直接 `scancel` 或旧 watcher；拒绝。

### B. 只部署 Codex Hook

OpenAI 当前官方文档确认 `PreToolUse` 可以 deny，但 `permissionDecision: "ask"` 仍不受支持；错误输出可导致 Hook 失败后继续。不能作为唯一防线；本轮不把 Hook 作为完成条件。

### C. 只把 `scancel` 改为 Host Policy `forbidden`

能直接关闭本次“长 prompt 直接执行 scancel”的事故入口，但旧 Python watcher 内部仍能调用 `scancel`；单独不足。

### D. 新建独立 daemon / 审批数据库 / 特权 broker

理论上可做更强隔离，但当前需求不值得新增长期控制面；共享 Unix UID 下仍需额外 OS/站点权限设计，明显延迟收尾；拒绝。

### E. 中央安全取消入口 + Longleaf 私有保护策略 + raw scancel 禁止 + 已知消费者适配

采用。

- 安全入口实时读取精确 Slurm 目标，调用 Stage A 的 `protected_cancel_decision`。
- `ALLOW_OWNED_UNPROTECTED` 才允许入口内部执行 `scancel`。
- `REQUIRE_FRESH_HUMAN` 只输出短确认信息并返回非执行结果；**即使用户在聊天中回复“确认”，Codex 也不执行该受保护取消**，用户必须在独立终端亲自运行实际取消命令。
- `DENY_UNKNOWN_OR_FORBIDDEN` 直接拒绝。
- Codex Host Policy 对原始 `scancel` / `/usr/bin/scancel` 使用 `forbidden`；官方 execpolicy 的有效决策支持 `allow/prompt/forbidden`，且严格规则优先于 allow。
- DII/CARE 正常取消脚本改为安全入口，不再直接 subprocess `scancel`。

这不是绝对 OS 沙箱，最终 claim 必须保守。

## 3. 冻结执行身份与仓库

### 中央仓库

- repo：`YuukiAS/AI_Skills_Collection`
- task branch：`reviewed/hpc--slurm-cancel-production-closure`
- canonical R：`/overflow/htzhu/mingcheng_new/AI_Skills_Collection`
- derived W：`/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-cancel-production-closure`
- base：执行前最新且被 Critic 绑定的 `origin/main`
- Stage A port：只选择性移植 `acf8bf29681b404a3c107d25ade527ad1dfe0b89` 的产品/测试改动；不得把旧 Reviewed control artifacts 当作新任务状态。若 cherry-pick 出现语义冲突，停止回 Planner，不做随意合并。

### DII consumer

此前用户给出的 Longleaf repo root：`/users/a/e/aereinh/Distributed_Imaging_Inference`。执行前必须只读重新核实 repo/origin/clean/branch/worktree；不能仅凭历史路径直接写入。

拟用：
- branch：`reviewed/hpc--slurm-cancel-production-closure`
- W：`/users/a/e/aereinh/Distributed_Imaging_Inference-hpc--slurm-cancel-production-closure`

### CARE consumer

此前用户给出的 Longleaf repo root：`/users/a/e/aereinh/CARE`。执行前必须只读重新核实 repo/origin/clean/branch/worktree。

拟用：
- branch：`reviewed/hpc--slurm-cancel-production-closure`
- W：`/users/a/e/aereinh/CARE-hpc--slurm-cancel-production-closure`

若任一消费者路径、remote、dirty 状态或现有同名 branch/worktree 不匹配，消费者适配停止；中央候选可继续，但不能宣布整体收口。

## 4. 中央实现范围

在现有 `slurm-workflows` 内新增最小正式安全取消入口；优先作为 `slurm_routing.py` 的 CLI 子命令或同 Skill 小型 executable，不新建顶级产品。

入口必须：

1. 接受精确 JobId/已展开 JobId 集合；拒绝范围表达式和来源不明的批量 filter。
2. 只通过 Slurm 只读查询取得 cluster、partition、GPU、state、数组/异构身份、owner 与目标完整性。
3. 加载现有 `~/.config/ai-skills/local-overrides.toml` 私有取消策略。
4. 调用同一 Stage A 决策核心。
5. 对 `ALLOW_OWNED_UNPROTECTED`：执行前再次复验目标和状态，只有仍满足 exact-owned-unprotected 才内部调用 `scancel`；执行后只读确认结果。
6. 对 `REQUIRE_FRESH_HUMAN`：打印短请求、默认保留、退出且不运行 `scancel`。
7. 对 `DENY_UNKNOWN_OR_FORBIDDEN`：拒绝。
8. 不提供“把模型生成的确认票据喂回来即可执行受保护取消”的生产入口；Stage A 的确认 representation 继续只表示语义绑定，不产生 execution authority。

公共代码不写死 Longleaf、`htzhulab` 或 H100。

## 5. Longleaf 私有部署范围

用户已明确的 private policy：

- site：真实 Longleaf cluster id，以部署时只读发现为准；
- `protected_partitions = ["htzhulab"]`
- `protected_accelerators = ["H100"]`
- `cancel_policy_confirmed = true`
- `cancel_policy_version` 使用一次明确版本字符串，例如 `2026-10-16-v1`；实际写入前显示完整四项，不从其他服务器复制。

生产动作仅在用户发送经 Critic 审过的 Kickoff 后授权：

1. 将最终候选安装到 Longleaf 当前用户级 AI Skills 正常安装位置；不改系统 Slurm、MUNGE、SSH key 或 Unix account。
2. 修改用户私有 `~/.config/ai-skills/local-overrides.toml` 对应 Longleaf section；保留文件其他站点和已有字段，不覆盖未知配置。
3. 在 Longleaf_Codex Host Policy 中增加 bounded execpolicy：
   - raw `scancel` 为 `forbidden`；
   - 通过 host executable identity 同样覆盖已确认的 `/usr/bin/scancel`；
   - 只允许中央安全取消入口承担代理取消；
   - 不把全部 shell/Slurm 查询改成人工审批。
4. 生产 Hook 不是 release 前置条件；如果现有 Hook 已部署，可作为额外 deny 层，但不因 Hook 存在改变 claim。
5. 只读验证：Host Policy 对 raw scancel 的 eval 为 forbidden；安全入口能读取 private policy；对受保护目标的 read-only evaluation 只返回 `REQUIRE_FRESH_HUMAN` 且没有 mutation。

任何真实取消验证一律禁止。现有 H100/htzhulab 作业只能被只读查看，不得用来做 mutation probe。

## 6. DII / CARE 适配

### DII

当前 GitHub main 没有发现活跃业务脚本直接调用 scancel；主要缺口是：
- `AGENTS.md` 的 standing H100/A100 race winner/loser cancellation contract；
- repo-local 已安装 `slurm-workflows` 仍是旧候选。

适配只需：
- 安装/同步最终中央 Skill；
- 将项目竞速语义改为“loser cancellation 必须走中央安全取消入口；若目标受保护或不属于当前 run，保留 loser 并进入本人取消请求，不把 standing race opt-in 当作确认”。

不修改科研预算、GPU 合同或训练逻辑。

### CARE

必须修改当前仍可达的直接取消入口，至少：

- `.agents/skills/slurm-routing-partition/SKILL.md`
- `scripts/route_B_round04/watch_B1_race.py`
- `scripts/evaluation/watch_care_srr_cascade_formal_race.py`
- `scripts/evaluation/watch_srr_v3_m7_routing.py`
- `scripts/evaluation/watch_srr_v3_m8_myops_race.py`
- `scripts/target_domain_gap_closure/monitor_interactive_takeover.py`
- 若 `results/20260711_srr_v3_m10_complete_mechanism_repair/wave2_partition_race_watcher.py` 仍可作为可执行入口使用，则同样适配；若仅为历史 artifact，则明确标为 historical/non-entry，不能由 production prompt 调用。

消费者不得复制一份中央保护逻辑；只构造精确事实/当前 run identity 并调用最终中央安全入口。返回 `REQUIRE_FRESH_HUMAN` 时必须保留目标并退出/继续监控，不用直接 scancel fallback。

## 7. 验收 G1–G6（延续原矩阵，不新增 Gate）

G1：真实 Longleaf private policy 被正常安装入口消费；两个集群同名分区、htzhulab 全分区保护、H100 跨分区保护、未知事实拒绝均直接验证。

G2：受保护目标的正常入口只产生短请求；聊天确认、auto_review、旧 race opt-in 都不能导致代理执行；用户独立终端是当前唯一实际取消路径。

G3：两层证据分开：
- 隔离 Docker/Podman/CI sandbox 中用 fake Slurm 回放 direct/absolute path/Python/shell/consumer-script/数组批量等危险案例；sandbox 必须 network none、无生产凭据、独立 PID namespace、无生产挂载；
- Longleaf 只验证 normal-entry enforcement：raw scancel execpolicy forbidden + consumers 不再直接调用 scancel。
即使两者 PASS，也不宣称共享 UID 任意自造 Python/Slurm API 已被 OS 级不可绕过隔离。

G4：安全入口执行前重新获取目标事实；状态/目标集合/策略变化 fail closed；旧 job 不因 unprotected 自动获得权属。

G5：中央现有 Slurm regressions、DII 当前竞速流程和 CARE watcher 正常状态机不退化；非保护当前-run loser 仍能经安全入口取消；受保护 loser 变为保留 + 人工请求，而不是任务崩溃或静默双算。

G6：最终候选必须同时具有：
- 中央 source/test；
- Longleaf 当前用户安装 identity 和 private policy readback；
- Host Policy raw scancel forbidden readback；
- DII/CARE exact consumer commit；
- 隔离 fake-Slurm evidence；
- 独立 Reviewer。
然后才可声明“Longleaf 正常 Codex/消费者路径已启用受保护取消防线”。不得声明绝对 OS 不可绕过。

## 8. 版本与集成

当前 main VERSION=5.4.4。

如果本 Plan 的中央代码、Longleaf 正常安装、DII/CARE consumer adaptation 和 G1–G6 全部通过：
- standalone `slurm-workflows`: 0.4 → 0.5；
- Repository：PATCH；若发布时仍为 5.4.4，则 5.4.5，否则使用当时实际版本的下一 PATCH；
- 中央 Marketplace Plugins：NO_BUMP；
- Bridge Kit：NO_CHANGE，除非执行证据证明现有 Host Policy 无法表达 `forbidden scancel`；若出现这种情况停止并回 Planner/Critic，不顺手改 Bridge。

集成顺序：

1. 冻结中央 final candidate。
2. 消费者分支测试绑定中央 final candidate。
3. 独立 Reviewer 检查完整跨仓库证据。
4. 经用户最终批准后集成/发布中央 0.5。
5. Longleaf 用户级安装 + private policy + Host Policy 更新。
6. read-only production smoke。
7. 集成 DII/CARE consumer。
8. README/CHANGELOG/version/maintenance closure，验证真实远端身份后结束。

不得先升级版本再补消费者。

## 9. 恢复与停止

- Stage A port 与新 main 冲突：停止，不手工扩大修复。
- Longleaf private override 不能无损修改：保留原文件，输出 diff，不覆盖。
- Host Policy `forbidden` 规则不能由当前 Codex 版本实际加载/验证：停止生产部署，不降级成 prompt/auto_review。
- 安全入口对任何目标事实 UNKNOWN：不执行。
- DII/CARE 仍存在可达 direct scancel：整体不 DONE。
- 生产只读 smoke 发现候选身份/配置不一致：回滚 user-level install 和 Host Policy 到部署前 backup；不碰任何 Slurm job。
- 不通过“为了验证安全而真的取消一个 H100/htzhulab 作业”。

## 10. 非目标

- 不新增审批服务、数据库、特权 daemon；
- 不改变 Slurm/UNC 站点权限模型；
- 不创建第二个 Slurm Plugin；
- 不修改 Bridge Kit 架构；
- 不要求用户逐行审长 prompt；
- 不做真实 H100 cancellation test；
- 不顺手清理 CARE 历史科学结果或 DII 其他科研逻辑。
