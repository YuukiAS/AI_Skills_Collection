# Legion ADAPTING Evidence Stub

Task key: `ai-skills-core--machine-update-orchestration`  
Consumer: `Legion`  
Status: `PENDING_CONSUMER_AUTHORITY`  
Prepared date: 2026-09-25

## Current Central Identity

- Tracking Issue: `#86`
- Project Status: `ADAPTING`
- Area: `ai-skills-core`
- Resolution commit: `c7776e202ae0324fc00b719b6ef8224b8e0498fe`
- Formal AI_Skills `main`: `c7776e202ae0324fc00b719b6ef8224b8e0498fe`
- Formal AI_Skills `release`: `c7776e202ae0324fc00b719b6ef8224b8e0498fe`
- Released repository version: `5.2.0`
- Released `ai-skills-core`: `0.5`
- Released `workflow-core`: `0.4`

## Authority Boundary

No consumer-local authority has been observed in this task for `Legion`.
Do not infer hostname, `CODEX_HOME`, Marketplace state, installed plugin state,
or Codex runtime identity from any other machine.

Before changing this status, the adapting run must be executed from this exact
consumer, or from a session with explicit bounded authority for this exact
consumer, and must follow `../ADAPTING_CONSUMER_RUNBOOK.md`.

## Required Evidence Before PASS

A future PASS for `Legion` must record:

- actual target identity: hostname, platform, user, `HOME`, `CODEX_HOME`, and Codex version;
- approved adaptation / update action for this consumer;
- exact `yuukias-ai-skills` Marketplace source, ref, sparse paths, last revision, and owning config layer;
- installed / enabled identity for `ai-skills-core@yuukias-ai-skills` and relevant companions;
- official Codex Marketplace/plugin commands used, if migration or reinstall is needed;
- exact old source metadata and restoration evidence if legacy `main -> release` migration is attempted;
- fresh production normal-entry consumption through installed `ai-skills-core@yuukias-ai-skills`;
- fresh-session or reload boundary evidence when required;
- should-not-change and failure-safety evidence for unrelated project/user state;
- durable evidence locator for this consumer.

## Forbidden Inferences And Side Effects

This stub does not authorize:

- paid API use;
- automation;
- AI_Skills or Bridge `release` advancement;
- Bridge runtime/source mutation;
- unrelated project mutation;
- hand-editing Codex config;
- marking the Board `DONE`.

## Current Handoff

```text
CONSUMER=Legion
STATUS=PENDING_CONSUMER_AUTHORITY
NEXT_ACTION=Run ADAPTING_CONSUMER_RUNBOOK.md only on this authorized consumer.
OVERALL_DONE=NO
```
