"""
Problem 5

input: List of tuples representing the friends' apartments.
output: List of apartment pairs.

TODO: implement your solution.
"""

import math
from heapq import heapify, heappop, heappush
from collections import Counter


def cookies_distrubution_map(apartments) -> list:
    
    n = len(apartments)
    starting_point = ((n + 1) / 2)
    
    print("starting point: ", starting_point)
    
    visited_apts = [(int(starting_point), int(starting_point))]
    
    result = []
    
    while ((len(visited_apts) - 1) < len(apartments)):
        min_distance = math.inf
        min_distance_apt = None
        min_distance_start = None
        
        for current_apt in visited_apts:
            # TODO need to make every apt check each new apt, currently it jumps to next one
            
            for next_stop in apartments:
                if(current_apt is not next_stop and next_stop not in visited_apts):
                    
                    cal_d = calculate_distance(current_apt, next_stop)
                    
                    if(cal_d < min_distance):
                        min_distance = cal_d 
                        
                        min_distance_apt = next_stop
                        min_distance_start = current_apt
            
        if(min_distance_apt is not None):
            visited_apts.append(min_distance_apt)
        
            result.append((min_distance_start, min_distance_apt))
    
    return result

def calculate_distance(aptA, aptB):
    a,b = aptA
    i,j = aptB
    
    return abs(a-i) + abs(b-j)

# print("result: ", cookies_distrubution_map([(2,3), (2,4), (5,5)]))
print("result: ", cookies_distrubution_map([(1,2), (3,2), (2,4), (2,6)]))