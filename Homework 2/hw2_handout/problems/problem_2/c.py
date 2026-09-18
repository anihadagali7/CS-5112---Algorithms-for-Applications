"""
Problem 2c

input: List of points in the plane.
output: List containing the two closest points.

TODO: implement your randomized-grid solution in expected Theta(n).
"""

import math
import random
from collections import defaultdict


def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def closest_pair(points):
    pass
