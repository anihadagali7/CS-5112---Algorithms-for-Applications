import sys
from pathlib import Path as _PublicTestPath

_PUBLIC_TEST_PROBLEMS_DIR = _PublicTestPath(__file__).resolve().parent.parent
if str(_PUBLIC_TEST_PROBLEMS_DIR) not in sys.path:
    sys.path.insert(0, str(_PUBLIC_TEST_PROBLEMS_DIR))
import unittest
from problem_4.a import most_frequent_difference_a
from problem_4.b import most_frequent_difference_b
from problem_4.c import most_frequent_difference_c


class Test(unittest.TestCase):

    def test_correctness_a_public_n2_gt(self):
        """Public base test #1"""
        delta_freq = most_frequent_difference_a([8, 2], 6)
        self.assertEqual(1, delta_freq)

    def test_correctness_a_public_n2_eq(self):
        """Public base test #2"""
        delta_freq = most_frequent_difference_a([7, 7], 0)
        self.assertEqual(2, delta_freq)

    def test_correctness_a_public_n2_lt(self):
        """Public base test #3"""
        delta_freq = most_frequent_difference_a([3, 11], 8)
        self.assertEqual(1, delta_freq)

    def test_correctness_a_public_n4_1(self):
        """Public test #1 n = 4"""
        delta_freq = most_frequent_difference_a([5, 5, 5, 5], 0)
        self.assertEqual(12, delta_freq)

    def test_correctness_a_public_n4_2(self):
        """Public test #2 n = 4"""
        delta_freq = most_frequent_difference_a([-2, 33, 5, -2], 35)
        self.assertEqual(2, delta_freq)

    def test_correctness_a_public_n8_1(self):
        """Public test #1 n = 8"""
        delta_freq = most_frequent_difference_a([8, 7, 6, 5, 4, 3, 2, 1], 1)
        self.assertEqual(7, delta_freq)

    def test_correctness_a_public_n8_2(self):
        """Public test #2 n = 8"""
        delta_freq = most_frequent_difference_a([8, 7, 6, 5, 4, 3, 2, 1], -1)
        self.assertEqual(7, delta_freq)

    def test_correctness_a_public_n8_3(self):
        """Public test #3 n = 8"""
        delta_freq = most_frequent_difference_a([8, -7, 6, -5, 4, -3, 2, -1], 2)
        self.assertEqual(6, delta_freq)

    def test_correctness_a_public_n8_4(self):
        """Public test #4 n = 8"""
        delta_freq = most_frequent_difference_a([8, -7, 6, -5, 4, -3, 2, -1], -2)
        self.assertEqual(6, delta_freq)

    def test_correctness_b_public_n2_gt(self):
        """Public base test #1"""
        delta_freq = most_frequent_difference_b([8, 2], 6)
        self.assertEqual(1, delta_freq)

    def test_correctness_b_public_n2_eq(self):
        """Public base test #2"""
        delta_freq = most_frequent_difference_b([7, 7], 0)
        self.assertEqual(2, delta_freq)

    def test_correctness_b_public_n2_lt(self):
        """Public base test #3"""
        delta_freq = most_frequent_difference_b([3, 11], 8)
        self.assertEqual(1, delta_freq)

    def test_correctness_b_public_n4_1(self):
        """Public test #1 n = 4"""
        delta_freq = most_frequent_difference_b([5, 5, 5, 5], 0)
        self.assertEqual(12, delta_freq)

    def test_correctness_b_public_n4_2(self):
        """Public test #2 n = 4"""
        delta_freq = most_frequent_difference_b([-2, 33, 5, -2], 35)
        self.assertEqual(2, delta_freq)

    def test_correctness_b_public_n8_1(self):
        """Public test #1 n = 8"""
        delta_freq = most_frequent_difference_b([8, 7, 6, 5, 4, 3, 2, 1], 1)
        self.assertEqual(7, delta_freq)

    def test_correctness_b_public_n8_2(self):
        """Public test #2 n = 8"""
        delta_freq = most_frequent_difference_b([8, 7, 6, 5, 4, 3, 2, 1], -1)
        self.assertEqual(7, delta_freq)

    def test_correctness_b_public_n8_3(self):
        """Public test #3 n = 8"""
        delta_freq = most_frequent_difference_b([8, -7, 6, -5, 4, -3, 2, -1], 2)
        self.assertEqual(6, delta_freq)

    def test_correctness_b_public_n8_4(self):
        """Public test #4 n = 8"""
        delta_freq = most_frequent_difference_b([8, -7, 6, -5, 4, -3, 2, -1], -2)
        self.assertEqual(6, delta_freq)

    def test_correctness_c_public_n2_gt(self):
        """Public base test #1"""
        delta_freq = most_frequent_difference_c([8, 2], 6)
        self.assertEqual(1, delta_freq)

    def test_correctness_c_public_n2_eq(self):
        """Public base test #2"""
        delta_freq = most_frequent_difference_c([7, 7], 0)
        self.assertEqual(2, delta_freq)

    def test_correctness_c_public_n2_lt(self):
        """Public base test #3"""
        delta_freq = most_frequent_difference_c([3, 11], 8)
        self.assertEqual(1, delta_freq)

    def test_correctness_c_public_n4_1(self):
        """Public test #1 n = 4"""
        delta_freq = most_frequent_difference_c([5, 5, 5, 5], 0)
        self.assertEqual(12, delta_freq)

    def test_correctness_c_public_n4_2(self):
        """Public test #2 n = 4"""
        delta_freq = most_frequent_difference_c([-2, 33, 5, -2], 35)
        self.assertEqual(2, delta_freq)

    def test_correctness_c_public_n8_1(self):
        """Public test #1 n = 8"""
        delta_freq = most_frequent_difference_c([8, 7, 6, 5, 4, 3, 2, 1], 1)
        self.assertEqual(7, delta_freq)

    def test_correctness_c_public_n8_2(self):
        """Public test #2 n = 8"""
        delta_freq = most_frequent_difference_c([8, 7, 6, 5, 4, 3, 2, 1], -1)
        self.assertEqual(7, delta_freq)

    def test_correctness_c_public_n8_3(self):
        """Public test #3 n = 8"""
        delta_freq = most_frequent_difference_c([8, -7, 6, -5, 4, -3, 2, -1], 2)
        self.assertEqual(6, delta_freq)

    def test_correctness_c_public_n8_4(self):
        """Public test #4 n = 8"""
        delta_freq = most_frequent_difference_c([8, -7, 6, -5, 4, -3, 2, -1], -2)
        self.assertEqual(6, delta_freq)


if __name__ == "__main__":
    unittest.main()
