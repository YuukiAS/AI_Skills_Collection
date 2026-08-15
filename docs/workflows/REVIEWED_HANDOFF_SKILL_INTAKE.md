# Reviewed Handoff Skill Intake Adapter

This adapter is specific to `YuukiAS/AI_Skills_Collection`. It extends the
project copy of Reviewed Handoff with repository intake rules. It does not
change the generic Reviewed Handoff product contract from
`GPT_Codex_AI_Bridge_Kit v0.5.0`.

Planner, Executor, and Reviewer must read this file before any Reviewed Handoff
task that handles AI Resources, Notion skill candidates, external skill repos,
profile exposure, marketplace exposure, provenance intake, or active skill
routing.

## Scope

This workflow only establishes the AI Skills Collection adapter. It must not
bulk-process `Type=Research` Notion candidates.

Do not install or copy Agent-Flow. Do not add extra generic control-plane
machinery to this repository to process skill intake. Keep source edits in the
repository authority layer first:

- `skills/`
- `profiles/`
- `docs/provenance/`
- `tests/`
- `scripts/codex_marketplace_config.json`

Only regenerate `.agents/plugins/marketplace.json` and `plugins/codex/plugins/`
after source-layer edits are complete.

## Candidate Inbox

Default discovery source:

```text
Notion
AI Resources
-> Skills Collection
```

Notion is a candidate inbox. It is not integration truth.

Current fields:

```text
Name
Type
Utilized
```

Default phase-1 query:

```text
Utilized = false
AND Type != Research
```

An empty `Type` value is a candidate. `Type=Research` is out of scope for this
phase and must be handled later in a separate workflow.

## Existing-History Gate

Before reading upstream content for any candidate, Planner must check:

- `docs/provenance/INTEGRATION_HISTORY.md`
- skill frontmatter provenance
- existing reference and intake docs under `docs/provenance/`

If the candidate source was already handled with one of these decisions, do not
import it again because Notion still says `Utilized=false`:

- `merged`
- `partially-merged`
- `reference-only`
- `reviewed-not-adopted`
- `rejected`

Record:

```text
ALREADY_PROCESSED
```

Also record the previous decision, target, and commit or current-tree marker.
Treat a mismatch between Notion and GitHub history as tracker drift, not as a
new skill intake.

Current smoke case:

```text
Name: 我把三年的ICLR全部审稿人做成了一个开源
Source: https://github.com/Haoran-98/ICLR-reviewer
Utilized: false
Type: <empty>
```

The repository already records:

```text
source: Haoran-98/ICLR-reviewer
decision: partially-merged
target: skills/writing/research/peer-review
date: 2026-07-28
```

The correct bootstrap result is `ALREADY_PROCESSED`. Do not create a duplicate
skill, repeat a merge, or append another provenance row for this source.

## Planner Decision Taxonomy

Codex Executor must not decide how an upstream repo enters the skill library.
GPT Planner owns the decision for every truly new candidate.

Planner must choose exactly one:

- merge into existing skill
- partially merge into existing skill
- create new skill
- create new top-level plugin
- reference-only
- reviewed-not-adopted
- unresolved-asset
- rejected

Creating a top-level plugin is rare. An upstream repo having its own skill,
plugin, MCP server, app, or library is not enough reason to create a new local
skill or plugin. Organize by user-facing task boundary, not source repository
boundary.

Use the existing `skill-library-analysis` and
`ai-skills-repository-maintainer` rules. Do not create a second decision
taxonomy.

## Routing Contract

Any plan that adds or changes an active skill, aggregate/front-door skill, or
plugin exposure must include a routing contract.

The routing contract must include:

- `should-trigger`: 5 to 10 natural user requests.
- `should-not-trigger`: 3 to 5 adjacent near-misses.
- `neighbor skills`: existing skills that could collide.
- `front-door`: the plugin, aggregate, or skill users should discover.
- `reason`: why users do not need to know upstream repo names or internal skill
  names.

Examples must be natural task language. Do not require users to name an
internal skill, upstream repository, or source file. Do not build a fake keyword
scorer for routing. Reviewer must judge semantic routing from frozen examples.

Reviewer must check:

- Whether descriptions cover natural task language.
- Whether the trigger is too narrow and requires internal names.
- Whether the trigger is too broad and collides with neighbors.
- Whether profile, marketplace, aggregate, or front-door exposure is correct.
- Whether multiple active skills now duplicate the same trigger boundary.

## Upstream Evidence

For a truly new external repository, Executor may temporarily clone under:

```text
.tmp/skill-intake/
```

Do not commit scratch clones. Before Planner adopts content, record:

- repository purpose
- actual files and skill/workflow content
- license
- current upstream commit
- provenance
- whether the repo is truly a model workflow source

Notion, Xiaohongshu, or public-post descriptions are discovery/context evidence.
They are not enough to decide a merge.

Software, MCP, library, or app/tooling repositories that are not model
workflows should not be forced into user-facing skills. Choose
`reference-only`, `reviewed-not-adopted`, or `rejected` when that is the honest
result.

## Notion Reconciliation

`Utilized=true` means the Notion source was actually used by this repository:

- `merged`
- `partially-merged`
- `reference-only`

Do not set `Utilized=true` just to hide a candidate when the decision is:

- `reviewed-not-adopted`
- `rejected`
- `unresolved-asset`

Processed status is determined by `INTEGRATION_HISTORY.md` and provenance, not
by the Notion checkbox. This adapter must not directly modify Notion. Tracker
write-back belongs in the final GPT/ChatGPT transaction for a real intake batch.

## Final Report Order

For AI Skills intake, `FINAL_REPORT.md` should tell the user first:

- number of candidates in the batch
- newly processed count
- already processed count
- adopted count
- partially absorbed count
- reference-only count
- rejected count
- new capabilities
- strengthened existing capabilities
- why no new plugin or skill was added, when applicable
- trigger collisions resolved
- natural requests users can now say
- example usage

Only after that should it list changed files, registry/catalog changes,
marketplace generated changes, tests, CI, provenance, and Notion reconciliation
status.

## Adapter Regression Coverage

Codex tests must cover adapter behavior with fixtures. Do not test the private
Notion connector itself.

Required cases:

- `Utilized=false` plus existing `partially-merged` provenance returns
  `ALREADY_PROCESSED` and creates no duplicate skill.
- already rejected candidates are not re-imported.
- a new candidate overlapping an existing trigger requires an explicit
  merge/conflict decision.
- new active skill plans without `should-trigger` examples are invalid.
- new active skill plans without `should-not-trigger` examples are invalid.
- new plugin plans without an explicit Planner decision are invalid.
- generated marketplace/plugin layers remain generated-only.
- `Type=Research` is excluded from phase-1 default intake.
