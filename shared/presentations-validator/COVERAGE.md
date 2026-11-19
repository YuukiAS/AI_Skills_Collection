# 规则与检测函数覆盖

以下是实现覆盖，不是独立验收结论。保留原通用集的 108 个 ID，新增 11 个文字检查 ID。每条 `partial` 即使初筛无命中也保留适用页的人判，不将缺少角色或源码证据改成 PASS。

20 条 `auto` 是当前可以给出确定模式或明确几何证据的检查；70 条 `partial` 含有对象语义、角色、共享源码或渲染边界，机械测量不等于完整判定；29 条 `judged` 需要理解内容或查过程证据。原表里的 measurable 不是本工具承诺无条件自动判定的标记。

每个函数实际检查的范围如下。表后的逐条映射可用来检查登记了规则却没有实现的情况。

| 检测函数 | 实际范围及边界 |
|---|---|
| `check_geometry` | 按显式 V19 配置核对物理尺寸，允许 PDF 小数舍入误差；不推断其他模板应有的尺寸。 |
| `check_cover_title` | 在首页可见文字中按字号层级识别标题；没有可识别标题则失败。 |
| `check_cover_author` | 识别首页可见署名行；不会读取 PDF metadata 补足署名或核验人物身份。 |
| `check_cover_date` | 识别首页可见的数字年月日或常见英文日期；不把 metadata 当作可见日期。 |
| `check_audit_tokens` | 查显式审计状态、receipt、哈希和中文检查过程标记；普通动词 pass 不命中。 |
| `check_file_paths` | 查路径和带文件扩展名的内部文件名；函数调用语法不作为文件名，不扫描输入文件名作判定。 |
| `check_internal_versions` | 查可见的内部修订式标记；版本是否确属必要科学内容仍可由人审解释。 |
| `check_contrast` | 按提取文字块查中英文固定对比句式，覆盖同块内换行及逗号后的否定对比；正则和少量例外在 rules.yaml。 |
| `check_meta` | 查 rules.yaml 配置的元说明和内部执行标签；允许配置具体语境例外。 |
| `check_closing_question` | 从书签/可见附录标题确定主线末页，分别检查主线与全套末页的可见问题块；不接受其他页的问题块代替。 |
| `check_word_budget` | 计算可见正文拉丁词、数字与汉字加权量；工程默认上限可显式配置。 |
| `check_extractability` | 无可提取可见正文即报告未覆盖，纯图片页不能伪造文字通过。 |
| `check_caption_joiners` | 对已识别图注查中点和分号；图注识别另有人判。 |
| `check_caption_runtime` | 对已识别图注查耗时词和时间量模式；必要科学时间量可能需要人工解释。 |
| `check_caption_version` | 对已识别图注查数据版次和来源核算。 |
| `check_caption_sentences` | 对已识别图注计句；小数点和常见 Figure 缩写不算句界。自然解释是否充分另由人判。 |
| `check_question_style` | 对已识别的结尾问题块按 V19 字号与水平居中容差核对。 |
| `check_question_y` | 对已识别的结尾问题块按 V19 正文轨道核对中心纵坐标。 |
| `screen_cover` | 将首页全部非导航/页脚文字与标题、署名、日期候选作集合比较，多余文字或对象自动报错。 |
| `screen_closing` | 检查要点和问题块的相对位置，查联系方式和资源线索；姓名和语义仍须人审。 |
| `screen_prose` | 为 judged 的标签短语、空话与免责句列出原文，所有候选只写 REVIEW；语义不自动判定。 |
| `screen_abbreviations` | 按阅读顺序记录全大写、含 & 和混合大小写缩写候选；TEXT-UNDEFINED-ABBREVIATIONS 对缺少首次展开者自动报错；COMP-TERMS 保留完整术语与符号的人判。 |
| `screen_captions` | 关联图表与图注；无图注且无外部正文解释者自动报错；有说明候选时继续复核；逐条输出图注原文供内容人判。 |
| `screen_typography` | 按候选角色测字号、字重、居中、行距、家族和全套一致性；颜色、源字体绑定与角色不确定性不自动放行。 |
| `screen_tex` | 只扫描显式提供的单份 TeX，查负间距、nointerlineskip、压缩表格和局部列表/卡片覆盖；不执行或展开宏。 |
| `screen_overflow` | 测文字、图像、矢量框的物理越界；裁剪后的可见性仍需最终渲染确认。 |
| `screen_footer` | 检查来源语法、分隔线、页码、控件、墨迹中心及安全间距；来源必要性和原生行为仍需人判。 |
| `screen_spacing` | 先合并同块续行，形成语义对象候选，再测列表、文字、表格、图、公式、分区与标题之间的框间距；完整墨迹边界及配对需复核。 |
| `screen_layout` | V19 已声明正文轨道的留白违规自动报错；其他配置仍复核。另测留白、轨道、列表锚点、双栏、导航、结尾分区和图内可读性候选；图示规则另测线段、文字碰撞、同组长度、线宽和内边距。 |

