# 048 writing-style Installed Routing Replay

You are running a public-safe production replay for AI_Skills_Collection task `048_writing_style_product_cutover_and_readable_report`.

Use the installed production plugin named `writing-style`. Do not edit files, do not access private plaintext, and do not print secrets.

Inputs:

- `replay_identity.json`

Task:

1. Read the input identity file.
2. Treat the following as ordinary user requests entering through the installed `writing-style` plugin. For each request, identify the skill route that should handle it and briefly state the visible routing evidence from the installed plugin:

Heavy should-trigger request:

> 请把下面这段中文科研报告改写得更像人写的、更适合连续阅读，但不要改科学含义、数字、公式、引用、路径或结论强度：本研究比较方法 A 与方法 B 在三组模拟条件下的覆盖率。结果显示，当 ICC=0.3 且样本量为 50 时，方法 A 的覆盖率为 0.94，方法 B 为 0.89；因此后续实验只把方法 A 作为默认候选，但保留方法 B 作为敏感性分析。

Light polish request:

> 帮我把这句话润色成自然中文：这个结果说明模型目前还可以，但是需要进一步检查。

Fidelity-only request:

> 只帮我检查这句话里的数字、公式、引用和路径有没有被改动，不要重写：模型使用 `configs/main.yaml`，公式为 \(y=X\beta+\epsilon\)，参考 [1]，样本量 n=128。

3. Return a concise public-safe JSON object with:
   - `status`;
   - `plugin_selector`;
   - `task_key`;
   - `routes`;
   - `installed_skill_paths_or_names_observed`;
   - `private_plaintext_requested`;
   - `findings`.

Expected routing:

- heavy should-trigger -> `scientific-rewrite`;
- light polish -> `chinese-prose` / `zh`;
- fidelity-only -> `writing-fidelity` / `fidelity`.

This replay is routing evidence only. It must not claim final Product PASS or user ACCEPT.
