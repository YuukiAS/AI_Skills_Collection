# Presentations：STAT5060 Rich v1 模板一致性与交付验收后续

日期：2026-10-04  
来源：STAT5060 Tutorial 1 rich edition v1 人工批注与 CUHK research Beamer 对照  
适用范围：`presentations` 的 `course-standard` 与 `cuhk-research` 两个 Beamer 路由

## 1. 证据身份

- STAT5060 rich v1 PDF：`STAT5060_Turorial_v1.pdf`
  - 37 页
  - SHA-256：`fe7b3e763667be6bc6eeff2a0794774d2b3fe8d4c30a3048149dab3fb683fb6a`
  - canonical repo：`YuukiAS/STAT5060-TA`
  - branch：`work/stat5060--tutorial-01-v2`
  - reviewed implementation HEAD：`071d1cc57c39ae0afd25aa7429c3807f2c16227a`
- CUHK 对照 PDF：`Meeting_2026_09_03.pdf`
  - 40 页
  - SHA-256：`6208180e57374ac42a090c3b71a7b7fbd6a5a8e092636094c8a268da142a7b73`
- AI Skills main at review：`c009ab7045c7f8358092bfbfc32a3b607bbba0b2`

## 2. 人工批注颜色协议

- 黄色：项目内局部修复。由 STAT5060 bounded revision 关闭，不自动提升为通用插件规则。
- 橙色：通用 Presentation 模板、编排、语言或验收缺口。必须进入本后续及相应维护 Issue。
- 绿色：课程内容与教学时序判断。由课程 Planner 冻结结论，不交给模板或 Codex 自行决定。

本次 PDF 有 23 个黄色、14 个橙色、2 个绿色高亮。橙色问题集中为：header 缩写、Question/terminology/caption style、显著数字、双栏基线、图示语法、页面底部空白、最终逐页验收和自然 slide language。

## 3. 当前事实：course-standard 尚未成为 canonical plugin template

当前 `AI_Skills_Collection/main` 的两个共享模板目录：

- `skills/tools/documents-media/presentations/shared/templates/`
- `plugins/codex/plugins/presentations/shared/templates/`

都只有 `cuhk/`，没有已 materialize 的 `course-standard/` canonical source。现有 Stage 1 文档已规划 course-standard adapter、4:3 默认和 16:9 variant，但当前 main 仍没有可被 runtime 直接读取的 canonical course-standard template。

STAT5060 repo 内的：

`materials/2026-27/shared/beamer/stat5060-tutorial-standard-beamer.tex`

是可工作的课程本地实现，也是 course-standard 的真实候选证据，但它仍与 CUHK core 在字体、headline 文字、语义样式、title/closing primitive 和最终 QA 上分叉。因此当前状态不是“standard template 已完成”，而是：

`LOCAL_COURSE_TEMPLATE_EXISTS = YES`

`CANONICAL_PLUGIN_COURSE_STANDARD = NO`

`CUHK_CORE_PARITY = INCOMPLETE`

## 4. 两个 Beamer 模板应采用 shared core + skin

`course-standard` 与 `cuhk-research` 不应各自复制一套逐渐漂移的字号、页眉、页脚和语义宏。应有一个共享 Beamer core，两个 skin 只覆盖品牌和主题色。

### 4.1 shared core 必须统一

- 页面比例适配后的正文边距、frame title 起点和上下间距；
- 正文字体体系与同角色字号；
- section navigation 的高度、字体、完整 section label 和 miniframe state；
- footline 高度、顶部细线、左右 inset、原生 action-button set、页码基线；
- bullets、表格字号/行距、代码块、caption、source-credit；
- Question、Answer、Terminology、Example、Takeaway、Limitation 等语义角色；
- diagram 的边框、节点文字、箭头、间距和对齐 token；
- title、section divider、ordinary content、closing 等 frame primitive；
- whitespace/composition preflight 和最终逐页验收。

### 4.2 skin 允许不同

- primary/accent colour；
- CUHK logo、title-page background 和品牌资产；
- course code/课程身份字段；
- 必要的品牌级 title/closing decoration。

“相同设置”不要求不同品牌页面逐像素相同；但同角色的字号、间距、header/footer 行为和语义样式不能无理由不同。

## 4A. Canonical font contract

