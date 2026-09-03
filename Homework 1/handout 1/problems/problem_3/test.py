import sys
from pathlib import Path as _PublicTestPath

_PUBLIC_TEST_PROBLEMS_DIR = _PublicTestPath(__file__).resolve().parent.parent
if str(_PUBLIC_TEST_PROBLEMS_DIR) not in sys.path:
    sys.path.insert(0, str(_PUBLIC_TEST_PROBLEMS_DIR))
import unittest
from problem_3.a import run_length_encode
from problem_3.b import huffman_compress


class Test(unittest.TestCase):

    def _is_prefix_code(self, codes):
        sorted_codes = sorted(codes.values())
        for i in range(len(sorted_codes) - 1):
            if sorted_codes[i + 1].startswith(sorted_codes[i]):
                return False
        return True

    def test_public_rle_basic(self):
        block = [52, -7, 0, 0, 3, 0, -2] + [0] * 57
        expected = [(0, 52), (0, -7), (2, 3), (1, -2), ("EOB",)]
        self.assertEqual(run_length_encode(block), expected)

    def test_public_huffman_basic(self):
        symbols = ["A", "A", "B", "C", "A", "A", "B"]
        codes, stream = huffman_compress(symbols)
        self.assertEqual(set(codes.keys()), set(symbols))
        self.assertTrue(self._is_prefix_code(codes))
        self.assertTrue(len(codes["A"]) <= len(codes["B"]))
        self.assertTrue(len(codes["B"]) <= len(codes["C"]))
        self.assertEqual(stream, "".join((codes[s] for s in symbols)))

    def test_public_huffman_with_rle(self):
        rle_symbols = [(0, 10), (2, -5), (0, 10), ("EOB",), (0, 10), (2, -5)]
        codes, stream = huffman_compress(rle_symbols)
        self.assertEqual(set(codes.keys()), set(rle_symbols))
        self.assertTrue(self._is_prefix_code(codes))
        self.assertTrue(len(codes[0, 10]) <= len(codes[2, -5]))
        self.assertTrue(len(codes[2, -5]) == len(codes["EOB",]))
        self.assertEqual(stream, "".join((codes[s] for s in rle_symbols)))


if __name__ == "__main__":
    unittest.main()
