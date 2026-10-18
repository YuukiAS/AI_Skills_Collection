# Protected-partition chat confirmation candidate result

## Status

```text
TASK = hpc--slurm-cancel-production-closure
RESULT = READY_FOR_INDEPENDENT_REVIEW
PHASE = 3
PRODUCTION_ACTIVATED = NO
REAL_SLURM_COMMAND = NO
REAL_SLURM_MUTATION = NO
```

This package implements the approved Proposal v2.1 in three standalone
candidate clones and freezes the canonical production identities offline. It
does not install, trust, or activate production Hooks. The user superseded the
candidate-clone live trust/Hook probe as a prerequisite; live native chat and
the single synthetic held-job acceptance remain production-stage work after an
independent Reviewer PASS and a separate exact production authorization.

## Frozen authority

```text
APPROVED_EXECUTION_PACKAGE = c3879065c782f1b0a03107a927bb3176a8788d02
APPROVED_PROPOSAL_BLOB = 26760ae8bb0a19809f1048436fa14aba0bb4e49a

AI_SKILLS_SOURCE = c3879065c782f1b0a03107a927bb3176a8788d02
DII_SOURCE = 747829b957b19e8fcffa6bd5f1bb7ae62ae11f6f
CARE_SOURCE = 75a40e454de43b64e59a0b0b438ff57ef2bb8345

AI_SKILLS_PRODUCT_CANDIDATE = 7bbe71d8849930131d5889dd7bb790dfc46fe22a
DII_PRODUCT_CANDIDATE = ee1e3f05906c00aa5a68cf6fc551414c3317eb4c
CARE_PRODUCT_CANDIDATE = 2f8145b5a5093557cc7c066bf4765c9d3930838f
```

All three candidates use branch
`work/hpc--slurm-protected-partition-chat-confirmation-v2-1`. Each checkout has
its own `.git` directory, resolves its own clone as `--show-toplevel`, and has
the frozen source commit as an ancestor. No post-source `main` content was
merged, rebased, or cherry-picked.

## Implemented contract

AI Skills provides the thin protected-partition cancellation guard, reviewed
binder and session sources, deterministic setup/render tooling, private
capability/runtime/consumed contract, SessionStart/SessionEnd/PostToolUse Hook
declarations, explicit `.codex` deny policy, and automation-only `scancel`
shim. Protected targets return an exact native `request_user_input` request
with zero first-pass mutation. The binder re-resolves the exact target, checks
project/session/turn/tool/capability/runtime/digests/partition/operation,
atomically reserves one consume record, and invokes the frozen absolute
`scancel` exactly once.

DII installs the exact central candidate and adds only project integration,
PATH resolution, and blocker propagation. It does not copy protected policy.
CARE adds the normal-entry adapter and propagates nonzero chat blockers through
B1, M7, M8, interactive takeover, and cascade cancellation without marking a
loser cancelled, waiting for accounting, launching work, or issuing a second
`scancel`.

## Gate A-D candidate evidence

### Gate A: partition routing

`PASS_OFFLINE`

- Non-protected exact jobs retain the ordinary route.
- Any protected member protects the entire explicit invocation.
- The first protected block returns zero mutation and exact native question
  metadata.
- Blanket initial authorization is not treated as confirmation.

### Gate B: native confirmation and authority boundary

`PASS_OFFLINE_LIVE_ACCEPTANCE_DEFERRED_BY_USER`

- Deterministic tests cover explicit confirmation, empty/retain/Other,
  subagent rejection, fabricated/mismatched request data, target/partition/op
  change, exact re-resolution, digest mismatch, one-time atomic consumption,
  duplicate/replay denial, absolute executable binding, and PATH spoofing.
- Generated config fixes `bypass_hook_trust=false`, enables native
  `request_user_input`, locks `.codex`, and denies raw/private executables.
- Candidate clone project trust, Hook live loading, and native Desktop chat are
  deliberately not claimed. The user moved these checks to final canonical
  production acceptance.

