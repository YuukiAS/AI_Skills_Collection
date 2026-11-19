---
name: content-selection
description: "GPT 端用于在制作前决定读者需要的内容、顺序与可见层级，并在真实成品出现后复审整件作品；Codex 端只按已批准计划渲染、运行验收器、发布和回读。"
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed: null
last_reviewed: 2026-11-19
profile_tags: null
recommended_scope: project
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
---
# Content Selection

用于文档、幻灯片、网站或软件界面、Blueprint 等面向读者的作品。GPT 在制作前决定该出现什么、按什么顺序出现、放在什么层级；真实成品出现后，GPT 再检查整件作品的焦点、层级、重复、留白和阅读负担。

## 执行边界

**CS-01｜GPT 负责内容判断。** GPT 读取用户目标、目标读者、权威材料、已接受版本和本轮编辑范围，完成本文件中的内容准入、排序、层级和成品复审。需要改变科学结论、产品事实、冻结故事线或授权边界时，将问题交回相应负责人。

**CS-02｜Codex 只做机械执行。** Codex 接收 GPT 已完成的内容计划、文字候选和返修指令，只执行渲染、运行验收器、发布与回读。Codex 不新增内容取舍，不改写表达，也不以验收器结果替代 GPT 的读者判断。

## 制作前内容计划

**CS-03｜绑定读者任务。** 使用 [content-plan.schema.json](schemas/content-plan.schema.json) 的顶层字段记录：

- `target_id`、`target_kind`：实际交付对象；
- `reader`、`reader_task`、`locale`：谁来读、要理解或完成什么、使用什么语言与地区表达；
- `source_refs`、`accepted_base`：当前权威来源与最新接受稿；
- `edit_scope`：本轮允许修改的范围和已经冻结的结构；
- `required_meanings`、`exact_items`、`rejected_content`、`required_relations`：必须保留的含义、精确项、已经拒绝的内容及关键关系。

读者或用途存在实质歧义且会改变删留结果时，先取得明确答案。已有材料足以确定时直接继续。

**CS-04｜逐个处置内容单元。** 在 `content_units` 中为每个语义单元记录来源位置、读者用途、处理结果和目标位置。处理结果从以下五类中选择：

- 直接保留：当前读者需要据此理解、判断或行动；
- 压缩表达：信息必要，展开程度可以降低；
- 改用图表：关系或比较适合由媒介负责人可视化；
- 移到次级位置：信息需要保留，适合附录、展开区或可回查链接；
- 删除：当前任务没有使用价值，或其含义已由其他位置充分承担。

同一含义出现在标题、正文、图注、侧栏或多页时，先合并判断其整体作用。审计记录、制作说明、分支、提交、验收状态和编辑对话只有在读者任务确实需要时才进入正文。

**CS-05｜安排顺序与可见层级。** 先放当前阅读任务的答案，再放理解答案所需的对象、关系、证据和条件。当前有效动作应先于历史记录；必要限制应靠近它限定的结论；次级页面或附录应具有独立回访价值。

**CS-06｜信息充分后停止。** 新增内容只有在增加理解、改变判断或支持行动时才进入作品。允许留白。字数、段落数、禁词、密度和技能调用记录只可用于定位问题，不能决定内容价值。

**CS-07｜冻结前完成交接。** 内容计划在正文或页面冻结前交给 Clear Writing 与产物负责人。Clear Writing 负责获准内容的表达，领域负责人负责事实与专业含义，媒介负责人负责布局、图形和交互实现。

## 真实成品复审

**CS-08｜查看实际消费对象。** 使用 [artifact-review.schema.json](schemas/artifact-review.schema.json) 记录当前候选与观察范围：

- `candidate_identity`：文字、源文件和渲染版本的对应身份；
- `visible_text`、`rendered_views`：全部目标可见文字和实际呈现；
- `observed_surfaces`、`unobserved_surfaces`：已查看与尚未取得的页面、状态或视口；
- `findings`：位置、读者影响、所需修改、必须保留的内容和负责方；
- `mechanical_results`：渲染、文件、版本或通用验收器结果；
- `reader_review`：GPT 对完整成品的内容判断。

完整文档要读全文，幻灯片要看整套目标页，界面要看相关状态和视口。检查焦点、信息层级、跨位置重复、删改后的布局平衡、内部过程泄漏以及解释过多或过少。通用 deck 验收器可以提供页面、布局和机械问题，其结果应与 GPT 的内容复审一起使用。

**CS-09｜把问题送回正确负责人。** 内容删留、顺序和层级问题回到内容计划；措辞问题交给 Clear Writing；科学或产品事实问题交给领域负责人；布局、渲染和交互问题交给产物负责人。每条 finding 都要指出具体位置和读者后果，避免只写抽象评价。

## 执行证据

**CS-10｜被调用时留下逐规则证据。** 使用 [execution-evidence.yaml](references/execution-evidence.yaml)。每条实际应用的规则复制一份模板字段，写明“规则编号 → 成品中的原句或位置”；发生改写时填写改前与改后，没有文字改写时将两项保留为 `null` 并给出位置。

- GPT 端把证据文件作为回答附件交付；
- Codex 端只为机械执行记录渲染、验收器、发布和回读位置，并把证据文件推送到任务约定路径；
- 本技能未被调用时，不创建或附加该证据文件。
