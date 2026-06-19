---
name: cardiacnexus-docs-markdoc
description: Project-specific guidance for the CardiacNexus documentation site in docs/. Use when editing Markdoc pages, navigation, metadata, Next.js static export settings, phenotype documentation, or preparing the site for static publishing behind Cloudflared and cardiacnexus-ukb.org.
status: active
provenance: unknown
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-05-14
profile_tags:
recommended_scope: project
metadata:
  short-description: Maintain the CardiacNexus docs site
---
# CardiacNexus docs Markdoc site

This skill is for the repository's documentation website, not for generic markdown writing.

## Use this skill when

- Editing `docs/src/**`
- Updating `docs/src/lib/navigation.ts`
- Editing `docs/next.config.mjs`, `docs/package.json`, or Markdoc extensions
- Replacing template content with real CardiacNexus content
- Preparing the site for static hosting or Cloudflared publishing

## Workflow

1. Work from source files only:
   - `docs/src/**`
   - `docs/package.json`
   - `docs/next.config.mjs`
   - `docs/src/markdoc/*`
2. Ignore build artifacts:
   - `docs/.next/**`
   - `docs/out/**`
   - `docs/node_modules/**`
3. Check route coherence:
   - source file path
   - navigation entry
   - page title / metadata
4. Prefer real phenotype documentation over template filler.
5. Keep the site compatible with static export.
6. If changing deployment assumptions, reason through `basePath`, `assetPrefix`, internal links, and image paths together.

## Hard constraints

- Do not preserve unrelated template pages just because they render.
- Do not add server-only features that break `output: "export"`.
- Do not hard-code GitHub Pages assumptions into content if the intent is Cloudflared-hosted publishing.
- Do not change navigation without checking the backing page actually exists.

## Content expectations

- Explain modality / field IDs correctly.
- Keep units and phenotype definitions consistent with code.
- Note validation caveats and known limitations where appropriate.
- Use Markdoc callouts, figures, math, and future tag badges in a way that is reusable across pages.

## References

- Site architecture and publishing notes: [references/site-architecture.md](references/site-architecture.md)
