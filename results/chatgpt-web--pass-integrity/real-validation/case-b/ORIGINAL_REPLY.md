# Case B 原始用户可见回复：Clear Writing 0.6 Phase C 安全停止

来源：用户转交的真实 Phase C 回复。  
用途：Planner–Critic 1.8 candidate 的已曝光 known regression；不得作为 unseen/fresh holdout。

---

Phase C 已按合同推进到安全停止点，**没有更新正式 Personal Plugin**。当前不是产品失败，而是执行面在 live mutation 前暴露了两个真实基础设施/实现接口 blocker；继续强行更新会违反已经批准的 Runbook。

实际完成的 P0 结果：
```
P0_ACCOUNT_READBACK=PASS

writing-style = 0.5.0
scope = USER
discoverability = PRIVATE
plugin identity = 与冻结基线相同
live file count = 27

冻结的 0.5 -> 0.6 delete_paths = 26
与 live 0.5 除 manifest 外的 26 个文件 = EXACT MATCH
```

但在保存真实账户旧版本并准备 forward restore 时发现第一个硬问题：**Plugin Creator 当前实际返回的完整旧版本 archive 是 `current.tar.gz` / `application/gzip`，而冻结 implementation 的 `prepare-restore` 内部只调用 `zipfile.ZipFile` 读取 baseline archive。** 也就是说，真实 Plugin Creator archive 不能直接进入已经冻结的 restore builder。要继续必须额外做 tar.gz→ZIP 转换，或者修改 builder；这两件事都不在批准合同里，而你明确禁止本轮改 frozen implementation。

第二个 blocker 更直接：批准的 G1-B/G2/G3 要求真正的：
```
fresh ChatGPT Web conversation
+ GPT-5.6 Sol
+ explicit Clear Writing selection
```

而当前 Planner execution surface 虽然可以读写 Plugin Creator、GitHub 和 Skill 文件，**没有创建新的 ChatGPT Web 对话并在其中显式选择插件的动作**。用 `skills__read`、当前线程自己回答测试题、本地 replay 或 helper 冒充都会直接违反 Gate 合同，尤其不能让 G3 PASS。

因此我没有先把 0.6.0 装上线再卡住。当前真实状态是：
```
PHASE_C_STATUS=BLOCKED_BEFORE_LIVE_MUTATION

P0_ACCOUNT_READBACK=PASS
PERSONAL_PLUGIN_MUTATED=NO
RESTORE_REQUIRED=NO

G1=NOT_RUN
G2=NOT_RUN
G3=NOT_RUN
G4=NOT_RUN
G5=NOT_RUN
```

没有创建 G3 branch，没有重新跑 Codex，没有改 frozen candidate，也没有发布 0.6。正式 Personal Plugin 仍是已验证的 `0.5.0`。

我已经把这次真实 P0 和两个 blocker 作为纯 evidence 提交到同一任务分支，没有碰 candidate-defining source：
```
PHASE_C_EVIDENCE_COMMIT=
38a81dc1df9a362ecee4be597cb3db5bd6fcac41
```

新增证据：
```
results/clear-writing--single-entry-artifact-finalization/phase-c/
  P0_ACCOUNT_READBACK.json
  PHASE_C_STOP_BEFORE_LIVE_MUTATION.md
  STATUS.json
```

下一步不需要重新授权，也不是重新设计 Clear Writing。**同一已批准 Phase C 只能在一个同时具备两种真实能力的执行面继续：能把 Plugin Creator archive / candidate archive 落成实际可上传文件；并能真正运行 fresh ChatGPT Web + GPT-5.6 Sol + explicit Clear Writing selection。** 在此之前更新 0.6.0 会制造“正式插件已变、但 Gate 根本跑不了”的状态，所以这里停下是 Runbook 要求的 fail-closed，而不是把 Gate 降级成假测试。
