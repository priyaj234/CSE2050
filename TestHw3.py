from hw3 import find_pairs_naive, find_pairs_optimized
import unittest
class TestHw3(unittest.TestCase):
    def test_find_pairs_naive(self):
        '''tests the different things that can be done with the find_pairs_naive function'''
        self.assertEqual(find_pairs_naive(), {(3, 2), (1, 4)})
        self.assertNotEqual(find_pairs_naive(), {(2, 2), (4, 1)})
        self.assertEqual(find_pairs_naive([1, 2, 3], 0), {})
        self.assertNotEqual(find_pairs_naive([1, 2, 3 ,4], 0), {(1, 2)})
    def test_find_pairs_optimized(self):
        '''tests the different things that can be done with the find_pairs_optimized function'''
        self.assertEqual(find_pairs_optimized(),{(2, 3), (1, 4)})
        self.assertNotEqual(find_pairs_optimized(), {(3, 2), (4, 1)})
        self.assertEqual(find_pairs_optimized([1, 2 ,3], 0), {})
        self.assertNotEqual(find_pairs_optimized([1, 2, 3 ,4], 0), {(1, 2)})
    
unittest.main()