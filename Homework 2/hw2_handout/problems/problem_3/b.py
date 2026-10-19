"""
Problem 3b-d

Skip-list implementation.
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

    def find_predecessors(self, x: int) -> list[Node]:
        # predecessors[i] is the last node on level i whose value is less than x
        predecessors = [self.sentinel] * self.max_level
        current = self.sentinel

        for level in range(self.max_level - 1, -1, -1):
            # move right while the next node on this level is still smaller than x
            while current.next[level] is not None and current.next[level].val < x:
                current = current.next[level]
            predecessors[level] = current

        return predecessors

    def insert(self, x: int) -> None:
        predecessors = self.find_predecessors(x)

        # x is already in the list
        candidate = predecessors[0].next[0]
        if candidate is not None and candidate.val == x:
            return

        height = self.random_level()
        new_node = Node(x, height)

        # splice the new node in on each level it appears on
        for level in range(height):
            new_node.next[level] = predecessors[level].next[level]
            predecessors[level].next[level] = new_node

        self.root = self.sentinel.next[0]

    def delete(self, x: int) -> None:
        predecessors = self.find_predecessors(x)

        target = predecessors[0].next[0]
        if target is None or target.val != x:
            return

        # unlink the node from each level it appears on
        for level in range(target.level):
            predecessors[level].next[level] = target.next[level]

        self.root = self.sentinel.next[0]

    def search(self, x: int) -> Node | None:
        predecessors = self.find_predecessors(x)

        candidate = predecessors[0].next[0]
        if candidate is not None and candidate.val == x:
            return candidate
        return None

    def random_level(self) -> int:
        height = 1

        # keep flipping: heads (probability p) adds a level, tails stops
        while height < self.max_level and random.random() < self.p:
            height += 1

        return height
