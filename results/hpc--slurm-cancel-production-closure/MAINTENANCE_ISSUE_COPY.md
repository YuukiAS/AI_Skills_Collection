# Slurm 受保护作业取消：当前聊天确认与安全隔离

## 当前正文

问题：受保护 Slurm 作业曾在缺少本人当次确认的情况下被取消；保护机制也曾误拦其它项目的普通 Bash 命令。

当前进度：冻结实现、无害原生确认卡的“保留 Job”返回值、确定性保留分支和两次真实确认取消均已验证，独立实现复核通过。用户已明确免除真实 held Job 的保留验收，历史 KEEP_TEST=NOT_RUN 保持不变。正式发布与安装验证尚未完成。

当前执行锚点：reviewed/hpc--slurm-cancel-production-closure；冻结实现 3e81802ab0251d3bf31ec2d808d4e3273505b2f6；results/hpc--slurm-cancel-production-closure/REVISED_G4_ACCEPTANCE.md 和 INDEPENDENT_FINAL_REVIEW.md。

下一步：保留最新 main 的并行更新，完成 5.5.2 / slurm-workflows 0.5 的最终 CI、正式发布和当前 Longleaf Codex 安装验证。禁止新增或再次操作 Slurm Job。

范围：standalone-skill / slurm-workflows；所有中央 Plugin、Bridge Kit、DII、CARE 不变。

唯一必需的安装使用方：当前 Longleaf Codex USERS identity，CODEX_HOME=/users/a/e/aereinh/.codex。其它机器不在本次验收范围内。

证据：原 Job 5693449 与 replacement Job 6028303 各准确取消一次；两次均零运行、零节点分配；OTHER_JOB_MUTATION=NO。实际测试的无害原生确认卡返回 decision=retain，零 Slurm mutation、零 cancellation reservation；同一候选版本的确定性 retain integration 为 PASS。focused 54、full Slurm 69、full repository 401、candidate CI 39434396011 PASS。最终 release CI 将单独绑定合并后的发布候选。

## 完成后正文模板（仅在全部实际通过后替换正文）

问题：受保护 Slurm 作业需要本人在当前根聊天中当次确认，且保护机制不得影响其它项目的普通 Bash 命令。

当前进度：已正式发布 Repository 5.5.2 / Slurm Workflows 0.5，最终 CI、独立复核及当前 Longleaf Codex 正式安装验证全部通过。无害原生确认卡的实际保留返回值与确定性保留分支均已验证；用户免除真实 Job 保留验收，历史 KEEP_TEST=NOT_RUN 保持不变。

当前执行锚点：Resolution commit: RELEASE_COMMIT；最终 CI: FINAL_CI_URL；results/hpc--slurm-cancel-production-closure/FINAL_RELEASE_CLOSURE.md。

下一步：本任务完成；禁止再创建或操作验收 Job。

范围：standalone-skill / slurm-workflows；中央 Plugin、Bridge Kit、DII、CARE 不变。

必需使用方验证：Longleaf Codex USERS identity，CODEX_HOME=/users/a/e/aereinh/.codex，安装源码和冻结 runtime bytes 一致，三项 Slurm Hook 信任保持不变，普通 Bash 正常通过。

验收：LIVE_JOB_RETAIN_TEST=WAIVED_BY_CURRENT_USER；LIVE_RETAIN_UI_MAPPING=PASS；DETERMINISTIC_RETAIN_PATH=PASS；LIVE_CONFIRM_PATH=PASS；OTHER_JOB_MUTATION=NO；G4_REVISED_ACCEPTANCE=PASS；G5=PASS。5693449 和 6028303 均只作为既有历史 confirm evidence，本轮没有 scheduler 访问、Job 操作或真实取消。
