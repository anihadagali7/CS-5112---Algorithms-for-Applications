import sys
from pathlib import Path as _PublicTestPath

_PUBLIC_TEST_PROBLEMS_DIR = _PublicTestPath(__file__).resolve().parent.parent
if str(_PUBLIC_TEST_PROBLEMS_DIR) not in sys.path:
    sys.path.insert(0, str(_PUBLIC_TEST_PROBLEMS_DIR))
import unittest
from problem_5.p5 import cookies_distrubution_map
import copy


class Test(unittest.TestCase):

    def check_solution(self, inputs, route, optimal_distance):
        self.assertEqual(len(inputs), len(route))
        for apt in inputs:
            cookies_delivered = False
            for walk in route:
                if walk[1] == apt:
                    cookies_delivered = True
            self.assertTrue(cookies_delivered)
        steps = 0
        for walk in route:
            steps += abs(walk[0][0] - walk[1][0]) + abs(walk[0][1] - walk[1][1])
        self.assertEqual(optimal_distance, steps)

    def test_correctness_public_n2_split(self):
        """Public test #1 n = 2"""
        inputs = [(1, 2), (2, 1)]
        route = cookies_distrubution_map(copy.deepcopy(inputs))
        self.check_solution(inputs, route, optimal_distance=2)

    def test_correctness_public_n2_sequential(self):
        """Public test #2 n = 2"""
        inputs = [(1, 2), (1, 5)]
        route = cookies_distrubution_map(copy.deepcopy(inputs))
        self.check_solution(inputs, route, optimal_distance=4)

    def test_correctness_public_n3_tie(self):
        """Public test n = 3"""
        inputs = [(1, 1), (1, 2), (2, 1)]
        route = cookies_distrubution_map(copy.deepcopy(inputs))
        self.check_solution(inputs, route, optimal_distance=3)

    def test_correctness_public_n4_sequential(self):
        """Public test #1 n = 4"""
        inputs = [(1, 1), (3, 3), (4, 4), (5, 5)]
        route = cookies_distrubution_map(copy.deepcopy(inputs))
        self.check_solution(inputs, route, optimal_distance=8)

    def test_correctness_public_n4_split(self):
        """Public test #2 n = 4"""
        inputs = [(1, 5), (2, 5), (1, 7), (6, 1)]
        route = cookies_distrubution_map(copy.deepcopy(inputs))
        self.check_solution(inputs, route, optimal_distance=11)

    def test_correctess_public_n6(self):
        """Public test n = 6"""
        inputs = [(1, 4), (5, 1), (5, 5), (5, 4), (3, 2), (6, 4)]
        route = cookies_distrubution_map(copy.deepcopy(inputs))
        self.check_solution(inputs, route, optimal_distance=12)


if __name__ == "__main__":
    unittest.main()
