# FFT C1 Failure Attribution

Status: `PLUGIN_DEFECT`

Candidate:

```text
C1 = 68a5bfb860ef09eeafb994de18878b86a2b13d0d
```

Replay:

```text
run_id = 20260915T062857Z-1380831
plugin_id = writing-style@ai-skills-candidate
plugin_version = 0.3
actual_consumption.proven = true
```

Artifact:

```text
results/055_clear_writing_release_convergence/known_regressions/fft_c1_failure/artifacts/fft_wikipedia.md
```

Failure:

The generated FFT candidate preserved the DFT relationship literally, but placed
the formula in a fenced `text` block:

```text
X_k = sum_{n=0}^{N-1} x_n e^{-i 2π k n / N},  k = 0, ..., N-1.
```

This violates the frozen G3 requirement for formula/render handling. Formula
identity must be preserved as reader-facing renderable math, not hidden in a
text/code fence. The failure matches the helper's existing
`formula-like fenced text` candidate-representation guard, but the normal-entry
generation path did not carry that obligation strongly enough into the writer.

Attribution:

```text
PLUGIN_DEFECT
```

Recovery:

Repair production guidance so `scientific-rewrite` and `REALIZE_MEANING` require
formula-like source blocks to be converted to renderable Markdown/LaTeX math.
This production-source change invalidates C1 as the active candidate; form a new
candidate C2, regenerate payload, rerun focused tests/parity, and rerun the FFT
known regression from exact C2 before continuing Phase 4.
