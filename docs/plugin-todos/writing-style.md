# writing-style — Long-Term TODO

Canonical maintenance inbox for the `writing-style` plugin.

## Incoming real-use feedback

### 2026-10-26：技术汇报改写后仍向用户暴露内部缺陷编号
status: NEW
source: 2026-10-26 用户对 STAT5060-TA 三套课程验证器独立验收的原始回答与明确调用 Clear Writing 后的中文改写进行比较，并直接反馈不应继续看到 `IVA-P` 一类内部编号。
evidence:
- 原回答按内部编号和状态码组织问题；改写版已改善开头结论、任务顺序及重复证据，但正文仍以 `IVA-P-001（P1）：三条规则永远无法正常通过`、`IVA-H-001（P1）` 等作为问题标题，并混入验证规则编号和内部状态。这些标识主要服务开发定位，读者只需理解缺陷、严重程度、影响和修复责任。
- 同一改写版也保留了必要的准确交付文件名（如 `SID_Project.pdf` 与 `SID_Project_source.zip`）；这类名称直接决定课程材料如何修复或提交，有明确的读者行动价值。原始验收报告及三份修复清单仍保存完整追踪编号，正文不展示编号不会丢失可定位证据。
- 改写版测试结果表还出现破碎的 Markdown 表格展示；属于本次成稿的实际可读性问题，应在全文输出检查中覆盖，不能只验收措辞。
problem:
- **保真误当逐字展示**：已有 `writing-fidelity` 对 issue ID、状态值、路径等精确字符串的保护，在普通解释中容易被解释为“所有源标识必须进入用户正文”。现有 `response-clarity` 虽要求把技术标识后移，却未可靠地判断标识是否值得出现。
- **正文与追踪证据缺少分层**：内部缺陷码、测试状态和审查规则号应可以留在源报告、可点击修复清单或必要的技术附录；面向用户的正常汇报应以“具体什么坏了—影响什么—下一步修什么”组织，而不要求读者翻译编号。
- **不能按字符串一律删除**：需要实际复制、提交、修复、复现、检索或精确核对的文件名、命令、代码标识，以及用户明确要求的逐项编号对照，应原样保留。P1/P2 的风险分级也应保留其含义，可在普通说明中写作“严重／次要”。
desired behavior / acceptance:
- 对同一份复杂验收材料执行普通中文结果汇报：开头给出真实完成度、主要缺陷、能否验收及修复顺序；保留事实数量、严重性、责任边界和不确定性；未经用户要求不把 `IVA-*`、规则 ID 和机器状态码当作正文标题或阅读前提。
- 加入成对回归：普通读者汇报应隐藏无当前行动价值的缺陷编号；明确要求“按修复单 ID 逐条指派 Codex”时必须准确展示原编号；学生/教师必须使用的实际交付文件名则始终正确保留。
- 检查最终完整回答与实际呈现的表格，不以“第一段清楚”或“所有字符串均被保留”作为通过条件。若正常入口仍失效，排查已存在的 `response-clarity` 内容取舍和全篇应用问题，而非追加一份编号禁词表。
project-specific context: `STAT5060-TA` 的内部 `IVA` 编号、课程规则、真实文件命名及修复判断仅是本次证据；不得固定为 Clear Writing 的领域规则。本条为用户观察到的 Clear Writing 调用前后对比，尚未取得独立的插件入口执行轨迹，不声称已定位内部平台路由原因。

### 2026-10-26：普通回答中的图片、卡片和流程图缺少必要性判断
status: NEW
source: 2026-10-26 用户提供三张 GPT-6 / ChatGPT Web 回答截图，要求分别裁定视觉形式应保留还是删除。
evidence:
- **应删除的实例**：Project Guide 验收结果被包装成占屏较大的卡片、醒目失败标签，并插入一张与实际受检 PDF 无关的外部排版示意图。说明“非本次实际 PDF”也无法为该图带来证据价值，反而容易误导读者。
- **可保留但应压缩的实例**：三步发布/验收安排确有时间顺序，且明确指出仅第二步需用户亲自操作；步骤结构能帮助快速识别自己的动作，但重复的图标、粗体、大间距和冗余提示可缩减为紧凑清单。
- **应删除的实例**：一条简单的研究失败循环被写成四个大灰框加箭头的流程图，没有分支、复杂依赖或新信息，视觉面积远大于其解释价值；普通因果分析段落更合适。
problem:
- **可生成的视觉组件被误认为应该生成**：图片、卡片、状态标签、流程图只有形式上的吸引力，缺乏对读者当前判断的独立增量；无关素材尤其会与真实证据混淆。
- **缺少视觉呈现前的内容取舍**：没有先识别哪些事实需要读者注意、哪些真实关系值得可视化，以及最小有效展示形式。之前 2026-10-15 的反馈已覆盖“代码框和箭头伪结构化”，本次补充了无关图片、巨大结果卡片以及真正有用的步骤结构应如何保留。
- **不可走向全面禁图禁卡片**：真实受检 PDF 页面、影响判断的实验图、跨对象比较、复杂依赖、进度与用户行动清单都可能值得图示或交互；必须按信息价值决定，而非按组件种类或固定数量限制。
desired behavior / acceptance:
- 对同三类情境分别做正反回放：验证课程 PDF 时，若需图片，只展示与当前检验对象真实对应且有证据价值的页面；连续三步且只有一步需用户操作时，允许紧凑的步骤清单并突出行动；简单线性因果关系默认自然段，只有存在真实复杂结构才使用流程图。
- 在用户可见成稿层评估“看过组件后，用户是否获得纯文本无法同样高效获得的信息”，同时检查视觉权重、滚屏成本、图文对应关系、真实文件身份和误导风险。不要靠图片数量、卡片数量、图标禁用名单或外观审美评分单独验收。
- Clear Writing 负责读者相关性、表达与呈现建议；实际界面组件是否可选择、图片检索与渲染、应用自动插入的组件需按平台和上游界面能力划清控制边界。不能把无法被插件直接控制的宿主 UI 行为宣称为已经由修改写作规则解决。
project-specific context: STAT5060 项目验收、MacBook Neo 上的软件验收安排及 DII 研究循环是三个具体反例/对照，不成为固定通用版式；本条与既有“伪结构化”“整篇阅读负担”反馈关联维护，不升级为全面的 UI 禁令。


### ChatGPT 网页端中文长回答的阅读层混排和冗余问题
status: NEW
source: 2026-10-14 用户提供的 ChatGPT Web 回答，并要求作为 Clear Writing 网页端回归记录。
evidence: 当前对话上传的回答文本，共 540 行、约 1.1 万字符；十个二级章节、十六个三级章节及 149 个项目符号。仅记录反馈与典型问题，不复制整份私人研究文本。
problem:
- 前几行能说明主要事实，但很快展开长篇任务说明，用户需要的判断、关键缺口及后续动作被大量细目淹没。即使用户要求完整可复制的执行提示词，面向人的解释与机器交付物仍应明确分层；提示词本身需要完整时不能为了缩短而删去必要条件。
- 多处重复边界、禁止事项和验收要求，章节与列表数量没有与实际阅读需求匹配。长不自动构成错误，但重复、分散和缺少取舍增加认知负担。
- 文件路径、状态字段等机器标识对执行者可能必要，但不应构成面向用户的解释主体。现有中文表达能力应区分解释层和机器交付层，不擅自改写正式命令、机器字段、权限或科研事实。
- 用户提供的复制文本存在数学标记和空白表格占位符的可读性问题；尚无网页截图，不能断言网页实际渲染同样出错。
- 目前缺少原始用户提问及插件实际调用身份，不能据此证明正式 Clear Writing 运行路径发生了产品回归；本条先记录已观察到的用户可见问题及后续核实边界。
project-specific context: 文章中的生态数据集、数值、路径和科学要求只属于具体研究任务，不成为通用写作规范。 


