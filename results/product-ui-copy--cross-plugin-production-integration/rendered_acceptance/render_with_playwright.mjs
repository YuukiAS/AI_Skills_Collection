import { chromium } from "playwright";
import { createHash } from "node:crypto";
import { readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const htmlPath = path.join(here, "product-ui-copy-fixture.html");
const cssPath = path.join(here, "product-ui-copy-fixture.css");
const htmlUrl = pathToFileURL(htmlPath).href;

const viewports = [
  { name: "wide-desktop", width: 1440, height: 1200 },
  { name: "narrow-mobile", width: 390, height: 1200 },
  { name: "trust-disclosure", width: 920, height: 900 },
  { name: "keep-control", width: 760, height: 820 },
];

function sha256(buffer) {
  return createHash("sha256").update(buffer).digest("hex");
}

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ deviceScaleFactor: 1 });
const captures = [];

for (const viewport of viewports) {
  await page.setViewportSize({ width: viewport.width, height: viewport.height });
  await page.goto(htmlUrl, { waitUntil: "networkidle" });
  await page.screenshot({
    path: path.join(here, `${viewport.name}.png`),
    fullPage: true,
  });

  const image = await readFile(path.join(here, `${viewport.name}.png`));
  captures.push({
    ...viewport,
    file: `${viewport.name}.png`,
    sha256: sha256(image),
  });
}

await browser.close();

const [html, css] = await Promise.all([readFile(htmlPath), readFile(cssPath)]);
const manifest = {
  fixture: "Product UI Copy rendered acceptance",
  html: {
    file: "product-ui-copy-fixture.html",
    sha256: sha256(html),
  },
  css: {
    file: "product-ui-copy-fixture.css",
    sha256: sha256(css),
  },
  captures,
  coverage: [
    "wide/desktop layout",
    "narrow/mobile layout",
    "multi-block linguistic page rhythm",
    "trust/help disclosure and CTA relationship",
    "already-good KEEP control",
  ],
};

await writeFile(
  path.join(here, "render-manifest.json"),
  `${JSON.stringify(manifest, null, 2)}\n`,
);
