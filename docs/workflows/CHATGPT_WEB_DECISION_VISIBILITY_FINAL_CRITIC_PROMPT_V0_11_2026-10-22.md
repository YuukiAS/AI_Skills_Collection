# Planner–Critic 1.8 v0.11：独立最终执行就绪 Critic 审查

你是 AI Research Stack 的**独立 Critic**，本轮审查的是设计阶段已获 `PROCEED` 后、准备交给 Codex 的**同一治理任务完整执行包**，不是对 Planner 表述表示赞同，也不是实施验收。你不能代 Planner 修改架构、不能自我授权，不能预设本版 `PASS`。

## 1. Active Review Context

```text
target_repo=YuukiAS/AI_Skills_Collection
target_plugin_or_domain=ChatGPT Web Planner–Critic governance
design_topic_or_task_key=chatgpt-web--pass-integrity
source_branch_or_ref=design/chatgpt-web--pass-integrity-v0-4
review_stage=FINAL_EXECUTION_READY_REVIEW_V0_11
previous_design_package_commit=1fb7edd9955764644edc299fb9bc5142ea882e58
previous_design_verdict=PROCEED
PACKAGE_COMMIT=<当前用户交接提供的准确 v0.11 完整包提交>
```

**本轮按正式 1.7 审查执行就绪**：最终唯一技术 `PASS + READY_FOR_CODEX=YES` 若成立，仍按当前 1.7 给用户短 `COPY TO CODEX`，不提前使用尚未实施的 1.8 “技术 PASS 先交 Planner”。后者是这次要审查批准的**未来产品行为**，不能提前拿它作为当前流程要求。其他阶段只给 `REVISE`，不使用设计期的 `PROCEED`。

## 2. 必须实际读到的权威材料

先读取最新 `YuukiAS/AI_Skills_Collection main` 的 `AGENTS.md`、`docs/workflows/PLANNER_ROLE_CONTRACT.md`、`docs/workflows/CRITIC_ROLE_CONTRACT.md`、`docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`、`docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md` 和仓库中当前 Project setting 快照。确认 1.7 仍是正式合同还是已有更新，不可依赖本 Prompt 宣称。

按准确 PACKAGE_COMMIT 完整读取：
- `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_PROPOSAL_V0_11_2026-10-22.md`；
- `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_EXECUTION_PLAN_V0_11_2026-10-22.md`；
- `docs/goals/CHATGPT_WEB_DECISION_VISIBILITY_GOAL_V0_11.md`；
- `docs/operations/prompts/CHATGPT_WEB_DECISION_VISIBILITY_KICKOFF_DRAFT_V0_11_2026-10-22.md`；
- `results/chatgpt-web--pass-integrity/VALIDATION_CONTRACT_V0_11_2026-10-22.md`；
- `results/chatgpt-web--pass-integrity/DESIGN_CRITIC_V0_10_USER_FORWARDED_HANDOFF_2026-10-22.md`，严格识别这是用户转交的完整 `COPY TO PLANNER` 内容，不是假造的 Critic GitHub commit，不等于已经读到了该 Critic 给用户的所有正文；
- `results/chatgpt-web--pass-integrity/USER_PARTIALLY_ACCEPTED_MULTIROUND_EXPLANATION_2026-10-22.md`；
- 该同版最终审查提示词。

以最小必要范围核实 v0.10 原 Proposal/Plan、原有 1.8 v0.7 接口真实性与停止恢复范围、当前仓库/Bridge 真实 Git 授权边界；不把历史坏回复或用户部分认可的 Slurm 教学段落变成强制模板。

可参考 `YuukiAS/AI_Research_Toolkit` 最新 `COMPLEX_ARCHITECTURE_EXPLANATION_STANDARD.md` 的跨领域因果、替代取舍和证据匹配方法；它不是本仓库新运行时依赖或独立 Gate。

## 3. 执行前完整产品、机制与真实入口检查

从完整用户承诺独立审，不要只关闭上一轮 Critic 的三个具体条件。需要核对：

**A. 稳定用户实际需求。** 每轮进度与 verdict 原因、可否决的具体技术选择、正常成功链和关键危险失败链、来源强度、中文阅读价值、多轮不丢架构、用户最小复制动作、实际下一接收者。当前 Proposal 第 1 节本身是否已把这些真实机制讲清？不能仅因段落存在就认定对用户充分。

**B. 被审用户说明的单一身份。** 第 1 节 `用户决策说明` 是否由 proposal path、version、exact package commit 唯一定位？Plan/Goal/Kickoff 是否引用同一来源而非制造副本？技术实质返修时更新，Critic 是否复核所有实质修改、不会拿旧 PASS 证明新架构？不要求每个复杂系统统一段落长度。

