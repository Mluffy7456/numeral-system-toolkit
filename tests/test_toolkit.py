import unittest

from converter import convert_number, to_decimal
from number_utils import from_decimal
from validator import validate_number_for_base
from bitwise import rotate_left, rotate_right
from truth_tables import OPERATIONS
from representations import group_bits

class ToolkitTests(unittest.TestCase):
    def test_conversion(self):
        self.assertEqual(convert_number("FF", 16, 2), "11111111")
        self.assertEqual(convert_number("-10", 10, 16), "-A")

    def test_round_trip(self):
        for base in range(2, 37):
            value = 123456
            encoded = from_decimal(value, base)
            self.assertEqual(to_decimal(encoded, base), value)

    def test_validation_rejects_symbol(self):
        with self.assertRaises(ValueError):
            validate_number_for_base("102", 2)

    def test_rotations(self):
        self.assertEqual(rotate_left(0b10000001, 1, 8), 0b00000011)
        self.assertEqual(rotate_right(0b10000001, 1, 8), 0b11000000)

    def test_truth_table_and(self):
        fn = OPERATIONS["1"][1]
        self.assertEqual([int(fn(a,b)) for a,b in [(0,0),(0,1),(1,0),(1,1)]], [0,0,0,1])

    def test_truth_table_xnor(self):
        fn = OPERATIONS["6"][1]
        self.assertEqual([int(fn(a,b)) for a,b in [(0,0),(0,1),(1,0),(1,1)]], [1,0,0,1])

    def test_group_bits(self):
        self.assertEqual(group_bits("10101010", 4), "1010 1010")

if __name__ == "__main__":
    unittest.main()
