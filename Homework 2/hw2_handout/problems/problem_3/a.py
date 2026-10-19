"""
Sorted linked-list baseline for skip lists.

TODO: implement insertion and search.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    val: int
    next: "Node | None" = None


class LinkedList:
    def __init__(self):
        self.root = None

    def insert(self, x: int) -> None:
        
        node = self.root
        
        # sorted linked list
        # new val needs to be greater than current val AND less than next node
        
        pointer = node
        
        # if list is empty
        if(node is None):
            newNode = Node(x)
            
            self.root = newNode
            
            return
            
        # if x is less than root
        if(x <= node.val):
            newNode = Node(x)
            
            self.root = newNode
            
            newNode.next = node
            
            return
        
        
        while(pointer is not None):
            if(pointer.val <= x and pointer.next is not None and pointer.next.val >= x):
                temp = pointer.next
                
                newNode = Node(x)
                newNode.next = temp
                
                pointer.next = newNode
                
                return
            elif (pointer.next is None and x > pointer.val):
                newNode = Node(x)
                pointer.next = newNode
                
                newNode.next = None
                
                return
            
            pointer = pointer.next         
        pass
      

    def search(self, x: int) -> Node | None:
        
        # search for int value in linked list
        # we need the node
        
        node = self.root
        
        if node is None:
            return
        
        pointer = node
        
        while pointer is not None:
            if(pointer.val == x):
                return pointer
            else:
                pointer = pointer.next
        
        pass
