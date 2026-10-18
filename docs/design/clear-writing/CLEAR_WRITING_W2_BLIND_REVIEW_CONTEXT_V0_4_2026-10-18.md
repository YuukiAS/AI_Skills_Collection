# Clear Writing W2 blind-review context contract v0.4

Date: 2026-10-18  
Status: FROZEN_BLIND_REVIEW_ISOLATION_CONTRACT  
Task: `clear-writing--every-response-invocation-policy`

This contract closes the remaining W2 reviewer-context isolation gap. It does
not run W2 or create any ChatGPT Project.

## 1. Required review surface

The initial W2 preference review must run in a context that cannot inherit the
current AI Research Stack Project, its chats, files, connected repository
context or the reveal map.

Preferred ChatGPT Web transport:

- create a new empty Project dedicated only to blind W2 preference review;
- use project-only memory;
- create one new review chat as the first and only task chat before verdict
  freeze;
- add no Project files;
- add no Project knowledge;
- add no Project instructions other than a minimal "evaluate only the supplied
  packet" instruction if the UI requires one;
- do not add or invoke GitHub, Files, Plugin, web-search or other connected
  sources.

Frozen test Project label:

`CW-W2-BLIND-v04`

The label is not evidence by itself; the isolation properties below are.

If the current surface cannot establish a context with these properties, W2
blind review cannot be valid and the W2 result is `INCONCLUSIVE`.

## 2. Project memory requirement

If ChatGPT Project is used, the review Project must use **project-only memory**
or a current platform mode with explicitly equivalent isolation semantics.

A normal/default memory mode that may reference chats outside this empty blind
Project is unacceptable.

Project-only memory is necessary but not sufficient: the Project must also be
new and empty so that no same-Project prior thread can carry reveal information.

## 3. Empty-context precondition

Before the first blind-review model response, the operator must record:

- surface/model/visible effort mode;
- opaque blind-review context id;
- Project label;
- Project memory mode;
- Project file count = 0;
- Project knowledge/source count = 0;
- prior task-chat count = 0;
- no current AI Research Stack Project membership;
- no copied execution-package/reveal-map content;
- hash of the sanitized blind packet;
- hash of the frozen blind-review prompt.

Record this as:

`results/clear-writing--every-response-invocation-policy/web-gate-v0.4/W2/blind/BLIND_REVIEW_CONTEXT_MANIFEST.json`

Do not store account ids, private Project URLs or credentials.

If any required property cannot be observed with adequate confidence, do not
start the blind reviewer.

## 4. Tool and source prohibition

Until P01-P08 verdicts and reasons are fully frozen, the blind Reviewer may
receive only:

- the frozen blind-review instruction;
- the sanitized W2 blind packet.

The blind Reviewer must not:

- enter or read the current AI Research Stack Project;
- open `YuukiAS/AI_Skills_Collection`;
- access GitHub;
- access Files/Project files;
- access Plugin Creator or Plugin Management;
- use connected apps/sources;
- use web search;
- request/retrieve cross-project memory;
- read the execution package;
- read the reveal map;
- receive Treatment/Control names, candidate identity, execution order,
  timestamps, invocation evidence or account/workspace locators.

Any visible tool/connector/source invocation during the initial blind review
invalidates the blind review. Do not retry to obtain a favorable result; record
the review as invalid and return to Planner.

## 5. Blind packet

The packet is generated from the frozen W2 outputs and Task Bank. For each
P01-P08 it contains only:

- exact task id;
- exact prompt;
- opaque label 1 + raw output;
- opaque label 2 + raw output;
- frozen preference/hard-failure rubric.

The opaque labels and Treatment/Control mapping remain frozen in:

`docs/design/clear-writing/CLEAR_WRITING_W2_REVEAL_MAP_V0_3_2026-10-18.json`

The blind Project is not allowed to access that file before verdict freeze.

## 6. Verdict freeze

The blind Reviewer must produce, for every P01-P08:

- verdict;
- concise reason tied to the frozen rubric;
- hard-failure finding if any.

The operator stores the complete judgment artifact before reveal:

`results/clear-writing--every-response-invocation-policy/web-gate-v0.4/W2/blind/BLIND_VERDICTS_FROZEN.md`

The file hash is recorded before reveal.

No task can be rescored after reveal.

## 7. Reveal boundary

Only after:

1. P01-P08 verdicts/reasons are complete;
2. `BLIND_VERDICTS_FROZEN.md` is saved and hashed;
3. the blind review Project/chat receives no further scoring request;

may the execution operator read/use the reveal map to create the causal W2
summary.

The blind Reviewer itself does not need reveal access.

## 8. Reviewer identity separation

The execution-ready Critic that reviews this v0.4 package is permanently
ineligible to be the W2 blind preference Reviewer because it can read the reveal
map.

The blind Reviewer must be a new independent thread inside the isolated blind
review context described above.

A "fresh thread" in the current AI Research Stack Project is explicitly
insufficient.

## 9. Repository reveal-map storage

The reveal map may remain in the GitHub repository because the blind Reviewer
is contractually and contextually unable to access that repository before
verdict freeze.

If the actual execution surface cannot guarantee this repository/context
inaccessibility, W2 blind review is invalid and W2 must not receive PASS.
