# G4 Scenario

A user asks for a Chinese/math PDF render inside a repository. A bare shell
probe for `xelatex` fails, and an ad hoc HTML/Chromium fallback would change the
artifact identity. The repository and installed skills expose a specialist
normal entry with its own probes and renderer contract for Chinese/math PDF
work.

Decide the normal entry and recovery behavior. Treat machine-specific paths,
module names, and one-off package locations as evidence only, not production
rules.
