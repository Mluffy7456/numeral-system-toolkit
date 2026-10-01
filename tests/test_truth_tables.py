import unittest
from truth_tables import OPERATIONS

class TruthTableTests(unittest.TestCase):
    def test_and(self):
        fn = OPERATIONS["1"][1]
        self.assertEqual([int(fn(a,b)) for a,b in [(0,0),(0,1),(1,0),(1,1)]],[0,0,0,1])
    def test_xor(self):
        fn = OPERATIONS["3"][1]
        self.assertEqual([int(fn(a,b)) for a,b in [(0,0),(0,1),(1,0),(1,1)]],[0,1,1,0])
    def test_nand(self):
        fn = OPERATIONS["4"][1]
        self.assertEqual([int(fn(a,b)) for a,b in [(0,0),(0,1),(1,0),(1,1)]],[1,1,1,0])

if __name__ == "__main__": unittest.main()
