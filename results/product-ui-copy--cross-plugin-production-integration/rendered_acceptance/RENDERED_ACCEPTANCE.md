# Product UI Copy Rendered Acceptance Evidence

Task: `product-ui-copy--cross-plugin-production-integration`

Rendered with: Playwright CLI 1.55.0 / Chromium 140.0.7339.16

Source fixture: `product-ui-copy-fixture.html` (8bffd3761d629b64b40f7b90051aa55a6a7f614b617fcb5313463eec22087f84)
CSS fixture: `product-ui-copy-fixture.css` (55bee25fa84d2fac2667beac2903d5b405f16aee8811f5254b42f19e9fcf569f)

## Captures

- `wide-desktop.png`: wide/desktop layout and multi-block page rhythm; viewport 1440x1200; PNG 1440x1423; sha256 `135e716a612773f7cfb226d1a39e50c82f10933e9647e30189a4cd348622cff1`
- `narrow-mobile.png`: narrow/mobile layout and stacked controls; viewport 390x1200; PNG 390x1850; sha256 `4a7b3c82c8eacef107a6699dc1adc4495587544479391f575e52a8947ddd1399`
- `trust-disclosure.png`: trust/help disclosure and CTA relationship; viewport 920x900; PNG 920x1685; sha256 `b1efbb0f1edcc0886e5dfeec8d4d5e7a8e6c623d385524267fcb30e5b25004e7`
- `keep-control.png`: already-good copy KEEP control; viewport 760x820; PNG 760x1909; sha256 `b6683edca7592e24cfed20d126e4f01e92e9abd12e0fb4cd2a00def5107515ec`

## Acceptance Notes

- The settings surface preserves trust semantics: local inspection precedes upload, and upload requires user confirmation.
- The trust panel keeps privacy/data-retention disclosure adjacent to the primary CTA instead of hiding it elsewhere.
- The mobile deletion surface preserves destructive/public-visibility/audit-retention consequences.
- The KEEP control intentionally keeps already clear copy unchanged.
- This evidence is browser-rendered representative fixture evidence only; it does not claim native desktop/mobile runtime execution.

## Review Round 1 Repair Note

Reviewer round 1 found an awkward 760px wrap in `keep-control.png`: the final character of `三步完成桌面端设置` appeared alone on a third line. The fixture CSS now switches `.surface-grid` to one column at widths up to 860px, keeping that heading in a normal two-line wrap at the 760px capture.

The four screenshots and `render-manifest.json` were regenerated after this fixture-only layout repair. Manual visual inspection of the regenerated `keep-control.png` confirms the orphan final-character wrap is gone. This does not change the H2 production candidate commit or rerun H4.
