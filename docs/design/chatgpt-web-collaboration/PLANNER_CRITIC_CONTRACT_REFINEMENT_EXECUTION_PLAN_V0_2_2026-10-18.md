# Planner / Critic 合同完善实施计划 v0.2

日期：2026-10-18  
状态：待 execution-ready Critic 审查  
设计依据：`docs/design/chatgpt-web-collaboration/PLANNER_CRITIC_CONTRACT_REFINEMENT_V0_2_2026-10-18.md`  
设计结论：用户转交的独立 Critic 已对 v0.2 给出 PASS；B1、B2 均关闭。  
任务：`chatgpt-web--planner-critic-contract-refinement`

## 1. 目标与边界

本实施只把已经批准的 v0.2 规则整合进现有两份角色合同：

- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`

两份合同版本从 1.4 升到 1.5。这里的 1.5 是角色合同自己的文档版本，不触发 AI_Skills repository 或任何 Plugin 版本升级。

本实施不重新设计九类问题的解决方案，不修改：

- `workflow-core`；
- 任何 Plugin / Skill；
- Bridge Kit；
- Reviewed Handoff / Control；
- Reviewer / Verifier / Terra 的既有机器或自动审查协议；
- AI Research Stack Project setting；
- GitHub Project schema；
- 任何运行时、状态机、自动任务或外部服务。

Repository bump decision: NONE。  
Affected plugins: none。

## 2. 执行位置与发布边界

执行目标分支：`main`。

Codex 使用机器上现有的 `YuukiAS/AI_Skills_Collection` canonical checkout，确认当前分支为 `main`、remote 指向正确仓库、工作区可安全修改后执行。不得为了本任务创建或切换新 branch / worktree。

本任务只允许修改上述两份合同。执行过程中发现其他文件似乎也需要修改时，先停止扩项并报告；不得顺手同步 Project setting、Bridge、AGENTS、README、Plugin 或其他 workflow 文件。

用户发送经 Critic 批准的 kickoff 后，视为对以下 bounded effect 的当前授权：

- 修改上述两份合同；
- 运行只读或本地 deterministic 验证；
- 提交仅包含这两份合同的 commit；
- 验证通过后对当前 `main` 做普通非强制 push 到 `origin/main`。

不授权 force push、rebase/autostash、reset/clean/restore、remote mutation、branch 创建/切换/删除、PR、release、部署、付费调用、私有数据传输或其他副作用。

## 3. Planner 合同的精确整合范围

目标文件：`docs/workflows/PLANNER_ROLE_CONTRACT.md`。

不要复制 v0.2 proposal 全文。把批准语义放回现有最合适章节。

### 3.1 文档版本

- 版本：1.4 → 1.5。
- 日期更新为 2026-10-18。

### 3.2 §2.1 Active Design Context：人类版本与机器定位分离

保留现有 task key / branch / path / commit 机器定位规则，并补充：

- 新的人类方案版本默认使用简单连续版本，如 `v0.1`、`v0.2`、`v1`、`v2`；
- alpha / beta / rc 只在确有成熟度语义时使用；
- 历史 `C11`、`R0`、Gate/批次编号等只作为已有 locator 兼容；
- 不新造 `C'` 一类临时人类版本体系。

不得重命名历史文件或 task key。

### 3.3 §4 / §6：正常使用六问、owner-first 与关键决定摘要

在现有五遍预检和提案最低内容中自然整合，不另建第二套 checklist。

对于会改变工作方式的工作流、架构、长期任务、权限/恢复或自动化设计，Planner 在送 Critic 前按适用范围能回答：

1. 用户怎样开始；
2. 正常运行时实际发生什么、用户能看到什么；
3. 哪些重要行为有默认值，哪些能逐任务配置；
4. 高影响或危险动作由哪一个真实层拦截或审批；
5. 失败、断线、等待或自动轮次耗尽后怎样恢复；
6. 当前阶段结束后用户侧下一入口是什么；若既有重型工作流会自动进入内部 Reviewer / Verifier / Terra 等后置环节，只说明该既有自动路径，不要求用户手工选角色。

任何核心能力若仍只能回答“以后再设计”“理论上可以”，不得提交 execution-ready package。

同一位置补强 owner-first：

- 跨组件设计先确认 canonical owner；
- 已有 owner / 调度器 / 平台原生机制 / 服务管理器 / 领域能力 / Bridge 正常入口能承担职责时优先复用或轻量适配；
- 新增控制层、路由器、watcher、状态机、长期服务前必须说明现有 owner 的具体不足和新增复杂度阻止的真实失败；
- 发现相邻 owner 的问题默认记录证据并交回 owner，除非职责调整本身已经进入批准范围。

复杂方案送 Critic 时应有简短“用户关键决定摘要”，只覆盖真正影响用户理解的机制、默认值、逐任务配置、安全/权限、通知/费用/外部副作用和恢复；不得把它写成第二份 Plan。

### 3.4 §10.1 / §11：用户侧角色、非终态续航与 Codex 前置门

