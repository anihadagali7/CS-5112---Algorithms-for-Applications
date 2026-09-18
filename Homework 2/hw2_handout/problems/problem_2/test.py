import sys
from pathlib import Path as _PublicTestPath

_PUBLIC_TEST_PROBLEMS_DIR = _PublicTestPath(__file__).resolve().parent.parent
if str(_PUBLIC_TEST_PROBLEMS_DIR) not in sys.path:
    sys.path.insert(0, str(_PUBLIC_TEST_PROBLEMS_DIR))
import unittest
from problem_2.a import closest_pair as brute_force_closest_pair
from problem_2.b import closest_pair as divide_and_conquer_closest_pair
from problem_2.c import closest_pair as randomized_closest_pair


def as_point_set(points):
    return {tuple(point) for point in points}


INPUT_1 = [(0, 0), (1, 1), (5, 5)]
INPUT_2 = [[0.47, 0.53], [0.99, 0.54], [0.4, 0.57], [0.83, 0.19], [0.73, 0.1]]
INPUT_3 = [
    [0.8, 0.62],
    [0.48, 0.56],
    [0.62, 0.77],
    [0.39, 0.22],
    [0.97, 0.46],
    [0.34, 0.56],
    [0.92, 0.45],
    [0.7, 0.37],
    [0.13, 0.54],
    [0.27, 0.68],
    [0.31, 0.37],
    [0.56, 0.06],
    [0.58, 0.07],
    [0.54, 0.59],
    [0.29, 0.84],
    [0.01, 0.28],
    [0.01, 0.04],
    [0.55, 0.47],
    [0.66, 0.62],
    [0.24, 0.66],
    [0.4, 0.61],
    [0.55, 0.63],
    [0.7, 0.05],
    [0.45, 0.16],
    [0.03, 0.07],
    [0.38, 0.03],
    [0.45, 0.15],
    [0.35, 0.53],
    [0.72, 0.47],
    [0.72, 0.33],
    [0.67, 0.12],
    [0.12, 0.33],
    [0.12, 0.7],
    [0.46, 0.23],
    [0.17, 0.67],
    [0.49, 0.77],
    [0.65, 0.13],
    [0.17, 0.36],
    [0.69, 0.45],
    [0.06, 0.99],
    [0.95, 0.13],
    [0.52, 0.29],
    [0.06, 0.89],
    [0.39, 0.64],
    [0.54, 0.05],
    [0.6, 0.19],
    [0.43, 0.76],
    [0.12, 0.03],
    [0.05, 0.6],
    [0.44, 0.52],
]


class Test(unittest.TestCase):

    def test_public_small_a(self):
        points = [(0, 0), (3, 4), (4, 4)]
        self.assertEqual(
            as_point_set(brute_force_closest_pair(points)),
            as_point_set([(3, 4), (4, 4)]),
        )

    def test_public_medium_a(self):
        points = [(0.1, 0.2), (0.8, 0.9), (0.4, 0.5), (0.42, 0.51), (0.9, 0.1)]
        self.assertEqual(
            as_point_set(brute_force_closest_pair(points)),
            as_point_set([(0.4, 0.5), (0.42, 0.51)]),
        )

    def test_public_small_b(self):
        points = [(0, 0), (3, 4), (4, 4)]
        self.assertEqual(
            as_point_set(divide_and_conquer_closest_pair(points)),
            as_point_set([(3, 4), (4, 4)]),
        )

    def test_public_medium_b(self):
        points = [(0.1, 0.2), (0.8, 0.9), (0.4, 0.5), (0.42, 0.51), (0.9, 0.1)]
        self.assertEqual(
            as_point_set(divide_and_conquer_closest_pair(points)),
            as_point_set([(0.4, 0.5), (0.42, 0.51)]),
        )

    def test_public_small_c(self):
        points = [(0, 0), (3, 4), (4, 4)]
        self.assertEqual(
            as_point_set(randomized_closest_pair(points)),
            as_point_set([(3, 4), (4, 4)]),
        )

    def test_public_medium_c(self):
        points = [(0.1, 0.2), (0.8, 0.9), (0.4, 0.5), (0.42, 0.51), (0.9, 0.1)]
        self.assertEqual(
            as_point_set(randomized_closest_pair(points)),
            as_point_set([(0.4, 0.5), (0.42, 0.51)]),
        )


if __name__ == "__main__":
    unittest.main()
