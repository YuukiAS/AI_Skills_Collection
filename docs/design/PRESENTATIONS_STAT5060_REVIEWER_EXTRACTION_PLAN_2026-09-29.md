# Presentations — STAT5060 Reviewer Extraction Plan

Date: 2026-09-29  
Status: planning input / do not implement from an intermediate reviewer

## Purpose

STAT5060 Tutorial 1 has become the first strong real-use stress test for the Presentations reviewer. Multiple deck revisions produced mechanically valid artifacts and even independent-review PASS results, but were immediately rejected by the human after inspecting the rendered slides.

The lesson is not to add another ad-hoc reviewer prompt. The final Presentations reviewer should be extracted from the **human-accepted, frozen reviewer contract** in `YuukiAS/STAT5060-TA` once that contract stabilizes.

Do not treat any intermediate V4/V5/V6/V7 reviewer as canonical.

## Source-of-truth rule

When the STAT5060 Tutorial reaches human acceptance:

1. record the exact `STAT5060-TA` commit containing:
   - final reviewer standard;
   - final reviewer prompts;
   - blind calibration protocol;
   - regression guard ledger;
   - final accepted Tutorial deck;
   - final standard-Beamer theme/usage note;
2. copy the reviewer semantics into Presentations;
3. genericize only course-specific facts;
4. preserve the gate architecture and evidence requirements;
5. replay historical rejected artifacts before promotion.

The generic reviewer must never be reconstructed later from memory, chat summaries or selected TODO bullets.

## Generic reviewer architecture to preserve

### 1. Human authority

A later human rejection invalidates earlier reviewer/executor PASS as acceptance evidence.

### 2. Blind reviewer calibration

A reviewer must prove it can detect defects on a rejected artifact before reviewing a new candidate.

Calibration:
- fresh isolated run;
- rejected artifact + rendered evidence + role + broad categories only;
- no human-rejection answer sheet;
- no expected failure list;
- no executor PASS narrative;
- expected failure set held by an external aggregator;
- calibration run ID/output hash linked to candidate review.

### 3. Independent reviewer roles

At minimum:

Visual/presentation role:
- template behaviour;
- composition;
- typography;
- figure/caption readability;
- navigation/footer;
- deck rhythm.

Audience/language role:
- natural language;
- teaching/scientific explanation;
- first-use order;
- source/lecture continuity where applicable;
- assessment/audience boundary where applicable.

Both inspect the whole deck. Their verdicts remain isolated until frozen.

### 4. Whole-slide rendered-pixel evidence

Every page is first judged at final whole-slide projection scale, no zoom.

High-resolution crops/pages are diagnostic evidence only; they cannot rescue a page that is unreadable at whole-slide scale.

### 5. Traceable findings

Every REVISE finding has:
- stable Finding ID;
- requirement ID;
- page;
- evidence path;
- exact required action.

Round-2 closure is role-scoped. Only after both verdicts freeze does an aggregator inspect the union. The aggregator cannot override reviewer findings.

### 6. Full-deck regression memory

Human-rejected patterns become semantic regression guards and remain active across later versions.

Examples of generic guard classes:
- answer/solution scaffold leakage;
- internal QA/release language;
- first-use before introduction;
- low-contrast navigation;
- misaligned footer controls;
- undersized scientific figures with unused space;
- missing/meaningless captions;
- meta captions;
- centred explanatory prose when the template requires left alignment;
- opening/closing frames losing their intended job.

### 7. First-use includes all visible surfaces

First-use scanning must include:
- body copy;
- legends;
- internal plot titles;
- captions;
- annotations;
- tables;
- footers/source lines.

### 8. Semantic caption review

Caption QA is not boolean.

Reviewer should classify figure explanation as:
- REQUIRED;
- OPTIONAL;
- REMOVE.

A caption should explain scientific meaning when needed, not narrate that an image exists.

## Template/product routing learned from STAT5060

Keep academic presentation routes distinct:

### CUHK research
Research/group-meeting template and research-deck reasoning.

### Course-standard / standard Beamer
Tutorials, lectures and teaching:
- restrained Beamer;
- section/miniframe navigation;
- readable footer/page count;
- title and closing primitives;
- figure/caption discipline;
- stable typography;
- optional recap/contact close.

The reference implementation should be the final human-accepted standard Beamer extracted from STAT5060, not any earlier failed theme.

### Commercial/business PPT
Separate workflow. Do not force business decks into the academic Beamer routes.

## What must remain course-local

Do not copy into the generic plugin:
- STAT5060 page numbers;
- crab/alligator/Ohio content;
- HW1 mappings;
- exact assessment weights;
- TA contact details;
- lecture page references;
- GLMM release blocker;
- course administrative language.

## Promotion tests

Before the extracted reviewer becomes production reviewer authority:

1. rejected STAT5060 V4 => REVISE;
2. rejected STAT5060 V5 => REVISE;
3. rejected STAT5060 V6 => REVISE;
4. any later human-rejected pre-final candidate => REVISE;
5. final human-accepted STAT5060 deck => PASS/READY_FOR_USER_ACCEPTANCE under the genericized reviewer;
6. one unrelated research deck regression test;
7. one unrelated teaching/course deck regression test.

A top-level PASS without page-level evidence is invalid.

## Relationship to current TODOs

This plan operationalizes presentation TODOs #54–#64 in `docs/plugin-todos/presentations.md`.

The TODO file remains the intake/triage surface. This document defines the extraction path once the STAT5060 reviewer and standard Beamer are finally frozen.
