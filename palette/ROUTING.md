# Palette Routing

`palette/` is only the canonical library for scientific figures, research plots,
publication-ready figure panels, and supplementary figure graphics.

## Route By Surface

| Surface | Use | Do not use |
| --- | --- | --- |
| Scientific figures | `palette/scientific-figure-palettes.json` | Deck-wide theme colors or product UI tokens |
| Research/business presentations | Presentation theme and template skills | Raw academic palette ids as slide themes |
| Product/frontend UI | Semantic design tokens | Journal-inspired or figure palettes as direct UI colors |

## Scientific Figure Defaults

- Categorical data: start with `okabe_ito`; use `Dark2`, `Set2`, or `Paired`
  when ColorBrewer is a better fit; use journal-inspired palettes only as
  non-official style inspiration.
- Sequential scalar data: prefer `viridis` or `cividis`; use `plasma`,
  `inferno`, `magma`, `Blues`, `YlGnBu`, or `OrRd` when the figure semantics
  fit the ramp.
- Diverging data: use `RdBu`, `BrBG`, `PuOr`, or `coolwarm` only when the data
  has a real midpoint.
- Cyclic data: use `twilight` for phase, angle, or wrapped values.

## Boundary Rules

- A presentation theme may reference a scientific palette for embedded plots,
  but the deck's background, typography, accents, and section system belong to
  presentation theme files.
- A frontend may expose chart semantic tokens that map to a scientific palette,
  but page backgrounds, buttons, alerts, links, and states must use semantic UI
  tokens.
- Journal-inspired entries are not official publisher brand specifications.
  They must not be described as official Nature, Science, Lancet, JAMA, BMJ,
  JCO, or NEJM branding.