#### 2026-10-14：伪澄清、反复变更建议和自我检讨式空话
feedback_status: NEW
source: CAT-TRACE 三个生态数据集的目录/分组研究讨论线程；用户对 ChatGPT Web 中文解释的再次直接否定与原文摘录，2026-10-14。
evidence:
- 直接反例：「这不是芬兰全国真菌名录，也不是从当前 1,021 个响应列中随机挑出一部分。」该句否定了两个读者未提出的备选，却没有正面回答「所指目录到底是什么、信息来自哪里、为什么有效、现在可否使用」。
- 讨论曾在「按纲」「按门」「生态功能」「木生真菌/其他真菌」之间切换，甚至一面建议分成木生和其他，一面承认「其他」未必是合理的同质组。先列建议、后堆限制和免责声明，并不能让用户知道哪些建议有依据、哪些已经撤回、现在究竟应相信什么。
- 用户反馈「不会说人话」时，回答却进一步讨论真菌分组合理性、重新提出方案，未对用户指出的实际表达问题作分析或改写。
- 用户本轮再次粘贴一份助手自我检讨：以「你不满的根本不是……而是……」开头，按四个错误长篇复述用户批评，反复强调「你不是要求……而是……」「我没有理解」，却缺少对应的原句定位、为什么该句无效及更有信息量的正面表达。形式上认错，实际继续占用阅读篇幅。
problem:
- **伪澄清**：先否定荒谬、未被提出或与问题无关的解释，制造谨慎/精确感，却不定义真正对象；即使没有英文术语且句子很短，也可能一句有用信息都没有。不能以「不是 X」「不意味着 Y」代替「具体是什么、凭什么、结论是什么」。
- **保留条件淹没判断**：缺乏支持时，应清楚说明不能推荐什么及究竟缺少哪项证据；若建议成立，应说明证据与理由。不能提出一个建议再用长串限定语让推荐状态含糊。表达层只能准确呈现研究层已经作出的判断，不得自行选择科学分组或制造未经证实的确定性。
- **变化无解释**：连续改变方案，却不比较变化原因、原建议退出原因或当前结论，容易让读者误以为存在稳定推荐。语言审校应暴露这种歧义并请求研究层澄清，不能靠润色抹平互相矛盾的观点。
- **反馈意图被忽视**：用户批评的是表达质量与理解负担时，回答应直接核对批评所指文本，指出空话、绕行和真正缺少的正面信息，而不另起领域研究。空泛道歉、冗长自我检讨、代替用户定义其心理诉求也不能算解决。
- **已有规则未发挥效果的证据**：现有 `skills/writing/core/chinese-prose/SKILL.md` 已明确限制机械「不是 X 而是 Y」、重复自我强调、机器腔并要求读者先看到实际判断；本例需要检查网页端普通自然回答是否真实消费这些能力以及最终是否有效。不要新增「禁用一切否定句」的通用规则：在确有读者误解、正式对照或风险排除时，否定句仍可必要。
project-specific context: 真菌目录、样本维度及分组优劣属于 CAT-TRACE 科学研究，不在 Clear Writing 中冻结科学答案；本条仅保留用否定代替解释、空泛自我检讨、回避关键结论和错误回应写作反馈的可迁移失败模式。还没有证据证明上述原始网页输出经过正式安装的 Clear Writing 正常调用，不据此声称正式插件运行回归或已经修复。

#### 2026-10-14：具体解释改善后的正反对照
feedback_status: NEW
source: 用户于2026-10-14提供另一份更具体的 ChatGPT Web 中文研究回答，要求与先前失败答案对照记录。
evidence: 本轮对话内的完整用户粘贴文本，不复制科研原文。
positive: 开头直接给出具体选择；随后用日常情境、分年示例解释抽象概念；明确区分建议方向与尚待核查的事实。比此前只罗列术语和否定备选的回答更便于理解、判断，应作为正面改进样本保留。
remaining: 多处重复同一组结论，若干否定句没有增加信息；强烈推荐措辞与尚待核查的条件不够协调；粘贴版本的表格、来源卡片和公式存在复制可读性问题，但未验证网页实际渲染。不可仅因答案较长就删掉必要解释和例子。
boundary: 写作层只负责使判断、依据与不确定性清晰，不能自行改动科学结论。该回答尚未证实经过正式插件正常入口，因此先作为网页端写作反馈，而非已证实的插件运行回归。

#### 2026-10-15：伪结构化导致的信息密度下降和纵向阅读负担
feedback_status: NEW
source: 用户于2026-10-15提供 ChatGPT Web 回答截图，并明确反馈“看的很累”，要求写入 Clear Writing 回归记录。
evidence:
- 回答用一个大面积“纯文本”代码框展示简单线性流程：Codex 制作 slides → render → 自动 Presentation QA → 发现问题后自修 → 再 QA → 达到内部质量线 → 必要时送 GPT Work。实际信息量很低，但每个箭头和步骤各占一行，右侧大量留白，强迫读者进行长距离纵向扫描。
- 紧接着又用第二个代码框逐行列出 `B1`、`oracle`、`47 mutants`、`permissions canary`、`exposure ledger`，目的只是说明这些内部设施“以后不应该看到”。这种表达为了说明信息不重要，反而先要求读者处理一遍这些内部名词。
- 普通解释中连续混用 `experiment`、`Presentation`、`slides`、`render`、`QA` 等可中文化词；`GPT Work` 属于正式产品名，可保留。问题不是存在英文，而是无定位价值的语言切换进一步打断阅读。
problem:
- **伪结构化**：代码框、箭头、树状图、逐行流程等形式只有在真实存在分支、层级、执行顺序或需要精确复制时才应使用。简单线性关系若用普通段落或一行紧凑流程即可说明，强行扩展为大面积视觉结构会降低信息密度、增加眼动距离和滚屏负担。
- **信息价值与视觉权重不匹配**：容器越像代码、流程或正式结构，读者越会提高注意力并预期精确语义。普通自然语言不应仅为“看起来有结构”而进入代码样式容器。
- **为说明“不必关心”而暴露内部名词**：若某些研发设施对当前结论没有必要，默认应概括为“内部测试/校准设施”，而不是先逐项展示其内部名称，再告诉读者无需理解。只有后续任务需要定位、比较或执行时才展开精确术语。
- **回归标准应衡量阅读成本而不是禁用形式**：不要新增“禁止箭头”“禁止代码框”的机械规则。正例是简单线性关系优先用紧凑自然语言；反例是存在真实分支、层级、逐步执行、命令复制或机器内容时，结构化形式仍应保留。
- **已有长回答问题的独立失败模式**：本例与 2026-10-14 的“伪澄清/自我检讨”和“具体解释改善后的正反对照”不同；这里主要暴露的是内容已经基本想清楚，但视觉组织把简单信息重新变难读。应纳入 G5 reader-facing quality / reader effort 的已知回归，而不是新增顶层 Gate。
boundary: Presentation validator 的具体 B1/B2、mutant、oracle、Bridge 权限设计属于原项目，不进入通用写作规则；Clear Writing 只记录“结构化形式是否真实降低阅读成本、内部实现名词是否有当前读者价值、普通解释是否被不必要地机器化展示”这一可迁移模式。



#### 2026-10-16：科研解释中过度断行和单句成段增加阅读负担
feedback_status: NEW
source: `Distributed_Imaging_Inference` 方法阅读讨论；用户连续阅读两份 ChatGPT Web 中文解释后直接反馈“这两次回答不行，换行太多了”，并要求记录进 Clear Writing。
evidence:
- 第一份回答继续解释 DII 报告第 5–8 章，科学逻辑和比较关系基本完整，但从“第10点”一直拆到“第21点”，大量小标题、短段和单句判断分别占行；同一因果链被切成许多视觉块。
- 第二份回答解释 (t_v(z)) 与“目标组成量”，把一个本可连续说明的推导拆成 8 个编号小节，并频繁把一句解释、一个短公式、一个结论分别独立成段。公式本身正确并不能抵消过度分页式写法造成的阅读负担。
problem:
- **一句一段不是清晰**：当相邻句子共同解释同一个概念、同一因果链或同一公式时，应组成自然段。把每个判断单独换行，会迫使读者反复重新进入上下文，并人为拉长页面。
- **标题数量必须服从信息层级**：不能因为内容较长就按“10、10.1、11、11.1……”持续切分。只有读者真的需要跳转、比较或区分独立问题时才增加标题；连续推导优先用少量段落完成。
- **公式不应机械独占一段**：简短定义、一步关系和局部推导优先行内；只有核心公式、复杂多行表达或需要被后文反复引用的关系才独立展示。公式前后的解释应尽量留在同一语义段附近。
- **阅读负担是整篇属性**：单个短段可能清楚，但几十个短段连续出现会形成“卡片流／讲义碎片”式阅读体验。QA 需要检查整屏和整篇的段落密度、滚动长度和视觉切换次数，而不是只判断每句是否可懂。
- **正例不能机械复制外形**：前一轮 DII 方法解释被用户认可，成功原因是先建立直觉、真实对照和证据边界；后续回答错误地继承了大量编号和短块形式。应保留解释逻辑，而不是把“分层解释”误实现成“每层都单独起标题、每句话都换行”。
desired behavior: 对复杂科研解释，优先使用连贯自然段；一段处理一个完整问题或推理单元。必要时保留少量标题和一个比较表，但不要把普通说明拆成列表式、卡片式或逐句换行。长答案可以详细，但视觉节奏应紧凑、连续。
boundary: DII、(t_v(z))、FedFisher、Dice 等属于项目内容，不进入通用规则。Clear Writing 只吸收“段落应按语义单元而非句子切分、标题/公式独立展示需要真实阅读价值、整篇纵向阅读成本需要验收”的通用问题。本例未证明正式 Clear Writing production path 已被调用，故记录为真实用户反馈，不作为插件运行回归或发布证据。

