"""
Problem 2b

input: List of points in the plane.
output: List containing the two closest points.

TODO: implement your solution in Theta(n log n).
"""

import math


def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def closest_pair(points):
    pass
