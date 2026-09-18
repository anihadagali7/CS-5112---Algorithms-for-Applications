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
        pass

    def search(self, x: int) -> Node | None:
        pass
