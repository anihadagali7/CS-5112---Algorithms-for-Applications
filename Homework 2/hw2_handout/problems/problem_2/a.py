"""
Problem 2a

input: List of points in the plane.
output: List containing the two closest points.

TODO: implement your solution in Theta(n^2).
"""

import math


def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def closest_pair(points):
    pair = []
    min_distance = math.inf
    
    for indexi, i in enumerate(points):
        for indexj, j in enumerate(points[indexi+1:], start=indexi+1):
            
            point1 = i
            point2 = j
            
            dist = distance(point2, point1)
            if(min_distance > dist):
                pair = []
                min_distance = dist
                pair.append(point1)
                pair.append(point2)
    
    return pair
