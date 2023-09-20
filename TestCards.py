from Cards import Card, Deck, Hand
import unittest

class TestCard(unittest.TestCase):
    '''a class to test the Card class and its methods'''
    def test_init(self):
        '''testing the initialization function in the card class'''
        self.c1 = Card(1, "hearts")
        self.assertEqual(self.c1.value, 1)
        self.assertNotEqual(self.c1.value, 2)
        self.assertEqual(self.c1.suit, "hearts")
        self.assertNotEqual(self.c1.suit, "clubs")
    def test_repr(self):
        '''testing the representation function in the card class'''
        self.c1 = Card(1, "hearts")
        self.assertEqual(repr(self.c1), "Card(1 of hearts)")
        self.assertNotEqual(repr(self.c1), "Card(2, hearts)")
    def test_lt(self):
        '''testing the less than function in the card class'''
        self.c1 = Card(1, "hearts")
        self.c2 = Card(1, "clubs")
        self.c3 = Card(1, 2)
        self.assertLess(self.c2, self.c1)
        self.assertFalse(self.c1 < self.c2)
    def test_eq(self):
        '''testng the equal to function in the card class'''
        self.c1 = Card(1, "hearts")
        self.c2 = Card(1, "hearts")
        self.c3 = Card(2, "hearts")
        self.assertEqual(self.c1, self.c2)
        self.assertNotEqual(self.c1, self.c3)

class TestDeck(unittest.TestCase):
    '''Testing the deck class'''
    def test_init(self):
        '''testing the initialization function in the deck class'''
        self.d1 = Deck([1], ["spades", "clubs"])
        self.assertEqual(self.d1.card_list, [Card(1, "clubs"), Card(1, "spades")])
        self.assertNotEqual(self.d1.card_list, [Card(2, "clubs"), Card(2, "spades")])
    def test_len(self):
        '''testing the length function in the deck class'''
        self.d1 = Deck([1], ["spades", "clubs"])
        self.assertEqual(len(self.d1.card_list), 2)
        self.assertNotEqual(len(self.d1.card_list), 3)
    def test_sort(self):
        '''testing the sort function in the deck class'''
        self.d1 = Deck([1], ["spades", "clubs"])
        self.assertIsNone(self.d1.sort()) 
    def test_repr(self):
        '''testing the representation fuction in the deck class'''
        self.d1 = Deck([1], ["spades"])
        self.assertEqual(repr(self.d1), "Deck: [Card(1 of spades)]")
        self.assertNotEqual(repr(self.d1), "Deck: [Card(2 of spades)]")
    def test_shuffle(self):
        '''testing the shuffle function in the deck class'''
        self.d1 = Deck([1], ["spades"])
        self.assertIsNone(self.d1.shuffle())
    def draw_top(self):
        '''testing the draw top card function in the deck class'''
        self.d1 = Deck([1, 2], ["spades"])
        self.assertEqual(self.d1.draw_top(), "Card(1 of spades)")
        self.assertNotEqual(self.d1.draw_top(), "Card(2 of spades")

class TestHand(unittest.TestCase):
    '''test the play class and its function'''
    def test_init(self):
        '''test the intialization function in the hand class'''
        self.h1 = Hand([1], ["spades", "diamonds", "clubs"])
        self.assertEqual(self.h1.card_list, [Card(1, "clubs"), Card(1, "diamonds"), Card(1,"spades")])
        self.assertNotEqual(self.h1.card_list, [Card(1, "diamonds"), Card(1, "clubs"), Card(1, "spades")])
    def test_repr(self):
        '''test the representation function in the hand class'''
        self.h1 = Hand([1], ["spades"])
        self.assertEqual(repr(self.h1), "Hand: [Card(1 of spades)]")
        self.assertNotEqual(repr(self.h1), "Hand: [Card(2 or spades)]")
    def test_play(self):
        '''test the play function in the hand class'''
        self.h1 = Hand([1, 2], ["spades"])
        self.assertEqual(repr(self.h1.play), "<bound method Hand.play of Hand: [Card(1 of spades), Card(2 of spades)]>")

unittest.main()





