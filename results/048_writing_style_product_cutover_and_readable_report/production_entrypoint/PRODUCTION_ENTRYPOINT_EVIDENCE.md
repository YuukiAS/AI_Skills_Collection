---
schema: AI_SKILLS_048_PRODUCTION_ENTRYPOINT_EVIDENCE_V1
task_key: 048_writing_style_product_cutover_and_readable_report
review_round: 1
status: EVIDENCE_RECORDED
private_plaintext_included: false
---

# 048 Production Entrypoint Evidence

This file records Review 1 repair evidence for the production maintenance and
normal installed-entrypoint gates. It intentionally contains only public-safe
metadata, routing outcomes, hashes, run ids, and local evidence paths. No private
Deep Research source text or rewritten report plaintext is included.

## Identity

- Review repair base: `3d60b50ee3e6dce276dddd5f4f4cc15699b9e4e1`
- Writing-style implementation identity: `928de2325d781ca630883d03e0f381092675b269`
- Current main snapshot checked before repair: `8faafd5a7ee60b394a53de5debfde3ccfe60b8cc`
- Identity manifest: `results/048_writing_style_product_cutover_and_readable_report/production_entrypoint/replay_identity.json`
- Identity manifest SHA-256: `446e51a9c63c55422471caf85c8f52b6d29ded25fa8004a5592e48732d126309`
- Generated marketplace manifest SHA-256: `680595dcf2f96352ff72a38b97d2cb107e5ba33b9818b9f4cc3a07b379c7f2ce`
- Generated `writing-style` plugin id/version: `writing-style@yuukias-ai-skills`, `0.1`
- Generated `ai-skills-core` plugin id/version: `ai-skills-core@yuukias-ai-skills`, `0.2`

## Production Maintenance Replay

Command shape:

```text
ai-bridge plugin-replay --target /tmp/ai-skills-048 --plugin ai-skills-core --task <public task> --input <identity manifest>
```

Environment note: the successful run unset inherited proxy variables before
launching the child Codex process.

- Replay run id: `20260902T102228Z-4c3b637c7857`
- Replay status: `completed`
- Replay exit code: `0`
- Task input SHA-256: `424758aca89ec36fcc7cc005febf0688fdf0edf1c906ae847562b341f92c3656`
- Identity input SHA-256: `446e51a9c63c55422471caf85c8f52b6d29ded25fa8004a5592e48732d126309`
- Write isolation: `passed`, canary changed `false`
- Read-scope diagnostic: neighbor probe result `READABLE`, strict read isolation `false`
- Replay output path: `/overflow/htzhu/mingcheng_new/.ai-bridge/plugin-replay/20260902T102228Z-4c3b637c7857/outputs/last-message.txt`

Observed final replay message:

```json
{
  "status": "preflight_valid_no_product_pass_claimed",
  "plugin_selector": "ai-skills-core",
  "maintenance_skill_observed": true,
  "task_key": "048_writing_style_product_cutover_and_readable_report",
  "writing_style_identity_observed": true,
  "presentations_scope_allowed": false,
  "private_plaintext_requested": false,
  "local_artifacts": []
}
```

Interpretation: the production maintenance companion was invoked through the
bounded replay wrapper, saw the 048 writing-style identity, kept presentations
out of scope, did not request private plaintext, and did not claim Product PASS.

## Installed Marketplace Entrypoint

The current generated marketplace was added to a shadow Codex configuration with:

```text
CODEX_HOME=/tmp/ai-skills-048-codex-home codex plugin marketplace add /tmp/ai-skills-048 --json
```

Then the relevant plugins were installed with:

```text
CODEX_HOME=/tmp/ai-skills-048-codex-home codex plugin add writing-style@yuukias-ai-skills --json
CODEX_HOME=/tmp/ai-skills-048-codex-home codex plugin add ai-skills-core@yuukias-ai-skills --json
```

`codex plugin list` in that shadow configuration showed marketplace
`yuukias-ai-skills` loaded from:

```text
/tmp/ai-skills-048/.agents/plugins/marketplace.json
```

and showed the generated plugins installed/enabled from this worktree:

```text
ai-skills-core@yuukias-ai-skills    installed, enabled  0.2  /tmp/ai-skills-048/plugins/codex/plugins/ai-skills-core
writing-style@yuukias-ai-skills     installed, enabled  0.1  /tmp/ai-skills-048/plugins/codex/plugins/writing-style
```

The installed cache copies matched the generated worktree copies for the
three routing-critical skill entrypoints:

```text
d6a5821c7f635a459a40d99c8e5ec0b87f459f52871056a65fc8c2b597b844b2  scientific-rewrite/SKILL.md
02c671fc37e3604ffb41e928996f1277b1a46f79215a71023a6264eeed885f0b  zh/SKILL.md
bdfed30b315c23e986bd00b513b57c3dda96ceebc759b50a91c8a117954c11f0  fidelity/SKILL.md
```

## Installed Writing-Style Routing

`ai-bridge plugin-replay` evidence:

- Replay run id: `20260902T102406Z-1c57d652ee1a`
- Replay status: `completed`
- Replay exit code: `0`
- Task input SHA-256: `a23a5139eac02412d4567895bc94552afc2d08519c1516e80c5c6e0e7ef59916`
- Identity input SHA-256: `446e51a9c63c55422471caf85c8f52b6d29ded25fa8004a5592e48732d126309`
- Write isolation: `passed`, canary changed `false`
- Read-scope diagnostic: neighbor probe result `READABLE`, strict read isolation `false`
- Replay output path: `/overflow/htzhu/mingcheng_new/.ai-bridge/plugin-replay/20260902T102406Z-1c57d652ee1a/outputs/last-message.txt`

Observed replay routing:

```text
heavy_should_trigger -> scientific-rewrite
light_polish -> chinese-prose / zh
fidelity_only -> writing-fidelity / fidelity
```

Fresh installed-entrypoint `codex exec` evidence was then run with the shadow
installed marketplace, read-only sandbox, ephemeral session, and `CODEX_HOME`
pointing at `/tmp/ai-skills-048-codex-home`.

- Output path: `results/048_writing_style_product_cutover_and_readable_report/production_entrypoint/installed_writing_style_routing_last_message.txt`
- Observed plugin id: `writing-style@yuukias-ai-skills`
- Observed task key: `048_writing_style_product_cutover_and_readable_report`
- Private plaintext requested: `false`
- Final Product PASS claimed: `false`

Observed fresh-session routing:

```json
{
  "heavy_should_trigger": ["scientific-rewrite", "writing-fidelity", "chinese-prose"],
  "light_polish": ["chinese-prose"],
  "fidelity_only": ["writing-fidelity"]
}
```

Interpretation: the normal installed `writing-style` entrypoint exposes the
expected route set for a heavy Chinese scientific rewrite request, a light
Chinese polish request, and a fidelity-only audit request.

## Secret Scan

A narrow scan over the public production-entrypoint evidence and the two replay
output directories found no OpenAI API key pattern, no private-key block marker,
and no explicit API-key environment variable name. A broader scan only matched
ordinary prose occurrences of the word `token` and the replay wrapper's
read-scope diagnostic labels; those were not secrets.

## Review 1 Boundary

This repair does not redo the private text transform, does not redo Text Review,
does not modify presentations production behavior, does not bump versions, does
not merge main, and does not claim user `ACCEPT`.
