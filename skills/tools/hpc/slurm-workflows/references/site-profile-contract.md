# Site Profile Contract

The generic Slurm skill must not hard-code site facts. Site profiles may provide:

- visible partitions and allowed defaults;
- account and QOS policy names when public-safe;
- CPU, memory, walltime, and GPU limits;
- scratch and log directory conventions;
- module initialization commands without secrets;
- race execution policy;
- smoke-test policy.

Local overrides may provide private account names, private paths, modules, and per-machine executables. Secrets must never be written to generated skill references.
