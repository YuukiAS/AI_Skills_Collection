# STAT5060 HW1 Instructor Solution Specification V1

- Status: FROZEN_COMPLETE_INSTRUCTOR_SOLUTION; authenticated encrypted content is committed alongside this wrapper because the repository is public.
- Date: 2026-09-28.
- Source authority: frozen student questions/rubric, newly authored fixtures and actual Python design-pilot results.
- Relation: the decrypted document owns every question's worked reasoning, canonical implementation, expected numerical behavior, figures, interpretations, acceptable alternatives, common errors and numerical tolerance. The rubric owns marks. This wrapper does not replace a missing answer key: the complete 27 KB-class plaintext document is present in encrypted form and in the private execution handoff.

## 1. Exact authoritative payload

Repository path: `docs/design/stat5060/STAT5060_HW1_SOLUTION_V1.aesgcm`.

```text
algorithm = AES-256-GCM
compression_before_encryption = gzip
AAD_UTF8 = STAT5060/HW1/SOLUTION/V1/2026-09-28
nonce_hex = 510bf4fc62985c872510aac6
ciphertext_bytes = 11554
ciphertext_SHA256 = dde5b9fd7acbb1acfbca5f3c463579e30790ca0f3c45872874c168bcad5089e6
ciphertext_Git_blob_SHA1 = dcb147c0804ad7c369ad668a9a89b14f4b7973dd
plaintext_filename = STAT5060_HW1_SOLUTION_FULL_V1.md
plaintext_SHA256 = 1a9c870646fe52f17b2daca7de3303a8ac480498a491ac2b8969b57c01ed8fd1
```

The key is **not in Git, this document or the Goal Prompt**. It is in the user-delivered private attachment `STAT5060_PRIVATE_HANDOFF_V1.zip`, SHA-256 `dd4823f973f386be378aba2e5d3db71dcf566e6a7e26fba0bbf3d0dc623b6ac0`. The attachment also includes the plaintext for straightforward use, the four exact case CSVs and private pilot evidence. Verify its checksum and the plaintext checksum before use.

AES-GCM encryption/decryption and exact plaintext round-trip were actually tested in the planning session. The Git blob SHA returned by the connected GitHub create operation matched the locally computed ciphertext Git blob SHA, so the uploaded encrypted bytes were verified. This is content-integrity evidence, not a claim that the future instructor PDF is already rendered.

## 2. Safe extraction and rendering

Before extracting the attachment, establish a durable ignored directory under the long-lived checkout: `private/exports/stat5060--materialize-frozen-v1/`. Confirm `git check-ignore` for the directory. If not already ignored, use a checkout-local exclude entry via `git rev-parse --git-path info/exclude`; do not alter global Git configuration. A separate private local directory outside the worktree is also safe for initial extraction, but final instructor deliverables must not exist only in a temporary review worktree.

Never print the recovery key, include it in a command line/log, stage it, put it in a student ZIP or publish the plaintext solution/expected-output tables. The encryption wrapper and ciphertext may remain public. Student CSVs are separately authorized original synthetic fixtures, not confidential answer content.

To authenticate/decrypt, read the 32-byte key from the private file; read ciphertext bytes from the repository; call AESGCM(key).decrypt(nonce,ciphertext,AAD); gzip-decompress; verify the plaintext SHA above. Use a standard authenticated-encryption library, not a custom cipher. `cryptography` is an instructor packaging utility only, not a HW1 dependency.

Missing private attachment/key is an **input-delivery problem**, not permission to reconstruct the solution from guesses. The user is supplied the complete attachment with the final Goal. Continue public materialization only if that input is unavailable, and report the exact missing input rather than claim the solution build passed.

## 3. Frozen solution contents

The complete decrypted document includes:

- Data/units checks; conditional versus raw overdispersion; Poisson/NB2 likelihood/shape correspondence; same-data coefficient/SE/AIC and zero-frequency references; omitted-offset sensitivity; eight-week predictions and causal limits.
- Online-baseline nominal equations, actual fitted coefficients/SEs, manual softmax probabilities, workshop-reference transformation, probability invariance, curve interpretation and distinct denominators across response types.
- Naive and random-intercept binary models; the subject-integrated likelihood; scalar-RE ML numerical evidence; convergence requirements; 200-panel model checks; four b=0 versus new-participant integrated profiles; conditional odds ratios and non-collapsibility cautions.
- The full fixed simulation design and definitions; all attempted-fit accounting; actual 500-replication Python pilot summaries; why mean consistency can coexist with conventional Poisson undercoverage; why neither exact 95% coverage nor universal NB RMSE superiority is expected.
- Part-by-part acceptable alternatives, frequent wrong answers, follow-through marking notes, cross-language/model-equivalence and numerical/Monte Carlo tolerances.
- Private case-generating mechanisms and links to actual pilot files, explicitly separate from student-release content.

No Bayesian programming or ordinal analysis is added to the answer key as an undeclared assessed task. A final R reference solution and Python-equivalence appendix must be executed by Codex and checked against the planner's numeric behavior; the planning pilot is clearly labeled, not misrepresented as a completed R/lme4/PyMC build.
