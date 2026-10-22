# Clear Writing 0.6 验收与交付手册 v0.4

状态：与Plan v0.4同包待审。task = `clear-writing--single-entry-artifact-finalization`；tracking: #13。

## 1. 唯一权威与继承规则

本版产品职责以 `CLEAR_WRITING_0_6_PRODUCT_AND_EXECUTION_PLAN_V0_4_2026-10-22.md` 为准。前版关于“六项canonical正文绝不能改”和“只让ChatGPT包装拥有内容选择”的语义不再生效；修改它们必须本次Critic批准后才实施。不得将历史appendix同时当作另一套产品合同。

避免再次复制数十页不变操作，以下机械/样本合同按exact历史快照明确继承：

- `d7b810d194ead881303aaca9c2e4f1d59a97c1f1` 的 `docs/design/clear-writing/CLEAR_WRITING_0_6_EXECUTION_READY_PLAN_V0_2_2026-10-20.md` §§4.4–4.6（两项路径投影、确定性ZIP）、§§5–7（包结构、正向精确删除、manifest）、§15（双恢复集合与forward restore）。新增fidelity支持文档仅按原相对路径复制，不新增文本变换。
- 同提交 `CLEAR_WRITING_0_6_GATE_EXECUTION_RUNBOOK_V0_2_2026-10-20.md` §9的T2–T7全部自然提示词、T8原传感器提示词；§10原Reader Guide G3修改任务的source/ref/path与完整用户提示词。
- `ca018937b3528b8cc62ace9c02e33c1d5f84fde6` 的 `CLEAR_WRITING_0_6_GATE_EXECUTION_RUNBOOK_V0_3_2026-10-20.md` §8的T1 Bridge、T9受阻交接，§16的T8-A CAT科研解释、T8-B原深度保护、G3-B新文件创建完整提示词，§17的无需CAT提示的理解质量判据。

继承以上文件意味着保留具体工具动作、任务输入、次数与判据，不是让执行者任选旧版本。若工具实际schema变化影响合法动作，停止并回Planner最小修订，不临场绕过。

## 2. 候选与开发顺序

先在原Codex任务修改Plan允许的canonical源与包装；检查变更只属writing-style。安全归档reader同时支持ZIP与真实gzip tar，拒绝绝对路径、越界、链接、特殊设备、重复和异常文件集合。真正读取真实账户旧包的前置独立验证，不用等价测试包替代账户备份。

使用现有builder和Marketplace生成器；同源连续两次raw ZIP字节必须相同，普通SHA-256绑定exact raw bytes。测试两项allowlisted path transform和所有支持文件可达；追加final-delivery引用不能产生其它顶层Skill。

跑直接受影响的已知开发回归和保护性样本，再跑必需CI与独立实施审查，不循环拼最好答案。冻结新版FINAL_CANDIDATE：源commit、全部canonical writing源、两个分发包/生成树、profile、archive/receipt哈希、路径投影规则、ZIP规范、归档reader身份、Gate合同v0.4。旧候选仅作历史。

## 3. G1：身份与入口

保留现有same USER/PRIVATE plugin identity，更新前真实回读当前0.5.0 release与完整文件集合，不能从旧聊天假定未漂移。只有真实旧包字节已保存、0.6.1恢复包及精确删除集合已生成、上传入口和fresh Web操作入口已确定后才能live update。

更新采用expected_release_id+冻结正向exact file deletion，不创建第二个writing-style。完整回读两manifest、version、唯一顶层clear-writing、旧六顶层路径不存在，以及全部route/support与候选相符。Codex安装同一候选的正式插件生成树，回读六个直接入口和profile，不以repo source替代installed source。

G1-B沿用原简单状态/branch/status/command真实Web提示词。普通用户无需知道内部route名字；仅文件清单或Skill自述不能证明路由完成。

## 4. G2：六路线与普通回答的真实体验

Web使用ChatGPT Web、GPT-5.6 Sol、fresh conversation、明确选择Clear Writing。完整继承T1 Bridge工程汇报、T2中文终审、T3长文重写及exact repo/ref/path输入、T4英文科研、T5界面文案、T6精确JSON、T7混合内容、T8-A CAT已知科研解释、T8-B传感器必要长答、T9阻塞交接。没有新增顶层Gate。

每项一个产品答案；仅完全没有模型答案的基础设施故障可相同输入/模型/release重试一次。质量失败不reroll。使用CAT私有材料必须保持原权限，结果全文留在受限位置并让独立Reviewer实际读取，不能公开研究全文以图方便。

对G2完整产物，先检查问题覆盖与事实/权限/数学正确保留，再检查读者能否建立理解：陌生对象是否有意义、例子是否解释关键关系、结论与证据是否关联、步骤是否可操作、是否在不需要时倾倒审计过程。长篇必要推导必须保留。新认可的Slurm说明是已知正向文字反馈，记录其保留未验证分支边界的价值；不新增真实Slurm操作或运行作业。

T1不含“参考CAT”提醒，验证通用解释能力而非仅照参考全文模仿。T9的下一责任方是依据工作流事实决定，Clear Writing不得自行发明授权/下一任务。来源自身不足时准确表述已知与待核实，不能为了交出完整漂亮答案造结论。

## 5. G3：聊天与GitHub全文分别验收

G3-A原Reader Guide完整修改+聊天，G3-B已冻结新路径的非覆盖创建+聊天，顺序、来源、目标分支与提示词全部按§1继承；各自fresh Web、同一插件release、一次产品答案。Gate分支已存在且不满足原前提时不得覆盖或换新分支规避。

