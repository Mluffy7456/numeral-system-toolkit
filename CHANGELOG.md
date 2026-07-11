# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog.

---

## [1.2.0] - 2026-07

### Added

- English localization
- Russian localization
- Localization system (`language.py`)
- Settings system (`settings.py`)
- Language persistence (`settings.json`)
- Translation files (`locales/en.json`, `locales/ru.json`)

### Changed

- Localized entire CLI interface
- Localized menus
- Localized prompts
- Localized validation messages
- Localized history table
- Localized number representations
- Improved project structure

### Improved

- More reliable path handling using `Path(__file__).resolve().parent`
- Cleaner localization architecture
- Better maintainability

---

## [1.1.0] - 2026-07

### Added

- Rich CLI interface
- Colored terminal output
- Rich tables
- Number representations
- Shift Left (`<<`)
- Shift Right (`>>`)
- Rotate Left (`ROTL`)
- Rotate Right (`ROTR`)

### Improved

- History view
- Error handling
- Result formatting

---

## [1.0.0] - 2026-07

### Initial Release

Features:

- Number Converter
- Calculator
- Bitwise Operations
- JSON History
- Validation
- Modular architecture