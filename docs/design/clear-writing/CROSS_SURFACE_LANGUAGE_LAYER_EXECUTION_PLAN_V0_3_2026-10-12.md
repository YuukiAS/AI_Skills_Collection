# Clear Writing 跨 ChatGPT / Codex — 执行方案 v0.3

- 状态：`DRAFT_FOR_EXECUTION_READY_CRITIC`，没有执行前 PASS，不得启动实现。
- 仓库：`YuukiAS/AI_Skills_Collection`；规划分支：`planner/clear-writing-cross-surface-v0.1`
- 架构依据：用户转述独立 Critic 对 `819f861de7dc626f473390df8a9c42b70d24dd92` 的架构阶段 PASS，并明确要求精简路线；原 Critic 全文未在仓库，不假称有正式仓库审查文件。
- 同版权威：`CROSS_SURFACE_LANGUAGE_LAYER_PROPOSAL_V0_3_2026-10-12.md`、`CROSS_SURFACE_LANGUAGE_LAYER_GATE_MATRIX_V0_3_2026-10-12.md`、`docs/goals/CLEAR_WRITING_CROSS_SURFACE_LANGUAGE_LAYER_GOAL_V0_3.md`、`docs/operations/prompts/CLEAR_WRITING_CROSS_SURFACE_LANGUAGE_LAYER_KICKOFF_V0_3.md`
- 跟踪：Issue #13；保留已发布前端文案能力与 Issue #90，不重做另一项任务。
- 最近实测仓库：`main@34e47fe6d0dc06d57ee1e6e37c0ff0f2fdfefc1b`，`VERSION=5.4.4`，`writing-style=0.4`；此身份为设计期事实，不可替代未来执行时的主线或发行基线。

## 1. 任务、角色及人工交接

唯一目标：普通 ChatGPT 的 Project 内/外首答可阅读、不要求每轮 `@Clear Writing`；Codex 的真实写作、界面、演示文稿和技术结果说明任务按场景选择已有表达能力；同一源和合法正式安装；保真、精确机器内容与现有五项能力不退化。

采用仓库现有 Reviewed Handoff，不自建状态机、守护程序、调度器或另一层自动化。用户实际发送**经本轮独立执行前 Critic PASS 的 Kickoff** 才授权建立任务；后续默认**人工 Planner/Reviewer 接手**，不宣称一次 Kickoff 自动完成全部流程。

`task_key = clear-writing--cross-surface-language-layer`
`reviewed_branch = reviewed/clear-writing--cross-surface-language-layer`
`sibling_worktree = <经现场核对的 canonical checkout 父目录>/AI_Skills_Collection-clear-writing--cross-surface-language-layer`
`base = 届时 fetch origin/main 后的精确提交`
`max_review_rounds = 2`
`ci_required = true`
`paid_text_review = false`
`paid_visual_review = false`

真实执行前读取执行时最新 Bridge Kit `AGENTS.md`、正式实现及本仓库 `automation/reviewed_handoff/README.md`；核验 repo、canonical checkout、HTTPS origin、最新同步的 `origin/main`、task branch、派生工作树与现有状态，不临时换路径或绕过 Bridge。**CW-ER-01 的首次交接必须遵守如下顺序，完成远端核验后才可交人工 Planner：**

