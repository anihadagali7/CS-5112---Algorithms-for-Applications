import sys
from pathlib import Path as _PublicTestPath

_PUBLIC_TEST_PROBLEMS_DIR = _PublicTestPath(__file__).resolve().parent.parent
if str(_PUBLIC_TEST_PROBLEMS_DIR) not in sys.path:
    sys.path.insert(0, str(_PUBLIC_TEST_PROBLEMS_DIR))
import random
import unittest
from problem_3.a import LinkedList
from problem_3.b import SkipList


def linked_list_values(linked_list):
    values = []
    node = linked_list.root
    while node is not None:
        values.append(node.val)
        node = node.next
    return values


def skip_list_values(skip_list):
    values = []
    node = skip_list.root
    while node is not None:
        values.append(node.val)
        node = node.next[0]
    return values


class Test(unittest.TestCase):

    def test_public_linked_list_orders_values_and_finds_nodes(self):
        linked_list = LinkedList()
        linked_list.insert(3)
        linked_list.insert(0)
        linked_list.insert(1)
        self.assertEqual([0, 1, 3], linked_list_values(linked_list))
        self.assertEqual(linked_list.search(0), linked_list.root)
        self.assertEqual(linked_list.search(1), linked_list.root.next)
        self.assertEqual(linked_list.search(3), linked_list.root.next.next)
        self.assertIsNone(linked_list.search(2))

    def test_public_skip_list_insertion_orders_values(self):
        random.seed(0)
        skip_list = SkipList(8, 0.5)
        for value in [3, 0, 1]:
            skip_list.insert(value)
        self.assertEqual([0, 1, 3], skip_list_values(skip_list))
        self.assertEqual(skip_list.root.val, 0)

    def test_public_skip_list_search_finds_nodes(self):
        random.seed(1)
        skip_list = SkipList(8, 0.5)
        for value in [0, 1, 3]:
            skip_list.insert(value)
        self.assertEqual(skip_list.search(0), skip_list.root)
        self.assertEqual(skip_list.search(1), skip_list.root.next[0])
        self.assertEqual(skip_list.search(3), skip_list.root.next[0].next[0])
        self.assertIsNone(skip_list.search(2))


if __name__ == "__main__":
    unittest.main()
