# Candidate C6 Partial G1-G6 Evidence

Status:

```text
PARTIAL_PASS_BLOCKED_BEFORE_REPRESENTATIVE_DEEP_RESEARCH_RECEIPT
```

Candidate:

```text
C6 = 79d620a0c60cdd086dd5828c8686bac843291cda
plugin = writing-style@ai-skills-candidate 0.3
runtime = codex-cli 0.153.4
```

Source / generated changes since C3:

```text
C4/C5: clarified that citation identity must not preserve raw wiki/HTML
       citation markup, and that formula/complexity expressions must render as
       Markdown/LaTeX math rather than inline code.
C6: added deterministic scientific-rewrite stage validation for raw citation
    markup and formula-like Big-O rendering issues.
```

Focused tests:

```text
python3 -m unittest tests.test_scientific_rewrite tests.test_codex_marketplace tests.test_reviewed_handoff_prompt_contract -q
Ran 75 tests in 13.166s
OK
```

Known regression replay:

```text
Bloom dirty-source replay:
- run: 20260915T085911Z-1686251
- actual_consumption.proven: true
- output: known_regressions/bloom_c6_replay/artifacts/bloom_filter.md
- stage receipt: raw_citation_markup_count=0, formula_rendering_issue_count=0

FFT formula/render replay:
- run: 20260915T090313Z-1731380
- actual_consumption.proven: true
- output: known_regressions/fft_c6_replay/artifacts/fft_wikipedia.md
- render: known_regressions/fft_c6_replay/render_qa/fft_wikipedia.html
- screenshot: known_regressions/fft_c6_replay/render_qa/fft_wikipedia.png
```

Compatibility replay:

```text
light_chinese_polish:
- run: 20260915T090607Z-1737626
- actual_consumption.proven: true

fidelity_only:
- run: 20260915T090643Z-1738447
- actual_consumption.proven: true

english_scientific_prose:
- run: 20260915T090732Z-1740397
- actual_consumption.proven: true

python_re_docs:
- run: 20260915T090817Z-1743221
- actual_consumption.proven: true
```

Hashes:

```text
95fc6e2687417cb8e012f101eace173aded21896eda6e197f9408b102477ba34  known_regressions/bloom_c6_replay/artifacts/bloom_filter.md
a8de4508a00a1c3df4c2175a3e4021495dd2882ce1a3419bddf814d24079bcf0  known_regressions/bloom_c6_replay/artifacts/run.json
e9812a3e90758a5087b87be9c277f640e837ae133557a23e5ec91eeef3d411b7  known_regressions/bloom_c6_replay/artifacts/stage_receipt.json
e3c5202320df31dbd91a3321bc4c0cc390f46364b7b8568ec0a7e726b9edda89  known_regressions/fft_c6_replay/artifacts/fft_wikipedia.md
0f6adf7d6a5c1ab40445d6f4e481a170b574a84fb8d67bb5ffa146442779a960  known_regressions/fft_c6_replay/artifacts/run.json
6ae0995b79923a18b71a39c8242cff278c8e4a0a28d7839e6803cf120e660285  known_regressions/fft_c6_replay/render_qa/fft_wikipedia.html
473106e3d037c5645c272e186abd2c4cbcb06eb38563094ed6f30b0417c01eb6  known_regressions/fft_c6_replay/render_qa/fft_wikipedia.png
8fa352c3a7bb214a251d1df67757d52db5e2a5812e811bbb0bc1385b3bdb8573  compatibility_replay_c6/light_chinese_polish/artifacts/output.md
daa468926af441a812869fcc264b5a60ac9f0b89e5e38dea2c57b99cbdb8e241  compatibility_replay_c6/fidelity_only/artifacts/output.md
e3b12f3e229bb8c29cdb532daec7b816343add89052d7226c440c17bd7c24648  compatibility_replay_c6/english_scientific_prose/artifacts/output.md
fb73a905cf57a689de94d62403fe58ebc7cc41a8121975846b802682e959a5cc  compatibility_replay_c6/python_re_docs/artifacts/output.md
```

Important limitation:

```text
This is not final G1-G6 PASS. The required representative 054 Deep Research
replay could not be closed because candidate_plugin_replay repeatedly hung
after writing private output but before returning stdout/run receipt. See
DEEP_RESEARCH_REPRESENTATIVE_REPLAY_BLOCKER_C6.md.
```