1. **冻结远端可读的权威**。用户将来发送获批准 Kickoff 时必须明确给出 `APPROVED_V03_PACKAGE_COMMIT`（完整六份 v0.3 执行包的不可变 40 位提交）、所有六份文档的准确路径、以及真正的独立执行前 Critic 评审文件 `EXECUTION_CRITIC_REVIEW_PATH@EXECUTION_CRITIC_REVIEW_COMMIT`。审查记录须真实存在、以精确 Git 提交可读，明确 `PASS / READY_FOR_CODEX=YES` 并绑定同一 v0.3 包；用户转述的先前 v0.2 `REVISE` 不得冒充。任何缺失时停止，不能先 bootstrap。
2. **仅本地 bootstrap**。从核实过的 canonical checkout 运行一次 `ai-bridge reviewed-handoff task bootstrap`，以当时已同步 `origin/main` SHA 为 `--expected-base-commit`。这个入口只创建本地 `reviewed/clear-writing--cross-surface-language-layer`、Bridge 派生的 sibling worktree 及未提交的首份 `REQUEST.md`、`CURRENT.json`；不会自动提交或发布远端。
3. **进入派生 reviewed 工作树，补足首次 REQUEST**。在 `automation/reviewed_handoff/tasks/clear-writing--cross-surface-language-layer/REQUEST.md` 保留 bootstrap 创建的任务身份、工作树定位与原有内容，明确追加：`APPROVED_V03_PACKAGE_COMMIT`、该提交内完整六份 v0.3 合同的路径、`EXECUTION_CRITIC_REVIEW_PATH`、`EXECUTION_CRITIC_REVIEW_COMMIT`、PASS 的绑定对象。这个 reviewed 分支从 `main` 派生，可能没有规划分支新文档；后续 Planner 必须通过这些不可变提交在 GitHub/只读 Git 获得设计，**不得要求把六份文档作为第三个首次提交文件**。`CURRENT.json` 保持 bootstrap 的合法原始状态。
4. **只提交 REQUEST/CURRENT 的首个直接子提交**。在相同 reviewed 工作树检查 `CURRENT.base_branch=main`、`base_commit=bootstrap 用的 origin/main SHA`、`state=PLAN_REQUESTED`、`next_action=RUN_GPT_PLANNER`、`review_round=plan_revision=0`、`implementation_commit=null`，以及 REQUEST 中的真实 sibling locator。只暂存新任务路径中的 `REQUEST.md`、`CURRENT.json`，先检查暂存差异恰好为两个 `A`；然后普通 `git commit` **只产生一个**直接继承 `CURRENT.base_commit` 的提交，原始树差异恰好是新增这两份元数据。不能有 PLAN、结果、生产源码或其它文件，不能增第二个提交/merge；确认工作树干净。
5. **正式首次远端发布**。仍在该 reviewed 工作树核对无上游、远端同名 reviewed 分支不存在，调用 `ai-bridge reviewed-handoff task publish-first --task-key clear-writing--cross-surface-language-layer --expected-repo YuukiAS/AI_Skills_Collection`。Bridge 的原始对象、单父提交、两文件和空期望租约等边界必须全部通过；不得转用 raw `git push`、`git push -u`、`--force` 或另建任务。结果不明确时保留证据并停止，不盲目重复推送。
6. **远端回读并交人工 Planner**。通过只读 Git/ GitHub 检查 `origin/reviewed/clear-writing--cross-surface-language-layer` 的远端 SHA 正好等于唯一基线提交、上游绑定正确、工作树干净；远端 REQUEST 必须含正确的六份合同路径、获批准不可变包提交与 Critic review 的路径/提交，远端 CURRENT 必须保持 `PLAN_REQUESTED / RUN_GPT_PLANNER`、正确 task/base/轮次与空 implementation。还需证明该规划提交和 review 提交按远端可取得。全部通过之后才向长期 Planner 发送准确 reviewed 分支、基线 SHA 和 `next_action=RUN_GPT_PLANNER`。

Planner 从**已发布的** reviewed 分支读取 `REQUEST/CURRENT`，再按首次 REQUEST 精确引用读规划分支六份 v0.3 合同与真实执行前 Critic PASS，写入并核对 `AI_BRIDGE_REVIEWED_PLAN_V2` task-local PLAN，最后合法从 `PLAN_REQUESTED` 推进 `PLAN_FROZEN / RUN_CODEX_EXECUTOR`。Executor 不能自写、自批 PLAN；未完成首次远端核验不允许提早交接。

## 2. 实际源码、配置与改动范围

核心允许文件范围：

- 新增 `skills/writing/core/response-clarity/SKILL.md`；按需有一个精简参考文件与 `evals/trigger_queries.json`（正向、间接、近似、排除场景）。
- 在 `skills/writing/core/chinese-prose/SKILL.md` 仅收紧触发描述和真正冲突的少量指令：普通用户对话与既有中文文档成稿须清楚区分。保留 `chinese-prose` 原名及中文报告/README/资料工作。
- `skills/writing/core/writing-fidelity/` 仍是统一保真原则负责人。每项可被单独选中的技能都要**在自己的实际加载内容中**具备适用的简短约束；不能假定额外 `writing-fidelity` 或其它技能按确定顺序调用。先核对现有五项保护条款，只补证据显示的缺口，避免另建同义规则。
- 保留 `scientific-prose`、`scientific-rewrite`、`product-ui-copy` 全部正式名称及原有专业职责。特别禁止改写 `scientific-rewrite` 的中文/中文主导复杂源重写含义映射、读者计划、中文实现、整篇组装与保真主链。
- 修改 `scripts/codex_marketplace_config.json` 中唯一 `writing-style` 项：增加 `source=skills/writing/core/response-clarity` 和 `artifact_id=response-clarity`，更新合适的插件描述/示例提示词；旧五项的 `artifact_id` 为 `fidelity`、`sci`、`scientific-rewrite`、`product-ui-copy`、`zh`，一律不动。示例提示词不承诺每轮强制使用。
- 使用原有 `scripts/build_codex_marketplace.py` 生成 `plugins/codex/plugins/writing-style/`、`.agents/plugins/marketplace.json`，按实际必要更新回归测试、生成一致性核对及 `profiles/codex-writing-style.json`；配置能工作时不得新增并行插件构建系统。
- 评估与结果只放在 `results/clear-writing--cross-surface-language-layer/`；私有账号资料、用户聊天、真实 Project 指令及敏感附件只可进入获得授权的 `private/exports/clear-writing--cross-surface-language-layer/` 或当前用户批准的私密载体，不可公开提交。

