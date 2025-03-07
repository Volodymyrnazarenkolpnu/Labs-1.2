"""testing"""
import unittest
from task1_level3 import find_longest_peak

class TestPeakSequence(unittest.TestCase):
    """testing for common cases"""

    def test_increasing(self):
        """test for incresting sequence"""
        self.assertEqual(find_longest_peak([1,2,3,4,5,6,7,8]), [])
    def teat_decreasing(self):
        """test for decreasing sequence"""
        self.assertEqual(find_longest_peak([8,7,6,5,4,3,2,1]), [])
    def test_2el(self):
        """test for 2 element sequence"""
        self.assertEqual(find_longest_peak([8,7]), [])
    def test_nopeak(self):
        """test fot sequence without peaks"""
        self.assertEqual(find_longest_peak([8,7,6,7,8]), [])
    def test_3peaks(self):
        """test fot sequence with 3 peaks"""
        self.assertEqual(find_longest_peak([1,2,0,4,7,5,2,3,2]), [0,4,7,5,2])
unittest.main()
