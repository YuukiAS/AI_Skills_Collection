# Research Authoring Wrapper Composition

Task: `research-authoring--formal-production-authoring`
Candidate commit: `1c37c0715aca0096606f24e56192b7857e72bbd6`
Wrapper name: `research-authoring`
Wrapper version: `0.1.0`
Scope: `USER`
Discoverability: `PRIVATE`
Composition type: skills-only offline package

## Included Payload

Research Authoring canonical payload:
- `plugins/codex/plugins/research-writing/**`

Clear Writing support snapshots from the same candidate commit:
- `skills/writing/core/writing-fidelity/**`
- `skills/writing/core/chinese-prose/**`
- `skills/writing/core/scientific-prose/**`

## Explicit Exclusions

This package does not include:
- renderer runtime, Pandoc/XeLaTeX, PDF engine, Office runtime, or presentation renderer;
- MCP servers;
- connectors;
- databases;
- watchers, daemons, ledgers, or state machines;
- Plugin Creator live mutation instructions;
- ChatGPT account mutation instructions;
- private research data.

## Live Mutation Boundary

This task is not authorized to create or update a live ChatGPT plugin/wrapper.
At the live mutation step, Executor must stop and request one bounded user authorization for creating/updating a PRIVATE USER-scope skills-only `research-authoring` wrapper from this exact candidate.
