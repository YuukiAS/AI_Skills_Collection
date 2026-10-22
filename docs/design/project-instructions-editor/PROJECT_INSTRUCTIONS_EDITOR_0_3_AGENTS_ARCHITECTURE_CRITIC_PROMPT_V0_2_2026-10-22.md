# PIE 0.3：AGENTS 模板归属、真实整理流程与自动调用——独立 Critic 审查 v0.2

你是 AI Research Stack 的**全新独立架构 Critic**。不要预设 PIE 必须继续扩展，也不要仅把上次 0.3 v0.1 当作正确答案。本轮专门审查经过用户否定、重写后的 v0.2 提案。

这是**设计阶段**，只准输出 `PROCEED` 或 `REVISE`；不得给 `PASS`、`READY_FOR_CODEX=YES`、Codex Goal，不得实施或修改任何生产代码/Bridge/消费者 AGENTS。

## 审查绑定

~~~text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = standalone Skill / project-instructions-editor
design_topic_or_task_key = project-instructions-editor--0.3-agents-authority-maintenance
source_branch_or_ref = main
review_stage = ARCHITECTURE_REVIEW_V0_2
proposal_path = docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_0_3_AGENTS_ARCHITECTURE_PROPOSAL_V0_2_2026-10-22.md
proposal_commit = a1da221b9bdc2c18fb163b6c4e1471a2d0b2b94c
tracking_issue = YuukiAS/AI_Skills_Collection#108
~~~

若当前 `main` 相对受审提交有相关变化，核对后说明。上一轮 v0.1 是历史设计，不是本轮通过结论。

## 首先读取真实规范，而非 Planner 摘要

从 `YuukiAS/AI_Research_Toolkit/main` 读取：

- `COMPLEX_ARCHITECTURE_EXPLANATION_STANDARD.md`
- `COMPLEX_SYSTEM_DESIGN_GUIDE.md`

这些要求说明实际用户故事、因果机制、真实调用链和证据等级；不因为 Proposal 写了很多模块名就称解释成功。

