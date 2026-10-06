"""
Problem 1b

input: Tree represented by values and adjacency dictionaries.
output: Maximum sum of non-adjacent tree nodes.

TODO: implement your solution.
"""

import sys

sys.setrecursionlimit(1000000)

def maxsum_tree(vertices, adjacency) -> int:
    # normalize every id to a string before using it
    vertices = {str(v): val for v, val in vertices.items()}
    adjacency = {str(v): [str(c) for c in children] for v, children in adjacency.items()}

    # treat every edge as going both ways
    neighbors = {}
    for v in vertices:
        neighbors[v] = []

    for v in adjacency:
        for child in adjacency[v]:
            if v not in neighbors:
                neighbors[v] = []
            if child not in neighbors:
                neighbors[child] = []
            neighbors[v].append(child)
            neighbors[child].append(v)

    visited = set()
    total = 0

    # the input could be a forest, so start a search from every unvisited node
    for v in neighbors:
        if v not in visited:
            pick, notPick = recursive_helper(vertices, neighbors, v, visited)
            total += max(pick, notPick)

    return total


def recursive_helper(vertices, neighbors, v, visited):
    visited.add(v)

    pick = vertices.get(v, 0)
    notPick = 0

    for n in neighbors[v]:
        if n in visited:
            continue

        childPick, childNotPick = recursive_helper(vertices, neighbors, n, visited)

        # if v is picked, its children can't be
        pick += childNotPick

        # if v is not picked, each child can go either way
        notPick += max(childPick, childNotPick)
        
    # returns (best sum if v is picked, best sum if v is not picked)
    return pick, notPick
