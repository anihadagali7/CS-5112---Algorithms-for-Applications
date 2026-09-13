"""
Problem 2

input: Integer M and a list of intervals [a, b].
output: List of list of integers composing the covering.

TODO: implement a correct greedy algorithm from the homework.
"""
import copy
import math

    # brute force
    # 'remove' the current interval from the list
    # get the union of rest of list
    # compare if current interval is redundant. if [a, b] and [c, d] (union), then if c<= a and d>=b
    # add it to the redundant list
    # add it back into the interval list for next comparison

    # now to remove the earliest finish time, go through the redundant list, and find the index of the interval that has the minimum b in [a,b]
    # remove it from intervals permanently 

    # start the whole process over
    
    # sorting version:
    # sort the intervals based on the start, if there are ties, then sort by finish time too
    #look at current interval, if the interval is overlapping the next interval, then it is redundant, and add it to redundant list
    # J = I

    # while there is a redundant interval:
    #     find all redundant intervals
    #     choose the redundant interval with smallest finish time
    #     remove it from J

    # return J

def interval_covering(M: int, intervals: list) -> list:
    answer = copy.deepcopy(intervals)
    remove_intervals = []
    
    redundant_list = []
    
    while True:
        for index, interval  in enumerate(intervals):
            temp = interval
            
            answer.pop(index)
            
            union = get_union(answer, M)
            
            a, b = interval
            
            if(union[a] == 1 and union[b] == 1):
                # redundant
                redundant_list.append(interval)
            
            answer.insert(index, temp)
                
        if((len(redundant_list) > 1)):
            break
        
    earliest_finish = remove_earliest_finish(redundant_list, M)
    
    if(earliest_finish in answer):
        answer.remove(earliest_finish)
    redundant_list = []
    
    ## need to loop back through the whole process again
    return answer

def remove_earliest_finish(redundant_list: list, M: int):
    min_interval = M
    interval_to_remove = None
    for slot in redundant_list:
        start, end = slot
        
        if(min_interval > end):
            min_interval = min(end, min_interval)
            interval_to_remove = slot
    
    return interval_to_remove

def get_union(intervals: list, M: int) -> list:
    coverage = [0] * (M + 1)
    
    for slot in intervals:
        start, end = slot
        
        coverage[start:(end+1)] = [1] * (end+1 - start)
    
    
    return coverage


print(f"interval: ", interval_covering(3, [[0, 1], [2, 3], [1, 2], [0, 2]]))