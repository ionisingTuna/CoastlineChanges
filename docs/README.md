# Documentation

- Large binaries (videos, high-res images, PDFs) should be tracked by Git LFS.
- Prefer adding heavy example assets to GitHub Releases rather than the main branch.
- Keep result images small (thumbnails) in-repo; link to full-size assets in Releases.

## Suggested structure

- `docs/` – documentation, smaller images for README
- `results/` – generated outputs (gitignored); commit only curated thumbnails
- `coastline/` – reusable processing code
- `notebooks/` – optional future notebooks if you split them

## Results gallery tips

- Export a 2x4 or 3x3 collage per region for quick viewing.
- Keep thumbnails under ~300 KB each.
