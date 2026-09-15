# FFT Known Regression - C2 Superseded

Status:

```text
SUPERSEDED_PLUGIN_DEFECT
```

Candidate:

```text
C2 = 3fb49b8f40ead208e4dad0fb3c94674394e23020
replay_run = 20260915T063255Z-1387678
plugin = writing-style@ai-skills-candidate 0.3
runtime = codex-cli 0.153.4
actual_consumption.proven = true
```

Evidence:

```text
artifacts/fft_wikipedia.md
render_qa/fft_wikipedia.html
render_qa/fft_wikipedia.png
artifacts/run.json
artifacts/plugin-add.json
```

Hashes:

```text
8f46b84c63d7e5941a66c1252b76d55e23581d4fdaee052cf056ebb7bb54a9e5  artifacts/fft_wikipedia.md
95eef3fe42786ad54f3c3d9710b198a2402fcead376cea1cd5e5f4222c514ac5  render_qa/fft_wikipedia.html
86023dfa55e0264f493b4eb81247b2005b59634f0074d0c38463bb5835df0eef  render_qa/fft_wikipedia.png
9d7309b0ab5433e75e43e0dcb86a761439026046da19a780f3dd849ffadb7413  artifacts/run.json
b63e6393314ce93796c54b0c8224396cab1d9ef8fce1c2247756580b2f0f42fe  artifacts/plugin-add.json
```

Observed result:

```text
PASS: no fenced code block or text fence for the DFT formula.
PASS: display math was present for the DFT definition.
FAIL: complexity formulas used plain math text such as $O(n log n)$ instead of
      standard LaTeX operator notation such as $O(n \log n)$.
PASS: no visible internal workflow leakage.
```

Failure attribution:

```text
PLUGIN_DEFECT
```

Rationale:

```text
This is a production guidance gap in math rendering. The defect is generic:
reader-facing mathematical functions/operators should be expressed with standard
LaTeX operators, not adjacent italic variables. C3 repairs the production
guidance without adding a sample-specific rule.
```
