# 插件现行决定

这里只记现行决定。决定变了就直接改这一页，旧说法删掉。

## 共同规则

- 下面七个能力都是独立插件：Research Authoring、Presentations、Artifact Content Design、Clear Writing、Reasoned Decision、Design Assurance、Delivery Assurance。
- GPT 写稿、做取舍、定措辞、判断成品。Codex 只做机械执行：渲染、建站、写代码、跑验收器、发布并回读。内容问题交回 GPT。
- 调用了插件，交付时附上或推送一份执行证据：规则编号对应成品里的原句或位置，改写附前后对照。
- v0.1 是骨架加少量必要回归，之后按版本加。
- 新设计按 `YuukiAS/AI_Instruction_Configuration` 的 `SPEC_DESIGN_WORKFLOW.md`：两路 GPT Pro 独立设计，合并成推荐稿，出对照 PDF，用户裁决。

## 产物插件

### Research Authoring（安装标识 `research-writing`）

- 四个技能，按读者分：`research-notes`（作者本人）、`research-story`（导师与组会）、`student-materials`（一份作业及其答案和评分说明）、`research-paper`（正式论文）。
- `research-citations` 负责检索、引用和核验。旧名 `paper` → `research-paper`，`litcite` → `research-citations`，旧名保留转接。
- GPT 端和 Codex 端分开写，各有各的职责。
- 动笔前调用 Artifact Content Design 做取舍，内容定了调用 Clear Writing 写清，成品出来再调用 Artifact Content Design 复看整件。

### Presentations

- v0.1 带上现行规则、验收器（`validator_v2`）和模板。
- 讲者备注只写给内容重的页，一份 PPT 配一个 Markdown，按页排序。讲解稿和会后自读稿共用一套幻灯片。
- 先走通 Beamer PDF，可编辑 PPTX 等真实需求出现再做。
- 调用方式同 Research Authoring：排页前取舍，渲染后复看，选定内容交 Clear Writing。

## 被调用的插件

### Artifact Content Design

- 独立插件，和 Clear Writing 同层。
- 制作前：按读者要理解、核验或完成的事，决定保留、压缩、可视化、降级或删除。内部审计说明、哈希、内部编号和页码、文件路径、新旧稿对照、自检通过说明、待确认、重复规定一律拦掉，直接删除，不留档。
- 成品后：按读者实际打开的方式看完整件，查缺漏、删后空洞、层级失衡、重复和内部过程外泄。
- 关键取舍写在原提纲或制作说明里。
- 调用方：Research Authoring、Presentations、Frontend Design、科研可视化、文档和图像生成。

### Clear Writing（安装标识 `writing-style`）

- 独立插件。三个技能：`response-clarity`（聊天回复）、`clear-artifact`（文档、报告、幻灯片文字）、`interface-text`（界面文字）。
- 只管已选定内容怎么写清；内容该不该出现归 Artifact Content Design。
- `interface-text` 以后和 Frontend Design 对接：前端定布局和交互，`interface-text` 定措辞。

## 任务型插件

### Reasoned Decision

- 独立插件，负责定义问题、调查现实解空间、核证据、比较方案、给出推荐，以及决定何时停止或改判。
- “被质疑就改口”这类问题归这里。

### Design Assurance 与 Delivery Assurance

- 两个独立插件，Design Assurance 管设计到冻结，Delivery Assurance 管冻结到交付。
- 先用 Clear Writing 把现有文档改成读得懂的版本，再继续 0.2。

## 全局指令（不做插件）

- Warm Response 和 Anti-Conservative 写进 ChatGPT 全局协作指令，由 `YuukiAS/AI_Instruction_Configuration` 管理。
