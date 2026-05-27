# Changelog

All notable changes to the **onomaturgy-data** package are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---
## [0.2.1] — 2026-05-27

### Removed
- **`Gothic`** toponym dataset and its `manifest.json` entry.

---

## [0.2.0] — 2026-05-27

### Added
- Compiled toponym namesets for **Basque** and **Catalan**: `_cleared`,
  `_beginnings`, `_endings`, `_separate_beginnings`, `_separate_endings` files
  added alongside the existing raw CSVs. Both languages are now fully usable
  with `PlaceNameGenerator`.
- `manifest.json` updated with all new files for Basque and Catalan.

### Removed
- **`PseudoOldFinnic`** personal-name dataset (`pseudo_old_finnic_f.csv`,
  `pseudo_old_finnic_m.csv`) and its `manifest.json` entry.

---

## [0.1.1] — 2026-05-26

### Added
- Compiled toponym namesets for **French**, **Italian**, and **Spanish**:
  `_cleared`, `_beginnings`, `_endings`, `_separate_beginnings`,
  `_separate_endings` files added. All three languages are now fully usable
  with `PlaceNameGenerator`.
- `manifest.json` updated accordingly.

---

## [0.1.0] — 2026-05-25

Initial release.

- Personal name corpora for ~45 languages (given names, surnames, patronymics
  where available).
- Ethnonym corpora for Baltic, Celtic, Germanic, and Slavic families.
- Toponym namesets for 28 languages (raw CSVs; compiled files for most).
- `manifest.json` listing all CSV paths, used by the download-on-demand manager
  when `onomaturgy-data` is not installed locally.
