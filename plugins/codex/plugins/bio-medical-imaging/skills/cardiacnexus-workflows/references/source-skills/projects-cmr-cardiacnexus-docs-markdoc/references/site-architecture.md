# CardiacNexus docs site architecture

## Current stack

- Next.js 14
- Markdoc pages under `docs/src/app/**`
- static export via `output: "export"`
- custom navigation in `docs/src/lib/navigation.ts`
- custom tags in `docs/src/markdoc/tags.js`

## Important current constraints

- `next.config.mjs` uses:
  - `basePath: '/documentation'`
  - `assetPrefix: '/documentation'`
  - `trailingSlash: true`
- `package.json` still contains a `gh-pages` deployment script, which is not the final long-term publishing story if the site moves behind Cloudflared or a first-party domain.

## Editing guidance

- Update source pages, not `out/` or `.next/`.
- Keep navigation aligned with the actual page tree.
- Replace example value/template pages with project-specific documentation incrementally.
- Treat homepage metadata, docs landing page, and phenotype pages as part of one information architecture.

## Future publishing direction

- Prefer deployment choices that keep the site a plain static export.
- If the site moves to `cardiacnexus-ukb.org`, revisit:
  - `homepage`
  - `basePath`
  - `assetPrefix`
  - canonical URLs
  - internal link assumptions