保持 Planner/Critic 两线程的既有独立性，并整合以下批准语义：

- ChatGPT Web 人工协作角色只有 Planner 与 Critic；
- Codex 是批准后的执行入口，不是第三个 ChatGPT Web 人工角色；
- Reviewer / Verifier / Terra 只在既有 Bridge Kit / Reviewed Handoff / Control 等明确重型流程本来要求时按原协议工作，不因本合同新增；
- 不要求用户手工选择 Reviewer / Terra。

Planner 处理外部审查结果、既有自动 Reviewer / Verifier / Terra 结果、执行中断或恢复结果时，只要不是终态，就必须确定唯一下一用户入口：

- 需要改设计/范围/职责/恢复语义 → Planner；
- 需要新的独立方案审查/复核 → Critic；
- 前置设计和审查完成 → Codex 执行入口；
- 真正 user-only 的选择/私有上传/必要授权 → 最小用户动作，完成后继续给出对应入口。

若既有重型流程的自动 Reviewer / Verifier / Terra 已真实绑定并可用，说明会按原协议自动继续；若不存在、已耗尽或不可用，不得假装接手，应按语义回 Planner 或 Critic。

任何 Codex handoff / Kickoff 在送 execution-ready Critic 前必须确认：

> Codex 开始当前批准的实质执行之前，不再存在未完成的 Planner 决策、Critic 审查或用户必要产品/授权选择。

Codex 可以在执行开始后做正常 source read、环境确认、安全 preflight，但这些只验证已冻结执行条件，不得承担“先 probe 再发现还缺设计/审查/用户选择”的职责。

实现完成后的既有 Reviewer / Terra / Verifier 后置审查不属于该前置门，不阻止 Codex kickoff。

### 3.5 §12：机制级事故的一跳邻域检查

在现有 incident 归因里补充：

当真实失败证明的是机制级缺口而非单例数据/环境故障时，Planner 在提出修复前检查同一因果机制的一跳邻域，例如成功/失败/恢复、首轮/轮次耗尽、自动接手有/无、权限允许/拒绝或同 owner 邻近入口。

只检查直接共享因果机制的邻域，不扩成全仓/全系统审计，不借此制造 successor 链。

## 4. Critic 合同的精确整合范围

目标文件：`docs/workflows/CRITIC_ROLE_CONTRACT.md`。

同样不得复制 v0.2 proposal 全文。

### 4.1 文档版本

- 版本：1.4 → 1.5。
- 日期更新为 2026-10-18。

### 4.2 §1 / §2.1：用户侧角色与人类版本

明确：

- ChatGPT Web 人工协作角色只有 Planner 与 Critic；
- Critic 是用户手工切换独立审查线程时的审查角色；
- Codex 是批准后的执行入口，不是第三个人工角色；
- Reviewer / Verifier / Terra 只在既有重型工作流本来要求时按其原协议工作；
- 不要求用户手工选择 Reviewer / Terra，也不修改其机器协议。

Active Review Context 中同步人类版本规则：新方案用简单连续版本；历史 locator 保留，不新造临时版本体系。

### 4.3 §4：从六个核心判断扩为七个，并强化过重设计检查

保留 A–F，新增一个正常用户路径判断。Critic 按适用范围独立追问：

- 怎么开始；
- 正常运行发生什么；
- 用户看到什么、能配置什么；
- 危险/高影响动作由哪一真实层阻断；
- 失败、断线、等待、轮次耗尽怎样恢复；
- 当前阶段结束后用户侧下一入口是什么；若既有重型工作流存在后置自动 Reviewer / Verifier / Terra，确认它属于原协议且真实存在。

核心承诺若只有“以后再补”“理论上可以”，则 REVISE。

在现有“是否过重或过简”中补强：

- 新路由器 / watcher / 状态机 / 长期服务 / 控制层必须正面证明已有 owner 为什么不足；
- 跨 owner 修改必须证明职责调整本身已批准；
- “为了统一”“更保险”“以后可能有用”不能成为充分理由；
- 成熟平台或现有 owner 能满足时，多余层应成为 blocker，而不只是可选优化。

### 4.4 §6：PASS 范围、用户机制说明与非终态下一入口

所有实质 PASS 的自然中文结论都必须明确：

- 本次批准了什么；
- 本次不代表什么。

不得让设计 PASS 被后续叙述成实现完成、正常入口可用或正式发布。

把当前 §6.3 从“曾经 REVISE 后的最终 PASS 才需要完整说明”扩为所有实质设计 / execution-ready PASS 的比例化用户说明。按当前对象真正相关的内容解释：

- 关键机制怎样工作；
- 用户正常使用看到什么；
- 默认行为与逐任务配置；
- 权限、安全或危险动作由哪一真实层执行；
- 通知、费用、外部副作用何时发生；
- 失败、断线、轮次耗尽怎样恢复；
- 哪些仍未实现、未验证或不在本次 PASS；
- 下一用户入口。

