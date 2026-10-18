# Clear Writing Web test candidate materialization contract v0.3

Date: 2026-10-18  
Status: FROZEN_TEST_ONLY_CONTRACT  
Task: `clear-writing--every-response-invocation-policy`

This contract defines the only Clear Writing Web candidate that may be used by
Web Gate v0.3. It does not create, update, install, delete or publish a plugin.

## Source authority

The only source authority is:

`fd7a1578a5042a46a55c5b638f6d550655b1096b`

Repository:

`YuukiAS/AI_Skills_Collection`

The six source Skill trees at that exact commit are:

- `skills/writing/core/writing-fidelity`
  - Git tree: `13e759a03e551e44f2ffe8513f5b1db542fd526a`
- `skills/writing/core/response-clarity`
  - Git tree: `85358b462caff5e2a7629c8349740e971255dd54`
- `skills/writing/core/scientific-prose`
  - Git tree: `e935f3e3ed0961bdca114db61ac1ea66beef142d`
- `skills/writing/core/product-ui-copy`
  - Git tree: `84f001d31be1f9ddd349197199c1858033fd1362`
- `skills/writing/core/scientific-rewrite`
  - Git tree: `77ab9af8add9926cd0c19a86f0c3b6d1f1e5024e`
- `skills/writing/core/chinese-prose`
  - Git tree: `dd03fb660ae3bf499abdae88ad641e901f2d339d`

Required support files include every file consumed by those six generated
skills, including references/assets/evals and
`scientific-rewrite/scripts/rewrite_support.py`.

The generated writing-style plugin root at the same commit is:

`plugins/codex/plugins/writing-style`

Git tree:

`a3b6842c8a870b455ca725e425bc1fbf9b336fc9`

This generated root is the archive-layout authority only after source/generated
parity has been rechecked against the six source Skill trees above. Source
semantics remain owned by `skills/writing/core/**`.

## Deterministic archive contract

After W2 matched-environment preflight PASS and before any Plugin Creator
mutation:

1. materialize the exact commit in an isolated clean worktree or immutable
   checkout;
2. verify the six source Skill trees and generated writing-style tree equal the
   Git identities above;
3. verify source/generated parity for all generated Skill files, including the
   scientific-rewrite support script;
4. copy exactly the contents beneath
   `plugins/codex/plugins/writing-style/` into the plugin archive root;
5. include no parent directory, repository metadata, TODO files outside the
   generated plugin tree, test results, user files or unrelated plugins;
6. create one deterministic ZIP:
   - paths sorted lexicographically;
   - original file bytes unchanged;
   - fixed ZIP timestamp for every entry;
   - no nondeterministic extra metadata;
7. record:
   - SHA-256 for every archive file;
   - archive SHA-256;
   - source commit;
   - generated-root Git tree SHA;
   - file count and total uncompressed bytes.

The archive and per-file manifest must be preserved under task-private evidence
until the Web release is independently re-read.

If any source/generated parity check fails, stop before Plugin Creator.

## Pre-create inventory guard

Before creating anything, use a read-only owned-plugin inventory check.

Expected starting condition for this execution package:

- there is no owned/private plugin identity that is already the intended Clear
  Writing Web test candidate.

If a Clear Writing candidate appears before execution, do not update, delete,
replace or reuse it automatically. Stop and return to Planner so its identity
and provenance can be reviewed.

Do not mutate Research Authoring, Project Instructions Editor, Project Thread
Handoff or any other plugin.

## Single private test-candidate mutation

Only after:

1. execution-ready Critic PASS;
2. user sends the approved v0.3 Kickoff;
3. `W2_MATCHED_ENVIRONMENT_PREFLIGHT=PASS`;
4. watcher preflight is fail-closed and permits manual Web transport;
5. deterministic archive/parity checks PASS;

the execution thread may create **at most one** private Clear Writing test
candidate using Plugin Creator's single-plugin archive creation path.

No create retry is allowed merely because the first created plugin has an
unexpected identity. A transport failure that proves no plugin/release was
created may use the general infrastructure-only retry rule once.

The creation result must record:

- `plugin_id`;
- `release_id`;
- `current_release_id`;
- `latest_release_id` when exposed;
- version;
- scope;
- discoverability;
- returned plugin URL only in private evidence if it contains private account
  context.

Required postcondition:

- discoverability is `PRIVATE`;
- scope/account-workspace boundary matches the preflight;
- one new candidate identity exists;
- no unrelated plugin changed.

Any unexpected `updated` result, non-private discoverability, unexpected
scope, or identity conflict stops W0.

## Post-create release parity verification

Before the first W0 prompt:

1. query the created plugin by its exact returned backend `plugin_id`;
2. verify metadata and `current_release_id`;
3. list current release files with Plugin Creator;
4. read all text files that fit the read interface;
5. obtain the complete current release archive for binary/large/remaining files;
6. recompute the complete release file manifest and archive/file SHA-256 values;
7. compare the actual Web release byte set with the frozen pre-create archive.

If the Web release cannot be proven to derive from the exact frozen archive,
stop W0. Do not test an approximate candidate.

The release evidence must bind the actual `plugin_id` and
`current_release_id` used by W0/W1/W2.

## Failure / retention semantics

The one test candidate is **retained unchanged and private** after any W0 FAIL,
W1 FAIL, W2 FAIL or W2 INCONCLUSIVE.

This execution package does not authorize:

- uninstall;
- delete;
- update;
- publish;
- permission changes;
- creating a replacement candidate;
- cleanup of other plugins.

Retention prevents a second unreviewed account mutation from being invented
after a failed gate. Later cleanup, replacement or release requires a separate
explicit user authorization and, when it changes test/release identity, a new
reviewed plan.

The retained private candidate must not be described as released or production
ready merely because it exists.
