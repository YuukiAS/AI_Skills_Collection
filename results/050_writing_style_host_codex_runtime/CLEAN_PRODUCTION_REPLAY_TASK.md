# 050 clean production replay task

Use the installed production `writing-style:scientific-rewrite` skill on the explicit input file supplied to this replay.

This is a production-entrypoint replay, not a freeform rewrite. Load and follow the installed skill instructions exposed to the child runtime. Do not read source-tree `SKILL.md` files from the repository checkout.

Rewrite the input as clear, natural Chinese scientific prose for a technically trained reader.

Requirements:

- Preserve all facts, numbers, formulas, citations, formal method/dataset/package names, comparison conditions, uncertainty, limitations, attribution, and conclusion strength.
- Do not summarize away scientific content.
- You may reorganize reader-facing headings, paragraphs, lists, tables, and explanation order when that makes the same scientific evidence easier to understand.
- Explain technical ideas before relying on compressed notation or terminology.
- Keep English only when it is genuinely needed for exact identity or useful technical recognition; otherwise use natural Chinese reasoning and transitions.
- Important formulas should appear in their scientific context with enough explanation for the reader to understand what they express and why they matter.
- Use lists or tables when parallel conditions or comparisons are substantially easier to understand that way; otherwise prefer normal connected prose.
- Make clear what is established evidence, what is interpretation, what remains uncertain, and what is only a possible next method or experiment.
- Optimize for minimum reader inference burden, not minimum character count.

Write the final rewritten artifact under the replay output directory. Also write the private stage evidence required by the installed skill under:

`<replay-output-dir>/stage_packets/`

At minimum, the output directory must include:

- `rewritten_report.md`
- `stage_receipt.json`
- `stage_packets/document_map.json`
- `stage_packets/meaning_cards/*.json`
- `stage_packets/candidate_units/*.md`
- `stage_packets/semantic_audits/*.json`
- `stage_packets/reader_plan.json`
- `stage_packets/final_assembly.json`
- `stage_packets/assembled_candidate_before_chinese_pass.md`
- `stage_packets/latin_span_inventory.json`
- `stage_packets/chinese_reader_pass.json`
- `stage_packets/post_chinese_self_audit.json`
- `stage_packets/final_candidate.md`

Do not access repository diagnosis files, prior smoke outputs, prior rejection notes, or any other unstaged source. Do not print the private input in the final console response.
