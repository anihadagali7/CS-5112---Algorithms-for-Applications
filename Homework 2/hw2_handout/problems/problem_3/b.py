"""
Problem 3b-d

Skip-list implementation.

TODO: implement insertion and search.
"""

from __future__ import annotations

import random


class Node:
    def __init__(self, val: int | None, level: int):
        self.val = val
        self.next = [None] * level
        self.level = level


class SkipList:
    def __init__(self, max_level: int, p: float):
        self.max_level = max_level
        self.p = p
        self.sentinel = Node(None, self.max_level)
        self.root = None

    def insert(self, x: int) -> None:
        level_to_insert = self.random_level()
        
        # add at level 0
        node = self.sentinel
        
        pointer = node
        
        if pointer is None:
            newNode = Node(x, 0)
            
            pointer.next[0] = newNode
            
        while(pointer is not None):
            if(pointer.val <= x and pointer.next[0] is not None and pointer.next[0].val >= x):
                temp = pointer.next[0]
                
                newNode = Node(x, 0)
                newNode.next[0] = temp
                
                pointer.next[0] = newNode
                
                return
            elif (pointer.next[0] is None and x > pointer.val):
                newNode = Node(x, 0)
                pointer.next[0] = newNode
                
                newNode.next[0] = None
                
                return
            
            pointer = pointer.next[0]
            
        
        # add node at random level
        
        for i in range(self.max_level, 1):
            if(i == level_to_insert):
                node = self.sentinel
        
                pointer = node
                
                if pointer is None:
                    newNode = Node(x, level_to_insert)
                    
                    pointer.next[level_to_insert] = newNode
                    
                while(pointer is not None):
                    if(pointer.val <= x and pointer.next[level_to_insert] is not None and pointer.next[level_to_insert].val >= x):
                        temp = pointer.next[level_to_insert]
                        
                        newNode = Node(x, level_to_insert)
                        newNode.next[level_to_insert] = temp
                        
                        pointer.next[level_to_insert] = newNode
                        
                        return
                    elif (pointer.next[level_to_insert] is None and x > pointer.val):
                        newNode = Node(x, level_to_insert)
                        pointer.next[level_to_insert] = newNode
                        
                        newNode.next[level_to_insert] = None
                        
                        return
                    
                    pointer = pointer.next[level_to_insert]
            
        pass

    def delete(self, x: int) -> None:
        pass

    def search(self, x: int) -> Node | None:
        
#         When search for k:
#           If k = key, done!
#           If k < next key, go down a level
#           If k ≥ next key, go right
        node = self.sentinel.next[self.max_level]
        
        if node is None:
            return
        
        pointer = node
        
        while pointer is not None:
            if pointer.val == x:
                return pointer
            elif x < pointer.next[self.max_level].val:
                pointer = pointer.next[self.max_level - 1]
            else:
                pointer = pointer.next[self.max_level]
                
        pass
    
    def random_level(self):
        heads_counter = 1
        
        while heads_counter < self.max_level:
            flip = random.random()

            if flip  < self.p:
                heads_counter += 1
            else:
                return heads_counter
            
        return heads_counter
