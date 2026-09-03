import sys
from pathlib import Path as _PublicTestPath

_PUBLIC_TEST_PROBLEMS_DIR = _PublicTestPath(__file__).resolve().parent.parent
if str(_PUBLIC_TEST_PROBLEMS_DIR) not in sys.path:
    sys.path.insert(0, str(_PUBLIC_TEST_PROBLEMS_DIR))
import unittest
from problem_2.e import interval_covering


class Test(unittest.TestCase):

    def test_cover_public_all(self):
        """Public test #1 for interval cover"""
        cover = interval_covering(4, [[2, 3], [3, 4], [0, 1], [1, 2]])
        self.assertEqual(
            set((tuple(pair) for pair in cover)), {(0, 1), (1, 2), (2, 3), (3, 4)}
        )

    def test_cover_public_size_1(self):
        """Public test #2 for interval cover"""
        cover = interval_covering(6, [[0, 2], [1, 6], [0, 6], [3, 5]])
        self.assertEqual(set((tuple(pair) for pair in cover)), {(0, 6)})

    def test_cover_public_size_2(self):
        """Public test #3 for interval cover"""
        cover = interval_covering(6, [[3, 6], [2, 4], [0, 3]])
        self.assertEqual(set((tuple(pair) for pair in cover)), {(3, 6), (0, 3)})

    def test_cover_public_size_3(self):
        """Public test #4 for interval cover"""
        cover = interval_covering(6, [[0, 2], [0, 1], [2, 3], [2, 4], [4, 6]])
        self.assertEqual(set((tuple(pair) for pair in cover)), {(4, 6), (0, 2), (2, 4)})

    def test_cover_public_size_4(self):
        """Public test #4 for interval cover"""
        cover = interval_covering(10, [[0, 5], [1, 6], [5, 10], [4, 9]])
        self.assertEqual(set((tuple(pair) for pair in cover)), {(0, 5), (5, 10)})


if __name__ == "__main__":
    unittest.main()
