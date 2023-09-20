import unittest
from MagicSort import linear_scan, reverse_list, insertionsort, quicksort, mergesort,  magic_sort
import random
random.seed(100)

def generate_halfsorted(n=8, idx_zero=None, pattern="random"):
    '''using functions from hw 6 to test the sorting functions'''
    if idx_zero is None: idx_zero = random.randint(0, n-1)
    L = []
    if pattern == "random":
      # [-3, -1, -2, 0, 3, 1, 2]
        for i in range(idx_zero): L.append(random.randint(-n,-1))
        L.append(0)
        for i in range(n-1-idx_zero): L.append(random.randint(1, n))
    return L, idx_zero

def is_sorted(L):
    '''another function from hw 6 that can be used to test sorting algorithms functionality'''
    'Returns True (False) if L is (is not) sorted'
    return not any(L[i] > L[i+1] for i in range(len(L)-1))


class Test_linear_scan(unittest.TestCase):
    def test_linear_scan(self):
        '''tests if the linear scan functions works as intended'''
        L_already_sorted = [1, 2, 3, 4, 5]
        L_reversed = [5, 4, 3, 2, 1]
        L_less_than_five = [1, 2, 4, 3, 5]
        L_typical = [2, 3, 0, 1, 7, 9, 11, 6, 4, 3, 13, 12, 21, 20]

        self.assertEqual(linear_scan(L_already_sorted), "Sorted")
        self.assertEqual(linear_scan(L_reversed), "Reverse")
        self.assertEqual(linear_scan(L_less_than_five), "Insertion")
        self.assertEqual(linear_scan(L_typical), "Quick")

class Test_reverse_list(unittest.TestCase):
    def test_reverse_list(self):
        '''tests if the reverse list function works as intended'''
        L = [5, 4, 3, 2, 1] #creates lists
        self.assertEqual(reverse_list(L), [1, 2, 3, 4, 5]) #sees if the list produced by reverse list and what the list reverse would be are the same


class Test_insertionsort(unittest.TestCase):
    def test_insertionsort(self):
        '''tests the insertionsort functions'''
        for list_size in range(50): #tests  50 lists
                    for i in range(list_size): #random list sizes
                        L, index = generate_halfsorted(list_size, i, pattern = "random") #creates lists with a random pattern
                        Lcopy = L[:] #creates a slice of a list
                        sorted = insertionsort(L, left = 0, right = None) #creates the sorted version of the list 
                        self.assertTrue(is_sorted(L)) #tests if the list is actual sorted
                        self.assertCountEqual(L, Lcopy) #makes sure no items are deleted or added.

class Test_quicksort(unittest.TestCase):
    def test_quick(self):
        '''tests the quicksort function using same testing process as test_insertionsort'''
        for list_size in range(50): 
                    for i in range(list_size):
                        L, index = generate_halfsorted(list_size, i, pattern = "random")
                        Lcopy = L[:]
                        sorted = quicksort(L)
                        self.assertTrue(is_sorted(L))
                        self.assertCountEqual(L, Lcopy)
        L = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0] #this line and the following check if quicksort defaults insertion if the list is 16 or less items
        types_sixteen = set()
        quicksort(L,0,None,types_sixteen)
        self.assertEqual(types_sixteen, {"Insertion", "Quicksort"} )

        types=set()
        L = list(range(0, 500)) #A list with too many items reachs recursion depth and ends up moving into mergesort and then into insertion sort
        quicksort(L,0,None,types)
        self.assertEqual(types, {"Quicksort", "Mergesort","Insertion" })


class Test_mergesort(unittest.TestCase):
    def test_mergesort(self):
        '''tests the mergesort function'''
        for list_size in range(50): 
                    for i in range(list_size):
                        L, index = generate_halfsorted(list_size, i, pattern = "random")
                        Lcopy = L[:]
                        sorted = mergesort(L)
                        self.assertTrue(is_sorted(L))
                        self.assertCountEqual(L, Lcopy)
        L = [15, 16, 13, 14, 11, 10, 12, 7, 8, 9, 6, 5, 3, 3, 2, 1, 0] #this line and the following check if quicksort skips over mergesort and defaults to insertion if the list is 16 or less items
        self.assertEqual(magic_sort(L),{"Insertion", "Quicksort"} )

class Test_magicsort(unittest.TestCase):
    '''tests the magicsort function using the same process as for the previous two sorting algorithms'''
    def test_magicsort(self):
        for list_size in range(50): 
                    for i in range(list_size):
                        L, index = generate_halfsorted(list_size, i, pattern = "random")
                        Lcopy = L[:]
                        sorted = magic_sort(L)
                        self.assertTrue(is_sorted(L))
                        self.assertCountEqual(L, Lcopy)


unittest.main()