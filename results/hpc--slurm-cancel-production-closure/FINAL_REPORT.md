# Slurm 取消保护正式发布完成

已正式发布 Repository **5.5.2** / Slurm Workflows **0.5**。发布提交
`f4517798a73adf29d3484306d60845488739f1fc` 已正常合入 main 并推进正式
release 分支；冻结 runtime 保持不变。最终 CI 39639471530 全部通过，
包括 406 项仓库测试；独立实现复核与正式安装 G5 均通过。

实际原生卡片返回 decision=retain，确定性保留分支通过。按用户最新
授权，真实 held Job 保留测试予以免除；历史 KEEP_TEST=NOT_RUN 保留。
原 Job 5693449 和 replacement Job 6028303 各准确取消一次，均零运行、
零节点分配，无其它 Job 修改。本轮未访问调度器、操作 Job 或执行真实取消。

正式安装后配置、三项 Hook 信任和既有取消记录完全一致；正常 reload、
实际普通 git status 与启动前阻断 help 均通过。没有再要求用户操作。
版本依据、CI、独立复核及可持久读取的安装证据见 FINAL_RELEASE_CLOSURE.md。
维护条目 tracking: #109。

LIVE_JOB_RETAIN_TEST=WAIVED_BY_CURRENT_USER
LIVE_RETAIN_UI_MAPPING=PASS
DETERMINISTIC_RETAIN_PATH=PASS
LIVE_CONFIRM_PATH=PASS
ORIGINAL_CONFIRM_JOB_ID=5693449
REPLACEMENT_CONFIRM_JOB_ID=6028303
OTHER_JOB_MUTATION=NO
G4_REVISED_ACCEPTANCE=PASS
INDEPENDENT_REVIEW=PASS
G5=PASS
FINAL_RELEASE_CI=PASS
REPOSITORY_VERSION=5.5.2
SLURM_WORKFLOWS_VERSION=0.5
PUBLISHED=YES
FORMAL_INSTALL_VERIFIED=YES
COMPLETE=YES
