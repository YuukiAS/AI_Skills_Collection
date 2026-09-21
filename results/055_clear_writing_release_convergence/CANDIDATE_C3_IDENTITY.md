# 055 Candidate C3 Identity

Candidate commit:

```text
baf8259a223b3d2ee975461b3c1d00da01af9181
```

Supersedes:

```text
C1 = 68a5bfb860ef09eeafb994de18878b86a2b13d0d
C2 = 3fb49b8f40ead208e4dad0fb3c94674394e23020
```

Reason:

```text
C1 failed the FFT known regression because the DFT formula was rendered inside
a fenced text block.

C2 fixed the fenced formula representation, but render QA showed plain math
operator text such as $O(n log n)$, which renders `log` as adjacent variables.

C3 keeps the formula-as-math repair and adds a generic production obligation to
use standard LaTeX math operators and spacing, e.g. $O(n \log n)$.
```

Release identity remains:

```text
repository version = 5.0.5
writing-style version = 0.3
```

Generated/source identity:

```text
writing-style generated payload git tree:
c1e780f7794f38aee00abd008ac89b216a15b649

scientific-rewrite source blob:
b640dae7224246de26f5c13b2eb6654795d0f1e0

chinese-prose source blob:
0a4396949d7df4ece8e6549892b7a2ff866b8f37
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
C3 is the current pre-final candidate commit.
All subsequent Phase 4 replay must pin C3, not C1 or C2.
Pre-final Critic PASS has not happened yet.
Fresh G7 and final Terra are still forbidden.
```