#### 2026-10-16：DII 融合方案评估仍存在过度断行与非必要英文
feedback_status: NEW
source: `Distributed_Imaging_Inference` 融合方案评估 Markdown；用户于 2026-10-16 明确要求“处理这份 markdown 里的非必要换行和英文”，并指定 `philosophy` 这类普通概念应改成中文，同时要求把原稿作为 Clear Writing negative sample。
evidence:
- 用户提供的原稿共 595 行。内容和数学论证已经基本完整，但大量相邻句子各自单独成段；同一个因果链会连续出现“一句判断 → 空行 → 一句解释 → 空行 → 下一句”，导致页面被人为拉长。
- 中文正文持续混用 `decoder`、`loss`、`memory`、`optimizer`、`objective`、`audit`、`held-out validation`、`inclusion probability`、`penalty`、`regularizer`、`philosophy`、`surrogate`、`trade-off`、`dataset compression`、`feature coreset`、`rare pathology`、`optimal allocation` 等普通技术或逻辑词。它们在当前语境中并不承担正式专名、代码、检索定位或逐字核对作用，可以直接用自然中文表达。
- 同一文档也包含确有保留价值的英文/缩写，如 `GPT-5.6 Pro`、`GPT-6 Pro`、`GPT Work`、`HAMP`、`DII`、`PSMR`、`MFAC`、`M&Ms`、`CARE`、`Dice`、`Transformer`、`U-Net`、`JPEG`、`Markdown` 以及数学变量。问题不是“出现英文”，而是没有逐项判断英文是否真的有当前阅读价值。
problem:
- **语义连续却视觉碎片化**：相邻句子共同完成一个解释单元时，应优先组成自然段；不能把“每句话都能独立理解”误当成“每句话都应该独立成段”。这与前一条 DII 过度断行反馈相互印证。
- **普通技术词不应靠英文制造精确感**：当中文译法不会妨碍复制、搜索、执行或精确核对时，应直接中文化。保留 `philosophy`、`memory`、`audit` 之类词不会增加科学精度，只会增加语言切换和阅读成本。
- **专名与普通概念必须分开处理**：不能把“减少非必要英文”实现成全局翻译。正式模型/方法名、稳定缩写、公式符号和文件格式仍需保留；普通概念则不应因为来源文档使用英文就机械继承。
- **清理必须保持内容保真**：本例的修复范围应限于合并非必要断行、中文化非必要英文和删除无读者价值的内部来源残片，不应趁机改变数学结论、公式、比较关系、方法选择或实验建议。
desired behavior: 对中文或中文主导的科研解释，在最终输出前做一次整篇阅读层检查：按语义单元合并段落；逐项审查保留的英文是否承担正式专名、机器字符串、检索定位或逐字核对作用；若没有，就用自然中文替换。长回答仍可保留必要标题、公式、引文和列表，但不能让这些结构退化成逐句分页。
boundary: DII、HAMP、PSMR、MFAC、M&Ms、CARE 及该文档的数学判断属于项目内容，不进入通用写作规则。当前样本是用户确认的真实负例；尚未证明正式安装的 Clear Writing production path 已处理过该文本，因此不作为插件运行回归或发布失败证据。

2026-10-17 follow-up：与 DSFedMed / D3S2 比较时再次退回英文概念堆叠。用户先要求“说人话”，助手上一条回答却在中文科研解释中重新大量使用 `patient structure`、`hierarchical multi-fidelity allocation`、`downstream reuse`、`independent high-fidelity audit`、`patient coreset`、`spatial-only memory`、`memory artifact`、`benchmark`、`feature memory` 等普通英文组合来承担核心论证。用户随即指出“又开始非必要英文了”，并要求作为 Clear Writing negative example 记录。

新增问题：
- 即使正式方法名如 DSFedMed、D3S2、HAMP 需要保留，**围绕这些方法解释创新点时的普通概念仍应使用自然中文**。例如“患者结构”“患者—空间两层多保真分配”“后续任务复用”“独立高保真审计”“患者核心集”“仅空间层方案”“压缩记忆造成的假象”等都能准确表达，不需要英文短语。
- 不能因为正在比较国际论文，就把英文论文中的抽象短语直接搬进中文解释。来源语言不构成保留英文的理由。
- 对用户已经连续要求“说人话、减少非必要英文”的项目，普通 Web 回复仍然反复回退到英文术语栈，说明这不是一次偶发措辞问题，而是**最终输出前缺少整篇语言层复查**。
- 正确修复不是把所有英文逐字翻译，而是保留正式方法/模型名和必要检索身份，把“我们到底比别人多做了什么”重新写成自然中文因果关系。

#### 2026-10-15：DII 方法解释成为可复用的 Clear Writing 正例
feedback_status: NEW
source: `Distributed_Imaging_Inference` / 用户阅读导师研究提案 PDF 后，要求“用人话解释我们到底要做什么、是否真的比 FedFisher 更有意义、是否真正受导师三个想法启发，以及应该怎样读方法”；用户随后明确反馈“我很喜欢你这个回答”，并要求作为 Clear Writing 正例记录。
evidence: 当前对话中的完整回答；不复制私人科研原文，只记录表达结构和用户确认的阅读体验。
positive:
- **先给一句可复述的主线**：开头不用术语堆叠，而把整项研究压成“医院不再每轮重新训练和上传模型，而是在一次参与窗口里告诉服务器：当前强模型附近，本地分割目标会怎样变化；服务器据此继续做几步适配”。读者先获得 mental model，再进入论文和公式。
- **用真实强基线解释‘为什么需要新方法’**：没有泛泛说“现有方法不足”，而是直接拿 FedFisher 对照，分别说明它“给服务器一个最终答案”和候选 DII“想给服务器一张局部地图”的使用场景差异；同时明确写出“目前不能说我们的东西比 FedFisher 更有意义”。这让价值判断与证据强度同时可读。
- **把导师三个想法落到算法里的不同角色**：MOSAiC 对应“传什么对象”；Dice/CE 等目标结构对应“哪些信息不能丢、怎样组合”；影像/组织/边界冗余对应“怎样把有限预算放到真正未知的非线性变化”。没有把三个想法并列成口号，也明确第三个想法仍是最需要验证的假设。
- **先解释一个公式，再逐层扩展**：读者先只需要理解 `局部目标 = 当前值 + 一阶变化 + 非线性余项`，把它理解成“切线 + 偏离切线的部分”；随后才解释 Dice、二次代理、NTK-FL 和空间响应。数学被用来固定已经建立的直觉，而不是让符号承担全部解释工作。
- **主动提供阅读路线而不增加新内容**：把 6 页 PDF 分成三遍阅读：先理解问题/前作/主意，再读目标与余项公式，最后看成本和实验。这个结构降低了第一次阅读的认知负担，但没有删掉详细数学、限制或竞争方法。
- **比较和 caveat 直接贴着结论**：例如“如果只需要一个模型、医院随时在线、PEFT 很小，FedFisher/FedAdam 可能更合适”；“第三个冗余想法仍待证明”；“如果二次代理已经足够就停止”。这些限定没有变成审稿式防御段落，而是直接帮助读者决定方法何时值得用。
- **中文主体稳定，英文只保留正式方法名或必要术语**：FedFisher、NTK-FL、MOSAiC、MAP 等作为精确身份保留；普通解释用自然中文完成，没有让英文术语替代因果关系。
why this is a useful positive sample:
- 这是“复杂科研方法解释”而不是简单短答，说明 Clear Writing 的目标不是把答案压短，而是让每一层细节都有明确进入顺序。
- 正向模式可以概括为：**一句人话问题/方法主线 → 一个真实对照说明为什么值得考虑 → 机制分解 → 单个核心公式的直觉 → 分层阅读路径 → 证据边界和停止条件**。这只是成功样例，不应被机械固定成所有科研回答的模板。
boundary: FedFisher、MOSAiC、NTK-FL、Dice、CARE、M&Ms 和具体方法判断属于 DII 科研内容，不能进入通用 Clear Writing 规则。Clear Writing 可复用的是读者负担管理、对比方式、公式引入顺序、证据强度与语言层次。当前回答未证明经过正式安装的 Clear Writing production path，因此记录为真实用户确认的正例，不作为插件运行 PASS 或版本发布证据。


