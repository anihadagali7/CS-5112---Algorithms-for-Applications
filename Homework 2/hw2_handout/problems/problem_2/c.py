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
    random.shuffle(points)
    
    min_distance = distance(points[0], points[1])
    
    if min_distance == 0:
        return [points[0], points[1]]
    
    min_pair = [points[0], points[1]]
    
    grid_map = build_grid(points[:2], min_distance)
    
    for index, new_point in enumerate(points[2:], start=2):
        cell = compute_cell(new_point, min_distance / 2)
        
        local_min = min_distance
        local_pair = []
        
        a, b = cell
        
        for x in range(a - 2, a + 3):
            for y in range(b - 2, b + 3):
                if((x,y) in grid_map):
                    
                    existing_point = grid_map[(x, y)]
                    
                    current_distance = distance(new_point, existing_point)
                    
                    if current_distance < local_min:
                        # rebuild the map
                        local_min = current_distance
                        local_pair = [new_point, existing_point]
        
        if(local_min < min_distance):    
            min_distance = local_min
            
            if min_distance == 0:
                return local_pair
            min_pair = local_pair
            grid_map = build_grid(points[0:index + 1], min_distance)
        else:
            grid_map[cell] = new_point
                        
    return min_pair
    
def build_grid(points, delta):
    subsquare_len = delta / 2
    
    grid = {}
    
    for p in points:
        grid[compute_cell(p, subsquare_len)] = p
    
    return grid
    
def compute_cell(point, subsquare_len):
    x, y = (point)
    
    cell_x = math.floor(x / subsquare_len) 
    cell_y = math.floor(y / subsquare_len)

    return (cell_x, cell_y)