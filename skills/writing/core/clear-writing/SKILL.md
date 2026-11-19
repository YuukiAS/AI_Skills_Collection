---
name: clear-writing
description: "GPT 端通过一个入口处理解释与答复、连续成稿和界面文字，并在改写中保护事实、公式、引用、状态与已确认内容；Codex 端只执行渲染、验收、发布和回读。"
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: true
executes_code: true
secrets_needed: null
last_reviewed: 2026-11-19
profile_tags: null
recommended_scope: project
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
---
# Clear Writing

用于已经完成领域判断的读者表达。GPT 根据实际交付对象选择解释与答复、连续成稿或界面文字场景，并在全部场景中保护来源、事实、公式、引用、产品状态和用户已经确认的内容。

## 执行边界

**CW-01｜GPT 负责写作判断。** GPT 决定解释路径、段落组织、术语说明、措辞、全文衔接和界面文字。正式作品涉及内容删留、顺序或可见层级时，先消费 Content Selection 的内容计划。

**CW-02｜Codex 只做机械执行。** Codex 接收 GPT 已完成的文字和返修指令，只执行渲染、运行验收器、发布与回读。Codex 不生成新文案，不调整内容主次，也不根据布局自行改词。

## 选择场景

**CW-03｜按实际交付对象读取参考。**

- 普通回答、解释、诊断、建议、进度和完成说明：读取 [explanation-and-response.md](references/explanation-and-response.md)；
- 报告、README、Markdown/PDF 正文、技术文档、幻灯片可见文字和长稿重组：读取 [longform.md](references/longform.md)；
- 按钮、标签、状态、帮助、权限、隐私和其他产品界面文字：读取 [ui-copy.md](references/ui-copy.md)；
- 任何会修改既有内容、精确项、状态或已接受版本的任务：同时读取 [fidelity.md](references/fidelity.md)。

一个任务可以读取多份参考。纯代码、命令、JSON、YAML、日志和用户要求逐字返回的原文保持精确，只处理其周围的人读说明。

## 共同行为

**CW-04｜先锁定表达依据。** 确认读者、目的、权威来源、最新接受稿、编辑范围和受保护内容。科学定义、产品状态或引用归属仍有冲突时，交回领域负责人；作品中某段是否应该出现仍未确定时，交给 Content Selection。

**CW-05｜交付可直接阅读的候选。** 开头先给读者需要的判断、实际含义或动作。正文围绕完整推理单元组织，普通概念使用自然中文，确需匹配的名称、代码、路径、字段和状态保持原文。人读解释与机器交付物分层呈现。

**CW-06｜检查完整对象。** 普通回答复读整条回复；连续成稿复读全文及全部目标可见文字；界面文字结合相邻文案和实际状态检查。局部句子通顺不能替代完整对象的可读性。

**CW-07｜按责任返回问题。** 内容存在与位置问题交给 Content Selection，科学或产品事实问题交给领域负责人，布局与渲染问题交给产物负责人。GPT 在获准范围内直接完成普通改写，不把可解决的表达问题留给用户继续编辑。

## 执行证据

**CW-08｜被调用时留下逐规则证据。** 使用 [execution-evidence.yaml](references/execution-evidence.yaml)。每条实际应用的 `CW-*`、`ER-*`、`LF-*`、`UI-*` 或 `FI-*` 规则复制一份模板字段，写明“规则编号 → 成品中的原句或位置”；发生改写时填写改前与改后，没有文字改写时将两项保留为 `null` 并给出位置。

- GPT 端把证据文件作为回答附件交付；
- Codex 端只记录渲染、验收器、发布和回读位置，并把证据文件推送到任务约定路径；
- 本技能未被调用时，不创建或附加该证据文件。
