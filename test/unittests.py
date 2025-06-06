"""unittests"""
import unittest
from task1_level3 import Node, enqueue

class TestTree(unittest.TestCase):
    """unittest class"""
    def insert_test(self):
        root_1 = Node(1,1)
        root_1 = enqueue(root_1, Node(0,0))
        self.assertEqual(root_1.right.value, 0)

unittest.main()
