# Anavaratha merged dataset — public-safe export (v2, 2026-11-16)

Public-safe export of the Anavaratha merged dataset (merge v2). The status of every row is **listed, not verified on the ground**. Licence: TBD.

Removed: `contact_public`, Oct-list email/phone, `price`, every address that is not CEA-published (DN-08; drop-point addresses too), archived data-request drafts (DN-02), and any phone/email pattern in any text field (scrubbed to `[phone removed]` / `[email removed]`).
Kept: CEA-published business addresses (DN-08), names, types, streams, licences as listed, source URLs, coordinates (approximate ones flagged in `coord_status`), evidence status (charter vocabulary, DN-04), domain tags (DN-05; `probable`/`uncertain` where not clear).
Oct-2026 L3 dump-site coordinates are rejected (68–93 km off) and never included.

Files: directory_public.csv (canonical + 6 proposed rows), directory_id_aliases.csv, droppoints_public.csv, operators_public.geojson, entities_public.csv, actors_public.csv, relations_public.csv, legal_items_public.csv, sources_public.csv.
Provenance: every entity traces to `sources_public.csv` (file + sha256); value-level provenance is in the private draft.
Note: directory `flags` can contain review notes — read before publishing.

Docs: `MERGED_MODEL.md` (data model, ids, statuses, privacy rules) and `DECISIONS.md` (decisions applied). The lossless check (15/15 merge checks and 8/8 applied checks pass) is kept in the private archive.