本轮根据 `render-chinese-math-pdf` 的稳定架构，冻结 Presentations 的 Beamer 字体策略。**字体不是 deck 级设计自由，也不允许按机器 fallback。**

两个内置 Beamer adapter 都必须使用：

- Latin text：TeX Gyre Termes；
- Math：TeX Gyre Termes Math；
- `cal/bfcal`：New Computer Modern Math，仅对应字形范围；
- CJK serif：Noto Serif SC；
- CJK sans/CJK mono：Noto Sans SC；
- Latin code：Latin Modern Mono，仅 code/listing context。

禁止作为生成文本字体或 fallback：

- Times New Roman；
- Liberation；
- DejaVu；
- Arial；
- Calibri/Carlito；
- Cambria/Caladea；
- Fandol；
- Windows font mounts；
- `fc-match` / fontconfig guessing。

具体 active policy：

- `skills/tools/documents-media/presentations/shared/font-policy.md`
- `plugins/codex/plugins/presentations/shared/font-policy.md`

字体资源由 `render-chinese-math-pdf` 的 `render_resources/chinese_math_pdf` 解析并以文件路径绑定。不存在“Times New Roman 不可用，所以换 Liberation”的运行时分支。legacy CUHK source 的 Times New Roman 属于历史实现；迁移 shared core 时必须改用上述固定 allowlist。

## 5. Header 合同

1. section label 默认必须使用完整名称；没有用户明确授权不得缩写。
2. `Introduction / GLMs / GLMMs / Simulation / Bayesian / Assessment / Summary` 必须完整显示；不得自动变成 `Intro / Sim / Bayes / Assess / Sum`。
3. 长 label 通过共享字体、间距和导航宽度解决，不能优先牺牲语义。
4. short title 仅可作为显式、逐 deck 决策，并必须出现在 deck plan 中；不存在“为了先编译通过自动缩写”。
5. miniframe dots 必须是原生可点击链接；current/completed/future state 可辨。
6. 最终检查必须读取 PDF GoTo links 并验证目的页覆盖，而不是只看圆点外观。

CUHK 40 页对照已经证明 7 个完整 section 名可以在 16:9 headline 中成立，因此 STAT5060 的缩写不是屏幕空间的必然结果，而是模板/实现选择。

## 6. Footer 合同

- 两个模板采用同一结构：左侧 source/course credit，右侧原生 slide navigation + section navigation，随后 `x/N`。
- action buttons 只保留已批准的两组；不新增 home/search/document/back-find-forward。
- 同一 shared core 控制 rule thickness、box height/depth、左右边距、按钮与页码的相对基线。
- skin 只改变颜色和左侧身份文字。
- 允许不同字体字形造成 1–2 px optical difference；验收应比较文字 baseline 和 icon optical centre，不要求不同 glyph 的 ink-bbox centre 完全相等。

## 7. 语义样式合同

### 7.1 Question

Question 是交互/判断角色，不是一般术语或重要句子的黄色高亮。

共享样式：
- 左侧细 accent rule；
- `Question` 小标签使用 accent semibold；
- 问题正文左对齐，可用 italic/medium italic；
- 不使用大色块、圆角卡片或与术语相同的处理；
- 同一 deck 的所有 question page 与普通页面内 question 都调用同一 macro。

### 7.2 Answer / Reveal

- `Answer` 标签与 Question 同一家族但不使用同一强调强度；
- 答案正文保持普通 upright body；
- Blackboard 静态 PDF 可在同页保留 question + answer，但样式层次必须清楚。

### 7.3 Terminology

- inline term：accent semibold，定义保持 neutral body；
- standalone term/subheading：accent semibold label，不用 question 的 vertical rule/italic body；
- 首次出现可带括号全称，但禁止把普通句子整段染成 accent；
- `NUTS: No-U-Turn Sampler`、`Hamiltonian Monte Carlo (HMC)` 属于 terminology，不属于 question。

### 7.4 Caption 与 source

- caption 对齐到 figure width，不对齐整页任意列；
- 单图、单行短 caption：在 figure width 内居中；
- 多行解释型 caption：在 figure width 内左对齐；
- source/data/photo credit 进入 footer source zone，不伪装成 caption；
- caption presence QA 升级为角色检查：`REQUIRED / OPTIONAL / REMOVE`，不是所有图片机械加同样 caption。

### 7.5 Significant digits

