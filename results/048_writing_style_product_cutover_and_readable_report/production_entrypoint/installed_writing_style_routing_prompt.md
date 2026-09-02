# Installed writing-style routing probe

You are running a public-safe installed-entrypoint evidence probe for AI_Skills_Collection task `048_writing_style_product_cutover_and_readable_report`.

Use the normally installed plugin `writing-style@yuukias-ai-skills` from the current Codex plugin configuration. Do not edit files, do not access private plaintext, and do not print secrets.

Read this identity file first:

`results/048_writing_style_product_cutover_and_readable_report/production_entrypoint/replay_identity.json`

Then classify the following ordinary user requests by the installed `writing-style` skill route they should use. Return only a concise JSON object.

Heavy should-trigger request:

> 请把下面这段中文科研报告改写得更像人写的、更适合连续阅读，但不要改科学含义、数字、公式、引用、路径或结论强度：本研究比较方法 A 与方法 B 在三组模拟条件下的覆盖率。结果显示，当 ICC=0.3 且样本量为 50 时，方法 A 的覆盖率为 0.94，方法 B 为 0.89；因此后续实验只把方法 A 作为默认候选，但保留方法 B 作为敏感性分析。

Light polish request:

> 帮我把这句话润色成自然中文：这个结果说明模型目前还可以，但是需要进一步检查。

Fidelity-only request:

> 只帮我检查这句话里的数字、公式、引用和路径有没有被改动，不要重写：模型使用 `configs/main.yaml`，公式为 \(y=X\beta+\epsilon\)，参考 [1]，样本量 n=128。

Required JSON fields:

- `status`
- `plugin_id`
- `task_key`
- `identity_observed`
- `routes`
- `installed_skill_names_observed`
- `private_plaintext_requested`
- `final_product_pass_claimed`
