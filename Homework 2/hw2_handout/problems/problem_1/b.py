"""
Problem 1b

input: Tree represented by values and adjacency dictionaries.
output: Maximum sum of non-adjacent tree nodes.

TODO: implement your solution.
"""


from ast import Set


def maxsum_tree(vertices, adjacency) -> int:
    # need to find the root
    
    node_childs = set()
    
    for v in vertices.keys():
        for child in adjacency.get(v, []):
            print("child: ", child)
            
            node_childs.add(child)
        
    ver = set(vertices.keys())
    
    root = list(ver - node_childs)
    
    print("root is: ", root)
    
    memo = []       
    
    pass

def recursive_helper(root):
    
    pass