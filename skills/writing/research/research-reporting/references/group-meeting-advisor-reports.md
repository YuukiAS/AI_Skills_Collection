# Advisor-facing group-meeting research reports

Use this reference when `research-reporting` creates or rewrites a report for a PI, advisor, group meeting, lab meeting, project decision meeting, or similar scientific audience.

## Audience model

Assume the advisor cares about the scientific decision, not the execution diary.

The main body should let a reader who has not followed the repo, Codex thread, Slurm state, or audit system answer:

1. What scientific problem are we trying to solve?
2. Why did we start from this paper / method / idea?
3. What is the strongest simple baseline?
4. What exact experiment was finally run?
5. What happened numerically?
6. What does the evidence support and not support?
7. What single uncertainty should be reduced next?
8. What decision, if any, is being asked of the advisor?

## Do not turn the report into a process log

Internal process is not scientific structure.

Do not give standalone main-body sections to:

- audit status or validator tokens;
- preflight;
- git commit / branch / push status;
- allocation / job state;
- minor correction rounds;
- debug history;
- retries that did not change the scientific contract;
- internal lifecycle labels such as `candidate`, `finalizer`, `closeout`, `route`, or `PASS`.

If an implementation correction changes the validity of the comparison, write the corrected rule directly in the final method. Example:

Bad:

> Why we had to run another correction + stability round

Better:

> In multi-round FedAvg, each client retains its AdamW optimizer state across communication rounds.

Only preserve the history when the historical error itself changes how earlier evidence must be interpreted.

## No invented time-boxed scripts

Do not automatically create:

- `30-second version`;
- `3-minute version`;
- `elevator pitch`;
- `if you only have X minutes`;
- `you can say it like this`;
- a verbatim talk track.

Create these only when the user explicitly asks for a timed script or speaking notes.

A normal group-meeting report should simply explain the science clearly.

## Prefer claim-driven structure over chronology

Do not default to:

`Round 1 -> Round 2 -> correction -> rerun -> final run`.

Prefer:

`scientific question -> relevant method idea -> obstacle -> final experiment -> results -> interpretation -> narrowed next question`.

Chronology is useful only when the sequence itself changes the scientific conclusion.

## Separate professor-facing and author-facing material

When the user wants one file for both the advisor and themselves:

- front/main section: scientific question, method relation, final design, results, interpretation, next decision;
- back/internal section: stop criteria, alternative hypotheses, candidate mechanisms, implementation risks, detailed evidence paths, commits, logs, and reproducibility metadata.

Do not mix the two audiences sentence by sentence.

## Tables and result prose

Tables should carry exact numbers. Prose should explain the few differences that change the decision.

Avoid this pattern:

1. table contains all values;
2. next paragraph repeats every value;
3. result subheadings repeat them again;
4. final summary repeats them a fourth time.

After a table, discuss only:

- the main comparison;
- direction/stability across repeats;
- clinically/scientifically relevant trade-offs;
- evidence boundary.

## Heading discipline

Avoid mechanical headings such as:

- Result 1 / Result 2 / Result 3 / Result 4;
- Step 1 / Step 2 / Step 3;
- Why we ran another round;
- Final audit;
- 30-second version.

Use a heading only when the argument changes level. Prefer descriptive headings such as:

- `Decoder one-shot remains below pooled`
- `Five communication rounds do not improve the trade-off`
- `Parameter count alone does not explain the result`

Do not create a heading for one or two sentences.

## De-template the prose

During final editing, search for repeated rhetorical machinery:

- `not X but Y`;
- `the real/core/most important thing is`;
- `most valuable`;
- `first/second/finally`;
- `this proves / overturns`;
- symmetrical three-part lists added only for rhythm.

Use them sparingly. Replace with the actual observation whenever possible.

## Evidence strength

Do not dramatize limited evidence.

For a single dataset, one fold, short training budget, or a few seeds, prefer:

- `we did not observe...`;
- `the current results do not support...`;
- `the direction was consistent across these seeds...`;
- `this remains a candidate explanation...`.

Avoid `prove`, `overturn`, `establish generally`, `significantly better` unless the statistical and design evidence supports that exact statement.

## Advisor questions

End with advisor questions only when a real scientific choice remains. Examples:

- whether to narrow the paper around a surrogate-objective formulation;
- whether to work in a controlled adapter/decoder subspace first;
- whether a second dataset is now necessary.

Do not manufacture a discussion section for things already answered by the data.

## Final QA

Before delivery, ask:

- Would this report still make sense if all repo paths, job IDs, and audit tokens were hidden?
- Is every main section relevant to a scientific decision?
- Are implementation corrections folded into the final method rather than narrated as project history?
- Is any conclusion repeated more than necessary?
- Did the report invent a speaking-time constraint the user never gave?
- Is the main result visible in a table or figure without reading internal logs?
- Is the next experiment narrow enough to falsify one current explanation?
