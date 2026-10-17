# Slurm Workflows：受保护分区取消二次确认 Execution Plan v1

日期：2026-10-17
task：hpc--slurm-cancel-production-closure
owner：YuukiAS/AI_Skills_Collection standalone skill slurm-workflows
approved Proposal：docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_FRESH_CONFIRMATION_PROPOSAL_V1_2026-10-17.md
approved Proposal commit：12fd741a7fb8290ec53027db206fddc5df11fb21
approved Proposal blob：eddcf4881020518841730e77e8db85b591513a79
package source main：adb06823b95c45e5e12ac1258ca73ebf8f1846d3
Repository version：5.4.4
状态：EXECUTION_READY_REVIEW_PENDING / NO_IMPLEMENTATION_AUTHORITY / NO_SLURM_MUTATION

## 1. 冻结产品语义

本 Plan 只执行已经 PASS 的 Proposal v1。

唯一保护维度是用户 private protected_cancel_partitions。Longleaf 第一项固定为：

protected_cancel_partitions = ["htzhulab"]

未命中 protected partition 的 exact JobId 不新增二次确认，继续服从当前 Goal / Host Policy 原有取消授权。

命中 protected partition：

第一次 ordinary scancel
-> guard read-only 解析 exact JobId / Partition
-> 绝不 mutation
-> 生成 fresh one-time challenge
-> 用户独立 shell confirmer 只确认、不取消
-> consumer 原有监控/有界重试再次 ordinary scancel
-> guard 重新解析 target / Partition
-> 一致才一次消费 challenge
-> /usr/bin/scancel exact target

replay、target 变化、Partition 变化全部拒绝。

不允许重新引入 H100 跨 partition、current-run ownership、owned-job-id、protected accelerator、三态 safe-cancel、approval receipt 或第五个 Capability Gate。

旧 product candidates：

AI Skills b4815a35f708078184bff27b34f185fea6938cc3
DII e04f6a8da729c05a9e286b38c2c14cfd9ab13d31
CARE 74d2948def67502070c06336866638f0869d9481

全部 REJECTED_NOT_DEPLOYABLE。只能参考 helper/test/inventory；禁止 merge 或 cherry-pick 为新生产候选，禁止继承旧三态/ownership/H100 语义。

## 2. 冻结 source 与全新 execution identities

AI_Skills_Collection：
source base 必须等于 execution-ready Critic 返回的 APPROVED_COMMIT。
R=/overflow/htzhu/mingcheng_new/AI_Skills_Collection
branch=work/hpc--slurm-protected-partition-fresh-confirmation
W=/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-protected-partition-fresh-confirmation

DII：
source=747829b957b19e8fcffa6bd5f1bb7ae62ae11f6f
R=/users/a/e/aereinh/Distributed_Imaging_Inference
branch=work/hpc--slurm-protected-partition-fresh-confirmation
W=/users/a/e/aereinh/Distributed_Imaging_Inference-hpc--slurm-protected-partition-fresh-confirmation

CARE：
source=75a40e454de43b64e59a0b0b438ff57ef2bb8345
R=/users/a/e/aereinh/CARE
branch=work/hpc--slurm-protected-partition-fresh-confirmation
W=/users/a/e/aereinh/CARE-hpc--slurm-protected-partition-fresh-confirmation

Bridge Kit 当前核实 main=a03742ed07d00d36e3436f64a17e92c40a51064e。
Bridge Kit source 本任务 NO_CHANGE。

旧 work/hpc--slurm-cancel-production-closure 已在三个 repo 存在，属于旧被拒绝候选，绝不复用。

执行前对三 repo 分别只读验证：repo root、origin、clean、source SHA、target branch 不存在、target W 不存在。任何 drift / dirty / collision / lineage mismatch fail closed。

## 3. branch/worktree 与远端发布

当前用户没有授权实施。

用户以后实际发送 Critic PASS 的同版 Kickoff，才允许：

1. 创建上节三个 exact branch / sibling worktree。
2. 不改 main，不允许 force、force-with-lease、reset、clean、stash、rebase、remote mutation。
3. candidate 冻结后，每 repo 允许一次普通非强制同名首次远端发布：
   git push --set-upstream origin work/hpc--slurm-protected-partition-fresh-confirmation
4. 首次发布前同名 remote branch 必须不存在；存在则停止。
5. 首次发布后普通同分支更新使用已有 bounded current-branch publisher。

