"""
Problem 1b

input: Tree represented by values and adjacency dictionaries.
output: Maximum sum of non-adjacent tree nodes.

TODO: implement your solution.
"""


def maxsum_tree(vertices, adjacency) -> int:
    # need to find the root
    node_childs = set()

    for v in vertices.keys():
        for child in adjacency.get(v, []):
            node_childs.add(child)

    ver = set(vertices.keys())

    roots = list(ver - node_childs)

    memo = {}

    total = 0
    for root in roots:
        total += recursive_helper(vertices, adjacency, root, memo)

    return total

def recursive_helper(vertices, adjacency, v, memo):
    if(memo.get(v) != None):
        return memo[v]

    children = adjacency.get(v, [])

    # base case
    if(len(children) == 0):
        return max(vertices[v], 0)

    pick = vertices[v]
    for child in children:
        for grandchild in adjacency.get(child, []):
            pick += recursive_helper(vertices, adjacency, grandchild, memo)

    notPick = 0
    for child in children:
        notPick += recursive_helper(vertices, adjacency, child, memo)

    memo[v] = max(pick, notPick)

    return memo[v]