#### 2026-10-16：DII 三方案对比形成正例，原始研究文档暴露术语与公式解释负担
feedback_status: NEW
source: `Distributed_Imaging_Inference` / 用户要求比较两份 GPT Pro 与一份 Deep Research 的 DII 设计，并明确要求“控制非必要英文和非必要换行，多用段落文本”；用户阅读后反馈“好了不少”，要求把该回答作为 Clear Writing 正例，同时把三份原始研究文档中的典型可读性问题作为反例记录。
evidence:
- 正例：当前对话中对三份方案的比较回答。回答分别用自然段解释 GPT-5.6 Pro、GPT-6 Pro 和 Deep Research 的核心设计，先说明“相比旧方案到底改了什么”，再给一个紧凑比较表和最终倾向；没有把数据集、文献清单或执行细节放在主叙事前面。
- 反例 1：原始研究文档中直接使用 `provenance`、`halo`、`tile`、`estimand` 等英文词承载关键概念，却没有在第一次出现时用自然中文解释其具体角色。用户明确反馈这些词“对我理解非常困难，完全没有意义”。其中 `halo` 实际指局部特征块周围为保证感受野而额外保留的上下文边缘，`tile` 是局部特征块；若读者不知道这些角色，保留英文不会增加精确性，只会增加术语切换成本。
- 反例 2：GPT-5.6 Pro 的“5.3 多尺度余项估计”直接写出 (widehat T_{kij}) 的构造式及 (mathbb E_S(widehat T_{kij})=T^H_{kij})，但没有先用一句话说明 (widehat T_{kij}) 究竟代表“第 k 个中心、第 i 位患者、第 j 个目标组成量的高分辨率近似估计”，它位于患者内部还是中心级、为什么需要估计它、后面怎样进入损失。用户因此在这一段无法建立数学对象的 mental model，必须额外追问。
positive:
- **先讲方案改变了什么，再讲细节**：例如把 GPT-5.6 Pro 压成“旧方案压缩模型附近的 loss 曲面；新方案压缩医院训练数据，使服务器以后还能重新训练”，让读者先理解方法类别变化，再看多 loss、多 decoder 等能力。
- **每份方案先给一句人话定义**：GPT-6 Pro 被解释为“全部患者便宜版 + 少数患者完整版”；Deep Research 被解释为“每位患者先做便宜计算，只有值得的病例升级到完整 3D 计算，并用概率校正保持原目标”。这比先上公式或术语更容易比较。
- **控制结构和换行**：三份方案各自一个 section，但 section 内主要用连续段落；只在三者都解释完以后使用一个比较表。长回答仍然详细，却没有回到逐句换行、十几层小标题或代码框。
- **必要英文只保留精确身份**：FedFisher、MOSAiC、GPT-5.6 Pro 等正式名称保留；普通概念如“患者训练记忆”“局部特征块”“目标量”“高低精度校正”优先用中文解释。英文术语如果确实需要检索，可在第一次中文解释后括号保留，而不是让英文替代解释。
- **最终判断建立在前文比较上**：回答最后明确偏向 GPT-6 Pro，并说明“能力更强、设计更简单、Deep Research 的成本原则必须带回主线”，没有再重复一遍三份报告的所有细节。
problem:
- **术语身份不等于读者解释**：专业英文只有在承担精确检索、正式方法名或机器身份时才应原样保留。普通技术概念第一次出现时，应先说明“它在这里具体是什么、为什么需要它、与相邻对象有什么区别”；必要时再括号给英文。不能用 `provenance`、`halo`、`tile`、`estimand` 这类词替代中文关系。
- **公式前必须建立数学对象的 mental model**：新符号第一次进入正文前，至少交代对象的层级/单位（患者、voxel、中心、目标组成量等）、它是已知量还是估计量、它要近似什么、为什么后文需要它。读者先知道“这个量是什么”，公式才负责精确定义；不能只给公式和无偏性/期望性质，要求读者自行反推符号语义。
- **下标越多，解释责任越高**：像 (widehat T_{kij}) 这种三重下标对象，第一次出现必须逐个解释下标角色，或者在上下文已经稳定时明确引用既有定义。否则即使公式数学上正确，用户仍会卡在符号解码而不是科学思想。
- **Clear Writing 不应擅自补科学定义**：如果上游 Research Authoring 没有说明某个符号究竟是患者损失、组成量还是中心摘要，语言层应标记“对象未定义清楚”并要求补足，而不是凭上下文猜测并润色成确定含义。
- **少英文、少换行的目标是降低推理负担，不是机械禁令**：正式模型名、论文名、代码 token、确实有稳定身份的术语可以保留；复杂公式和真正独立的比较也可以单独展示。判断标准是读者是否能沿着一个连续推理单元理解，而不是英文词数或段落数本身。
desired behavior: 对复杂科研方法解释，优先采用“先用一句自然中文定义对象/机制 → 给必要直觉或对照 → 再给公式/正式术语 → 紧接着解释公式如何进入下一步”的顺序。一个段落尽量完成一个完整推理单元；只有独立比较、真正的新问题或需要跳转时才起新标题。数学式出现后，正文应立刻回答“这个式子算出来以后拿来做什么”。
boundary: DII 的 PSMR、MFAC、双保真记忆、具体公式和科研判断属于项目内容，不进入通用 Clear Writing 规则。可迁移的是术语首次解释、符号对象定义、公式与直觉的顺序、英文密度、段落连续性和比较后的决策表达。本例来自 ChatGPT Web/用户附件，未证明正式 Clear Writing production path 已实际调用，因此作为真实用户确认的正反例，不作为插件运行 PASS 或版本发布证据。

#### 2026-10-15：研究综合回答退化为小型方案文档，重复结论与结构化包装压过决策
feedback_status: NEW
source: 用户于2026-10-15提供一份 ChatGPT Web 对 AI Research Stack 三份独立架构研究的综合回答，并明确指出：项目设置已经反复要求降低阅读负担，但普通回答仍然失效。
evidence:
- 回答开头其实已经给出最重要的事实与结论：三份研究均已完成，且共同反对新建中央“研工台”，更倾向把窄的交付保障能力嵌入现有 Bridge/Codex 正常入口。
- 随后又依次展开“七条共同点”“三者最大的不同”“最终应该做什么”“四个核心部分”“放在哪里”“两个实验”“最终判断”，多次用不同结构重复“不要新中央平台、只做身份/证据/返修接线”这一核心结论。
- 多个代码框只承载概念流程或示意关系，例如任务→源码候选→构建产物→真实运行对象→专业验收结果；并非需要复制执行的机器内容。表格与分节也重复了前文已经解释过的职责边界。
- 普通中文解释继续暴露较多可中文化内部术语，如 Owner、Reviewer、thread、Hook 等；Slurm、Bridge、Codex、GPT Work、`sbatch/scancel` 等正式专名或机器字符串可按定位需要保留。
- 回答把“研究报告共同事实”和“助手进一步合成的产品建议”放得过近：例如先总结三份报告的共识，随后把“复杂交付保障层”“真正的新能力只有三件”作为进一步方案。虽然有部分“我认为”提示，但整体视觉结构容易让读者误以为这些命名和产品边界本身也是三份报告已经共同冻结的结论。
problem:
- **结论已经成立后仍继续重建结构**：当开头两三段已经足以回答“完成了吗、共同结论是什么、差异在哪里”时，后续不能因为材料复杂就机械追加多层标题、七点清单、组件分解、位置表和最终再总结。新增结构必须带来新的决策信息，而不是换一套分类重复已有判断。
- **综合回答不应自动膨胀成方案文档**：用户要求同步研究结论时，默认任务是提炼共同判断、关键差异与当前下一步；除非用户明确要求架构设计/执行计划，不应顺势生成一份新的完整产品方案。详细实现构想可在核心回答后按需展开。
- **来源共识与助手建议必须分层**：先明确“3/3 报告都支持什么”“只有哪份报告支持什么”，再把“据此我建议什么”单独压缩呈现。不得让新的产品命名、组件拆分或实验设计看起来像已经由来源共同决定。
- **伪结构化与重复会叠加阅读成本**：本例与同日“伪结构化导致的信息密度下降”相关，但新增了长篇综合任务中的另一层失败——标题、列表、代码框、表格各自都可读，组合后却要求读者反复重新归类同一结论。回归判断应看整篇信息增量，而不是单个段落是否清楚。
- **项目设置/普通入口的消费可靠性是独立问题**：用户明确指出其长期 Project 设置已反复要求中文、先结论、减少非必要英文、避免机械分节和内部状态堆砌，而该普通 Web 回答仍明显回到“完整架构 memo”风格。这可以作为 Project 设置或普通回复语言层未稳定生效的真实证据；但在没有插件实际调用身份前，不能声称正式 Clear Writing candidate 本身已经运行失败。
- **正向回归目标不是强制短答**：同类综合回答应优先压成少量自然段，先交代完成状态、共同结论、真正分歧和是否需要动作；只有确有比较价值时再用一个紧凑列表或表格。若用户明确要求完整研究综述、逐份报告比较或可执行设计，较长结构仍然合法。
regression use: 该样本在 ChatGPT Web 正式验收前已经暴露，因此只能进入 `response-clarity` / G5 的 known regression bank，不能以后再冒充 G7 unseen/fresh holdout。
project-specific context: AI Research Stack、Bridge、CARE、Lucerna 及三份报告的具体架构结论属于项目内容，不进入通用写作规则；通用规则只保留“结论后的信息增量、来源共识与助手建议分层、普通综合回答不要自动膨胀为内部方案文档、Project 设置是否真实约束普通回复”这些可迁移失败模式。