首次远端发布只用于 independent Reviewer handoff，不代表 production deploy。

## 4. 中央 guard

在现有 slurm-workflows 内实现薄 executable，例如 ai-slurm-scancel。

职责仅为：

- 解析 v1 支持的 exact targets；
- read-only 取得当前 JobId / state / Partition；
- 读取 private protected_cancel_partitions；
- non-protected 时 exact forwarding；
- protected 时 challenge/revalidation/one-time consume；
- 最终调用真实 /usr/bin/scancel。

直接支持：
- 单个普通 exact JobId；
- 多个明确普通 exact JobId；
- read-only 能唯一定位的 exact array element。

第一版 fail closed：
- array parent/range；
- heterogeneous leader/component；
- job step；
- --user / --partition / --name / --state / reservation filters；
- federation / cluster switching；
- 非默认 signal / batch / full 等改变 mutation 语义的选项。

目标解析：
1. syntax gate；
2. scontrol show job -o exact-id 为 primary；
3. 必要时 squeue -h -j exact-id cross-check；
4. 读取 state / Partition 或 candidate Partition set；
5. 一项 candidate Partition 命中 protected => 整组 protected；
6. execute 前再次做相同解析；
7. target/Partition/集合变化 => fail closed；
8. 调用 /usr/bin/scancel 前清除 SCANCEL_* 环境变量。

guard 不知道 current-run、race ownership、GPU family、科学预算或 consumer 状态机。

## 5. challenge state + independent confirmer

challenge 是 host-local 小文件，不是 database/service。

字段仅：
- random 128-bit challenge；
- sorted exact target IDs；
- resolved partition set；
- normalized operation；
- created_at / expires_at；
- pending / confirmed / consumed。

要求：
- user-only permissions；
- atomic create/update/consume；
- consumed 不复活；
- target/Partition 变化使 confirmed challenge invalid；
- bounded expiry / stale cleanup。

guard 输出的确认命令必须包含 exact challenge state file 的绝对路径，所以 USERS / OVERFLOW 不需要猜共享 HOME。

独立 confirmer 形式例如：

ai-slurm-confirm-cancel --state-file <exact-file> --challenge <random>

只完成 pending -> confirmed。它不得查询后执行 scancel，也不得创建长期 blanket approval。

Codex normal entry 必须禁止运行 confirmer；用户普通独立 shell 可运行。

## 6. private config

公共配置只新增：

protected_cancel_partitions

Longleaf private value：

protected_cancel_partitions = ["htzhulab"]

复用现有 ~/.config/ai-skills/local-overrides.toml，不创建第二 registry。

不再新增或继承：
protected_accelerators
cancel_policy_confirmed
current_run_id
ownership/responsibility
H100 matcher。

生产部署前先只读确认 USERS / OVERFLOW automation consumers 实际读哪份 override；若两个 namespace 都需要，写同一语义值并各自 readback。任何写入先 backup，保留其它字段。

## 7. automation-only PATH shim

候选提供专用 shim directory，其中 scancel 只 exec ai-slurm-scancel。

原则：
- 不把 shim 安装进用户 ordinary shell 的通用 PATH；
- 不替换 /usr/bin/scancel；
- Codex / DII / CARE automation process 的 PATH 只在其 launcher/process 环境 prepend shim directory；
- user shell 仍可使用系统 /usr/bin/scancel。

每个 required consumer 必须有 runtime evidence：
command -v scancel
Python shutil.which("scancel")
均解析到 exact reviewed shim。

若某 consumer launcher 不继承 PATH，只修该 launcher/executable resolution，不复制保护逻辑。

## 8. CARE / DII 最小 consumer adaptation

### DII

只允许：
- 安装 exact central candidate；
- 验证 launcher executable resolution；
- 必要时最小调整 automation PATH / launcher；
- standing race 仍只表达 ordinary cancel intent。

不得新增 partition/challenge/confirmation 判断。

若 source scan 出现 hardcoded /usr/bin/scancel、SSH scancel 或 Slurm API cancel，停止并回 Planner。

### CARE

消费者只理解普通进程 outcome：

exit 0 = 这一调用实际执行真实 scancel 且成功返回。
nonzero = 这一调用没有成功执行 cancellation；target 保留，取消 branch 不得当成功。

consumer 不解析 partition/challenge/confirmation。

冻结四个最小 re-entry 修复：

