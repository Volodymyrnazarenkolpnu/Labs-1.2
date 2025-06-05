"""unittest mod"""
import unittest
from task1_level3 import main

class TestGraphs(unittest.TestCase):
    """testing class"""
    def test_case1(self):
        """self explanatory"""
        a = main()
        self.assertEqual(a, 23)
if __name__ == "__main__":
    unittest.main()
