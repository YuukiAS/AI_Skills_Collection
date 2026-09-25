# Slurm Site Context Contract

The generic Slurm skill must not hard-code deployment facts. Runtime planning is based on:

- bounded live Slurm facts from explicit field-whitelisted commands;
- optional public-safe site profiles as hard-policy overlays;
- user-local facts and preferences outside the repository;
- workload-family resource contracts and capacity-family enrollment.

Site profiles may restrict or clarify public policy, but they are not a supported-server registry and cannot invent a live route. A no-profile Slurm site can still plan/apply/doctor when live discovery or explicit local facts provide a local site id.

Local overrides may provide private account names, QOS, partitions, local site ids, private paths, modules, partition preference and accelerator preference. Secrets and raw discovery dumps must never be written to generated skill references.

Generated references should contain only a public-safe locator and summary: `local_site_id`, optional `policy_overlay_id`, scheduler family, profile revision, local override path, runtime availability and fact provenance. Hidden or unavailable facts remain `UNKNOWN`.