最终 deck 需要按统计角色建立精度表：同一表/同一参数族中的 estimate 与 SE 使用一致小数位；概率/比率、AIC、诊断值分别按各自规则。不得让一次返修在相邻页面随意改变精度。具体统计精度由项目冻结，插件负责全 deck 一致性检查。

## 8. Diagram grammar：一套系统，多种 primitive

不要求所有 diagram 只有一种构图，但要求共享视觉语法。允许：

- process flow；
- branching/shared-parent diagram；
- layer/route matrix；
- comparison table。

它们必须共享：边框粗细、节点 padding、同角色字号、箭头样式、peer alignment、label clearance 和颜色语义。不能让 CUHK 用克制 scientific diagram，而 course-standard 临时用一组不相容的大框/黄标。

Final QA 还要问：这个 diagram 是否比一句话或一个表更快传达关系。语义正确但抽象、拥挤或浪费空间的图仍需返修。

## 9. Whitespace/composition 双阶段门禁

本次最明显的系统性失败是：页面没有 overflow，却有大量正文停在上半页或对象过小，executor/reviewer 仍然交付。

### 9.1 制作阶段 preflight

每个 content slide 在实现前记录：

- page job；
- primary object；
- planned body regions；
- expected bottom edge；
- 是否存在有意留白及理由。

普通 content slide 的最后一个 meaningful object 通常应到达 usable body 的约 78% 高度。以下任一情况触发 revise：

- bottom gap > 25% usable body，且不是 title/section-divider/closing；
- bottom gap > 18%，同时 primary object 高度 < 50% 或宽度 < 65%；
- 内容集中在顶部、下半页空白，但对象本可放大或重新编排；
- 双栏一侧拥挤、另一侧或底部大幅空置；
- 为消除空白而新增无信息句子、放大装饰元素或制造无意义卡片。

阈值是 audit trigger，不是 safe harbour。小于阈值仍可能因失衡构图失败。

### 9.2 交付前 whole-deck acceptance

- 全部最终页先以固定 1920×1080 whole-slide/no-zoom 逐页查看；contact sheet 只能辅助。
- 对每页记录 body bbox、bottom gap、primary-object bbox、视觉重心和 intentional-whitespace reason。
- 普通内容页出现大片无意义底部空白时不得 PASS。
- reviewer 必须看最终全 deck，而不是只审改动页或几个 crops。
- 未逐页查看不得返回 global PASS。
- executor 的 build success、无 clipping、无 overfull 不能替代 composition review。

## 10. Natural slide language 的边界

本次继续暴露：`What it assesses`、重复 `What/How ...`、`not X but Y`、名词冒号标签等，即使语法正确仍可能像模板化 AI 文案。

- 一般英文自然度交给 Clear Writing / scientific prose；
- table header、Question/Answer/Terminology 等角色命名由 Presentations 拥有；
- 最终 rendered deck 需要第二次 spoken-slide pass，不能只对 source diff 跑语言检查。

例如诊断表第二列优先使用名词角色 `Interpretation`，而不是机械的 `What it assesses`；这属于 presentation information architecture，不只是句子润色。

## 11. 本次橙色批注的维护映射

- Header 不缩写、CUHK/standard core parity：新增模板一致性 Issue。
- Question / terminology / caption / colour role：补充 Issue #32，并纳入 shared semantic macros。
- page-bottom whitespace、双栏基线、最终逐页验收：补充 Issue #35。
- `What/How`、`not X`、冒号标签和 spoken slide language：补充 Issue #48。
- caption alignment 与语义角色：同时关联 scientific-visualization caption contract，但 Presentation 负责页面内布局和最终呈现。

## 12. 预期实现顺序

1. 先在 STAT5060 rich v2 bounded repair 中验证完整 header、shared semantic styles、whitespace gate 和最终验收。
2. 将验证后的 local course-standard theme 提炼成 canonical `course-standard` adapter，不直接把项目内容带入插件。
3. 抽取 shared Beamer core；CUHK 与 course-standard skin 消费同一 core。
4. 建立 4:3 与 16:9 fixture，以及 question/term/caption/process/layer/whitespace regression fixture。
5. 独立审查两个 template 的 source identity、render 和同角色 token parity。

项目专属内容（STAT5060页码、crab/alligator/Ohio/Bayesian文字）不进入插件；进入插件的是模板核心、语义角色、布局门禁和验收协议。