### Gate C: consumer/runtime and should-not-change

`PASS_OFFLINE_LIVE_LOADING_DEFERRED_BY_USER`

- AI Skills, DII, and CARE config/Hook/rules documents compile and render.
- DII and CARE `command -v` / `shutil.which` checks resolve the reviewed local
  automation shim; raw and absolute system `scancel` remain denied to Codex.
- CARE blocker propagation tests pass; DII contains no copied policy logic.
- Headless protected cancellation fails closed.
- Representative AI Skills, DII, and CARE regressions pass as listed below.
- Candidate project live Hook loading is not claimed.

### Gate D: target integrity and claim truth

`PASS_OFFLINE`

- Only exact numeric job or array-element targets are accepted; complex
  selectors fail closed.
- The binder re-resolves immediately before mutation and rejects changed
  identity, partition, owner, operation, capability, runtime, or digest.
- Tests mock subprocess boundaries. No destructive fake subprocess path was
  executed, so the strict fake-Slurm isolation requirement was not invoked:
  `ISOLATION_STATUS=NOT_REQUIRED_FOR_EXECUTED_TESTS`.
- No same-UID OS-level unbypassable claim is made.

## Production-rendered identities

The exact candidate generator rendered all three canonical roots under
`production-render/` without writing a canonical checkout, creating a
capability, or activating/trusting a Hook. Every listed file SHA and Hook
`current_hash` was independently recomputed from the rendered bytes.

Common contract:

```text
BINDER_SHA256 = 5808f8620fd5aff981e32c15a140833e3cdeaca615d39e02f074b55172ad73fd
SESSION_HOOK_SHA256 = dc48faf031313757e5f628abc91ca9b2d6668551e9c4af77aaabeb681b0ff73d
SCONTROL = /usr/bin/scontrol
SCANCEL = /usr/bin/scancel
PROTECTED_PARTITIONS = htzhulab
```

AI Skills:

```text
ROOT = /overflow/htzhu/mingcheng_new/AI_Skills_Collection
BINDER = /overflow/htzhu/mingcheng_new/AI_Skills_Collection/.codex/slurm-protected-cancel-private/bin/slurm-protected-cancel-binder
POST_TOOL_USE_KEY = /overflow/htzhu/mingcheng_new/AI_Skills_Collection/.codex/hooks.json:post_tool_use:0:0
POST_TOOL_USE_HASH = sha256:6ce3e138d43141fb6f66b389932d30237d562d16067443a4857c93a0a753e223
SESSION_END_KEY = /overflow/htzhu/mingcheng_new/AI_Skills_Collection/.codex/hooks.json:session_end:0:0
SESSION_END_HASH = sha256:1843575556c6fdaac85bfb3632af34b0b83f5a4c34694cc2929b9d8a0f9655c7
SESSION_START_KEY = /overflow/htzhu/mingcheng_new/AI_Skills_Collection/.codex/hooks.json:session_start:0:0
SESSION_START_HASH = sha256:f8393cee2aeb16ef9349beeb869aedf1a5fa7784f6e2253a29744b080fa72042
```

DII:

```text
ROOT = /users/a/e/aereinh/Distributed_Imaging_Inference
BINDER = /users/a/e/aereinh/Distributed_Imaging_Inference/.codex/slurm-protected-cancel-private/bin/slurm-protected-cancel-binder
POST_TOOL_USE_KEY = /users/a/e/aereinh/Distributed_Imaging_Inference/.codex/hooks.json:post_tool_use:0:0
POST_TOOL_USE_HASH = sha256:32077858013d08dffc5bf05e615821815f99d0eda2d5a15e8277b644dd1cf8df
SESSION_END_KEY = /users/a/e/aereinh/Distributed_Imaging_Inference/.codex/hooks.json:session_end:0:0
SESSION_END_HASH = sha256:0ff974e5ee8b544385fd802be9f7cb6dada7db30a63a479363035fb48ee379dc
SESSION_START_KEY = /users/a/e/aereinh/Distributed_Imaging_Inference/.codex/hooks.json:session_start:0:0
SESSION_START_HASH = sha256:59fe59db5999f04121c16fc0dd07e500549516eea736a4a2b7b83d213188b454
```

