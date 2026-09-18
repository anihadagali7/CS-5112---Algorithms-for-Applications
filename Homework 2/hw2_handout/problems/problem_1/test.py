import sys
from pathlib import Path as _PublicTestPath

_PUBLIC_TEST_PROBLEMS_DIR = _PublicTestPath(__file__).resolve().parent.parent
if str(_PUBLIC_TEST_PROBLEMS_DIR) not in sys.path:
    sys.path.insert(0, str(_PUBLIC_TEST_PROBLEMS_DIR))
import unittest
from pathlib import Path
from problem_1.a import maxsum_list
from problem_1.b import maxsum_tree

INPUT_DIR = Path(__file__).parent / "input"


class Test(unittest.TestCase):

    def test_correctness_public_a1(self):
        """Public test for n = 2"""
        self.assertEqual(maxsum_list([1, 2]), 2)

    def test_correctness_public_a2(self):
        """Public test #1 for n = 3"""
        self.assertEqual(maxsum_list([1, 2, 3]), 4)

    def test_correctness_public_a3(self):
        """Public test #1 for n = 4"""
        self.assertEqual(maxsum_list([1, 2, 6, 4]), 7)

    def test_correctness_public_a4(self):
        """Public test #2 for n = 4"""
        self.assertEqual(maxsum_list([10, 1, 1, 10]), 20)

    def test_correctness_public_a5(self):
        """Public test for n = 5"""
        self.assertEqual(maxsum_list([10, 1, 1, 1, 10]), 21)

    def test_correctness_public_b1(self):
        """Public path-shaped tree test"""
        self.assertEqual(
            maxsum_tree({0: 1, 1: 2, 2: 3, 3: 4}, {0: [1], 1: [2], 2: [3], 3: []}), 6
        )

    def test_correctness_public_b2(self):
        """Public branching tree test"""
        self.assertEqual(
            maxsum_tree({0: 1, 1: 2, 2: 3, 3: 4}, {0: [1, 2], 1: [3], 2: [], 3: []}), 7
        )


if __name__ == "__main__":
    unittest.main()
