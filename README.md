# CoastlineChanges

A tool to monitor historical coastline changes from Landsat imagery using classic computer vision techniques.

- Presentation: [Project slides](Presentation.pdf)
- Demo video: see repository video or Releases

## Features

- Fetch historical and recent Landsat imagery via Google Earth Engine
- Segment water vs land and extract coastline edges
- Visual overlay to compare change over time

## Prerequisites

- Python 3.9+
- Jupyter Notebook (classic; note: interactive map may not render in JupyterLab)
- Google Earth Engine account and authentication (personal Google account)

## Quickstart

1. Create and activate a virtual environment (recommended).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Authenticate Earth Engine (first run only):
   ```bash
   python -c "import ee; ee.Initialize()"
   ```
   If prompted, a URL will open in your browser to authenticate; paste the token back into the prompt.
4. Launch Jupyter Notebook and open `CoastlineChanges.ipynb`.
5. Run all cells. Use the region selector to pick a demo region or provide a custom AOI.

## Usage notes

- The map widget is designed for Jupyter Notebook (not Lab). If using JupyterLab, enable widgets extensions or switch to classic Notebook.
- Generated outputs are written under `results/` (gitignored). A JSON metadata file is saved alongside the image.

## Repository layout

- `CoastlineChanges.ipynb` – main demonstration notebook
- `coastline/` – minimal processing utilities (edge detection, metadata saving)
- `docs/` – documentation and guidance
- `Results/` – curated images from prior runs (consider moving large assets to Releases)

## Large files

This repo is configured for Git LFS (see `.gitattributes`) for large binaries like videos, PDFs, and high-res images. Prefer GitHub Releases for heavy assets.

## Acknowledgements and references

This project references Landsat datasets and techniques like K-Means segmentation, Gaussian filtering, Canny edge detection, and contour extraction. See the notebook for complete references and links.

## License

MIT