#### 2026-10-20 follow-up：已证明 response-clarity 加载后仍发生整篇失控
feedback_status: NEW
source: Bridge Kit 0.11.1 完成汇报线程；用户在同一消息中手动选择 Clear Writing，并随后明确指出最终回答仍有 24 个编号章节、超长纵向结构和大量对判断无帮助的内部实现细节。
evidence:
- 当前线程的真实工具轨迹在最终答复生成前实际读取了 installed `writing-style/response-clarity` 与 `writing-style/writing-fidelity`，因此本例不再属于“无法证明 Clear Writing 技能是否加载”的旧证据级别。现有观测仍不能证明 ChatGPT UI 中手动选择的 app id 与技能加载之间的内部平台路由链，也不能观察模型内部每一步如何消费规则；但可以证明对应 production skill 内容已经进入本次生成上下文。
- 同一线程同时存在用户/Project 层的中文、结论先行、降低阅读负担、避免内部状态和不必要英文等明确约束；最终回复仍把“说服用户产品确实完成”误实现成逐项重述 architecture/gate/evidence。
- 典型无价值展开包括“没有 daemon / 数据库 / 第二状态机 / 长期 Codex session / app-server progress thread / watcher hierarchy”等负面实现清单。它们对架构审查曾有价值，但对当前用户判断“是否完成、正常怎么用、还剩什么”没有新的决策信息；一句“Persistent Run 只负责断线存活，不引入新的常驻控制层”即可保留必要含义。
root-cause evidence:
- 本例首先排除“完全没有加载 response-clarity”这一归因；技能已读取但没有形成可靠的整篇最终输出约束。
- 现有 `response-clarity` 已明确要求结论先行、减少内部流程噪声、整篇检查碎片化，并规定核心问题回答后如果后续材料不增加新证据/改变决策就停止。因此当前失败不是简单缺少“少用列表/少写内部词”规则。
- 更符合证据的失败机制是：内容选择阶段把 repository audit 中“证明判断成立所需的内部证据”误当成“用户必须看到的正文”，随后没有可靠的 whole-response final pass 把已无信息增量的 architecture/evidence 展开删除或下沉。当前 normal skill load 是 advisory context，不等于存在一个独立、强制、可观测的最终产物审校阶段。
repair target:
- 不新增禁词表、固定长度、固定章节数或 Bridge 专用特判；也不把项目技术事实写进通用规则。
- AI_Skills Planner 应先判断应修的是 `response-clarity` 的 whole-response application/normal-entry acceptance，还是 ChatGPT plugin routing/finalization 的消费可靠性；只有能证明 production source 缺口时才修改 skill 文本。
- 回归必须使用同类“复杂技术完成汇报/综合判断”正常入口：给足真实架构和验收事实，同时要求详细说明；PASS 不是单纯变短，而是第一屏回答完成状态、架构主线、正常使用和真实剩余项，技术证据只保留能改变信任判断的部分。必须证明完整最终回复改善，而不是只检查局部句子或字符串。
- 本例是已知 regression，不能作为后续 unseen holdout；它应与 2026-10-15 的“综合回答膨胀成方案文档”合并维护，而不是新增重复顶层规则。
boundary: Bridge Kit 的具体模块、Gate、SHA、Notifier/Persistent 实现属于本次产品事实，只用于重放输入，不进入通用 Clear Writing 产品规则。当前线程可以证明 skill load，但不能观察 ChatGPT 平台内部 app-selector → skill-router 的专有调用日志；如需证明手动选择本身的路由链，必须由 ChatGPT/plugin runtime 可观测面或正式 normal-entry replay 提供。

### 任何 README.md 修改都必须经过 Clear Writing 检查
status: PROMOTED
tracking: #12
source: 用户反馈 / AI Research Stack README authoring, 2026-09-24；Issue #12 follow-up, 2026-10-04
evidence: Codex 多次跨仓库修改 README 时，可能让技术事实保持正确，却在明确中文的文档里留下不必要的英文脚手架。2026-10-04 的真实反馈进一步指出：现有 README 修改再次出现了普通英文可以中文化却仍保留的问题，说明当前 Clear Writing / `chinese-prose` 已有对应语言能力，但正常 README 修改入口没有稳定消费它。
target layer: 仓库维护 / README 消费入口 / Clear Writing 终审
problem: README 是主要面向读者的仓库入口，但 Codex 仍可能把它当作普通维护文本处理，绕过专门的语言终审。缺口不在于 Clear Writing 缺少“中文 README、中文为主、删除非必要英文、保留精确技术字符串”的能力，而在于 README 修改任务没有稳定触发它。当前任务负责人 / repository maintainer 仍负责事实、命令、版本、安装步骤、架构和范围；Clear Writing 负责最终读者可见语言质量，并且不得改变技术含义。
candidate_action:
- 只要本仓库根 `README.md` 被当前任务修改，无论修改大小，任务结束前都必须实际调用当前安装的 Clear Writing（`writing-style`）做读者可见语言检查。只读 source `SKILL.md`、在 prompt 里声称遵守规则或做字符串扫描，都不能算已经调用。
- 检查至少覆盖受影响的读者区域；如果局部修改造成上下文语言不一致，就扩大到相关章节，而不是只看 diff 中新增的几个词。
- 中文 README 的普通解释、标题、连接语、维护说明和面向读者的技术说明默认使用自然中文；普通英文概念不因代码、配置或来源使用英文就继续暴露给读者。
- 产品正式名称、插件名称、代码、命令、路径、文件名、字段、配置键、版本、协议值、状态值和其他必须精确匹配的机器字符串可以保留，不为了中文化而翻译。
- 如果本次 README 修改只有版本号、链接或其他机器字符串，Clear Writing 检查后可以原样放行，不得为了证明调用而强行改文案。
- repository maintainer / 当前任务负责人负责 README 的事实、版本、命令、架构和范围；Clear Writing 负责最终面向读者的语言质量，不接管 Research Authoring、`workflow-core` 或技术事实判断。
observed_handling: 2026-10-04 已提升为仓库级 `AGENTS.md` README 修改合同，并新增最小回归测试，防止规则退回“只有新建或大改 README 才触发”。本次只改变仓库治理规则和 tracking 文案；没有修改 `writing-style`、`ai-skills-core`、`workflow-core` 或 `research-writing` 的 production skill source，也没有版本发布。后续 normal-entry smoke 中，用户只要求做根 `README.md` 的小型中文化整理，并没有显式要求调用 Clear Writing；Codex 读取仓库 `AGENTS.md` 后实际调用了当前安装的 `writing-style:chinese-prose`，先读取 skill 规则，再对 README 受影响的读者区域执行语言终审。该 smoke 清理了 `thread`、`handoff`、`wrapper`、`source`、`coordinator` 等非必要英文，同时保留正式产品名、plugin slug、路径、命令、字段和版本，证明仓库级 README contract 已被正常入口实际消费，而不只是静态规则存在。随后修复了一个陈旧单元测试，避免它继续把 README 的英文读者措辞冻结为合同。
promotion_gate: 已满足。当前推广条件由用户明确确认的长期跨项目偏好（“任何 README 修改都必须经过 Clear Writing”）和 2026-10-04 真实 normal-entry README smoke 共同满足；后续其他中文仓库和英文 README 案例属于持续泛化/回归证据，不再阻塞 #12 closure。这里不声称已经完成旧版 2 个中文 README + 1 个英文 README 对照回放。


### Promote `writing-style` into the generic content-preserving language layer
status: READY_FOR_PROMOTION_AFTER_050
tracking: #13
source: 050 Deep Research rewrite failures + Distributed Imaging report v2 + CAT-TRACE presentation reviews + cross-plugin boundary audit, 2026-09-05
evidence: `docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md`; task 050 smoke/replay evidence; `docs/plugin-todos/research-writing.md`; `docs/plugin-todos/presentations.md`
release evidence (2026-10-19): Clear Writing `0.5` / repository `5.5.1` formally released at `fd79c4be54fc50bd66d9a51bbc1e681f361f6a77` and integrated into main at `57c5a2c8124752587688475b3ebc09c198d35186`. The user confirmed the existing USER / PRIVATE ChatGPT plugin is `0.5.0`, with all 27 files read back and compared against the formal generated payload, no drift beyond version normalization `0.5 -> 0.5.0`. This completes the bounded release, not this item's broader promotion gate. Required statistical result/caption adaptation remains pending in `docs/plugin-todos/statistical-modeling.md`, heading `Delegate reader-facing wording without giving away statistical semantics`, tracking `#73`; scientific-visualization caption/annotation adaptation remains pending in `docs/plugin-todos/scientific-visualization.md`, heading `Delegate captions/annotations without giving away visual semantics`, tracking `#49`. Keep the original promotion gate and source maturity unchanged until those handoffs and the remaining required evidence are satisfied. Release closure evidence: `results/clear-writing--release-closure/STAGE_B_CLOSURE.md`.
target layer: routing/language/fidelity
problem: the old `Writing Style` display name undersold the product and was easy to confuse with `research-writing`. The current display-name decision is now settled as `Clear Writing`, while the canonical plugin slug remains `writing-style` and no slug migration is planned in this cleanup. The remaining capability TODO is broader and still unresolved: make this plugin the reusable content-preserving reader-facing language layer that can be called by research reports, presentations, statistical analysis, scientific visualization, medical imaging, bioinformatics and other domain plugins for captions, conclusions, table/figure wording, slide copy, technical explanations and long source-faithful rewrites. It must improve clarity without taking ownership of domain semantics.
candidate action:
- Treat the plugin as the canonical source for generic reader-facing language behavior: Chinese-first wording, exact-name vs ordinary-reasoning English decisions, sentence/paragraph connective logic, first-use explanation, formula/caption/conclusion wording, local readability review and source-fidelity-preserving repair.
- Support multiple task sizes from the same canonical source: microcopy/caption/label/conclusion; paragraph/subsection; long existing-document rewrite; slide copy from a presentation-owned page brief; result explanation from a domain-owned claim/evidence brief.
- Keep domain semantics outside this plugin. `statistical-modeling` owns models, assumptions, inferential targets and conclusions; `scientific-visualization` owns visual encoding; `research-writing` owns document plan/evidence selection/tables/citations; `presentations` owns slide sequence/page jobs/rendered QA. The language layer may clarify their already-frozen content but must not change it.
- Do not maintain a separate “说人话” rule set inside every domain plugin. Reuse the canonical `skills/writing/core/...` source through the production-compatible packaging/companion route rather than forking behavior.
- Keep the fidelity contract strong: facts, numbers, formulas, citations, uncertainty, attribution, comparators, evidence authority and conclusion strength cannot drift for readability.
- For long existing-text structural rewrite, allow reader-facing regrouping/order changes while preserving every source proposition/evidence boundary; for short captions/microcopy do not force the heavy rewrite runtime.
- Current naming decision: displayName is `Clear Writing`; slug remains `writing-style`; do not perform slug migration, directory migration, compatibility aliasing, profile migration or production identity changes as part of this TODO.
- Any future slug migration would need a separate bounded migration with source config, generated plugin, profiles/docs/tests, real installed replay and compatibility retirement evidence. This item should not assume such a migration.
promotion gate: do not treat the display-name cleanup as resolving this capability item. Promote the remaining language-layer work only after 050 identity/acceptance is closed and replay verifies at least one long rewrite, one advisor report, one presentation handoff, one statistical result/caption, and one scientific-visualization caption/annotation without domain-semantic drift.

