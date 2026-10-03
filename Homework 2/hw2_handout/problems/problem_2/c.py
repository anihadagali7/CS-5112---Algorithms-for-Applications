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
    
    delta = distance(points[0], points[1])
    
    min_distance = delta
    min_pair = [points[0], points[1]]
    
    grid_map = build_grid(points, delta)
    
    for p in points[1:]:
        cell = compute_cell(p, delta / 2)
        
        # now we know where the new point belongs on grid
        # we need to check surrounding squares
        
        a, b = cell
        
        for x in range(a - 2, a + 2):
            for y in range(b - 2, b + 2):
                if(grid_map[(x, y)]):
                    
                    # list of points in that cell, or is it only one point ?
                    list_p = grid_map[(x, y)]
                    
                    for cell_p in list_p:
                        current_distance = distance(p, cell_p)
                        
                        if current_distance < delta:
                            # rebuild the map
                            delta = current_distance
                            
                            # i know this is wrong, but i need to figure out what this function takes in as params
                            build_grid(points[:i], delta)
                        else:
                            # either append to list, or just set value, based on earlier question
                            grid_map[cell] = grid_map[cell].append(p)
                        
    pass
    
def build_grid(point1, point2, delta):
    subsquare_len = delta / 2
    
    grid = {}
    
    grid[compute_cell(point1, subsquare_len)] = point1
    grid[compute_cell(point2, subsquare_len)] = point2
    
def compute_cell(point, subsquare_len):
    x, y = point
    
    cell_x = math.floor(x / subsquare_len) 
    cell_y = math.floor(y / subsquare_len)

    return (cell_x, cell_y)
