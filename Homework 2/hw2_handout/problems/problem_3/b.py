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
        pass

    def delete(self, x: int) -> None:
        pass

    def search(self, x: int) -> Node | None:
        pass
