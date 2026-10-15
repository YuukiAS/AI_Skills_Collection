# Stage A read-only consumer inventory

This inventory records reachable downstream cancellation paths. The inspection was read-only; no DII or CARE file was changed and no watcher was run.

## Distributed_Imaging_Inference

- Repository commit: `f5066f5760d707fa85bb326a5716c82026929c25`
- `AGENTS.md`
  - SHA-256: `3aa00d59a0bd1bcf49ac8c8a988bfbfdc30f839a7926e4e2b2a58ca32b2ddc10`
  - Current contract allows a bounded H100/A100 race and says to cancel the pending loser after a winner starts.
  - Gap: the project rule does not yet route that cancellation through the Stage A exact-target decision and fresh-human representation. Its standing race opt-in cannot be treated as cancellation confirmation.

## CARE

- Repository commit: `f9703d609849655570d4d98ae9c7520c0c485e4c`
- `.agents/skills/slurm-routing-partition/SKILL.md`
  - SHA-256: `93f1a9590048bdff6ae676994dd1463dc3e9c5764c8d8198d8782bda9aab5bc4`
  - Requires routing-race loser cancellation and records cancellation commands, but has no exact-target protected-cancellation gate.
- `scripts/route_B_round04/watch_B1_race.py`
  - SHA-256: `ba648749be3c914dc22fac312374751fa79b65c7526085f00af8983dbae23773`
  - Directly runs `scancel` for a pending loser.
- `scripts/evaluation/watch_care_srr_cascade_formal_race.py`
  - SHA-256: `08f4fd392f9522ed3419d8f659ad602329fab864af484819ef0bc2d1be7af1f6`
  - `cancel_if_pending()` runs `scancel`; `--dry-run` only changes execution and is not an isolation boundary.
- `scripts/evaluation/watch_srr_v3_m7_routing.py`
  - SHA-256: `b9ec290986e439291e74cc91f458e0a81b8f4fe0677dcec3ebff7e5a34192628`
  - Directly runs `scancel` after observing one mirror in `RUNNING`.
- `scripts/evaluation/watch_srr_v3_m8_myops_race.py`
  - SHA-256: `34a8431fb0246bfc963a7c673cf0b2a6938a57f59cdc4ea4bd402fe55d9ce372`
  - Directly runs `scancel` for a pending mirror; simultaneous running falls back to manual intervention.
- `scripts/target_domain_gap_closure/monitor_interactive_takeover.py`
  - SHA-256: `68b0cdc953e2b8293b33282b9d5786d254c70a687fffea09351a16695c3f872a`
  - Directly runs `scancel` for a queued job during interactive takeover.

## Adaptation boundary

All listed consumer paths remain unadapted. A later separately authorized consumer change must load the reviewed central helper, build trusted exact target facts, preserve project-specific scientific contracts, and refuse automatic cancellation where the central decision requires fresh human confirmation or denies unknown facts. Stage A does not modify, install, or run these consumers.