复杂方案只解释最重要的 5–10 个决定；简单方案保持简短。不得复制整份 Plan 或让路径、字段、测试名占据正文。

非终态仍沿用已有自动 prompt 机制，但用户人工入口只在 Planner / Critic 中选择；若已经 execution-ready，则给 Codex 执行入口。既有重型工作流中的内部自动 Reviewer / Verifier / Terra 可说明会按原协议自动继续，但不得要求用户手工转发。

### 4.5 §6.1：Codex execution-ready 前置依赖硬门

保留 Proposal / Goal / Kickoff 同版审查，增加：

> `READY_FOR_CODEX=YES` 前，Codex 开始当前批准的实质执行所需的 Planner 决策、Critic 审查以及用户必要产品/授权选择必须全部完成。

若 kickoff 预计让 Codex 只做 read / inspect / preflight / probe，随后才发现或决定上述关键事项，则不可 `READY_FOR_CODEX=YES`。

正常任务内读取、环境确认、安全 preflight 不被禁止，只要服务于已批准执行。

若当前任务采用既有 Bridge Kit / Reviewed Handoff / Control 重型工作流，且其原协议规定实现后由 Reviewer / Terra / Verifier 做后置审查，该后置审查无需在 kickoff 前完成，不构成 blocker。本合同不新增 execution segment、角色、状态机或 review protocol。

### 4.6 §9：机制 blocker 关闭前的一跳反证

机制级 blocker 关闭前，Critic 检查 Planner 是否覆盖同一因果机制的一跳邻域。不得借此无限新增 blocker；只有直接共享因果机制的相邻失败才能要求补齐。

## 5. 九类问题与实施落点

| 问题 | Planner 合同 | Critic 合同 |
|---|---|---|
| 1. PASS 后一问就露洞 | 正常使用六问 | 新增用户路径反证 |
| 2. PASS 范围膨胀 | 保留阶段绑定 | 明确“批准什么 / 不代表什么” |
| 3. 角色混乱 | 人工角色仅 Planner / Critic，Codex 为执行入口 | Critic 为唯一人工独立审查角色 |
| 4. 非终态不知道给谁 | 唯一下一用户入口 | REVISE/非终态必须给唯一入口和完整 prompt |
| 5. 伪 Codex handoff | 前置依赖关闭门 | `READY_FOR_CODEX` 同一硬门，后置 Reviewer 例外 |
| 6. 地鼠式回归 | 机制级一跳邻域检查 | blocker 关闭前同一检查 |
| 7. 越界与过重设计 | owner-first | 新层必须正面举证，否则阻塞 |
| 8. 临时版本体系 | 简单连续人类版本 | 审查同一规则 |
| 9. PASS 后不知道批准内容 | 用户关键决定摘要 | 所有实质 PASS 的比例化机制说明 |

## 6. 验证

Codex 完成编辑后必须至少执行以下相称验证：

1. 重新读取两份完整合同，确认版本均为 1.5、日期正确。
2. `git diff --check`。
3. `git diff --name-only <base>..HEAD` 或等价检查，确认 implementation commit 只修改两份合同。
4. 对照批准的 v0.2，逐项检查 P1–P7、C1–C9 均有明确且唯一的合同落点，没有复制第二套平行规则。
5. 专门检查 B1：
   - 不把 Codex 描述为第三个 ChatGPT Web 人工角色；
   - 不要求普通用户手工选择 Reviewer / Terra；
   - 不修改既有 Reviewer / Verifier / Terra 机器协议。
6. 专门检查 B2：
   - `READY_FOR_CODEX` 前置依赖门存在；
   - task-local read / preflight 仍允许；
   - 后置既有 Reviewer / Terra / Verifier 不被误判为 kickoff 前置 blocker。
7. 检查没有新增状态枚举、角色、execution segment、review protocol、watcher、daemon、数据库或控制层。
8. 检查没有修改 `workflow-core`、Plugin/Skill、Bridge、Project setting、AGENTS、README 或其他文件。
9. 对人类可读正文做一次语言检查：新增规则应使用自然中文解释，不以内部英文流程词堆叠替代含义；精确机器字符串保持原样。

不要求运行全仓测试矩阵，因为本任务只改两份 Markdown 合同，没有 production code / generated payload / plugin runtime 变化。若仓库存在专门针对这两份合同的轻量 deterministic 文档检查，可运行；不得为了“更稳”升级为无关 full CI。

## 7. 完成标准

只有同时满足以下条件才可报告实施完成：

- 两份正式合同均更新到 1.5；
- 实施内容与 v0.2 一致；
- 九类问题均有合同落点；
- B1 / B2 语义没有回归；
- diff 仅包含两份合同；
- 验证通过；
- 已提交并按 kickoff 授权普通非强制 push 到 `origin/main`；
- 最终回复用自然中文说明改了什么、九类问题分别落到哪里，以及哪些层明确没有改。

如果执行时发现 v0.2 无法无歧义落入现有合同、需要改变已批准语义或必须修改第三个文件，停止并返回 Planner，不自行扩项。