**硬排除**：Research Authoring（正式源码、个人插件、打包、安装、测试/迁移）、PIE 0.2、Plugin Creator 未授权的线上操作、Project Thread Handoff、Bridge Kit、其它中央插件源码；Frontend Design 与 Presentations 现有交接入口默认只读并验收，不搞无收益重构。若真正暴露现有消费者的生产缺陷，需要 Planner/Critic 单独复核授权范围。

## 3. 专业场景的正常路由

`response-clarity` 处理同一轮中已经形成领域判断后的普通解释：先给结论和实际含义，把不必要的英文来源用语、长日志与机器标签变成自然目标语言，按信息结构写段落，但不得产生新事实、重断定完成或改受保护字符串。纯 JSON/YAML、代码、逐字引用、原始日志请求无解释时完全绕过；混合请求只重写解释层。

`chinese-prose` 处理中文文档/报告/README/普通修稿，`scientific-prose` 处理英文科研表述，`scientific-rewrite` 处理已有中文技术科研长文的完整源保真结构性重写，`product-ui-copy` 处理冻结产品语义后的界面短文案。`writing-fidelity` 可以独立审高风险改写，但其它技能单独加载也必须遵守自己可用的最小保真规则。

Codex 的 Frontend Design 已在 `skills/tools/frontend/frontend-visual-systems/SKILL.md` 交接 `product-ui-copy`，由前端负责内容架构、产品真实性和实际界面验收；Presentations 已在 `skills/tools/documents-media/presentations/shared/ppt-skill-routing.md` 交接 `writing-fidelity` 与中英文文案技能，仍由演示文稿负责人检查整套真实渲染。普通编程、统计与服务器场景向用户说明结果时用轻量解释，绝不改代码/日志。论文和报告的论点、证据、章节规划不属于 Clear Writing；**不调用或改动 Research Authoring**，可以使用公开安全且独立于它的原文作为普通语言任务的材料。

## 4. 两端实际打包与候选一致性

### Codex

用仓库正式 Marketplace 生成和安装候选，从新会话中的普通任务实测六条选择路径与不应触发的负例。优先使用现有 `scripts/candidate_plugin_replay.py` 与已验证的 `ai-bridge plugin-replay` 受控正式入口，先实际核对选项与环境，不自造嵌套 `codex exec`。不能以技能文件存在、主动要求使用插件、读取生成源码或仅运行单元测试替代正式安装行为。所有可发布关键证据绑定相同最终源提交和生成包指纹。

网页表面对复杂脚本有独立资格要求：`scientific-rewrite` 的重度中文重写可能使用 `rewrite_support.py` 一类本地帮助脚本。Plugin Creator 接受一个带代码文件的 ZIP，不等于普通 ChatGPT Web 一定执行这些脚本；必须用真实个人安装和源保真任务检查该表面是否支持。缺乏必要运行条件时，Web 该功能明确标为 `UNSUPPORTED/INCONCLUSIVE`，不得假装全部六项同等能力已在 Web 成立，也不得擅自删改重型流程。若这影响已批准的跨表面产品承诺，停止并返回 Planner/Critic 裁定。

### ChatGPT 个人 Web

由同一最终候选的**六项技能及必要支持文件**构建一个个人私有 `skills-only` Clear Writing 包。包装使用受支持的 `.codex-plugin/plugin.json`，不含 MCP、外部模型、钩子、账号密钥和服务；展示名 Clear Writing，个人包装分发版本按平台格式，例如 `0.5.0`，中央 `writing-style` 仍使用两段 `0.5`。必须记录最终源提交、各技能及支持文件哈希、包装 ZIP SHA256 和个人插件发行身份，不能因外壳版本不同误称不同语义实现。

