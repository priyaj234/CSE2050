import unittest
from BET import BETNode , create_trees, find_solutions


class TestBETNode(unittest.TestCase):
    def test_repr(self):
        r"""String representation
               *
              / \
             A   -
                / \
               2   +
                  / \
                 3   4
           
        """
        root = BETNode('*')
        root.add_left(BETNode('A'))
        root.add_right(BETNode('-'))
        root.right.add_left(BETNode('2'))
        root.right.add_right(BETNode('+'))
        root.right.right.add_left(BETNode('3'))
        root.right.right.add_right(BETNode('4'))
        expected_str = '(A*(2-(3+4)))'
        self.assertEqual(repr(root), expected_str)


    # TODO: Add test cases below. Repr is provided for you.
    def test_evaluate_tree1(self):
        'tests a tree that would not be able to evalute because we cannot divide by 0'

        r"""String representation
               +
              / \
             1   *
                / \
               2   +
                  / \
                 3   3
           
        """

        root = BETNode('/')
        root.add_left(BETNode('1'))
        root.add_right(BETNode('*'))
        root.right.add_left(BETNode('2'))
        root.right.add_right(BETNode('-'))
        root.right.right.add_left(BETNode('3'))
        root.right.right.add_right(BETNode('3'))
        expected_str = '(1/(2*(3-3)))'
        self.assertEqual(repr(root), expected_str)

        self.assertEqual(root.evaluate(), "Error: cannot divide a number by 0")

    def test_evaluate_tree2(self):
        'testing if a different tree structure still evaluates correctly'
        r"""String representation
               *
              / \
             -   +
            / \   / \
           6   A  K  J
        """
        root = BETNode('*')
        root.add_left(BETNode('-'))
        root.add_right(BETNode('+'))
        root.right.add_left(BETNode('K'))
        root.right.add_right(BETNode('J'))
        root.left.add_left(BETNode('6'))
        root.left.add_right(BETNode('A'))
        expected_str = '((6-A)*(K+J))'
        self.assertEqual(repr(root), expected_str)
        self.assertEqual(root.evaluate(), 120)

    def test_evaluate_tree3(self):
        'testing whether a tree where the node is a value and the branches are operators just returns the number
        r"""String representation
               A
              / \
             *   -
               
           
        """
        root = BETNode('A')
        root.add_left(BETNode('*'))
        root.add_right(BETNode('-'))

        self.assertEqual(repr(root), '(*)A(-)')
        self.assertEqual(root.evaluate(), 1)

class TestCreateTrees(unittest.TestCase):
    def test_hand1(self): 
        'tests if create_trees with a fully unique set of cards produces up to 7680 different types of trees'
        self.assertTrue(len(create_trees(('A', '6' , '7' ,'K')))<= 7680)
        
    def test_hand2(self):
         'tests if create_trees with one duplicate card produces up to 3840 different types of trees '
         self.assertTrue(len(create_trees(('A', '1' , '7' ,'A'))) <= 3840)
        

class TestFindSolutions(unittest.TestCase):
    def test0sols(self):
        'tests the find_solutions function for a solutions that is known to provide 0 solutions'
        self.assertEqual(len(find_solutions(('3', '6', '4', '7'))), 0)
        pass
    def test_A23Q(self):
        'tests the find_solutions function for the A 2 3 Q function that needed to be tested as per the hw pdf'
        self.assertEqual(len(find_solutions(('A', '2', '3', 'Q'))), 33)
        
unittest.main()