# 055 Candidate C2 Identity

Candidate commit:

```text
3fb49b8f40ead208e4dad0fb3c94674394e23020
```

Supersedes:

```text
C1 = 68a5bfb860ef09eeafb994de18878b86a2b13d0d
```

Reason:

```text
C1 failed the FFT known regression by rendering the DFT formula inside a fenced
text block. This is a G3 formula/render product defect. C2 repairs production
guidance so formulas must be rendered as Markdown/LaTeX math, not fenced text or
code.
```

Release identity remains:

```text
repository version = 5.0.5
writing-style version = 0.3
```

Payload hashes:

```text
writing-style generated payload tree hash:
f98f56aaf700a807c737b89f39f740cc5372d8423c7c39735ceb4b76884cfd5b

scientific-rewrite + chinese-prose source tree hash:
2e690f636bfc7f9d8b8e7de922dd8af86d888de5ce4249133bf048a57a7a40ea
```

Validation before this identity record:

```text
python3 scripts/build_codex_marketplace.py --write --validate --check --path-report
result: generated layer matches source config, path budget over_budget=0

python3 -m unittest tests.test_scientific_rewrite tests.test_codex_marketplace tests.test_reviewed_handoff_prompt_contract -q
result: 71 tests OK
```

Status:

```text
C2 is superseded by C3 = baf8259a223b3d2ee975461b3c1d00da01af9181.
C2 fixed fenced formula rendering, but its rendered FFT evidence still used
plain math text such as $O(n log n)$ instead of LaTeX operator notation such as
$O(n \log n)$. This is a generic math-rendering quality defect, not a
sample-specific exception.
Pre-final Critic PASS has not happened yet.
Fresh G7 and final Terra are still forbidden.
```
