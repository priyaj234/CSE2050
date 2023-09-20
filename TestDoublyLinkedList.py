from DoublyLinkedList import DoublyLinkedList as DLL
import unittest

# Basic tests are provided for you, but you need to implement the last 3 unittests
class testDLL(unittest.TestCase):
    def test_addfirst_removefirst(self):
        'adds items to front, then removes from front'
        dll = DLL()
        n = 100

        for j in range(5): # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), n-1-i)

            with self.assertRaises(RuntimeError):
                dll.remove_first()

    def test_addlast_removelast(self):
        'adds items to end, then removes from end'
        dll = DLL()
        n = 100

        for j in range(5): # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_last(), n-1-i)

            with self.assertRaises(RuntimeError):
                dll.remove_last()

    def test_add_remove_mix(self):
        'various add/remove patterns'
        dll = DLL()
        n = 100

        # addfirst/removelast
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_last(), i)

        # addlast/removefirst
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), i)

        # mix of first/last
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                if i%2: dll.add_last(i) # odd numbers - add last
                else: dll.add_first(i)  # even numbers - add first

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                if i%2: self.assertEqual(dll.remove_last(), n-i) # odd numbers: remove last
                else: self.assertEqual(dll.remove_first(), n-2-i) # even numbers: remove first

    # TODO: Add docstrings to and implement the unittests below
    def test_contains(self):
        '''This functions tests the __contains__ function'''
        testLL = DLL(range(5))
        
        for i in range(5):
            self.assertTrue(i in testLL)
        for i in range(5):
            testLL.remove_first()
            self.assertFalse(i in testLL)

    def test_neighbors(self):
        '''This functions tests the neighbors functions'''
        testLL = DLL(range(5))
        self.assertEqual(testLL.neighbors(1), (0, 2))
        self.assertEqual(testLL.neighbors(0), (None, 1))
        self.assertEqual(testLL.neighbors(4), (3, None))
        with self.assertRaises(RuntimeError):
            (testLL.neighbors(7))

    def test_remove_item(self):
        '''tests the remove_node function'''
        testLL = DLL(range(5))
        testLL.remove_node(0)
        self.assertEqual(testLL._head.item, 1)
        self.assertEqual(testLL._head._next.item, 2)
        self.assertEqual(None, testLL._head._prev)
        self.assertTrue(0 not in testLL)
        testLL.remove_node(4)
        self.assertEqual(testLL._tail.item, 3)
        self.assertEqual(testLL._tail._next, None)
        self.assertEqual(testLL._tail._prev.item, 2 )
        self.assertTrue(4 not in testLL)
        testLL.remove_node(2)
        self.assertEqual(testLL._head._next.item, testLL._tail.item)
        self.assertEqual(testLL._tail._prev.item, 1)
        self.assertTrue(2 not in testLL)
        with self.assertRaises(RuntimeError):
            (testLL.remove_node(10))

unittest.main()