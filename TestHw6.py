import unittest
from hw6 import find_zero, sort_halfsorted, bubble, selection, insertion
from TestHelpers import generate_halfsorted, is_sorted

# TODO: implement tests for sort_halfsorted

class Test_SortHalfSorted(unittest.TestCase):
   def test_halfsorted_bubble(self): 
      # use sort_halfsorted(L, bubble) to test
      '''a function to test that bubble sort works how it's supposed to'''
      for list_size in range(50): #testing list with length of up to fifty
         for i in range(list_size): #testing the random list size
            L, index = generate_halfsorted(list_size, i, pattern = "random") #generating a random half sorted list
            Lcopy = L[:] #creating a copy to store the original
            sort_halfsorted(L, sort = bubble) #calling the sort_halfsorted using bubble sort in this case
            self.assertTrue(is_sorted(L)) #using helper function is_sorted to asserted whether the list actually got sorted
            self.assertCountEqual(L, Lcopy) #making sures there was no duplication or deletion in when sorting

   def test_halfosrted_selection(self): 
      # use sort_halfsorted(L, selection) to test
      ''' a function to test that selection sort works how it's supposed to'''
      for list_size in range(50): 
                  for i in range(list_size):
                     L, index = generate_halfsorted(list_size, i, pattern = "random")
                     Lcopy = L[:]
                     sort_halfsorted(L, sort = selection)
                     self.assertTrue(is_sorted(L))
                     self.assertCountEqual(L, Lcopy)

   def test_halfsorted_insertion(self):
      '''a function to test that insertion sort works how it's supposed to'''
      for list_size in range(50): 
            for i in range(list_size):
               L, index = generate_halfsorted(list_size, i, pattern = "random")
               Lcopy = L[:]
               sort_halfsorted(L, sort = insertion)
               self.assertTrue(is_sorted(L))
               self.assertCountEqual(L, Lcopy)

# Test provided for you
class Test_FindZero(unittest.TestCase):
   def test1_allLengthsAllIndices(self):
      '''Tests find_zero for every possible index, for lists from 1 to 100 items

         Lists
         -----
            '-' and '+' denote negative and positive ingeters, respectively
                                 idx_zero
            n = 1                
               L = [0]           0

            n = 2
               L = [0, +]        0
               L = [-, 0]        1

            n = 3                
               L = [0, +, +]     0
               L = [-, 0, +]     1  
               L = [-, -, 0]     2

            n = 4
               L = [0, +, +, +]  0
               L = [-, 0, +, +]  1
               L = [-, -, 0, +]  2
               L = [-, -, -, 0]  3
            ...
            n = 100
               L = [0, ..., +]   0
               ...
               L = [-, ..., 0]   99
      '''

      # note the use of `subTest`. These all count as 1 unittest if they pass,
      # but all that fail will be displayed independently
      for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(1, 50):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                        L, idx_zero = generate_halfsorted(n, idx_zero=i, pattern=pattern)
                        self.assertEqual(find_zero(L), idx_zero)

unittest.main()