Executor 在任务分支中生成确定的公开安全包装材料清单与可再现配方；由拥有 Plugin Creator 权限的 GPT Planner/Work 在获用户授权后**从固定公开 GitHub 提交重新获取相同源**并在自己的可访问容器内打包、哈希比对，才调用 Plugin Creator。不得假设 Codex 私人工作目录路径能在 ChatGPT 读取，也不得为方便而将私人测试聊天或凭据传到公共仓库。若正式 ZIP 不能通过这种受支持方式重建，G0 停止，报告准确接收/传输缺口；用户没有批准的新通道不可作为静默替代。

当前个人插件目录中尚未看到独立 Clear Writing。安装前重新查询，若不存在则最多创建**一个**私人 Clear Writing，若已存在则按唯一合法身份更新；以后优化同一候选使用有界版本更新，不累积多个同名插件。保留其他个人插件不动，尤其不碰冻结的 Research Authoring；若其他已安装技能造成不可区分的选择冲突，记录真实证据，不能偷删别的插件来制造通过。

### Project 与个性化的基础规则

有 Project：阅读当时有效的 Project 指令并把它作为语言/数学/机器内容合同；无 Project：有效全局个性化指令提供基础规则。Project 指令会覆盖全局规则，不把安装插件等同每个 Project 一定自动遵循。若测试需添加一条短激活桥，只能在用户批准的隔离或试点位置短暂进行，明确保存旧值与恢复方式，不批量改 Project；普通回答在插件未加载时仍靠独立生效的基础阅读合同保持可读性。

ChatGPT Project 的 G1 必须分别做 **A/E（基础语言合同相同、双方均无短桥）** 与 **B/C（基础语言合同和短桥相同）** 两组候选插件有无的匹配增量对照；D 显式 `@Clear Writing` 仍只作诊断。A＝候选无桥，E＝无候选无桥，B＝候选加桥，C＝无候选加同桥；各组除候选插件状态外应保持模型、任务、语言合同、次数和评审准则一致。Project 外另做固定个性化指令下有/无候选对照；无法合法、可靠建立匹配时记 `INCONCLUSIVE`，不归功于插件，不能用模型自述或仅一条成功回答代替完整首答证据。

## 5. 严格执行时序和恢复

1. **执行前审查**：独立 Critic 读 v0.3 Proposal、G0–G7、Plan、Goal、Kickoff 和现实源码；必须给准确版本的 `PASS / READY_FOR_CODEX=YES` 并写真实持久审查文件。仅有用户转述的架构 PASS 不可替代。
2. **用户 Kickoff、首次提交与远端交接**：获得批准后核验真实包提交、六份合同路径与执行前 Critic 的独立真实 review 提交；对最新主线、发行基线、Bridge、用户账号及插件能力作合法预检。按上文 CW-ER-01 顺序：bootstrap → 派生 reviewed 工作树内补 REQUEST → 只提交 REQUEST/CURRENT 的唯一直接子提交 → `task publish-first` → 远端 SHA/REQUEST/CURRENT/`RUN_GPT_PLANNER` 回读 → 人工 Planner 冻结 V2 PLAN。任何步骤缺失均不能先执行产品实现。
3. **开发与已知回归**：`workflow-core + ai-skills-core + writing-style` 同时参与；新增轻量技能、调整极少的描述与必要保真条款；跑直接/间接/边界/负例与现有五技能回归，保持普通软件操作精确。已曝光 C5–C11、050–055 或项目案例可重复用于修复，不称未见。
4. **代表性完整用户产物**：在不可调优的最终批次之前，先让独立阅读者看到完整普通聊天答复、中文/英文文稿、中文科研长文、实际 Web/应用界面渲染、整套演示文稿与对应来源；修复定性阅读发现的真实问题，防止最后才发现整篇仍像机器。
5. **同一生产候选冻结**：先核对当时最新主线/`origin/release` 的兼容差异，按照版本政策将正式候选源、插件版本、变更日志、生成包、必要 README、评分合同、代表性结果封成 `C_n`。要求同一最终候选进入预最终独立 Critic；一旦该审查后改变代码/包/评分/正式版本，旧通过失效并重新生成完整代表性证据。
6. **正式双端安装及 G0–G6**：获批准后创建/更新个人 Web 候选、核对发行身份，并从同一源安装 Codex 市场插件；完成 G1 **A/E 无桥匹配、B/C 同桥匹配**、D 显式诊断及无 Project 个性化有/无候选对照。若两组匹配无法真实建立，一律记 `INCONCLUSIVE`，不能归因插件增量；仍须检查完整首答、专业消费者、整套演示、界面、文稿、保真和多轮负例。失败时返回 Planner，而非声称隐藏强制终审。
7. **冻结未见样本及最终独立质量审查**：只有已知回归、真实完整产物与入口能够成立时，冻结未见批次及最大尝试次数，G7 在同一 `C_n` 的双端版本执行；不得换题、挑赢家、拼不同候选 PASS。科学语义与语言分别定性审查；真产品失败使该批候选失败。
8. **Reviewer、用户验收和集成**：Reviewer 必须实际获取完整来源、文字及渲染；人工 Planner/Reviewer 交接，不启用未经证实的定时恢复。项目 Gate 全通过并有用户最后明确接受后，才按正式仓库 release 合同正常合并、更新发行版本与插件个人正式身份；主线并发若触及发布关键路径，停回 Planner/Critic，不做 force/reset/rebase 覆盖。

