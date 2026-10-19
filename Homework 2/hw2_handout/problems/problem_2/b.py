"""
Problem 2b

input: List of points in the plane.
output: List containing the two closest points.

TODO: implement your solution in Theta(n log n).
"""

import math


def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def recursive_helper(points, points_y):
    closest_pair = {}
    if(len(points) <= 3):
            # find the closest between all 3 
            if (len(points) == 2):
                min_distance = distance(points[0], points[1])
                min_pair = [points[0], points[1]]
                
                closest_pair['min_distance'] = min_distance
                closest_pair['min_pair'] = min_pair
                
                return closest_pair
            else:
                min_distance1 = distance(points[0], points[1])
                min_distance2 = distance(points[0], points[2])
                min_distance3 = distance(points[1], points[2])
                min_pair1 = [points[0], points[1]]
                min_pair2 = [points[0], points[2]]
                min_pair3 = [points[1], points[2]]
                
                min_distance = min(min_distance1, min_distance2, min_distance3)
                min_pair = min_pair1 if min_distance == min_distance1 else min_pair2 if min_distance == min_distance2 else min_pair3
                
                closest_pair['min_distance'] = min_distance
                closest_pair['min_pair'] = min_pair
                
                return closest_pair
            
            
    n = len(points)
    middle_index = int(n / 2)
    
    middle_x = points[middle_index][0]
    
    left_points = points[:middle_index]
    right_points = points[middle_index:]

    # points_y is already sorted by y
    # split it to match the x-halves in O(n)
    left_ids = {id(p) for p in left_points}
    left_y = []
    right_y = []
    for p in points_y:
        if id(p) in left_ids:
            left_y.append(p)
        else:
            right_y.append(p)
    
    split_left = recursive_helper(left_points, left_y)
    split_right = recursive_helper(right_points, right_y)
    
    obj = min(split_left, split_right, key=lambda x: x['min_distance'])
    delta = obj['min_distance']
    
    strip = []
    
    for p in points_y:
        x, y = p
        
        if (delta >= abs(x - middle_x)):
            strip.append(p)
    
    for index, s in enumerate(strip):
        for j in range(index + 1, min(index + 11, len(strip))):
            delta = min(delta, distance(s, strip[j]))
            if (delta < obj['min_distance']):
                obj['min_distance'] = delta
                obj['min_pair'] = [s, strip[j]]
            
    return obj


def closest_pair(points):
    # sort by x coordinate
    # find the median 
    points.sort(key=lambda item: item[0])
    points_y = sorted(points, key=lambda item: item[1])
    
    obj = recursive_helper(points, points_y)
    return obj['min_pair']    
