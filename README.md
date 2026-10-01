# 🔢 Numeral System Toolkit

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Version](https://img.shields.io/badge/version-2.0.0-success)
![License](https://img.shields.io/badge/license-MIT-green)

A modular Python toolkit for numeral-system conversion, arithmetic, bitwise operations, digital logic, binary encodings, and low-level data representation.

## ✨ Features

- 🔄 Number conversion between bases **2–36**
- 🧮 Arithmetic calculator in arbitrary bases
- ⚙️ Bitwise operations with configurable 8/16/32/64-bit width
- 📊 Binary/Octal/Decimal/Hexadecimal representations
- 🧠 Truth tables: AND, OR, XOR, NAND, NOR, XNOR
- 🔬 Configurable bit representation and bit grouping
- IEEE 754 binary32/binary64 converter
- ASCII encoder/decoder
- UTF-8 hexadecimal encoder/decoder
- Two's complement encoder/decoder
- Gray Code encoder/decoder
- 📜 Persistent JSON history
- 🌍 English/Russian localization
- 🖥️ Optional Tkinter GUI

## 🚀 Installation

```bash
git clone https://github.com/Mluffy7456/numeral-system-toolkit.git
cd numeral-system-toolkit
pip install -r requirements.txt
python main.py
```

For the GUI, run:

```bash
python gui.py
```

> Tkinter is part of the standard Python distribution on most desktop installations. On Linux, install your distribution's Tk package if it is missing.

## 📦 v2.0.0

### IEEE 754
Supports:
- binary32 / float32
- binary64 / float64
- decimal float → sign/exponent/fraction/binary/hex
- binary or hexadecimal IEEE 754 → Python float

### ASCII
Bidirectional conversion between ASCII text and decimal character codes.

### UTF-8
Bidirectional conversion between Unicode text and UTF-8 byte sequences represented as hexadecimal.

### Two's Complement
Encode signed integers into a selected bit width and decode binary two's-complement values.

### Gray Code
Encode non-negative integers into Gray code and decode Gray code back to integers.

### GUI
A lightweight Tkinter interface provides a base converter and common encoding tools without adding a GUI dependency.

## 📂 Project Structure

```text
├── main.py
├── gui.py
├── converter.py
├── calculator.py
├── bitwise.py
├── truth_tables.py
├── bit_representation.py
├── bit_grouping.py
├── ieee754.py
├── ascii_converter.py
├── utf8_converter.py
├── twos_complement.py
├── gray_code.py
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
├── tests/
└── locales/
    ├── en.json
    └── ru.json
```

## 📅 Roadmap

### ✅ v1.0.0
Core converter, calculator, bitwise operations, history, validation.

### ✅ v1.1.0
Rich CLI, number representations, shifts and rotations.

### ✅ v1.2.0
English/Russian localization and settings.

### ✅ v1.3.0
Truth Tables, Bit Representation, Bit Grouping.

### ✅ v2.0.0
IEEE 754, ASCII, UTF-8, Two's Complement, Gray Code, GUI Version.

## 🧪 Tests

Run:

```bash
python -m unittest discover -s tests -v
```

## 🛠 Technologies

Python 3 · Rich · Tkinter · JSON · unittest

## 📄 License

MIT