**区分日常质量控制与发布独立审查。** 普通GPT在同一次显式调用中完成来源读取、整篇候选生成、模型自己的完整保真检查、读者通读、必要返修、写入和真实回读；它不得声称自动启动第二个独立审稿模型。G3是**正式验收**，在真实正常入口任务结束后，由原独立Critic/既有实际产物审阅者对已经生成的完整产物另作判断，两层证据不能互相代签。

每个任务必须可供独立审查直接读取：原始用户问题、完整源文/授权依据、实际路线、写前候选全文、写前保真与读者通读的具体依据、工具写入记录、真实目标回读全文、实际最终聊天全文。Reviewer要独立检查文本质量，不能只看候选自评报告/自检摘要。模型声明“读过技能/审过文档/已通过”不等于审校确实改变了全文，必须看到最终文本具备自然阅读顺序、术语解释、重要条件和无重复噪声的质量。

修改路径：fetch完整源/blob→正确专业路线→唯一已审全文候选→写前复查同blob→update_file带expected blob→保存commit/content identity→完整回读匹配。创建路径：完整依据/目标授权→确认路径不存在与写前branch head→全文审校→create_file非覆盖创建→核对返回提交parent及目标→完整回读匹配。事后parent检查不是事务锁，不夸大为阻止所有并发变更；发现不一致准确停止未验证，不伪报完成。

**每份文件分别判定三件事：事实/权限保真、读者质量、保存一致。** 三项全成立才该文件通过；聊天另按G2完整答复标准独立判定。任一对象严重失败则G3整体FAIL。不得用文件hash证明文章好读，也不得用漂亮聊天替代完整文件处理。

**防止发布前文本看似已审、实际上只是模板套话：** 对G3-A既有长文和G3-B新文，不准仅据工具提交内容推断写前自审成功；Reviewer须能指出最终文稿的具体读者问题、信息层次、首次概念解释、无必要英文和原文重要条件的对应位置。若全文仍呈内部审计报告、重复否定、信息跳跃或逐行机器状态堆叠，即使写前模型说合格且写后hash一致，仍属**产品质量失败**，按原合同停止并恢复，不因其他Gates通过而发布。

## 6. G4：保真与任务权限

G4在G6之前，只审G2与G3全部完整来源/最终产物。特别检查摘要/全文重写模式区别、普通概念中文化与机器token精确保留、公式/条件、未完事项、用户豁免与真实已验证行为不混淆。用户认可Slurm说明中的技术陈述仅为其提供的文本事实，Clear Writing任务不运行scancel、不重验发布。

G6自己先保真后可读性，不反向成为G4前提。最终总评汇总既有Gate，不建G7。

## 7. G5：Codex实质消费与共享源兼容

共享源改变使本轮不能仅以ChatGPT通过发布。保留已有Codex六路直接回放，不简单增加一批相似用例；用已有普通回复回放位验证与G2-T1等价的工程问题，用必要长答位验证T8-B，用已有正式文档位验证完整候选、本地实际写入/回读与附带聊天。其余英文科研/UI/精确输出覆盖保持。用户已明确授权推GitHub的任务才执行remote publish；本地回读不能代签G3远端证据。

需看到真实installed plugin被选择、相关canonical规则进入任务、完整生成物经过应用，而非运行目录只存在文件。G5的语义质量判断与G2同标准；hash parity另作机械证据。Codex保留当前任务原有运行配置，在首个候选回放前冻结具体model/client/config identity；若原配置无法从既有记录确定，不允许临场换模型，先返回Planner。Web型号仍完全保持原批准值，不能相互替代。

下游边界检查复用既有Research Authoring/Presentations/statistical-modeling/scientific-visualization消费任务与保护性输入，不修改它们的产品，也不声称#73/#49接入已完成。六个canonical文件改动须按源→生成→实际安装比对。

## 8. G6、失败与恢复

G1–G5真实通过后，把完整证据与同一候选交原Critic，结论只为PROCEED_TO_FINAL_EVALUATION/REVISE。原Critic冻结唯一fresh长技术文档、完整输入、模型、目标及rubric；样本一旦看过用于调优就失去fresh身份，不换题或挑赢家。

正式评估每任务一次产品答案；日常开发返修可以在同一任务修复，但不得把重跑后的已知样本当fresh。live更新后终止失败或批准的基础设施恢复耗尽，按exact v0.2 forward restore恢复旧行为的0.6.1个人包装；删除集合为(S06-S05)-restore archive paths，使用exact existing paths，不上传/删除同一路径。完整回读旧行为文件；中央0.6不发布。没有live update则0.5.0原样保留。

当前仍未完成真实档案字节下载与正式Web会话执行前置。2026-10-22只读尝试确认接口返回tar.gz，但本容器下载连接失败；不得将它写成restore PASS。由能真实下载/运行builder/上传的既有工具入口处理，fresh会话可由不同合法入口完成。用户只承担实际UI-only动作；Planner负责完整输入、证据与恢复协调。

## 9. 发布声明

正式版本只在同一候选、两端所声明能力与G1–G6都获对应证据后发布。**独立审查者只属于正式发布和最终评估阶段；日常每次ChatGPT写作的质量动作由同一模型完成，不能冒充有额外独立审稿人的产品服务。** 用户看到的说明回答：聊天何处改善、文件是否全篇审校并真实保存、必要深度是否保留、已见严重退化是否重现、失败谁负责。不要再堆样本数或Skill已加载证明质量。

如果独立Critic认为Codex运行配置、Phase C材料取得、真实会话操作或某项工具能力仍未满足执行就绪，必须明确REVISE和最小闭合条件，不能再让最后阶段首次发现。
