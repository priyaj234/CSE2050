import itertools
class BETNode:
    """Node for binary expression tree"""

    # Don't modify the provided code below - start working at add_left()

    # Some class variables (no need to make a copy of these for every node)
    # access these with e.g. `BETNode.OPERATORS`
    OPERATORS = {'+', '-', '*', '/'}
    CARD_VAL_DICT = {'A':1, '1':1, '2':2, '3':3, '4':4,
                     '5':5, '6':6, '7':7, '8':8, '9':9,
                     '10':10, 'J':11, 'Q':12, 'K':13}

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # These are proficed for you - do not modify. They let you hash BETs (so they can be stored in sets)
    # and compare them (so you can write unittests more easily).
    def __eq__(self, other):
        """Two nodes are equal if their values are equal and their subtrees are (recursively) equal"""
        if other is None: return False
        return self.value == other.value and self.left == other.left and self.right == other.right
    
    def __hash__(self):
        """Hash the whole tree (value + left and right subtrees)"""
        return hash((self.value, self.left, self.right))
    
    # START HERE
    def add_left(self, node):
        'a function to add a left branch to a node'
        self.left = node

    def add_right(self, node):
        'a function to add a right branch to a node'
        self.right = node
    def evaluate(self): 
        'a function to take all of the nodes and using the operators and the key values to find the total value of the tree'
        if self.value in BETNode.CARD_VAL_DICT:
            return BETNode.CARD_VAL_DICT[self.value]
            
        r = self.right.evaluate()
        l = self.left.evaluate()
        if r == 0 and self.value == "/":
            return "Error: cannot divide a number by 0"
        if self.value == "+":
            return l + r
        if self.value == "-":
            return l - r
        if self.value == "*":
            return l * r
        if self.value == "/":
            return l / r
        
 
    def __repr__(self): 
        'a function to represent a tree as a string'
        x = ""
        y = self.helper()
        for i in y:
            x += (i)
        return x
    
    def helper(self):
        'the helper functions to create the string representation of a tree'
        if self.value in BETNode.OPERATORS:
            yield "("
        if self.left is not None: yield from self.left.helper()  
        yield self.value                                             
        if self.right is not None: yield from self.right.helper()
        if self.value in BETNode.OPERATORS:
            yield ")"
        


def create_trees(cards):
    'a function that creates all possible trees for a four-card hand and returns them'
    trees = set()
    for c in itertools.permutations(cards):
        for x in itertools.product(BETNode.OPERATORS ,repeat = 3):
            #CCXCCXX
            cards = [c[0], c[1], x[0], c[2], c[3], x[1], x[2]]
            trees.add(create_trees_helper(cards))
            #CCXCXCX
            cards = [c[0], c[1], x[0], c[2], x[1], c[3], x[2]]
            trees.add(create_trees_helper(cards))
            #CCCXXCX
            cards = [c[0], c[1], c[2], x[0], x[1], c[3], x[2]]
            trees.add(create_trees_helper(cards))
            #CCCXCXX
            cards = [c[0], c[1], c[2], x[0], c[3], x[1], x[2]]
            trees.add(create_trees_helper(cards))
            #CCCCXXX
            cards = [c[0], c[1], c[2], c[3], x[0], x[1], x[2]]
            trees.add(create_trees_helper(cards))
    return trees
                  
def create_trees_helper(L):
    'helper function for the create_trees function that creates a tree based on the different permutations'
    stack = []
    for i in L:
        stack.append(BETNode(i))
        if i in BETNode.OPERATORS:
            x = stack.pop()
            right = stack.pop()
            left = stack.pop()
            x.add_right(right)
            x.add_left(left)
            stack.append(x)
        
    return stack.pop()


def find_solutions(cards): 
    'a function that iterates through the set produced by create_trees and form a set of trees that evaluate to 24'
    return_set = set()
    for j in create_trees(cards):
        if j.evaluate() == 24:
            return_set.add(repr(j))

    return return_set

print(len(create_trees(('K', '1' , '2' ,'3'))))