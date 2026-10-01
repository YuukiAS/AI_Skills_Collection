你现在继续 AI Skills Maintenance Board v7 Stage B，只处理 blocker：

DUPLICATE_PROJECT_AUTOMATION_READD_FALSE_DONE

Repository:
YuukiAS/AI_Skills_Collection

Task:
repo--maintenance-board-issue-maturity

Existing branch:
reviewed/repo--maintenance-board-issue-maturity

Primary environment:
Longleaf_Codex

只有当 independent Critic 对 v0.4 recovery package PASS，且我随后实际发送本 Kickoff，才形成执行授权。

必须读取：

- AGENTS.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
- docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_STAGE_B_RECOVERY_PLAN_V0_4_2026-10-01.md
- docs/goals/AI_SKILLS_MAINTENANCE_BOARD_V7_STAGE_B_RECOVERY_GOAL_V0_4.md
- results/repo--maintenance-board-issue-maturity/STAGE_B_BLOCKER_HANDOFF.md
- results/repo--maintenance-board-issue-maturity/STAGE_B_DUPLICATE_AUTOMATION_READD_BLOCKER.json
- results/repo--maintenance-board-issue-maturity/STAGE_B_DUPLICATE_AUTOMATION_READD_CONTINUATION_READBACK.json

不要重新设计 taxonomy / Forms / Action / hierarchy / audit / v6.1 / Longleaf route。

==================================================
一、冻结恢复方案
==================================================

只采用方案 A：

Project auto-add filter 从：

is:issue label:maintenance-track

改为：

is:issue is:open label:maintenance-track

maintenance-track 继续保留在 historical duplicate Issues。

禁止：
- 通过移除 maintenance-track 解决本 blocker
- 新增补偿 bot / Action / watcher / controller / database

==================================================
二、先在 existing task branch 准备 canonical policy amendment
==================================================

只修改当前 canonical：

docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md

把 auto-add active admission contract 收紧为：

is:issue is:open label:maintenance-track

并明确：

1. active admission：
   open + maintenance-track 才自动加入 Project。

2. historical completed：
   已经在 Project 的 completed DONE/History 继续保留。
   auto-add filter不是 completed History 的重建机制。

3. closed non-completion：
   duplicate / not-planned / rejected / superseded 从 Project 移除后保持移除；
   maintenance-track可保留为历史 tracking metadata；
   因为 is:open=false，不再被 auto-add。

4. reopened tracked Issue：
   truthfully reopen 后重新成为 open，可再次匹配 auto-add。

5. issue-closed -> DONE workflow保持不变。

不要修改历史 Proposal / Review / Goal / Kickoff 去伪装旧规则不存在。

==================================================
三、Project workflow mutation preflight
==================================================

在任何 Project workflow mutation 前保存：

results/repo--maintenance-board-issue-maturity/STAGE_B_AUTO_ADD_PRE_CHANGE.md

必须记录：

- Project = AI Skills Maintenance
- project number = 5
- target workflow = existing Auto-add to project
- workflow enabled state
- repository = YuukiAS/AI_Skills_Collection
- exact current visible filter
- readback surface

预期 old filter：

is:issue label:maintenance-track

如果 live old filter 与预期 materially 不一致：
- stop
- 不 mutation
- 返回 Planner

==================================================
四、exact Project workflow mutation
==================================================

只修改 existing Auto-add to project workflow 的 filter：

is:issue is:open label:maintenance-track

保持：

- same Project
- same linked repository
- workflow enabled
- issue-closed -> DONE unchanged
- Pull request merged -> DONE existing BOARD-01 state unchanged
- no duplicate auto-add workflow
- no auto-archive

优先使用当前 available supported UI-capable GPT/Work surface。

如果没有 supported UI automation，只允许一次 HUMAN_ONLY exact UI handoff：

1. 打开 AI Skills Maintenance Project
2. Project menu -> Workflows
3. Auto-add to project
4. Edit
5. repository保持 YuukiAS/AI_Skills_Collection
6. filter改成 exactly：
   is:issue is:open label:maintenance-track
7. Save and turn on workflow

用户完成这一个UI动作后，同一 Goal自动继续。

不要让用户参与后面的 duplicate cleanup / audit / migration / acceptance。

Workstation掉线不是前置条件。

==================================================
五、filter readback
==================================================

mutation 后必须保存：

results/repo--maintenance-board-issue-maturity/STAGE_B_AUTO_ADD_POST_CHANGE.md

必须实际看到：

filter = is:issue is:open label:maintenance-track
enabled = true
repository = YuukiAS/AI_Skills_Collection

如果无法确认 exact filter：
- 不删除11个duplicate
- rollback workflow到old filter
- stop

==================================================
六、repair exact 11 duplicates once
==================================================

filter readback PASS 后，处理 exactly：

