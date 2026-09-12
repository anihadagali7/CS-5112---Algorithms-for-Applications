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
    starting_apt = (int(starting_point), int(starting_point))
    visited_apts = [starting_apt]
    
    result = []
    heap = []
    hashmap = {}
    
    for apt in apartments:
        distance_to_starting_apt = calculate_distance(starting_apt, apt)
        
        heappush(heap, (distance_to_starting_apt, (starting_apt, apt)))
        hashmap[apt] = (distance_to_starting_apt, starting_apt)
    
    while(len(visited_apts) - 1 < len(apartments)):
        # find the closest 
        
        distance, object = heappop(heap)
        start, end = object
        
        if(end not in visited_apts):
            visited_apts.append(end)
            result.append((start, end))
        
            for current_apt in apartments:
                if(current_apt != end):
                    distance_to_starting_apt = calculate_distance(end, current_apt)
                    
                    old_shortest_path = hashmap[current_apt]
                    
                    old_distance, old_path = old_shortest_path
                    
                    if(old_distance > distance_to_starting_apt):
                        hashmap[current_apt] = (distance_to_starting_apt, (end))
                        heappush(heap, (distance_to_starting_apt, (end, current_apt)))
    
    return result

def calculate_distance(aptA, aptB):
    a,b = aptA
    i,j = aptB
    
    return abs(a-i) + abs(b-j)

# print("result: ", cookies_distrubution_map([(2,3), (2,4), (5,5)]))
# print("result: ", cookies_distrubution_map([(1,2), (3,2), (2,4), (2,6)]))
# print("result: ", cookies_distrubution_map([(1,1), (1,5), (1,6), (5,6)]))
# print("result: ", cookies_distrubution_map([(1,2), (2,1)]))
# print("result: ", cookies_distrubution_map([(1,1), (1,2), (1,3), (1,4)]))
# print("result: ", cookies_distrubution_map([(1,1), (1,5), (1,6), (5,6)]))
# print("result: ", cookies_distrubution_map([(1,3), (3,1), (3,5), (5,3)]))
# print("result: ", cookies_distrubution_map([(1,1), (1,10), (10,1), (10,10)]))
# print("result: ", cookies_distrubution_map([
#     (1,1),
#     (1,5),
#     (3,7),
#     (6,6),
#     (7,2)
# ]))
# print("result: ", cookies_distrubution_map([
#     (1,2),
#     (2,8),
#     (4,4),
#     (5,1),
#     (6,7),
#     (8,3)
# ]))