从 `YuukiAS/AI_Skills_Collection/main` 读取：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/skill-todos/project-instructions-editor.md`
- `skills/core/codex-system/project-instructions-editor/SKILL.md`
- `skills/core/codex-system/project-instructions-editor/agents/openai.yaml`
- `skills/core/codex-system/project-instructions-editor/evals/trigger_queries.json`
- `skills/core/codex-system/project-instructions-editor/references/editor-contract.md`
- `shared/templates/AGENTS.md.template`
- `docs/INSTALLATION.md`
- Issue #108 及已知版本/安装状态。

从 `YuukiAS/GPT_Codex_AI_Bridge_Kit/main` 读取 `AGENTS.md`、`templates/repo/AGENTS_TEMPLATE.md`、`ai_bridge_kit/cli.py` 的 `projected_agents_snippet` / `install_agents_snippet`、写入前容量验证实现及对应测试。核实真实行为：没有根文件时创建什么、有根文件时修改什么、`--force` 的边界、是否向现有仓库迁移模板。

从 `YuukiAS/SeminarArc/main` 读取 `AGENTS.md`、`docs/DEVICE_TESTING.md`、`TODO.md`、`prompts/AGENT_RULES.md`。按真实语义独立判断 v0.2 的目标结构示例有没有错误删弱受保护规则、混淆历史 `0.1.x` 与当前路线图，或假设不真实存在的入口。

从 `YuukiAS/AI_Research_Toolkit` 的 `research/software-production-decision-20261013` 分支读取：

`docs/research/software-production/16_THREE_RUN_SYNTHESIS_AND_DELIVERY_ASSURANCE_20261015/DELIVERY_ASSURANCE_AGENTS_LIFECYCLE_AND_PIE_0_3_REQUIREMENTS_V0_1_20261019.md`

这是 Delivery Assurance 需求输入，不代表其中全部 schema 已成为 PIE 源码。独立检查受管任务三件套、`workflow-core` 自动维护义务与 v0.2 的边界是否兼容。

针对性核查 OpenAI 当前官方资料：

- https://developers.openai.com/codex/agent-configuration/agents-md
- https://developers.openai.com/plugins/concepts/skills
- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/plugins/concepts/plugins
- https://openai.com/index/harness-engineering/

## 六个必须给出实质判断的问题

**一、Bridge 模板应当留下还是迁移？**
阅读实际 `ai-bridge init` 后明确判断：Bridge 保留原始结构模板、PIE 负责项目长期维护，是否是最小充分方案？没有 Bridge 的仓库是否仍可创建 `AGENTS.md`？模板更新以后不迁移旧仓库是否合理？现有两个 managed block 的 owner 是否唯一？不能只说“职责清晰”。

**二、未来 AGENTS 架构是否足以实际使用？**
用真实 SeminarArc 核对：根文件保留了哪些行动前安全底线；深层文档存了什么；哪些指令会条件读取；版本/目录/嵌套如何处理。特别审 `AGENTS.override.md` 遮蔽、`CODEX_HOME`、fallback 和 `project_doc_max_bytes`。若拟议示例不能在真实项目中保留全部有效不变量，就要求 `REVISE` 并点出具体缺失，不因它比旧版短而放行。

**三、一次正常整理是否真的闭合？**
独立走完整链：用户提出自然请求 → 技能是否被发现并实际读取 → exact 当前文件和权威 → 冲突与保真 → 完整候选及带标记预览 → 已授权写入 → 写后读回 → 用户看到具体变化 → 在需要证明加载时由正确 owner 用新会话复验。任何箭头没有真实消费者或执行主体，指出准确缺口。用一个正例、一个安全失败例和一个不应修改的普通代码任务检验。

**四、Codex 的“自动”到底是什么？**
检查现在 `allow_implicit_invocation: true` 是否只表示允许调用，而不是成功；尤其核实 0.2 `trigger_queries.json` 把 AGENTS 请求放在 near_miss。判断修改 metadata + 现有技能索引后，真实新会话自然任务能否足够可靠地调用；如果需要 Bridge/Host/DA 的另一个触发入口，必须给出最小具体方案及 owner，不能让实施 Codex 临场猜，也不能降级为手动 `$skill` 仍称自动。区分「未发现技能」「未加载 AGENTS」「加载了但没遵守」。

**五、PIE 内部是否太重或太轻？**
评审 v0.2 的四个逻辑步骤、现有 v0.2 Project setting 兼容、managed block 字节保护、多文件编辑、冲突停止、受管 DA 任务与普通任务不同证据要求。不准要求为普通一行修改新建 registry/daemon/几份证据；但也不能让 DA 受管任务逃避已经批准的完整证据义务。

**六、是否选对产品形态？**
独立比较扩展现有 standalone Skill、新独立 `repository-agents-editor`、中央 Plugin、Bridge 全权维护、继续专项手工整理。比较真正的用户摩擦、可读性、触发歧义、跨宿主分发、原有 PIE 回归风险和长期成本。若更优路线存在，可否决 v0.2。

## 结论和交接

先用中文说清楚：真实架构是什么，用户怎样整理一次 AGENTS，模板在哪里，现阶段哪部分尚未实现，是否满足用户的自动调用要求。指出最多真正阻止设计继续的关键问题，而不是制造新的无关控制层。

然后给唯一判断：

~~~text
REVIEW_OBJECT = PIE_0_3_AGENTS_ARCHITECTURE_V0_2
REVIEW_COMMIT = a1da221b9bdc2c18fb163b6c4e1471a2d0b2b94c
DECISION = PROCEED | REVISE
BLOCKERS = <none or specific evidence-backed defects>
NEXT_HANDOFF = PLANNER
READY_FOR_CODEX = NO
~~~

`PROCEED` 仅允许 Planner 准备实现方案、正式 Capability Gate 与 execution-ready 复核；不能修改正式代码或消费者仓库。Critic 本轮不能冒充实现验收，也不能要求用户自己同步 GitHub 看板。