**C. 独立 Critic 技术权威。** 现有角色只有 Planner 和独立 Critic。Critic 从用户要求及源码真正判断技术方案，`PASS` 一次，不能靠 Plan 自评。没有 repo 写权限时怎样把实际 findings/verdict/身份完整传给原 Planner？受审对象缺失或过期时是否可真正停止？

**D. 下一接收 Planner 的独立交付检查。** 只允许从 Critic 原始 findings 和已审 Proposal 修复叙述，不得新创技术结论、改变授权或删除限制；若原独立技术审查不足必须退回 Critic。是不是新增第二技术裁决者？如果质量差的 Critic PASS 仍可直接产出 Codex 提示词，则该提案没解决用户原问题。

**E. 最终 PASS 的改路由是否值得。** 只在未来正式 1.8 生效后的插件/Bridge 任务：Critic 技术 PASS 后 `NEXT_HANDOFF=PLANNER`，该原 Planner 一次读者接受，才有短 Codex 入口；无第三人/新状态。成本是最终技术 PASS 后用户多一次机械转发。当前任务自身的首次 1.8 实施批准仍遵正式 1.7 直达 Codex。若对此存在冲突，不能留给 Codex 猜，应 `REVISE` 最小修正。

**F. 早期 1.8 正确能力不能丢。** task-specific prompt 与中央合同冲突、关键接口 actor/input/output/materialization/conditional evidence、Phase C STOP 的真实下一责任、PASS 后解释与新证据、同候选回归及实际 main 合入读回；没有真实自动 Web 浏览器控制不能假装会自动开 fresh 会话。

**G. 是否过度设计。** 本版不改 Project setting/AGENTS、第三角色、Mica/Bridge、付费/后台服务、发行版。计划若将测试文本/字数判分升级成专业语义证明或为安全感增加新控制层，应阻塞。反过来如果 Critic 认为必须改现有用户入口才能完成承诺，应提供当前事实与明确 owner，不得假设已支持。

## 4. 执行包、授权与验证可行性

检查 Codex 收到**本次**批准短入口后，能在已有 `design/chatgpt-web--pass-integrity-v0-4` branch、实际已授权目标 checkout 做冻结文本修改与测试；当前环境不匹配或需新 worktree 时本 Plan 要求先停止并报告，不得默默使用旧 `/tmp` 工作树。需核对现行 AGENTS/Bridge 对 Git、实际权限和集成的规则，不应让普通机器定位替代产品设计。是否有真正不可推迟的高影响用户决定留给 Codex？有则 REVISE；合法普通源码读取/环境预检可以留执行开始。

逐一检查同版 Validation Contract 的 A（错误旧包）、B（Phase C 非终态）、C（复杂技术 PASS 与原 Planner 接收）、D（真实多轮技术变化）、正式 main 后首个新任务，及旧 deterministic eight-case 回归。不同场景实际证明何种能力，生成线程是否被喂答案、历史正例是否被强迫 PASS、质量评审是否能看到用户完整答复、失败时是否有原责任方/恢复、用户必要 Web UI 操作是否实际可行、成本是否有界。旧已见不能冒充 fresh，新任务出现之前不声称长期默认可靠。

看候选冻结的真实来源/身份、实现后独立 `PROCEED_TO_FINAL_EVALUATION/REVISE` 入口、正常评估与合入 main/远端回读如何发生；只有真正执行/观察才能说已生效。不能用未来实际例子还没出现为由，要求在当前设计阶段凭空造新任务；应核实“未验证”状态如何保留，是否不妨碍合法的阶段性结论。

## 5. 你的回复本身也要符合用户标准

先给真实用户能看懂的自然中文：本包究竟批准了什么、为什么最终 PASS 交 Planner 有意义、比旧治理增加哪一条真正的交叉验收、会不会增加大量额外人工工作、真实当前能做什么以及尚未证明什么。可用实际技术机制与简短因果例子，但不能倒出所有文档路径/审计摘要。关键技术名称保留精确，不以减少英文作为质量本身。

若 `REVISE`，实质 blocker 逐项写事实、来源、因果风险、最小修复和真实责任方；保留已有正确设计，不移动终点。后面自动给原 Planner 完整、可复制的 `NEXT_HANDOFF=PLANNER` 和 `COPY TO PLANNER`，包含实际 package/ref 与 findings，不要求用户拼材料。

若唯一 execution-ready `PASS`，必须在同一回复中给 `READY_FOR_CODEX=YES`、批准准确 package/ref、自然中文架构说明、真实实现与未验证边界，并按**当前 1.7** 给短而可直接发送的 `COPY TO CODEX`。这仅批准同版本治理合同实现、必要只读真实验证与明确的 bounded 集成，不批准任何未经用户实际发送确认的费用/权限/发布动作。

不得自称“1.8 已生效”，不得拿你当前这个审查 PASS 证明未来用户回复长期都变好。若有不能直接访问的材料则限定事实边界，不凭想象认定实际通过。正式审查本轮只读，不修改仓库、个人插件、浏览器、集群或其它项目。