### Advisor-facing English can sound AI-authored even when every sentence is correct
status: NEW
tracking: #14
source: Distributed_Imaging_Inference / MOSAiC group-meeting report rewrite, 2026-09-19
evidence: DII advisor-facing draft at commit \`fcf3713ede17afbcfebce2c070dd6e888608edae\`; user-supplied independent style review; revised DII report at commit \`55acbcdcb7253da34a6167be35661e40fba74805\`
target layer: scientific-prose / advisor-facing English / document-level QA
problem: A technically accurate English report can still feel obviously LLM-shaped when the entire document is built from repeated rhetorical templates. The DII draft had correct facts and careful evidence boundaries, but the prose repeatedly used highly regular patterns such as \`What ...?\`, \`Why ...?\`, \`How ...?\`, \`The key conceptual shift is...\`, \`The important point is...\`, \`The purpose is therefore...\`, and repeated \`not X, but Y\` corrections. Sections had similar length and internal grammar: announce thesis -> define -> contrast -> explain why it matters -> summarize. An independent fresh-thread review identified exactly this uniformity, rather than grammar or vocabulary, as the strongest AI-writing signal. The Chinese explanatory notes felt more natural because they followed the researcher's actual thought process and allowed uneven emphasis.
candidate_action:
- Do **not** use \`What / Why / How\` question headings as a default outline generator. Prefer headings that name the actual scientific object: \`Tensor Train as the compression layer\`, \`M&Ms cardiac MRI\`, \`The first imaging version of MOSAiC\`, \`Information sent by each site\`.
- Do not force every section into the same rhetorical shape. Allocate detail according to scientific importance. A dataset section may be factual; a method section may need intuition + formula; a limitation may need only one sentence.
- Remove redundant signposting when the next sentence already carries the meaning. Phrases such as \`The key point is\`, \`The important computational tool is\`, \`This matters because\`, \`The purpose is therefore\`, and \`This gives a clean target\` should appear only when they add real orientation, not as paragraph glue.
- Treat repeated \`not X but Y\` framing as a specific smell. Use it only when the reader is genuinely likely to hold misconception X. Otherwise state Y directly. Example: prefer \`A frozen segmentation model converts each image into logits, and MOSAiC operates on the resulting risk function\` over \`The central technical step is not to apply TT to MRI and not to compress neural weights; instead...\`.
- Avoid mechanically symmetric \`Question 1 / Question 2 / Question 3\` sections when ordinary prose or one compact comparison table is clearer. Decision tables are useful when a real decision exists, but should not be generated merely to make the report feel complete.
- Preserve a researcher voice where appropriate. Advisor-facing prose can naturally say \`At the last meeting, the main question was...\`, \`For this first experiment, we keep the adaptation space small\`, or \`I do not want to interpret Centre as scanner\`. This is often clearer than detached research-brief language.
- Caveats should sit next to the claim they qualify. Do not pre-emptively defend every paragraph against an imagined reviewer. Keep necessary provenance/evidence limits, but do not let qualification become the dominant rhythm.
- Use concrete scientific nouns early. Name the model, modality, patient/site count, risk object or comparison before introducing abstract phrases such as \`function-centric perspective\`, \`decision logic\`, or \`operational property\`.
- Vary sentence and paragraph length only as a consequence of content, not as an artificial humanization trick. The goal is natural authorial reasoning, not deliberate imperfection.
- A final English QA pass should ask: **Does this sound like a PhD student explaining the project to an advisor, or like a polished research brief generated from a prompt?** Flag repeated rhetorical templates across the whole document, not only locally awkward sentences.
- This is **not** detector-evasion. Do not inject mistakes, slang, random inconsistency, fake personal anecdotes, or arbitrary sentence variation. The objective is reader fit and authorial voice while keeping all facts, numbers, formulas, citations, uncertainty and claim strength unchanged.
observed_handling:
- The revised DII report removed the repeated question-heading skeleton, collapsed several meta transitions, reduced \`not X but Y\` usage, and reused the user's earlier plain-language explanation of the imaging bridge.
- The new English version begins from the advisor's prior question, explains MOSAiC in the same order the researcher would speak, gives dataset background before project-specific splits, and lets equations appear only where they clarify the actual statistical object.
promotion_gate: replay on at least one additional advisor-facing English research report and one manuscript-like technical summary. Promote only if the same over-symmetry / over-signposting pattern recurs; do not build a fixed banned-phrase list.

### English scientific slide microcopy and full-deck prose remain cognitively heavy after a nominal final pass
status: NEW
tracking: #15
source: TRACE / CAT-TRACE group-meeting deck v4–v8 reviews
evidence: `YuukiAS/TRACE` commits `e36cb5d93fc882ce158d88ac9201fe494b98b69a`, `1de90f2f26b3f787073ecedd7a4df41a985712eb`, `ef08bc25673fb33b639e523504676c0f333d93f4` and `26fd2ad0f042f0a8d7c7dc2154392e3f9460760d`. Earlier rounds exposed `Failure prevented`, mechanical `Example.` language, `What it measures`, `Focal method`, `Backbone` and `Rare fit`. The 33-page v8 deck still contains first-use domain terms that are expanded but not placed in enough context for a statistics audience (`COI`, `Metabarcoding`, `VicFlora`, `MGP`), source-note-like wording such as `That threshold is an implementation choice, not a CAT-TRACE theoretical constant.`, and dense table/slide language that is grammatically valid but unnecessarily hard to parse. The v8 English-final-pass record explicitly says that it only reviewed visible wording touched in v8, so untouched but still difficult language could survive.
problem: `scientific-prose` / presentation handoff needs to distinguish grammatical correctness from reader effort. A research slide should let a first-time expert reader understand what an unfamiliar term is, why it appears here, and what the sentence is asking them to retain. Expanding an acronym alone is insufficient when the term remains contextless. Final slide prose review also cannot be limited only to source lines modified in the current round: layout changes alter wrapping and old wording may still be cognitively heavy. The desired behavior is a full-deck audience-facing pass after scientific freeze: direct sentences, explicit local context for unfamiliar terms, natural action labels, short explanatory bridges where needed, and removal of internal/defensive/meta wording. This is not detector evasion and must not weaken scientific precision.
project-specific context: CAT-TRACE, TRACE, CORAL, VicFlora, COI, OTU, GBIF, MGP, catalogue/open-tail and the specific slide sentences belong to this project. Do not create a CAT-TRACE-specific banned-word list, and do not let writing-style alter equations, scientific claims, dataset values, theorem status, citations or slide layout.

### Versioned Chinese technical documents can regress into English-keyword scaffolding during content-preserving revision
status: NEW
tracking: #16
source: TRACE / CAT-TRACE canonical architecture and code implementation plan, 2026-09-09
evidence: compare `YuukiAS/TRACE/docs/model/catalog_aware/CAT_TRACE_CANONICAL_NOTATION_AND_ARCHITECTURE_20260908.md` with `...20260909.md`, and `CAT_TRACE_CODE_IMPLEMENTATION_MASTER_PLAN_20260908.md` with `...20260909.md`; user review of the rendered 20260909 PDFs found the newer technical content substantially stronger but the reader-facing Chinese markedly worse. Examples include prose such as `TRACE continuity + 按组标记的开放尾部 + residual structure`, `极端 rare-tail / scale stress test`, `production inference`, `composite 后验 interval`, `independent-residual`, `working set`, `source script`, `taxonomy-proxy variant`, `structured dependence`, `large-p engine`, and many sentences built from English noun chains joined by `/` or `+`. The 20260908 versions were easier to read despite containing older scientific decisions.
problem: content-preserving revision of an existing Chinese technical document needs a version-aware prose contract: the newest version is authoritative for scientific content, notation, numbers and decisions, while an earlier accepted version may be the style/readability baseline. A revision pass must compare the full document, not only newly changed lines, and must prevent ordinary reasoning words from drifting back into English merely because the executor is editing technical content. Exact code identifiers, library names, method names and necessary acronyms should remain unchanged, but ordinary connective logic, section prose, role descriptions, implementation explanations and phase descriptions should be natural Chinese. This is a readability/fidelity problem, not a request to ban English globally or to alter domain semantics.
project-specific context: CAT-TRACE notation, zero-slot logic, `C^{tax}`/`C^{phy}`, rd001–rd003 roles, R/C++ API names and implementation phases belong to TRACE. Do not promote those details into generic wording rules. The general reusable lesson is to support `current content authority + prior accepted prose baseline + full-document readability diff`, while preserving formulas, code fields, filenames, method/library names, citations and scientific claim strength.


### Product UI microcopy should state user consequence, not internal implementation reassurance
status: NEW
tracking: #17
source: Lucerna task 01050 full-panel user review, 2026-09-24
evidence: normal UI copy included implementation-facing reassurance and verbose maintenance prose such as force-push disclaimers, repair-visibility explanations, and dense first-sync file-operation summaries even when the primary user question was simply whether the feature was ready and what action was available
problem: Technically accurate microcopy can still be poor product language when it narrates implementation policy, defensive guarantees or exhaustive operation detail that the user did not ask for. Normal UI needs a strict reader-value filter: say the current state, consequence and next action first; move low-frequency implementation guarantees, diagnostics and detailed change summaries behind details/help/confirmation surfaces.
project-specific context: Lucerna's Overleaf, recovery and Zotero wording is project-specific. Frontend Design owns placement, progressive disclosure and visual hierarchy; writing-style owns the reusable wording discipline once the UI role is frozen.

## Open candidates

### Audit `academic-humanizer` only for genuinely missing academic-writing capabilities
status: CANDIDATE_GENERIC
tracking: #18
source: external resource discovery, 2026-09-02
evidence: `AIScientists-Dev/academic-humanizer` at commit `94b88b23703bed7df507acae7d6d5876209a0cdf` (`SKILL.md` v0.3.3), MIT. The inspected public skill focuses on English academic editing: AI-assisted paper/thesis/rebuttal/proposal cleanup, claim-evidence calibration, author-voice matching, and paper-vs-NSF/NIH proposal register. It has useful before/after academic examples, but much of its claim-strength and anti-template guidance overlaps the current `scientific-prose`; it also contains team-specific stylistic preferences such as broad AI-tell lists and a blanket em-dash removal rule.
target layer: writing
problem: this source may contain a few capabilities that are genuinely missing from the current `writing-style` / `research-writing` stack, especially author-reference voice matching and paper-vs-grant register separation. It should not be added to the active 047 scientific-rewrite architecture merely because it is popular, and its AI-tell catalog must not become another phrase wall. The current 047 frozen Plan intentionally uses only `shuorenhua` and `human-writing-skills` as selectively ported architecture sources.
candidate_action: keep `academic-humanizer` as `REFERENCE_ONLY` during 047. After 047 closes, run a bounded source-vs-current-capability audit against `scientific-prose`, `writing-fidelity`, and relevant `research-writing` skills. Selectively port only a concrete capability that is absent, non-duplicative, license-compatible, and supported by a real task. Do not wholesale vendor the repo, create a new top-level humanizer plugin, copy broad banned-word/AI-tell lists, import author-specific house-style rules as universal rules, or duplicate claim-evidence behavior already implemented.
promotion_gate: promote only if the later audit identifies a specific missing production capability and a real replay shows that current skills fail without it. Otherwise record `REVIEWED_NOT_ADOPTED` / `REFERENCE_ONLY` and leave production behavior unchanged.

### Keep style cleanup downstream of scientific structure
status: CANDIDATE_GENERIC
tracking: #19
source: real Presentation and advisor-report revisions
evidence: repeated user feedback on AI-like internal language, rhetorical templates and unnatural Chinese
target layer: writing
problem: style rules can accidentally take ownership of scientific structure or artifact mechanics.
candidate_action: preserve the current boundary: `writing-fidelity` protects facts, `scientific-prose` / `chinese-prose` polish reader-facing language after evidence/structure are stable.
promotion_gate: only add new style rules when repeated across independent real artifacts; do not duplicate research-reporting/presentation structural rules.

#### 2026-09-11：导师文稿需要摆脱内部策划口吻，而不只是减少英文
feedback_status: NEW
source: Distributed_Imaging_Inference / 将研究记录改写为上次会议纪要和下次会议报告。
evidence: DII内部记录 `docs/research/DII_FEW_SHOT_ADAPTATION_LITERATURE_POSITIONING_2026-09-11.md`（`59e45ed0d2abbccf4e5090ad960e24c0e1388db4`）；两份新草稿位于DII `deliverables/group_meeting_2026-09-05/meeting_minutes_2026-09-05.md` 与 `deliverables/group_meeting_2026-09-12/group_meeting_report_v1.md`（`6d295317cdcbc0d02958d5f0bf6ca9b90c77defd`）。
problem: 用户明确指出，“如果DGST后gap仍存在”“最终论文需要怎样的benchmark结构”“明日组会的完整叙事”不是面向老师的表达。即使把gap和benchmark逐词译成中文，句子仍在指导写作者如何准备材料，而不是直接向读者解释研究对象、证据和问题。
observed handling: 在研究文体、章节职责和证据范围先确定后，改写为“相关文献把问题推进到了哪里”“DGST：本次直接比较的方法”“下一阶段拟研究的问题”等直接讨论内容的句子。用完整中文解释参考病例、模型更新和测量修正之间的关系；保留正式方法名、指标及单位，不用内部状态代替结论。正文先说明实际含义，再在表注或附录交代可比性限制；删除的是面向执行者的措辞，不是尚未验证的事实边界。
project-specific context: 本例与Research Authoring的文体、时间线和来源工作分开记录，不重复接管证据选择、数据解释或会议归因。原文是有意保留的内部记录，不能因目标读者后来变化而追认其为原任务失败。当前没有正式Clear Writing插件调用或生产回放证据，新草稿也尚未获得用户认可；此处仅补充现有候选的真实需求和人工改写案例，等待后续回放，不修改正式插件规则。

### Deep Research 中文报告作为 `writing-style` 的真实压力测试输入
status: MANUAL_BASELINE_CAPTURED
source: ChatGPT Deep Research 中文科研报告，2026-08-31；2026-09-03 完成一次人工“说人话”重写作为可读性 baseline。该 PDF 由 Deep Research 直接生成，**没有经过 `writing-style` plugin**。
evidence: 用户提供的 22 页 PDF《共享预训练医学分割模型下的极低通信联邦适应：项目事实审计、算法前沿与下一轮实验决策》；正文反复出现 `anchor`、`provenance`、`estimand`、`scientific gap`、`method gap`、`residual gap`、`resource contract`、`strict one-shot contract`、`testbed`、`axis`、`comparator`、`correction/stability run` 等表达，并存在“法律意义上证明”“forensic-level exact provenance proof”一类不必要的法律/取证腔。2026-09-03 的人工重写在不重新检索文献、不改变实验数值、公式、算法名、数据集名、结论强度和未验证事项的前提下，把全文重新组织为读者先能回答“现在到底知道什么、为什么、下一步为什么这样做”，再进入算法和公式。
target layer: writing
problem: 这份 PDF 证明的是一个真实的中文科研写作痛点，不是当前 `writing-style` 的 production failure，因为插件尚未实际处理过它。用户要求“说人话”层在不改变任何事实、数字、公式、算法名、数据集名、引用、结论强度和证据边界的前提下，大幅降低阅读难度；不能只做逐词翻译，而要在语义完全保真的前提下按中文逻辑重新组织句子和段落，让读者直接知道“谁做了什么、为什么、结果说明什么”。现有 `chinese-prose` 已有中文优先、非必要英文清理、报告终审等规则，因此后续仍需要 production replay 才能判断具体缺口在哪一层。
manual_rewrite_lessons:
- **真正有效的是结构级重写，不是词级替换。** 原文最重的认知负担来自“英文名词链 + 内部审计标签 + 长句”共同作用。人工版通常先把一句话改成明确的中文问题或结论，再解释机制，最后保留必要英文定位词。单独把 `provenance` 换成“来源”并不足以改善可读性。
- **保真合同必须允许段落重排、合并和显式分层。** 在不改变 claim/evidence 对应关系的前提下，人工版会把散落在数页里的“已知事实 / 研究解释 / 不能声称什么 / 下一步决策”重新聚到一起。若 `writing-fidelity` 只允许 sentence-local paraphrase，会天然卡住真正的中文重写。
- **证据边界应变成读者可见的叙事骨架。** `[项目事实]`、`[文献事实]`、`[研究判断]`、`[候选方法]`、`[仍需核验]` 这类区分值得保留；但需要把“审计语气”改成读者能直接理解的作用说明，而不是让内部流程标签主导正文。
- **公式前后都需要中文解释。** 人工版不是删公式，而是先说公式在回答什么问题，再给公式，再解释变量和结论。对于方法报告，这一能力应比单纯 LaTeX 保真更高优先级。
- **方法综述表应服务一个决策问题。** 原始大表同时混合 venue、通信、server data、heterogeneity、objective relation、工程难度，读者很难抓主线。人工版先问“client 到底传了什么信息”，再按机制分组，最后保留完整方法表。插件应允许在零事实丢失前提下重建表格/段落层级，而不是逐行润色。
- **科研缩写与专有名词应保留，但普通逻辑必须中文化。** `FedFisher`、`FedLPA`、`M&Ms`、`LoRA` 等需要保留；`scientific gap`、`method gap`、`resource contract`、`testbed`、`axis` 等普通逻辑词应优先改成自然中文。关键判据不是“英文多不多”，而是删除英文后是否损失定位能力。
- **结论不能被“谨慎语气”埋掉。** 原文经常先写 provenance/法律式免责声明，再到真正结论。人工版将证据边界保留在结论之后或同段后半，使第一屏先回答“这对研究意味着什么”。这不是削弱谨慎性，而是调整信息顺序。
project-specific context: PDF 的具体研究对象是 one-shot federated medical segmentation、CARE、M&Ms、FedFisher/FedLPA 等；这些算法、数据集、公式和研究判断属于项目内容，不应被写成通用风格规则。该 PDF 只能作为已知 replay/stress case，不能在反复迭代后再冒充 unseen/generalization holdout。人工重写全文本身不得提交到 repository。
candidate_action: 下一步不再先扩规则，而是把 2026-09-03 人工版作为 readability reference，使用当前 production `writing-style` 对原 PDF 做完整 replay；Reviewer 只比较通用维度：claim/evidence 零漂移、段落重组能力、中文逻辑、公式解释、表格重构、非必要英文清理、未验证事项保留。若 production 输出明显只能做 sentence-local paraphrase，优先检查 `writing-fidelity` 是否过度限制结构级重写，再检查 `chinese-prose` / routing；不要为该项目增加词汇禁表。
promotion_gate: 当前 `writing-style` 在该真实 replay 上无法同时满足“内容/证据零漂移”和“阅读难度显著下降”，或随后另一个独立真实中文科研材料复现同类问题；若当前 plugin 已经能达到人工 baseline，则不为了制造 diff 修改 production skill。


### Reader-facing artifacts from upstream plugins need an automatic Clear Writing handoff before copy freeze
status: NEW
tracking: UNASSIGNED
source: STAT5060 Project final human-facing assessment production, 2026-10-08
evidence: the Project workflow produced Chinese/English Question Bank, examiner-guide and marking-guide copy under Research Authoring, then froze exact copy and sent it to Codex for production. The first human-facing Chinese PDFs contained machine-facing mixed language such as `pre-read`, `PRIMARY_FAMILY_UNCLEAR`, `private log`, malformed token splicing, and schema-like wording even though `chinese-prose` already declares that any reader-facing Chinese Markdown/PDF/report should automatically receive its final pass. The current Marketplace topology keeps `writing-style` and `research-writing` as separate plugins; the released Research Authoring plugin does not bundle or automatically dispatch to Clear Writing, while `research-main` includes the underlying writing skills only when that profile is actually used.
target layer: writing-style normal routing / cross-plugin handoff / Research Authoring integration
problem:
- The skill-level “automatic trigger” is not enough when the skill is not in the active plugin/profile surface. An upstream plugin can author a final reader-facing document without ever invoking Clear Writing.
- Student-assessment workflow can reach exact-copy freeze before any language-quality pass. Once the Planner/Controller freezes copy and tells the executor not to rewrite, a later Clear Writing trigger is correctly suppressed, so the defect survives into rendering.
- This means the current contract depends on a human remembering to name Clear Writing in the task prompt, which defeats the intended automatic-trigger behavior.
candidate_action:
- Add a cross-plugin **reader-facing language handoff** that occurs before exact-copy freeze for document-producing upstream plugins. Research Authoring should hand stable human-facing copy to writing-style automatically: `writing-fidelity` first, then `chinese-prose` for Chinese/Chinese-reference artifacts or `scientific-prose` for English scientific/technical prose as applicable.
- Make a successful language-pass receipt a prerequisite for freezing a newly authored human-facing copy surface, unless the user explicitly supplied exact final wording or explicitly opted out of rewriting.
- If writing-style is not installed/available in a standalone Research Authoring execution, fail closed with a precise companion-plugin blocker rather than silently treating raw Planner/Executor prose as final.
- Keep the handoff bounded: preserve question IDs, scores, formulas, exact English public questions, citations, dates, paths/tokens that are intentionally protected, and assessment semantics. Clear Writing may improve reader-facing realization only.
- Add normal-entry integration tests where a user asks Research Authoring to produce a bilingual student/instructor assessment package **without naming Clear Writing**. PASS requires that the Chinese/English human-facing sources automatically receive the appropriate writing-style pass before freeze and that the receipt is bound to the frozen source hash.
- Add a negative test: a render-only/exact-copy task after freeze must not opportunistically rewrite the document; the language pass belongs upstream of the freeze.
promotion_gate: replay on one new bilingual assessment artifact and one advisor-facing report initiated through an upstream plugin without an explicit “use Clear Writing” instruction; require automatic handoff, source-bound receipts, zero semantic drift, and no user-discovered Chinglish/machine-prose defects.

## Do not do

- Do not create detector-evasion or generic humanizer behavior.
- Do not let style rewriting change equations, claims, labels, versions or citation meaning.

### Product UI copy naturalness needs a dedicated microcopy capability, not more long-form prose rules
status: NEW
tracking: #90
source: CUHK Date / Meet at CU production copy-naturalness audit + founder calibration, 2026-09-26
evidence_path: `docs/design/product-ui-copy/evidence/CUHK_DATE_PRODUCT_COPY_NATURALNESS_AUDIT_2026-09-26.md`
target layer: writing-style routing / Chinese product microcopy / cross-plugin frontend handoff
evidence: anonymous production audit classified 150 public-facing zh-Hans/zh-Hant-HK strings as A=53 natural, B=72 readable-but-modelish, C=15 clearly unnatural, D=10 product/semantic problems. Repeated B/C patterns included product self-definition before user action, unnecessary explicit second person, over-balanced `not X but Y / only X then Y / first X then Y` rhetoric, ordinary status turned into slogans, internal product-state nouns, over-complete reassurance, and mechanical Simplified/Traditional adaptation. Founder independently identified examples such as `你先完成资料` and `只开放注册 / 先把资料准备好` as readable but not like mature product UI.
problem: current `chinese-prose` already performs well for reports, README, technical/scientific documents and general Chinese de-template cleanup. Its unit of reasoning is primarily prose/document-level readability. UI microcopy requires a different unit: **one text role inside a rendered product state, with neighboring copy and spatial/interaction context**. Expanding `chinese-prose` with many UI-specific rules risks regressing its now-useful long-form behavior while still failing to decide when a string should be deleted rather than rewritten.
candidate_action:
- Design a dedicated sibling capability such as `product-ui-copy` / `product-copy-naturalness` under the writing layer rather than turning `chinese-prose` into a universal UI copy skill.
- Keep `writing-fidelity` as the protected-meaning layer: registration/matching state, verification meaning, consent/privacy boundaries, legal facts and other product truths must not be softened away for naturalness.
- Require structured UI context from Frontend Design: surface, UI role, product state, user consequence/action, neighboring copy, locale, protected meaning, and length/viewport constraints. A bare sentence should not be the preferred production input.
- Use a line-level classification with at least: **KEEP/NATURAL**, **NATURALNESS_REWRITE**, **LOCALE_OR_REGISTER_REWRITE**, and **ESCALATE_PRODUCT_SEMANTICS**. The last class must not be automatically rewritten.
- Add a page-level rhythm pass after line realization. Detect accumulated rhetorical symmetry, repeated explicit pronouns, sloganization of state, repeated reassurance, repeated internal nouns, and multiple differently worded copies of one state.
- Realize zh-Hans and zh-Hant-HK independently from the same protected meaning. Do not implement localization as character conversion.
- Prefer state/action/consequence-first copy over product self-definition when the UI role is transactional or status-bearing; however do not create a universal `please` rule or phrase ban-list.
- Build evaluation from abstracted real-project patterns plus independent holdouts. CUHK Date exact strings may be retained as maintenance evidence/replay cases, but project-specific tone must not become a universal house style.
- Add positive/negative/near-miss trigger tests so long-form Chinese reports continue to route to `chinese-prose`, while labels/help/status/CTA/empty/error/landing microcopy route to the dedicated UI capability.
- Do not build AI-detector evasion or a generic humanizer.
boundary: Frontend Design decides whether/where/how much to say and owns rendered hierarchy; the writing layer realizes natural language after UI role and product meaning are frozen.
promotion_gate: do not implement this as an isolated Clear Writing patch while Frontend Design remains an unstable upstream owner. First establish a usable Frontend Design baseline; then run one cross-plugin Planner/Critic task that freezes ownership, routing, handoff schema and shared evaluation before implementation.