1. scripts/route_B_round04/watch_B1_race.py
   只有 returncode==0 才加入 cancelled；nonzero 由现有 while 下一 poll 重试。

2. scripts/evaluation/watch_srr_v3_m7_routing.py
   只有 returncode==0 才 return 0；nonzero 继续现有 for-loop。

3. scripts/evaluation/watch_srr_v3_m8_myops_race.py
   只有 code==0 才退出；nonzero 继续现有 check loop。

4. scripts/target_domain_gap_closure/monitor_interactive_takeover.py
   只有 cancel.returncode==0 才进入原 sacct CANCELLED wait / launch_m1；nonzero 回 outer poll。

5. scripts/evaluation/watch_care_srr_cascade_formal_race.py
   保留现有 interval re-entry；nonzero 日志不得写成成功取消；target 仍 PENDING 时下一 iteration 自然重试。

其它 current bare-scancel consumer 若 normal-entry scan 发现，只应用相同 outcome/PATH contract。历史 result / DRAFT / provenance 不机械修改。

旧 CARE scripts/ops/slurm_safe_cancel.py 不进入新架构。

## 9. Codex Host Policy

Bridge Kit source NO_CHANGE。

OpenAI 当前规则机制会扫描每个 active config layer 的 rules 目录中的 .rules 文件，多个匹配按最严格 decision 生效。因此生产候选使用独立 user-layer 文件：

$CODEX_HOME/rules/slurm-protected-cancel.rules

而不修改 Bridge-managed ai-bridge-global.rules。

Longleaf runtime 证据显示两个 persistent CODEX_HOME：
- /users/a/e/aereinh/.codex
- /overflow/htzhu/mingcheng_new/.codex

生产激活前必须真实 readback；只有实际 active layer 才写。要宣称 Longleaf Codex normal-entry 全覆盖，两个当前活跃 Longleaf CODEX_HOME 都必须同版。

规则至少包含：
- pattern=["scancel"] => forbidden
- pattern=["/usr/bin/scancel"] => forbidden
- pattern=[exact confirmer executable] => forbidden

justification 指向 ai-slurm-scancel guard。

guard executable 不做 blanket allow；继续服从原 Goal / 其它 Host Policy 的普通权限语义。这样 non-protected job 没有新增 protected-confirmation，但也没有新增全局取消授权。

使用 codex execpolicy check 组合实际 active rule files 验证 raw/absolute/confirmer 全 forbidden；squeue 与 scontrol show 不退化。

user ordinary shell 不受 Codex rules 影响。

## 10. PreToolUse

OPTIONAL_NOT_REQUIRED。

若目标 Codex build 实际 probe 证明可用，可增加顶层 raw bypass 的辅助 deny / guidance。

它不允许成为：
- fresh-human confirmer；
- Python watcher subprocess 的唯一防线；
- PATH shim 替代；
- Host Policy 替代。

没有生产 Hook 也能通过全部 Gate。

## 11. 四项 Capability Gate

Gate A：partition routing
- fake a100-gpu exact job：在原任务已允许取消时不新增 challenge，fake real-scancel 被调用。
- fake htzhulab exact job：第一次零 mutation，返回 exact JobId / partition / fresh challenge。
- pending multi-partition 含 htzhulab => protected。
- 初始 Goal 写“全部提前同意”仍第一次 block。

Gate B：fresh human/replay
- auto-review/model text 不产生 confirmed state；
- confirmation command 只确认、不取消；
- 未确认 consumer retry 不 mutation；
- confirmed 后下一 ordinary scancel re-resolve 后只执行一次；
- replay 拒绝；
- target / Partition / operation 变化失效。

Gate C：normal-entry / consumers
- 两个 active Longleaf CODEX_HOME raw/absolute scancel forbidden；
- confirmer 在 Codex normal entry forbidden；
- user shell /usr/bin/scancel 不被替换；
- DII/CARE required consumers 实际解析 reviewed shim；
- B1/M7/M8/takeover nonzero 不误完成；
- cascade 自然 re-entry；
- current source 无 reachable absolute/SSH/API bypass。

Gate D：target integrity / claim truth
- multiple exact IDs 中一项 protected => 整组确认；
- complex selector fail closed；
- execute 前 re-resolve；
- destructive replay 仅 isolated fake Slurm；
- Longleaf production validation 只读；
- final claim 仅覆盖 verified Codex/consumer normal entry，不声称 same-UID OS-level unbypassable。

