---
name: slurm-workflows
description: Plan, submit, monitor, diagnose, and safely iterate Slurm jobs with generic resource estimation, job arrays, log/scratch layout, queue inspection, failure classification, and optional race execution policy supplied by a site profile.
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: true
executes_code: true
secrets_needed:
last_reviewed: 2026-07-13
profile_tags:
  - hpc
  - server
  - slurm
recommended_scope: user
display_name: Slurm Workflows
short_description: Generic Slurm planning, monitoring, and diagnostics.
icon_small: assets/slurm-workflows.svg
icon_large: assets/slurm-workflows.svg
default_prompt:
  - Plan and monitor this Slurm workload using the current site profile.
---
# Slurm Workflows

## Trigger Boundary

Use this skill for Slurm or HPC batch work that needs resource planning, script generation, submission review, job arrays, queue/status interpretation, log triage, failed-job diagnosis, or safe resubmission.

Do not use it for generic shell scripting, non-Slurm schedulers, or site-specific partition/account decisions unless a site profile or local override provides those constraints.

## Required Site Context

Before giving final Slurm commands, read the generated site profile reference when present:

`references/_generated/site-profile.md`

If no site profile is installed, ask for or detect the minimum non-secret site facts: partitions, account/QOS policy, GPU availability, walltime limits, scratch/log conventions, module setup, and whether race execution is permitted.

## Workflow

1. Identify workload shape: CPU/GPU, memory, walltime, array size, input/output paths, scratch needs, dependency graph, and restartability.
2. Apply site constraints from the profile. Do not invent partition, account, QOS, or hostname values.
3. Produce a script with explicit logs, working directory, environment setup hook, resource requests, and failure-visible shell options.
4. Prefer dry-run or header review before submission when the user is deciding resources.
5. Monitor with current scheduler status and logs; distinguish queued, running, failed, cancelled, timed out, out-of-memory, dependency-held, and completed states.
6. On failure, classify the cause and propose the smallest safe retry.

## Race Policy

Race execution means submitting multiple alternative jobs and cancelling losers after a winner is verified. Only use it when the site profile explicitly allows race execution and the user approves the resource cost. Always record cancellation criteria.

## Outputs

Return the job script or commands, expected log paths, monitoring commands, stop conditions, and final verification checks. Submission is not completion; completion requires current job state and final output validation.
