import math
import unittest

from ascii_converter import text_to_ascii, ascii_to_text
from utf8_converter import text_to_utf8, utf8_to_text
from twos_complement import encode_twos, decode_twos
from gray_code import encode_gray, decode_gray
from ieee754 import encode_float, decode_float

class V2Tests(unittest.TestCase):
    def test_ascii_round_trip(self):
        self.assertEqual(text_to_ascii("ABC"), "65 66 67")
        self.assertEqual(ascii_to_text("65 66 67"), "ABC")

    def test_utf8_round_trip(self):
        text = "Привет 🌍"
        self.assertEqual(utf8_to_text(text_to_utf8(text)), text)

    def test_twos_complement(self):
        self.assertEqual(encode_twos(-1, 8), "11111111")
        self.assertEqual(encode_twos(-128, 8), "10000000")
        self.assertEqual(decode_twos("11111111"), -1)
        self.assertEqual(decode_twos("10000000"), -128)

    def test_gray_code(self):
        for value in range(256):
            self.assertEqual(decode_gray(encode_gray(value)), value)

    def test_ieee754_float32(self):
        sign, exponent, fraction, binary, hexadecimal = encode_float(1.0, 32)
        self.assertEqual(sign, "0")
        self.assertEqual(exponent, "01111111")
        self.assertEqual(fraction, "00000000000000000000000")
        self.assertEqual(decode_float(binary, 32), 1.0)
        self.assertEqual(hexadecimal, "3F800000")

if __name__ == "__main__":
    unittest.main()