#52 #60 #61 #62 #66 #67 #68 #69 #70 #71 #72

对每个先确认：

- state = CLOSED
- state reason = DUPLICATE
- maintenance-track present
- reviewed taxonomy labels present
- currently in AI Skills Maintenance / DONE

然后只：

- remove Project item

禁止：

- reopen / re-close
- 改title/body
- 删除maintenance-track
- 改source TODO maturity/evidence/tracking:#N
- 改taxonomy classification
- 改Project Area

保存：

results/repo--maintenance-board-issue-maturity/STAGE_B_DUPLICATE_REPAIR_V0_4.json

包含all-11 before/after Project membership。

==================================================
七、验证 closed duplicate 不再 re-add
==================================================

先等待 bounded Project automation settling period，再read back all 11：

必须：

- CLOSED / DUPLICATE unchanged
- maintenance-track retained
- taxonomy labels retained
- no AI Skills Maintenance Project item

然后用 #52 做 representative update-trigger probe：

1. snapshot #52 current labels
2. temporarily remove existing:
   kind:enhancement
3. immediately restore:
   kind:enhancement
4. verify final label set exactly equals pre-probe snapshot
5. verify state仍 CLOSED / DUPLICATE
6. maintenance-track never changes
7. wait bounded automation settling
8. verify #52仍不在Project
9. verify other ten仍不在Project

如果 #52 再次被加入：
- stop
- 不继续audit
- 不加补偿bot
- 返回Planner

==================================================
八、completed History preservation
==================================================

workflow filter修改前后，snapshot所有当前：

CLOSED / COMPLETED
+ maintenance-track
+ Project DONE/History

items。

filter change + duplicate repair 后必须验证：

- completed items仍在Project
- Status仍DONE
- Resolution commit值不变
- 没有 completed History item 因filter收紧而消失

==================================================
九、full audit
==================================================

运行现有 deterministic metadata audit，logic不得改。

必须：

ok = true
violation_count = 0

不 grandfather。
不 suppress known violation。
不修改audit contract。

若audit仍失败：
- stop
- 不继续Forms/Action/Search
- 返回Planner/Reviewer exact violations

==================================================
十、branch / main integration boundary
==================================================

当前v7 functional source已在main，taxonomy migration已完成。

本recovery不要 replay G7或taxonomy migration。

执行顺序：

1. approved v0.4 recovery package
2. existing task branch准备exact canonical policy amendment
3. latest-main drift check
4. auto-add workflow filter mutation + exact readback
5. remove 11 duplicates + readback
6. #52 update-trigger probe
7. full audit PASS
8. ordinary non-force integrate exact reviewed policy amendment + recovery evidence into latest main
9. verify remote main

不要把已集成的v7 functional source重新当成新implementation merge。

如果步骤4–7未PASS：
- main policy保持旧语义
- 按rollback处理external recovery
- stop

==================================================
十一、rollback
==================================================

workflow mutation前必须snapshot old filter/enabled state以及11个duplicate Project metadata。

如果workflow mutation失败：
- restore exact old filter：
  is:issue label:maintenance-track
- verify
- 不移除duplicates
- stop

如果11-item repair partial fail：
- re-add已经remove的duplicate到same Project
- restore exact pre-recovery Project Area / Status / Resolution
- restore old broad filter
- verify rollback
- stop

maintenance-track永不改变。

rollback回known false-DONE baseline只是为了避免partial mixed state；
它不算PASS，audit仍blocked。

一旦：

- new filter PASS
- all 11 absent PASS
- sentinel probe PASS
- full audit PASS

recovery视为committed。
后面 unrelated Forms/Action/Search failure 不应再rollback本fix。

==================================================
十二、继续现有Stage B剩余工作
==================================================

recovery + policy main integration完成后，只继续剩余 gates：

1. live Issue Forms chooser acceptance
2. pre-admission Action smoke
3. GitHub search usability acceptance
4. stale-safety final readback
5. README closure
6. Issue #92 reader-facing closure evidence update
   - mutation前调用Clear Writing
7. Resolution commit
8. close #92 completed
9. verify Project DONE

禁止重跑：
- classification
- G7 label cutover
- taxonomy migration

如果 Longleaf 最终只缺 supported live Issue chooser UI：
- 隔离这一项作为最后 bounded UI acceptance handoff
- 不要求Workstation恢复
- 不重跑前面步骤

==================================================
十三、禁止
==================================================

不允许：

- 实现v6.1
- production plugin source mutation
- Project Status lifecycle redesign
- taxonomy redesign
- audit relaxation
- stale automation
- compensating Action/bot/watcher/controller
- database/registry
- repository/plugin version bump

Repository bump = NONE
all plugins = NO_BUMP
Production Plugin Capability Gate = NOT REQUIRED

任何关键readback失败时停止，不得静默继续。
