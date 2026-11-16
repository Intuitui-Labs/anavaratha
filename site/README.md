# Anavaratha site (prototype)

Static Astro 7 site with Svelte 5 islands: home, atlas (timeline, relations, map, flows, patterns), lineage, desk notes, data, method, changelog.
Stage: **Sensemaking**. No intervention claims. Listed ≠ verified. `noindex` on every page and as a header. Licence: **TBD**.

## Run

```bash
cd site
pnpm install
pnpm dev      # http://127.0.0.1:4322
pnpm build    # -> dist/
```

Only `/atlas` loads chart code. Each island hydrates when scrolled into view (`client:visible`). Initial load is the timeline and d3-scale (~110 KB). Cytoscape, MapLibre and Observable Plot load when their sections are reached. The other pages ship no JS.

## Deploy (Vercel; not done yet)

1. New Vercel project from `Intuitui-Labs/anavaratha`, **Root Directory = `site`**. `vercel.json` sets the framework (Astro), pnpm, and the output (`dist`).
2. Settings → Domains → add `anavaratha.intuituilabs.studio`.
3. DNS: none needed. Cloudflare already has `anavaratha` CNAME → `cname.vercel-dns.com`. Keep it **DNS-only (grey cloud)** so Vercel can issue the certificate.
4. Optional env: `ANAVARATHA_SITE` (canonical origin), `ANAVARATHA_BASE` (to serve under a subpath, e.g. `/projects/anavaratha/atlas-site`).

## Data

`src/data/*.json` and `public/data/*` are generated and committed. Every node, edge, event and row carries a `src` path into the research files (`anavaratha-legacy/…`, `phase1/…`). Those files are not all in this repo.

- `operators_public.geojson`: contact, address and price fields removed; phone and email patterns scrubbed; coordinates rounded to 4 dp. Points with `geocoded_by_atlas: true` sit at the centre of the town named in their own address (OSM Nominatim, checked against the stated district). They are approximate.
- `operators_unmapped.json`: rows with no usable coordinates, with the reason for each. No coordinates are invented.
- Map tiles: OpenFreeMap. Map data © OpenStreetMap contributors (ODbL).

`scripts/provenance/` holds the scripts that produced the data and screenshots. They read local research snapshots, so they are a record of method, not a build step.

## Accessibility

- Every chart has a text or table version, or a text list.
- Timeline items and graph nodes work from the keyboard (Tab + Enter; "Find a node" box).
- Reduced motion is respected (no smooth scroll, no graph animation, no map fade).
- Palette checked with `@intuitui-labs/a11y-gate`: WCAG ≥ 4.5:1 for all marks on white, and CVD ΔE checks for protanopia, deuteranopia and tritanopia.
