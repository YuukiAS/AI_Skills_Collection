---
name: simpy
description: Build and validate process-based discrete-event simulations in Python with SimPy: entities, resources, queues, event timing, replications, sensitivity analysis, and reporting.
status: active
provenance: unknown
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-06-19
profile_tags:
recommended_scope: project
license: MIT License
metadata:
  skill-author: K-Dense Inc.
---
# SimPy Discrete-Event Simulation

## Workflow

1. Define system boundary, entities, resources, queues, events, time units, warm-up, and output metrics.
2. Specify stochastic assumptions and distributions separately from process logic.
3. Implement small composable processes, resource requests, and monitors.
4. Run multiple replications with controlled random seeds and collect summary statistics.
5. Validate event traces against hand-calculated toy cases before scaling.
6. Run sensitivity/scenario analysis and report uncertainty across replications.

## References

- Read `references/simulation-workflow.md` for model structure, validation, and reporting checklists.
- Read `references/legacy-full-skill.md` for older SimPy patterns and examples.

## Validation

- Time units and resource capacities are explicit.
- A small deterministic or hand-checkable scenario passes before full simulation.
- Reported results include replication variability, not a single run only.
