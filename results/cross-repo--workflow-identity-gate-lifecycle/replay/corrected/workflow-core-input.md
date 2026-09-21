# Corrected Public Input: Verified Workflow Gate Selection Cases

Classify these four cases. They intentionally provide facts, not the answer.

## Case W1: Explainably Isolated Local Change

A task changes one local validator helper in one repository. It renames a local variable that shadows an imported module and adds a test that executes the affected script directly. No shared prompt, runtime, router, marketplace metadata, generated plugin payload, paid path, credential path, or cross-plugin behavior changes. The only affected user path is that standalone validator.

Expected risk question: can this use a narrow gate if the direct standalone validator smoke and affected test suite pass?

## Case W2: Shared Normal Entry Change

A task changes the normal task-authoring template used by new users, the reviewed-handoff task-init path, the generic workspace validator, and generated docs that are copied into installed projects. The behavior affects both semantic task creation and legacy validation across multiple entry points.

Expected risk question: is a narrow local script test enough, or does the release need broad/full evidence over the shared normal-entry surfaces?

## Case W3: Unresolved Multi-Gate Failure

A candidate passes source/generated parity and loads under a candidate plugin identity. However the reviewer cannot inspect the substantive runtime output, and one required gate about scope semantics has no direct evidence. A different old commit passed that gate before later source edits.

Expected risk question: can the candidate be called release-ready by stitching old PASS evidence to the current loading receipt?

## Case W4: Maturity Promotion Request

A plugin author asks to promote a capability from unclassified to stable after one successful replay, two deterministic tests, and no real user acceptance history. The task has no fixed paid-review or fresh-holdout count in the frozen plan.

Expected risk question: does maturity promotion require a mechanically fixed number of paid/fresh calls, or evidence appropriate to independent real usage and the frozen acceptance contract?
