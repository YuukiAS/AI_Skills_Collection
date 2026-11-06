# Research Authoring：先跑通正式文档的交付链

建议继续 #99 的既有发布工作。公开分支已经走到新版私有包装包的上线前审查，剩余证据集中在真实 ChatGPT 入口及其与 Codex 的交接。课程材料的回归先由项目侧现有流程承接。科研学习笔记有独立读者目标，可在 Research Authoring 内另做一轮取证。

## 正式版、实现候选和待跑验证

| 对象 | 2026-11-06 查到的事实 |
| --- | --- |
| 正式 `research-writing 0.2` | 基线 `ff5be718` 和稳定通道 `release@f4517798` 的安装清单均为 0.2，包含 `report`、`paper`、`litcite`。0.2 已明确科研报告的内容职责与正式 PDF 交接。只要求 Markdown 时保留 Markdown。明确要求正式 PDF 时，`research-main` 安装渲染依赖，独立 Marketplace 环境缺该依赖时停止并报告。正式 PDF 通常走 `render-chinese-math-pdf`，期刊已有授权模板和编译路线时遵循其实际约束。[主线清单](../../../../plugins/codex/plugins/research-writing/.codex-plugin/plugin.json) · [稳定通道清单](https://github.com/YuukiAS/AI_Skills_Collection/blob/f4517798a73adf29d3484306d60845488739f1fc/plugins/codex/plugins/research-writing/.codex-plugin/plugin.json) · [插件发布历史](../../../plugin-changelogs/research-writing.md) |
| 059 与公开 #99 | #99 仍 open，正文及其更新停在 C0 准备和独立 pre-final Critic 交接。正式设计与执行就绪判断有独立评审记录。GitHub 已有更靠后的执行证据，后续维护者可以更新链接并保留未完成的验收项。[Issue #99](https://github.com/YuukiAS/AI_Skills_Collection/issues/99) · [执行就绪审查](../../../design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_EXECUTION_READY_CRITIC_REVIEW_V0_1_2026-10-04.md) |
| 已跑的历史验证 | 历史候选 `1c37c071` 的公开结果记录 G1–G3 通过，并创建、回读了私有 ChatGPT 包装插件 0.3.0。此后 G4 的 ChatGPT 阶段被独立审查判失败，包内声称已完成本应由 Codex 承担的 PDF 编译和视觉检查。另一次恢复试跑未证明实际消费了目标入口。这两类失败分别属于跨端职责越界和运行时选错执行入口。[历史验收状态](https://github.com/YuukiAS/AI_Skills_Collection/blob/25cadb2f31bb3a865cc421e99f7fc337c31ca444/results/research-authoring--formal-production-authoring/FINAL_GATE_STATUS.md) · [G4 失败评审](https://github.com/YuukiAS/AI_Skills_Collection/blob/25cadb2f31bb3a865cc421e99f7fc337c31ca444/results/research-authoring--formal-production-authoring/G4_CHATGPT_STAGE_REVIEW.md) · [入口恢复记录](https://github.com/YuukiAS/AI_Skills_Collection/blob/25cadb2f31bb3a865cc421e99f7fc337c31ca444/results/research-authoring--formal-production-authoring/G4_C1_C2_REPAIR_STATUS.md) |
| 当前公开任务分支 | `work/research-authoring--formal-production-authoring@25cadb2f` 的最新审查把源码候选锁定在 `9ed9140c7a131c1f8a5ba02b0262639a44af66eb`。历史 G2 科研报告和增量更新的语义证据经审查可保留。G3 原接受包保持不变，重跑并审查受影响的模板编译、渲染及科研验收环节。审查结论为 `PASS_FOR_LIVE_G1_G4_ENTRY`。当前私有包装包候选为 0.3.1 v2，档案检查确认六个顶层 Skill 都在 manifest 声明的目录内。正式 0.3 仍缺当前候选的 G1/G4 真入口证据、独立审查和发布闭环。[验证影响与证据复用](https://github.com/YuukiAS/AI_Skills_Collection/blob/25cadb2f31bb3a865cc421e99f7fc337c31ca444/results/research-authoring--formal-production-authoring/RELEASE_GATE_IMPACT_REBIND.md) · [上线前独立审查](https://github.com/YuukiAS/AI_Skills_Collection/blob/25cadb2f31bb3a865cc421e99f7fc337c31ca444/results/research-authoring--formal-production-authoring/RESEARCH_RELEASE_PRELIVE_REVIEW.md) |
| 学生课程材料 | 主线已有面向学生/教师的共享工作流程、保留既有批准内容的增量修改和语义分页规范。课程方向在独立 Skill 的 TODO 中有记录，正式单独安装包和当前普通入口的消费尚未证明。另有两个远端 TODO 分支记录文字与宏观布局的批准权，以及长表格的语义换行。它们是待归并的证据，增量尚未进入基线，不作为已部署规则。[课程 Skill TODO](../../../skill-todos/course-assessment-authoring.md) · [共享流程](../../../../plugins/codex/plugins/research-writing/shared/student-assessment-end-to-end-pre-execution-runbook.md) · [分页规范](../../../../plugins/codex/plugins/research-writing/shared/student-assessment-semantic-pagination-amendment-v1.md) · [权威锁补充](https://github.com/YuukiAS/AI_Skills_Collection/commit/80dfb6c658d24738b754f9bbb7c91122ca3bfc12) · [表格补充](https://github.com/YuukiAS/AI_Skills_Collection/commit/b4a13a6178f206b943ecf133970a1a1360ed087e) |

本次只读核对公开文件和审查结论。候选的原始科研材料、评审附件和真实账户状态仍沿原任务授权使用。任何后续更新或正式集成都需要重新确认当前候选、稳定通道和可复用证据范围。

## 同类反馈怎样归并

| 可复用的问题 | 证据、归属和验证方向 |
| --- | --- |
| 导师报告先安排读者的科学决策，再呈现证据 | DII 相关案例反复出现研究需要藏在执行背景之后、方法和数据过晚交代、结果显著性表述超出证据。已有 `research-reporting` 明确按科学问题、对照、主证据、限制组织。这些应合并到报告语义回归。早期进展稿的结果占位、双语版本各自校准、可追溯引用和公式位置是同一能力的不同样本。尚未确认所有失败都由正式安装入口产生。[报告源码](../../../../skills/writing/research/research-reporting/SKILL.md) · [真实反馈](../../../plugin-todos/research-writing.md) |
| 课程材料的内容准入与现有成品保护 | STAT5060 复盘记录了批准日期漂移、评分内容混入行政规则、教师信息进入学生稿、窄改动损坏其他页。已有学生受众、权威、锁定范围、完整成品对照规则。先查调用时读取了哪些批准源和共享流程，渲染实际用了哪个基线，以及错误成品怎样被提到交付位置。作业题目、评分、处罚和课程日期继续由课程方持有。跨领域可复用的是来源冲突的处理、读者需要哪些信息及相关约束怎样传给执行者。[案例复盘](../../../design/research-authoring/STUDENT_ASSESSMENT_HW1_FINAL_PROJECT_POSTMORTEM_AND_NONRECURRENCE_V1_2026-10-07.md) · [学生受众条目](../../../skill-todos/course-assessment-authoring-student-audience-gate.md) |
| 语义分页与表格可扫描性 | 版面在无溢出、字数和页数均符合时仍可能拆开规则、表格和后果，或断开数值与单位。既有分页规范覆盖整块保留和允许续页。长表行内可换行的位置提供了更窄的补充例子，可并入现有文档可读性检查。先对真实排版候选做反例，在冻结字号和语义下测量可行版式，检查实际页面。先为课程和技术报告分别取证，再判断能否共用规则。[文档构成候选](../../../plugin-todos/reader-facing-document-composition-protocol.md) · [语义分页](../../../../plugins/codex/plugins/research-writing/shared/student-assessment-semantic-pagination-amendment-v1.md) |
| 本人科研学习笔记要能重建推导 | CAT-TRACE 多版笔记反复把关键代数、定义到近似之间的推理压成结论，后续经用户认可的好例通过读者熟悉的例子恢复了缺失环节。与报告共享事实、引用、证据权威和数学保真，新增的是按读者具体疑问重建推理、条件和例子。单个项目的多轮样本尚不能证明正常安装入口或跨项目泛化。Notion 远端读回确认内容和目录，真实客户端排版应单独取证。[学习笔记样本](../../../plugin-todos/research-writing.md) |
| 渲染和用户可取件 | 0.2 的已有证据覆盖指定渲染伴随 Skill 的消费。PDF 首次可另存交付也已有正式发布案例。领域检查报告、论文或课程文档实际可读和可信。交付能力检查同一个已验收成品是否在首个面向用户的交付消息中可取用。复发优先按实际消费者修复。[渲染回放](../../../../results/documents-media--scientific-pdf-rendering-reliability/FINAL_EXECUTION_REPORT.md) · [首次 PDF 交付闭合](../../../../results/documents-media--pdf-save-as-delivery/FORMAL_RELEASE_CLOSURE_5_4_5.md) |

## 下一轮产品构想

读者可以按常用语言直接发起任务，例如「用仓库里的证据写导师更新」「新增一组实验后只更新相关结论」「按投稿模板交付可编译稿件」「只改作业提交文件名」。同一插件识别文档类型和读者后，保留既有领域路线。首轮聚焦前 3 项，后两项待证。

1. **从来源到读者任务**。先厘清科学问题、有效证据、读者需要做的决定和不能越过的结论，再组织报告或稿件。科研事实和不确定性用 Clear Writing 改写时继续保留。
2. **证据增量只改变受影响的结论**。把新比较、结果或决定定位到实际源文件和已批准文档，再修改受影响的段落、引用或表图。来源或旧基线不明确时说明缺什么。
3. **完成指定文档及实际产物**。ChatGPT 确立内容和交接，Codex 核实真实 repo 和版本、交接范围、目标产物与模板，调用现有 renderer 并读回真实 PDF。科研与排版分别验收，Delivery Assurance 消费成品与实际交付事件。Markdown 任务在成稿处结束。
4. **课程专用的受众与语义保护**。从现有 runbook 起步，验证考试、作业或开放项目如何分离学生和教师材料，如何在真正的成品上保护冻结题目、数值、允许改动和相关排版。课程 owner 批准教学决策。Design Assurance 只查执行前能否落实及反例。
5. **能在日后复习的学习笔记**。在用户已有背景上补齐中间推导、局部示例、成立条件和易混区别。先做作者可直接冷读和迁移验证，不增加新的编辑平台入口。

GPT 擅长和用户收敛科学问题、解释对象、材料取舍和证据强度。Codex 擅长读取准确 repo 状态、验收增量修改、调用真 renderer 和核对成品。双方共享来源优先级、科学含义和文档身份。保留 Codex 已有的报告、论文与文献入口。对 059 的现行双端交付承诺，先验证已批准的 ChatGPT 正常入口和 Codex 交接消费。历史的 Codex 普通请求入口竞争不能自动成为本次发布的新门槛。

扩大禁词只能改变表层表达。统一格式迁移会改写 venue 与用户模板权威。按既有文档类型修实际入口可集中解决当前缺口，也保留以后对课程或学习笔记独立取证的余地。

## 正反回放

| 场景 | 成功要直接看到 | 对照 |
| --- | --- | --- |
| 正式报告和有限增量 | 从冻结原始材料写出完整导师报告，随后用预冻结 delta 只更新受影响的结论和表图。能指出新增证据与不变限制。 | 日期变化不能自动改变实验设计，已有结论受影响时须同步改交叉引用，未运行的结果保持未完成。 |
| 论文及双端正式交付 | 真实 ChatGPT 请求加载目标包，按 venue 生成必要文档交接。Codex 确认候选身份，消费交接，完成真实编译、科学及渲染验收，独立评审读实际文件，用户可取件。 | 旧包、只有说明文件的交接、Markdown 请求误入渲染、缺依赖后走浏览器、ChatGPT 越权宣称已编译以及仅有文件路径，分别识别失败或预期行为。 |
| 学生材料窄改 | 经授权修改一个提交文件名或组件，真实页上保持已接受的内容、学术文档样式、学生/教师隔离。规则和配套表格可以同行理解。 | 批准基线丢失时停。测量发现整块放不下时遵循合法续页或提交有限决策。正控制保留适当换页与留白。 |
| 科研学习笔记 | 读者能从材料复述关键近似的条件，重建一步代数并应用于另一个小例。公式在实际目标载体正确显示。 | 终式和术语齐全但缺推理的摘要失败。本来只问简短释义时仍能简洁回答。 |

这些是候选验证场景。正式 G1–G4 保持已冻结要求，回放的验收权继续由独立角色承担。

## 外部参考

网页均于 2026-11-06 访问。采用判断仅针对本轮产品研究。

| 来源与许可 | 查了什么及适用边界 | 采用判断 |
| --- | --- | --- |
| Quarto Manuscripts，自 1.4 提供。Quarto CLI 主仓 MIT | 同一来源支持稿件、计算和多格式交付，图、表、公式、引文有可定位的交叉引用。论文包结构和标签身份可借鉴。项目/venue 允许哪些附件、主张是否符合科研证据仍需领域判断。[项目文档](https://quarto.org/docs/manuscripts/) · [交叉引用](https://quarto.org/docs/authoring/cross-references.html) · [许可证](https://github.com/quarto-dev/quarto-cli#license) | `REFERENCE_ONLY`，不作为当前通道的 renderer 替换。 |
| The Turing Way，文档及数据 CC BY 4.0，软件 MIT | 查看 research compendium 如何分别组织输入、代码、环境、结果和执行说明。可以指导报告证据可重建。并不规定什么应留在导师正文，也不授权把原始材料打进交付包。[研究材料组织](https://book.the-turing-way.org/reproducible-research/compendia/) · [许可证](https://github.com/the-turing-way/the-turing-way/blob/main/LICENSE.md) | `REFERENCE_ONLY` |
| Carnegie Mellon Eberly Center，网页未标开放许可，适用站点使用条款 | 查看可做什么、交什么、读者是谁、如何评分及与学习目标对齐。可作为课程文档内容准入的比较基线。课程批准源、教师材料保护和真实分页需另行验证。[Creating Assignments](https://www.cmu.edu/teaching/assessment/assesslearning/creatingassignments.html) · [网站条款](https://www.cmu.edu/legal/) | `REFERENCE_ONLY` |
| LaTeX `needspace` 1.3e，LPPL 1.3c | 查看按剩余空间决定是否提前换页的控制。可解释为什么硬编码预留会在现有 LaTeX 路线上产生和硬断页一样的结果。宏包无法决定两段文字是否是同一个读者动作。[CTAN 说明](https://ctan.org/pkg/needspace) | `REFERENCE_ONLY`，由现有 renderer 在其合同下决定是否复用。 |
| Typst，编译器 Apache-2.0，讨论内容未另核许可 | 检查 `block` 的不可拆与粘连、表头重复，以及用户讨论多行分组和特定不可拆单元内容消失的反例。语义单元可映射到排版原语，但嵌套、超长和真实阅读顺序要看成品。相关 issue 不证明本仓 LaTeX 有同一个技术缺陷。[块](https://typst.app/docs/reference/layout/block/) · [表格](https://typst.app/docs/guides/tables/) · [讨论 #5337](https://github.com/typst/typst/discussions/5337) · [Issue #8780](https://github.com/typst/typst/issues/8780) · [许可证](https://github.com/typst/typst/blob/main/LICENSE) | `REFERENCE_ONLY`，用来找分页反例。 |
| Chi 等，1989，期刊页未标开放许可 | 读原始论文摘要。对物理习题样例的口述分析发现，能够把示例步骤连回原理和适用条件的学生对原样例依赖更少。可据此设计「读者能否在不同例子中重建解释」的笔记验证。研究不能证明模型生成的笔记会改善真实学习。[原始论文](https://doi.org/10.1207/s15516709cog1302_1) | `REFERENCE_ONLY` |

## 下一步如何分开

- **继续既有 059**。刷新 #99 的建议锚点到当前公开独立审查，核对 main、稳定通道与准确发布候选的变动。保持发布门槛，优先证明当前包装包正常加载以及端到端真实 G4。G2/G3 在受影响范围变化时按既有证据复用政策处理。
- **课程验证先于独立包装**。把两个远端补充条目并入现有内容批准、语义分页与版面回归。先问哪个普通入口有责任消费这些约束、保护旧成品和交付正确材料。课程文档的现有晋升说明要求作业、开放项目指南、阶段表单、教师材料、批注恢复和受众分包都具备回放证据。在此之前保留 standalone Skill 方向及共享候选。若已有入口消费失败，优先修实际 consumer。
- **学习笔记作为下一轮窄提案**。Planner 应选择至少另一个独立研究场景，定义作者能否从笔记恢复中间推理和迁移到新例。先确认回归来自路由、内容选择或平台成品，之后再选 `report` 内细分模式或共享内容候选。无需新 Plugin、Notion 连接服务或另一份领域 QA。
