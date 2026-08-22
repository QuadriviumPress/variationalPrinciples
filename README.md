# Variational Principles in Classical Mechanics (MyST edition)

Web-native [MyST Markdown](https://mystmd.org/) edition of Douglas Cline's
*Variational Principles in Classical Mechanics* (University of Rochester River
Campus Libraries).

## Status

Full book converted from the structured
[LibreTexts edition](https://phys.libretexts.org/Bookshelves/Classical_Mechanics/Variational_Principles_in_Classical_Mechanics_(Cline))
(aligned with the third edition), with figures downloaded from LibreTexts.
Author PDFs (2e and 3e) are kept locally for reference (git-ignored).

- **Live site**: [quadriviumpress.com/variationalPrinciples](https://quadriviumpress.com/variationalPrinciples/)
- **CI/CD**: `.github/workflows/ci.yml` on pull requests;
  `.github/workflows/deploy.yml` publishes to GitHub Pages on pushes to `main`.

## Source and license

© Douglas Cline (2017–2021), ISBN 978-0-9988372-3-9.
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

Original: [classicalmechanics.lib.rochester.edu](http://classicalmechanics.lib.rochester.edu/)

## Build

```bash
npm install
npm run start          # preview
npm run build          # static site in _build/html/
```

## Convert from LibreTexts

```bash
npm run crawl          # fetch HTML → work/html + outline.json
npm run convert        # HTML → Markdown + images
npm run verify
```

Requires Python 3 with `beautifulsoup4`, and Node ≥ 20.

## Layout

| Path | Role |
| --- | --- |
| `outline.json` | LibreTexts page tree |
| `myst.yml` | Project metadata and TOC |
| `scripts/` | Crawl + HTML→MyST pipeline |
| `work/html/` | Cached LibreTexts pages (git-ignored) |
| `chapters/` | Nineteen chapter Markdown files |
| `front/` / `back/` | Preface, prologue, epilogue, glossary |
| `images/` | Figures from LibreTexts |

Chapter files concatenate LibreTexts sections; display math is kept as `$$…$$`
from the LibreTexts LaTeX source.