CARE:

```text
ROOT = /users/a/e/aereinh/CARE
BINDER = /users/a/e/aereinh/CARE/.codex/slurm-protected-cancel-private/bin/slurm-protected-cancel-binder
POST_TOOL_USE_KEY = /users/a/e/aereinh/CARE/.codex/hooks.json:post_tool_use:0:0
POST_TOOL_USE_HASH = sha256:2c7f3373dcc6814b3329c80bb11e938de645241b5ebe5301c9d2e5fa38c1c19a
SESSION_END_KEY = /users/a/e/aereinh/CARE/.codex/hooks.json:session_end:0:0
SESSION_END_HASH = sha256:df3ac41fe47f91883c7f3b969ab1563211fe004383c3844d895cd8de1e541d29
SESSION_START_KEY = /users/a/e/aereinh/CARE/.codex/hooks.json:session_start:0:0
SESSION_START_HASH = sha256:d2be18ac672eb6c4f694c2f359c96b192763f580bee66dc585d7505494bf6ab4
```

The manifests are the complete authority for file hashes, runtime paths,
project config/rules, and declarations:

- `production-render/ai-skills/protected-cancel-render-manifest.json`
- `production-render/dii/protected-cancel-render-manifest.json`
- `production-render/care/protected-cancel-render-manifest.json`

## Validation

Final validation commands and results:

```text
python -m unittest tests.test_slurm_protected_cancel
  PASS: 12 tests

python -m unittest discover -s tests
  PASS: 356 tests

python scripts/skills.py validate
  PASS

python scripts/skills.py audit --all
  PASS

python scripts/build_codex_marketplace.py --write --validate --check --path-report
  PASS

CARE: python -m unittest tests.ops.test_slurm_cancel_chat_blocker
  PASS: 7 tests

DII: python -m unittest tests.test_supervisor_bridge_layer_a_2026_09_18
  PASS: 12 tests
```

The full DII discovery baseline ran 16 tests but could not import four
torch-dependent modules because the frozen source environment has no `torch`.
No dependency was installed and no broader scientific test claim is made. The
task-owned non-torch integration regression passed.

The production render integrity check recomputed every manifest file SHA,
binder/session digest, and Hook `current_hash`, and rejected candidate-clone
path leakage: `PRODUCTION_RENDER_INTEGRITY=PASS`.

## Version and release

```text
Repository bump decision: NONE
Reason: candidate-only implementation; production activation and formal release are not authorized.
Repository version: 5.4.5 (unchanged)
slurm-workflows: 0.4, NO_BUMP
central Marketplace Plugins: NO_BUMP
Bridge Kit: NO_CHANGE
```

## Side effects, rollback, and next action

```text
EXISTING_CANONICAL_DIRTY = IGNORED_OUT_OF_SCOPE
CANONICAL_CHECKOUT_WRITE = NO
CANDIDATE_PROJECT_TRUST = NO
CANDIDATE_HOOK_TRUST = NO
USER_CODEX_CONFIG_WRITE = NO
PRODUCTION_CAPABILITY_CREATED = NO
PRODUCTION_HOOK_ACTIVATED = NO
```

Rollback before production consists only of abandoning the three task branches
or standalone candidate clones. No production rollback is presently needed.
After Reviewer PASS, production still requires a separate user authorization
binding the three reviewed commits and the exact production identities above.
Only then may canonical setup, official Hook trust, and the one authorized
synthetic held `htzhulab` job acceptance occur. No existing job may be touched,
and no second test job is authorized.

`NEXT_ACTION=INDEPENDENT_REVIEWER`
