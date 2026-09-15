# FFT Known Regression - C3 Replay

Status:

```text
PUBLIC_KNOWN_REGRESSION_PASS_FOR_C3
```

Candidate:

```text
C3 = baf8259a223b3d2ee975461b3c1d00da01af9181
replay_run = 20260915T064318Z-1407675
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
9edfbb246ef746fd0eb9ae889266fe8d332ee7195d6a25f8d6405bd14a3cb6ba  artifacts/fft_wikipedia.md
5ea2f30ba6da2a803d3fbdfbb2a627e5c8661d0fc22fbce2ffb9e50e2fb71d49  render_qa/fft_wikipedia.html
08ba8a5fe4f5339e42c90560cb9b2c018d3b9b79d649b2930348a139dc122901  render_qa/fft_wikipedia.png
638b7553d41b5f3b70c7b469581a2a360f2bc330ae7e6b44530a935cf6ae1bfd  artifacts/run.json
b63e6393314ce93796c54b0c8224396cab1d9ef8fce1c2247756580b2f0f42fe  artifacts/plugin-add.json
```

Mechanical checks:

```text
fence_count = 0
has_text_fence = false
has_display_formula = true
has_latex_log = true
has_plain_math_log_pattern = false
internal_workflow_leakage = false
```

Literal preservation spot checks:

```text
FFT, DFT, O(n^2), O(n \log n), O(N^2), O(N \log N), X_k, N^2-N,
N(N-1), Cooley-Tukey, (N/2) \log_2 N, N \log_2 N, 1805, 1965,
Gilbert Strang, IEEE
```

Render QA:

```text
Pandoc HTML render succeeded with MathML.
Firefox headless screenshot succeeded using task-local HOME/XDG cache.
The screenshot was visually inspected: the DFT equation renders as math, the
complexity expressions render inline as math, and the page has no obvious text
overlap or code-block formula regression.
```

Scope note:

```text
This is only the public FFT known-regression replay for C3. It does not complete
Phase 4/G1-G6 representative replay, because the authorized private 054 source
and prior attempt directories are currently absent.
```
