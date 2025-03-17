"""unittests"""
import unittest
from task1_level3 import find_min_spaces

class TestSmallest(unittest.TestCase):
    """unittsets"""
    def test_one(self):
        """basic sequence test"""
        self.assertEqual(find_min_spaces([1,2,8,4,9], 3), 3)
unittest.main()
