import sys
from pathlib import Path as _PublicTestPath

_PUBLIC_TEST_PROBLEMS_DIR = _PublicTestPath(__file__).resolve().parent.parent
if str(_PUBLIC_TEST_PROBLEMS_DIR) not in sys.path:
    sys.path.insert(0, str(_PUBLIC_TEST_PROBLEMS_DIR))
import unittest
from pathlib import Path
from problem_1 import b
from problem_1 import c

TEST_DIR = Path(__file__).resolve().parent
INPUT_DIR = TEST_DIR / "input"


class Test(unittest.TestCase):

    def setUp(self):
        self.a_good_format = None

    def test_public_formatting_input_a(self):
        """Check format of a_test.txt"""
        input_path = TEST_DIR / "a_test.txt"
        lines = [line.split() for line in input_path.read_text().splitlines()]
        lines = [line for line in lines if line]
        try:
            self.assertEqual(len(lines[0]), 1)
            n = int(lines[0][0])
            self.assertLess(n, 100)
            self.assertEqual(len(lines), 2 * n + 1)
            for preference in lines[1:]:
                self.assertEqual(len(preference), n)
                [int(value) for value in preference]
        except (AssertionError, IndexError, ValueError):
            self.fail(
                "a_test.txt is not well formatted. Please review the assignment for the expected input format"
            )
        print("a_test.txt is well formatted!")

    def test_correctness_public_b_n2(self):
        """Public test for n = 2"""
        pair = b.stable_matching(INPUT_DIR / "test_public_n2.txt")
        self.assertEqual(pair, {1: 1, 0: 0})

    def test_correctness_public_b_n3_1(self):
        """Public test #1 for n = 3"""
        pair = b.stable_matching(INPUT_DIR / "test_public_n3_1.txt")
        self.assertEqual(pair, {1: 1, 0: 0, 2: 2})

    def test_correctness_public_b_n3_2(self):
        """Public test #2 for n = 3"""
        pair = b.stable_matching(INPUT_DIR / "test_public_n3_2.txt")
        self.assertEqual(pair, {0: 0, 1: 2, 2: 1})

    def test_correctness_public_c_n2(self):
        """Public test for n = 2"""
        pair = c.stable_matching(INPUT_DIR / "test_public_n2.txt")
        self.assertEqual(pair, {1: 1, 0: 0})

    def test_correctness_public_c_n3_1(self):
        """Public test #1 for n = 3"""
        pair = c.stable_matching(INPUT_DIR / "test_public_n3_1.txt")
        self.assertEqual(pair, {1: 1, 0: 0, 2: 2})

    def test_correctness_public_c_n3_2(self):
        """Public test #2 for n = 3"""
        pair = c.stable_matching(INPUT_DIR / "test_public_n3_2.txt")
        self.assertEqual(pair, {0: 0, 1: 2, 2: 1})

    def test_public_formatting_input_d(self):
        """Check format of d_test.txt"""
        input_path = TEST_DIR / "d_test.txt"
        lines = [line.split() for line in input_path.read_text().splitlines()]
        lines = [line for line in lines if line]
        try:
            self.assertEqual(len(lines[0]), 1)
            n = int(lines[0][0])
            self.assertEqual(n, 3)
            self.assertEqual(len(lines), 2 * n + 1)
            for preference in lines[1:]:
                self.assertEqual(len(preference), n)
                self.assertEqual({int(value) for value in preference}, set(range(n)))
        except (AssertionError, IndexError, ValueError):
            self.fail(
                "d_test.txt is not well formatted. It must describe three students and three hospitals, with each preference row containing a permutation of 0, 1, and 2"
            )
        print("d_test.txt is well formatted!")


if __name__ == "__main__":
    unittest.main()