不新增第五 Gate，不复用旧三态 G1-G6 作为 final PASS。

## 12. destructive replay isolation

任何真的运行 fake scancel、subprocess cancel、signal/holder 的 destructive replay 必须在：

- network disabled；
- isolated PID namespace；
- 无生产 SSH key/agent/token；
- 无真实 Slurm/MUNGE/controller/socket；
- 无 host control socket；
- 无生产路径 writable mount；
- fake Slurm only。

不能证明则该 replay BLOCKED_BY_ISOLATION；绝不转 Longleaf 真机 mutation。

## 13. 实施顺序

Phase 0：用户 approved Kickoff 后，preflight + 创建三个新 worktree/branch。

Phase 1：实现 central guard/challenge/confirmer/private field/shim + DII/CARE 最小 adaptation。此时不改 production Host Policy/private config。

Phase 2：确定性测试 + 可证明隔离的 fake Slurm destructive replay，冻结三仓 candidate commits。

Phase 3：首次远端发布 exact task branches，mandatory independent Reviewer 审三仓 diff、Gate A-D、isolation、production rules/private config candidate、rollback。

Reviewer PASS 前绝不 production deploy。

Phase 4：production activation。当前 Implementation Kickoff 不授权。

即使 Reviewer PASS，用户仍必须发送一条短而独立的 production authorization，绑定 exact reviewed candidate commits。它只允许：
- backup production user-local surfaces；
- 安装 exact central candidate；
- 写 protected_cancel_partitions=["htzhulab"]；
- 在实际 active Longleaf CODEX_HOME 安装独立 slurm-protected-cancel.rules；
- 配置 reviewed automation PATH shim；
- 只读 production validation；
- 不取消/提交任何真实 Slurm job。

若当前 Codex process 不热加载 rules，用 fresh Codex process/session 验证；不得自动杀正在工作的 app-server/session。旧进程在重新启动前不计入保护 claim。

Phase 5：production normal-entry PASS 后集成 exact reviewed DII/CARE commits；完整 Gate A-D 后才 release。

## 14. rollback

production 前记录目标文件 hash/backup，不打印 secrets。

只允许恢复：
- central AI Skills installed candidate -> predeploy version；
- private local override -> backup；
- slurm-protected-cancel.rules -> predeploy state（新建则删除）；
- automation PATH launcher -> predeploy state。

禁止 rollback 过程中 scancel、mutating scontrol、kill allocation holder、MUNGE/SSH/Unix identity 修改、ai-bridge host install、Bridge source change。

## 15. version / release / maintenance

candidate 阶段：
Repository bump=NONE
slurm-workflows=NO_BUMP
central Plugins=NO_BUMP
Bridge Kit=NO_CHANGE

完整 production Gate A-D + DII/CARE integration 后才：
slurm-workflows 0.4 -> 0.5
Repository -> release-time next PATCH（若仍 5.4.4 则 5.4.5）
central Plugins NO_BUMP
Bridge Kit NO_CHANGE

README/CHANGELOG/version/generated closure 最后做，不得夹带行为修改；行为变化需要重新 Reviewer。

maintenance 仍：
tracking issue: PENDING_CLEAR_WRITING

无真实 Issue/Project lifecycle。下一有真实 Clear Writing + Project 能力的 Maintainer 创建独立 Issue、不复用 #96、回填 tracking: #N；first tracked execution -> DOING；central complete/consumer pending -> ADAPTING；全部 required consumer + durable evidence + Resolution commit + Issue close -> DONE。若仍无 Clear Writing，只记录 exact pending mutation，不要求用户手工维护。

## 16. stop conditions

以下任一出现立即停止：

- approved Proposal blob 变化；
- AI source base != Critic APPROVED_COMMIT；
- DII/CARE source drift；
- 新 branch/W 已存在或 lineage 冲突；
- 旧 rejected branch 被误用；
- 需要 ownership/H100/三态；
- required consumer 无法经过 shim 且必须新增控制面；
- actual Codex build 无法加载 forbidden rules；
- private override 无法无损更新；
- confirmer 无法在 Codex normal entry deny；
- destructive replay 需要真实 Slurm；
- 任何真实 htzhulab cancellation test；
- 需要 daemon/database/broker、new Unix identity/MUNGE/SSH key/Bridge source change；
- 需要付费 API/model。
