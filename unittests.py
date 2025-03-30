"""mod for unittests"""
import unittest

from task1_level3 import find_max_distance, Node

class TestTree(unittest.TestCase):
    """unittests"""
    def test_one(self):
        root = Node(10)
        root.right = Node(5)
        root.left = Node(4)
        root.left.left = Node(3)
        self.assertEqual(find_max_distance(root), 3)

unittest.main()