不同规则可以复用同一函数；函数按规则 ID 选择对应测量。共有 28 个登记函数，另有 1 个被布局初筛调用的图示辅助函数。

| 规则 | 方式 | 配置 | 函数 |
|---|---|---|---|
| LAY-GEOMETRY | auto | v19 | check_geometry |
| LAY-RAILS | partial | v19 | screen_layout |
| ROLE-COVER-CONTENT | auto | all | screen_cover |
| TYPE-COVER-TITLE | partial | v19 | screen_typography |
| TYPE-COVER-BYLINE | partial | v19 | screen_typography |
| LAY-COVER-SPACING | partial | v19 | screen_layout |
| TYPE-FRAME-TITLE | partial | v19 | screen_typography |
| TYPE-BODY | partial | v19 | screen_typography |
| TYPE-SUBHEAD | partial | v19 | screen_typography |
| TYPE-TABLE | partial | v19 | screen_typography |
| TYPE-CODE | partial | v19 | screen_typography |
| TYPE-CAPTION | partial | v19 | screen_typography |
| TYPE-FOOTER | partial | v19 | screen_typography |
| TYPE-FONT-FAMILIES | partial | v19 | screen_typography |
| TYPE-DECK-CONSISTENCY | partial | all | screen_typography |
| TYPE-NORMAL-LEADING | partial | v19 | screen_typography |
| TYPE-LIST-PARAMETERS | partial | v19 | screen_tex |
| TYPE-LIST-STYLE | partial | all | screen_typography |
| LAY-SPACE-LIST-ITEM-GAP | partial | v19 | screen_spacing |
| LAY-SPACE-PARAGRAPH-TO-LIST | partial | v19 | screen_spacing |
| LAY-SPACE-PARAGRAPH-TO-TABLE | partial | v19 | screen_spacing |
| LAY-SPACE-PARAGRAPH-TO-FIGURE | partial | v19 | screen_spacing |
| LAY-SPACE-PARAGRAPH-TO-DISPLAY-MATH | partial | v19 | screen_spacing |
| LAY-SPACE-DISPLAY-MATH-TO-TABLE | partial | v19 | screen_spacing |
| LAY-SPACE-DISPLAY-MATH-TO-BODY | partial | v19 | screen_spacing |
| LAY-SPACE-TABLE-TO-INTERPRETATION | partial | v19 | screen_spacing |
| LAY-SPACE-CAPTION-TO-BODY | partial | v19 | screen_spacing |
| LAY-SPACE-QUESTION-TO-NEXT | partial | v19 | screen_spacing |
| LAY-SPACE-WITHIN-GROUP | partial | v19 | screen_spacing |
| LAY-SPACE-BETWEEN-GROUP | partial | v19 | screen_spacing |
| LAY-SPACE-MAJOR-SECTION | partial | v19 | screen_spacing |
| LAY-SPACE-TITLE-TO-QUESTION | partial | v19 | screen_spacing |
| LAY-SPACING-ROLES | partial | v19 | screen_layout |
| LAY-CONTINUATION-ANCHOR | partial | all | screen_layout |
| LAY-TABLE-ATOMS | partial | all | screen_layout |
| LAY-COLUMN-REASON | partial | all | screen_layout |
| LAY-COLUMN-PRESETS | partial | v19 | screen_layout |
| LAY-COLUMN-ANCHORS | partial | v19 | screen_layout |
| LAY-COLUMN-BOTTOMS | partial | all | screen_layout |
| ROLE-FULL-WIDTH-TRANSITION | partial | v19 | screen_layout |
| PROC-DENSITY-REPAIR | judged | all | —（只列人判） |
| TYPE-NO-COMPRESSION | partial | v19 | screen_tex |
| LAY-BODY-WHITESPACE | partial | all | screen_layout |
| CAP-NATURAL-SENTENCE | partial | all | screen_captions |
| CAP-BELOW-OBJECT | partial | all | screen_captions |
| CAP-LINE-AWARE-ALIGNMENT | partial | all | screen_captions |
| CAP-MULTILINE-ANCHOR | partial | all | screen_captions |
| LAY-DIAGRAM-SHAFT | partial | v19 | screen_layout |
| LAY-DIAGRAM-BOUNDARIES | partial | v19 | screen_layout |
| LAY-DIAGRAM-PEER-EDGES | partial | v19 | screen_layout |
| LAY-DIAGRAM-SHARED-STYLES | partial | v19 | screen_layout |
| LAY-DIAGRAM-PADDING | partial | v19 | screen_layout |
| COMP-DIAGRAM-SEMANTICS | judged | all | —（只列人判） |
| FOOT-NECESSARY-SOURCES | partial | all | screen_footer |
| FOOT-NATIVE-COMPONENTS | partial | v19 | screen_footer |
| FOOT-OPTICAL-CENTERS | partial | v19 | screen_footer |
| FOOT-SOURCE-REFINEMENT | partial | v19 | screen_footer |
| ROLE-CLOSING-CONTENT | partial | all | screen_closing |
| LAY-CLOSING-ZONES | partial | v19 | screen_layout |
| TYPE-CLOSING-QUESTION | auto | v19 | check_question_style |
| LAY-CLOSING-QUESTION-Y | auto | v19 | check_question_y |
| ROLE-CLOSING-NO-EXTRAS | partial | v19 | screen_closing |
| TYPE-NAVIGATION | partial | v19 | screen_typography |
| LAY-NAVIGATION-BUDGET | partial | v19 | screen_layout |
| LAY-NAVIGATION-GAPS | partial | v19 | screen_layout |
| ROLE-EXACTLY-ONE | partial | all | screen_layout |
| ROLE-QUESTION-PRIMITIVE | partial | v19 | screen_tex |
| CAP-REQUIRED | partial | all | screen_captions |
| CAP-NO-LABEL-CHAINS | auto | all | check_caption_joiners |
| CAP-NO-UNDEFINED-TERMS | partial | all | screen_abbreviations |
| CAP-NO-BARE-RESULTS | partial | all | screen_captions |
| CAP-NO-RUNTIME | auto | all | check_caption_runtime |
| CAP-NO-DATA-VERSION | auto | all | check_caption_version |
| PROC-CAPTION-RELOCATION | judged | all | —（只列人判） |
| TEXT-NO-CONTRAST | auto | all | check_contrast |
| TEXT-NO-LABEL-PHRASES | judged | all | —（只列候选原文并交人判） |
| TEXT-NO-META | auto | all | check_meta |
| TEXT-NO-ENDING-DISCLAIMER | judged | all | —（只列候选原文并交人判） |
| PROC-REPAIR-TARGET-PAGES | judged | all | —（只列人判） |
| PROC-REPAIR-PROTECTED-TEXT | judged | all | —（只列人判） |
| PROC-REPAIR-DIFF | judged | all | —（只列人判） |
| COMP-DATA-COMPARISON | judged | all | —（只列人判） |
| COMP-TERMS | partial | all | screen_abbreviations |
| COMP-NUMBERS | judged | all | —（只列人判） |
| COMP-REASONING | judged | all | —（只列人判） |
| COMP-RETELL | judged | all | —（只列人判） |
| COMP-DECK-STORY | judged | all | —（只列人判） |
| PROC-COLD-READ-BLIND | judged | all | —（只列人判） |
| PROC-COLD-READ-CHECKLIST | judged | all | —（只列人判） |
| PROC-COLD-READ-REWRITES | judged | all | —（只列人判） |
| PROC-COLD-READ-SCOPE | judged | all | —（只列人判） |
| COMP-TALK-DURATION-REVIEW | judged | cold_read_v2_15min | —（只列人判） |
| PROC-VISIBLE-OVERFLOW | partial | all | screen_overflow |
| PROC-IDENTITY-INDEPENDENCE | judged | all | —（只列人判） |
| PROC-DEFERRED-NOT-PASS | judged | all | —（只列人判） |
| PROC-REFERENCE-NOT-INDEPENDENT | judged | all | —（只列人判） |
| PROC-REAL-COVERAGE | judged | all | —（只列人判） |
| COMP-FIRST-USE-ORDER | partial | all | screen_abbreviations |
| FOOT-SAFE-ZONE | partial | all | screen_footer |
| COMP-INFORMATION-COMPOSITION | judged | all | —（只列人判） |
| LAY-FIGURE-INTERNAL-READABILITY | partial | all | screen_layout |
| PROC-ENGLISH-FINAL-PASS | judged | all | —（只列人判） |
| LAY-SPARSE-RECOMPOSITION | partial | all | screen_layout |
| PROC-ACCEPTED-COMPONENT-REGRESSION | judged | all | —（只列人判） |
| PROC-NO-FIXED-STORYLINE | judged | all | —（只列人判） |
| PROC-HOLDOUT-HONESTY | judged | all | —（只列人判） |
| PROC-EXISTING-DECK-BASELINE | judged | all | —（只列人判） |
| COMP-THEORY-GUARANTEES | judged | all | —（只列人判） |
| TEXT-COVER-TITLE | auto | all | check_cover_title |
| TEXT-COVER-AUTHOR | auto | all | check_cover_author |
| TEXT-COVER-DATE | auto | all | check_cover_date |
| TEXT-NO-AUDIT-TOKENS | auto | all | check_audit_tokens |
| TEXT-NO-FILE-PATHS | auto | all | check_file_paths |
| TEXT-NO-INTERNAL-VERSIONS | auto | all | check_internal_versions |
| TEXT-WORD-BUDGET | auto | all | check_word_budget |
| TEXT-EXTRACTION-COVERAGE | auto | all | check_extractability |
| CAP-SINGLE-SENTENCE | auto | all | check_caption_sentences |

| TEXT-UNDEFINED-ABBREVIATIONS | auto | all | screen_abbreviations |
| TEXT-CLOSING-QUESTION | auto | all | check_closing_question |

所有配置项的原始数值均见 `rules.yaml`；未冻结的阈值保持为空，不增加来源未给出的硬下限。图注、字体等候选识别参数只决定初筛范围，不替代角色验收。


已知边界（`REVIEW`）：缩写检查遇到 `ABC: alpha beta comparison is our measure.` 这类冒号展开后继续接解释的句子时，当前首字母匹配可能误报缺定义并输出 `FAIL`，需人工复核。对应合成正例保留失败，不能据此宣称缩写检查全部通过；本轮达到单条规则 3 次修改上限后停止处理。纯展开形式 `ABC: alpha beta comparison.` 不受这一尾随文字问题影响。
