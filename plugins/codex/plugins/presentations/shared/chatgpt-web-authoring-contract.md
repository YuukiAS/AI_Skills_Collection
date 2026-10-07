# ChatGPT Web Presentation Authoring Contract

Status: **canonical app-facing authoring contract**  
Applies to: non-trivial presentation creation, revision, recovery, and review planning initiated from ChatGPT Web

## 0. Mandatory first read

Before ChatGPT Web plans, revises, or hands off any non-trivial presentation task, read:

`pre-execution-cumulative-acceptance-contract.md`

The Planner must classify the task, determine whether a Critic is required, identify the current freeze state, and bind the cumulative guard/lock state before production planning.

## 1. Purpose

ChatGPT Web is the presentation author and Planner. It may invoke the presentations capability to understand sources, design the deck, freeze audience-facing decisions, digest human feedback, inspect rendered artifacts, and prepare autonomous Codex production Goals.

ChatGPT Web is not the slide-production executor. It does not replace Codex for source implementation, figure generation, build, rendering, tests, or repository delivery.

The intended split is analogous to Research Authoring:

```text
ChatGPT Web = source understanding + content/communication judgment + frozen specification
Codex = implementation + rendering + deterministic QA + autonomous repair
Fresh Reviewer / GPT Work = independent rendered-artifact judgment
User = final subtle preference and acceptance
```

## 2. When ChatGPT Web should invoke presentations

Invoke the presentations authoring capability when the user asks to:

- create a new deck, slides, PPTX, Google Slides, Beamer, or presentation PDF;
- restructure or substantially rewrite an existing deck;
- revise a deck from user/advisor/reviewer annotations;
- recover a deck with multiple failed historical versions;
- assess page count, storyline, page jobs, copy, layout, or audience suitability;
- prepare a Codex production or revision Goal;
- review a rendered candidate or delta before user handoff.

A trivial mechanical edit may route directly to a bounded executor task, but it still retains the exact baseline, requested edit, and protected scope.

## 3. ChatGPT-owned decisions

ChatGPT Web owns:

- audience, purpose, duration, format, and desired audience change;
- source reconciliation and claim/source boundaries;
- narrative and section order;
- page count or bounded page-count range;
- stable PageIDs and one teaching/decision/research job per page;
- required and forbidden content objects;
- exact visible copy, or an explicitly bounded writing stage;
- student/audience versus speaker/instructor/internal boundaries;
- semantic relationship and layout archetype;
- historical-feedback interpretation, lifecycle, supersession, and conflicts;
- page/component locks and explicit unlocks;
- classification as new deck, minor revision, major revision, or failed-version recovery;
- whether a prebuild Critic is mandatory;
- Controller Goal scope and acceptance requirements.

These decisions cannot be silently delegated to the layout executor.

## 4. ChatGPT must not do

ChatGPT Web must not:

- give Codex an open-ended request such as “make the deck better”;
- ask Codex to decide what should be taught, claimed, deleted, merged, or split;
- treat a latest PDF as the only authority when cumulative feedback exists;
- freeze exact copy before reading the relevant source and human feedback;
- use a component proof or golden page as a substitute for complete content planning;
- turn ordinary user review into repeated full-deck annotation;
- expose large internal ledgers, QA logs, hashes, or controller chatter unless requested.

## 5. Required authoring outputs

For a non-trivial task, ChatGPT Web should materialize or clearly freeze the following objects before production:

```text
DECK_BRIEF
SOURCE_AND_BASELINE_MANIFEST
PAGE_AUTHORITY
VISIBLE_COPY_AUTHORITY
LAYOUT_AUTHORITY
SHARED_COMPONENT_SPEC
HISTORICAL_FEEDBACK_AND_LOCK_STATE      # revision/recovery only
ROUND_SCOPE_AND_ALLOWLIST                # revision only
PREBUILD_CRITIC_REQUEST                  # major/recovery when required
AUTONOMOUS_CODEX_CONTROLLER_GOAL
```

The exact file format may be YAML, JSON, Markdown, or a repository-native schema, but the authority and precedence must be unambiguous.

## 6. Major versus minor routing

### Minor revision

ChatGPT may proceed without a separate prebuild Critic only when all are true:

- page count and section order are unchanged;
- no page job or scientific/teaching claim changes;
- no shared title/header/footer/navigation/template redesign;
- no new layout archetype or page split/merge;
- visible-copy changes are local and source-supported;
- scope is normally at most three pages and at most one already-defined component;
- no previously closed historical guard has recurred;
- the user has not requested a broad redesign or full rethink.

ChatGPT freezes the bounded scope and sends it directly to an autonomous Codex revision Controller.

### Major revision

A fresh prebuild Critic is mandatory when any of these holds:

- page count, section order, page jobs, or storyline changes;
- substantial copy or content changes across multiple pages;
- shared shell/template/header/footer/navigation changes;
- new layout archetypes, page splits, page merges, or major figure redesigns;
- a human-rejected lineage or repeated regression must be recovered;
- the user asks to rethink, rebuild, overhaul, or reread all historical feedback;
- the proposed revision changes statistical/scientific/pedagogical meaning;
- the Planner is uncertain whether the current specification faithfully reflects history.

If uncertain, classify as major.

A major Planner amendment after Critic review requires a fresh Critic pass before production. Minor wording or metadata corrections explicitly permitted by the Critic do not require a full new architecture round unless they change its judgment basis.

## 7. Feedback intake in ChatGPT Web

For a major revision or recovery, ChatGPT must reread the full raw feedback history and rendered lineage, not only normalized guards. It reports the recovered counts and unresolved conflicts before freezing the new specification.

For a minor revision, ChatGPT reads:

- current user feedback;
- the exact reviewer-seen baseline;
- active global guards;
- affected PageID/component history;
- current locks and consumer dependencies.

Raw human feedback remains higher authority than a derived registry. Derived guards may organize and enforce history but cannot reverse an active human decision.

## 8. Render review in ChatGPT Web

ChatGPT may inspect PDFs, page images, and contact sheets to:

- compare a candidate with raw user feedback;
- identify statistical/pedagogical specification defects;
- decide whether a finding requires Planner amendment or ordinary Codex repair;
- update locks after user acceptance;
- prepare a filtered delta for the user.

ChatGPT should not duplicate deterministic build or artifact checks that belong to Codex/Auditor. Its comparative advantage is source fidelity, statistical/scientific meaning, teaching sufficiency, and communication judgment.

## 9. User-facing behavior

The user should see:

- the core judgment;
- the real artifact or filtered delta;
- only genuine decisions still requiring human preference;
- exact next action when one is needed.

The user should not be asked to:

- relay Producer/Auditor messages;
- launch routine reviewers;
- find obvious layout defects;
- repeatedly re-annotate unchanged pages;
- approve internal implementation choices that the frozen specification already decides.

## 10. Handoff to Codex

The Codex Controller Goal must name:

- exact repository/branch/baseline;
- task classification and Critic status;
- authority files and precedence;
- allowed and forbidden paths;
- exact PageIDs/components in scope;
- locks and dependency consumers;
- copy/layout/component authority;
- deterministic and rendered review requirements;
- automatic repair/re-review rules;
- user-interruption policy;
- versioning and final delivery artifacts.

Codex may not reinterpret a missing decision as permission. A genuine semantic conflict returns to ChatGPT Planner with one precise question.
