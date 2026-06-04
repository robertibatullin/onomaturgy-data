# Changelog

All notable changes to the **onomaturgy-data** package are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.2.4] — 2026-05-31

### Added
- **Ethiopian** personal name corpus (`names/Ethiopian/`): `ethiopian_f.csv`,
  `ethiopian_m.csv`, `ethiopian_s.csv`.
- `manifest.json` updated with all new files.

---

## [0.2.3] — 2026-05-27

### Added
- **English/American** personal name corpus (`american_f.csv`, `american_m.csv`,
  `american_s.csv`) added to the existing `names/English/` directory.
- **Indonesian** personal name corpus (`names/Indonesian/`): given names and
  surnames for both genders.
- **Japanese** personal name corpus (`names/Japanese/`): given names and
  surnames for both genders.
- **Korean** personal name corpus (`names/Korean/`): South Korean given names
  and surnames for both genders.
- `manifest.json` updated with all new files.

---

## [0.2.2] — 2026-05-27

### Added
- **Arabic/Algerian** personal name corpus (`algerian_f.csv`, `algerian_m.csv`,
  `algerian_s.csv`) added to the existing `names/Arabic/` directory.
- **Cameroonian** personal name corpus (`names/Cameroonian/`): given names and
  surnames for both genders.
- **Chinese** personal name corpus (`names/Chinese/`): given names and surnames
  for both genders.
- **Israeli** personal name corpus (`names/Israeli/`): given names and surnames
  for both genders.
- `manifest.json` updated with all new files.

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