基础设施、来源、真实插件缺陷、评审标准错误、授权/费用缺口与流程错误应分开归因。对已通过的公开安全开发回归可以有界修复；最终未见批次之后的失败不得靠增题或再次重试变成通过。回滚时恢复测试前记录的原个性化/Project 设置、同一个人插件旧发行、Codex 原正式版本；如个人插件是首次创建而无历史发行，不能谎称可以回滚到不存在的旧版，需依用户后续批准停用/卸载。回滚未确认成功不报发布完成。

## 6. 权限、费用及明确禁止

**当前只授权**在规划分支起草和提交文档以及只读研究。没有启动任何实现、个人插件创建、用户设置修改、外部服务或付费调用。

未来用户发送获批准的 Kickoff 后，才有权按准确任务身份做一次 Bridge bootstrap/任务分支、工作树、普通非强制发布；task-owned 技能/生成包/回归/版本/文档有限修改；零额外付费测试与公开安全资料的完整交付物；以及在用户个人范围内最多一个 Clear Writing 私有 Plugin Creator 身份的受控新建与后续候选更新。账户安装/测试仍服从平台批准。Kickoff **不授权**批量改真实 Project 或全局个性化、私有数据广泛外传、公开插件发布、合并主线/移动 release、修改其它插件或 Research Authoring；最终发布/主线合并需单独用户 `ACCEPT`。

额外模型费用、新 API key、托管服务、浏览器扩展、MCP、后台 watcher、外部 Terra、C12、PIE 0.2、无授权远程资源写入、任意销毁 Git 状态全部禁止。需要超出约定权限/范围时先停并请求最小确切批准；没有工具不能用另一渠道绕过。

## 7. 版本、质量门槛、跟踪与下一步

`Repository bump decision = PATCH`（正式发布时以当时有效 `release` 基线算具体三段号；当前 5.4.4 只为本轮检视值，开发 commit 不升）。
`Affected plugins = writing-style 0.4 -> 0.5`（仅同批真实产品能力/回归/审查/发行通过后一次）。
`All other central plugins = NO_BUMP`。
`Maturity = NO_CHANGE`。
`README checked: design-only, no update required now.` 任何后续 README 修改必须真实经过现有 Clear Writing 正常入口审校，不能用本设计自述代替。

仍沿用 Issue #13 和源 `docs/plugin-todos/writing-style.md` 的 `tracking: #13`；因当前 ChatGPT 没有独立正式 Clear Writing 可调用，而维护看板要求更新读者向 Issue 文案前真实调用已安装的 Clear Writing，本轮不冒充已完成 Issue 改写，记录待下一合法维护环境同步 `DOING`、`Area=writing-style`、本执行包锚点与 Critic 下一动作；Project 字段当前不可写，不要求用户手工搬动。

验收定义：同一正式候选 G0–G7 支持的真实 ChatGPT Web 首答、个人/项目两种入口、专业 Codex 消费、旧五项不回归、真实报告/界面/整套幻灯片渲染和科学/技术保真、独立 Reviewer 及用户最后接受。某端缺口必须明确报告；不得把“写了规则”或“Critic 批准方案”报为产品已成功。

本 Plan 草稿的唯一下一步是独立执行前 Critic 审查。尚不允许部署、生成个人插件、执行任务 bootstrap 或启动 Codex Executor。
