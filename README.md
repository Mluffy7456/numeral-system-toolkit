# 🔢 Numeral System Toolkit

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Version](https://img.shields.io/badge/version-1.3.0-success)
![License](https://img.shields.io/badge/license-MIT-green)

A modular Python CLI toolkit for numeral-system conversion, arithmetic, bitwise operations, digital logic, and low-level bit inspection.

## ✨ Features

### 🔄 Number Converter
Convert signed integers between bases **2–36** with validation and automatic Binary/Octal/Decimal/Hexadecimal representations.

### 🧮 Calculator
Perform arithmetic in bases **2–36**: `+`, `-`, `*`, integer `/`, `%`.

### ⚙️ Bitwise Operations
AND, OR, XOR, NAND, NOR, NOT, shift left/right, rotate left/right with **8/16/32/64-bit** widths.

### 📊 Number Representations
Display results in Binary, Octal, Decimal, and Hexadecimal. Binary output can be grouped for readability.

### 🧠 v1.3 Features
- Truth tables for AND, OR, XOR, NAND, NOR, XNOR
- Bit-by-bit representation with configurable width
- Configurable binary bit grouping

### 📜 History
JSON-based operation history with a Rich table view and clear-history action.

### 🌍 Localization
English and Russian UI with persistent language settings.

## 🚀 Installation

```bash
git clone https://github.com/Mluffy7456/numeral-system-toolkit.git
cd numeral-system-toolkit
pip install -r requirements.txt
python main.py
```

## 📂 Project Structure

```text
├── main.py
├── converter.py
├── calculator.py
├── bitwise.py
├── truth_tables.py
├── bit_representation.py
├── bit_grouping.py
├── representations.py
├── history.py
├── validator.py
├── number_utils.py
├── language.py
├── settings.py
├── settings_menu.py
├── rich_utils.py
├── utils.py
├── config.py
└── locales/
    ├── en.json
    └── ru.json
```

## 📅 Roadmap

### ✅ v1.0.0
Number Converter · Calculator · Bitwise Operations · JSON History · Validation · Modular architecture

### ✅ v1.1.0
Rich CLI · Number representations · Shift and rotate operations

### ✅ v1.2.0
English/Russian localization · Settings and language persistence

### ✅ v1.3.0
Truth Tables · Bit Representation · Bit Grouping

### 🔮 v2.0.0
- IEEE 754 Converter
- ASCII Converter
- UTF-8 Converter
- Two's Complement
- Gray Code
- GUI Version

## 🛠 Technologies
Python 3 · Rich · JSON

## 📄 License
MIT
