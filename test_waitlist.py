import unittest
from waitlist import Waitlist, Time, Entry

class test_Waitlist(unittest.TestCase):
    def setUp(self):
        '''creates an instance of the waitlist class that can be added to throughout the waitlist class'''
        self.test_waitlist = Waitlist()
    
    def test_init(self):
        '''tests the Waitlist class initialization'''
        self.assertEqual(repr(self.test_waitlist._entries._L) , '[]')

    
    def test_add_customer(self):
        '''tests whether the add_customer function actually works'''
        self.test_waitlist.add_customer('A', '11:45')
        self.test_waitlist.add_customer('B', '11:45')  
        self.test_waitlist.add_customer('C', '02:30') 
        self.test_waitlist.add_customer('D', '09:30')
        self.test_waitlist.add_customer('E', '11:00')

        self.assertEqual(self.test_waitlist._entries._L[0].name, 'C') 

        self.assertEqual(self.test_waitlist._entries._L[2].name, 'A')
        self.assertEqual(self.test_waitlist._entries._L[1].name , 'D')

        self.assertEqual(self.test_waitlist._entries._L[3].name, 'B')
        self.assertEqual(self.test_waitlist._entries._L[4].name , 'E')


    def test_peek(self):
        '''tests the peek method to see if retrieves the customer with the highest priority'''
        self.assertEqual(self.test_waitlist.peek(), 'There are no people in the waitlist') 

        self.test_waitlist.add_customer('Priya', '02:45')
        self.assertEqual(self.test_waitlist.peek(), 'Priya')

        self.test_waitlist.add_customer('Naomi', '01:30')
        self.assertEqual(self.test_waitlist.peek(), 'Naomi')

 
        self.test_waitlist.add_customer('Huizhen', '12:15')
        self.assertEqual(self.test_waitlist.peek(), 'Naomi')



    def test_seat_customer(self):
        '''tests whether seat customer takes removes and returns the customer with the highest priority'''
        self.test_waitlist.add_customer('Naomi', '12:45')
        self.test_waitlist.add_customer('Huizhen', '10:30')
        self.test_waitlist.add_customer('Priya', '03:30')

        self.assertEqual(self.test_waitlist.seat_customer(), ('Priya', '03:30'))
        self.assertEqual(repr(self.test_waitlist._entries._L), '[Waitlist(Huizhen, 10:30), Waitlist(Naomi, 12:45)]')


    def test_print_reservation_list(self):
        '''tests whether print reservation list is correctly ordering and returning the waitlist'''
        self.test_waitlist.add_customer('Huizhen', '12:15')
        self.test_waitlist.add_customer('Tobey', '03:01')
        self.test_waitlist.add_customer('Priya', '03:01')

        self.assertEqual(self.test_waitlist.print_reservation_list(), "These are the current reservations [('Huizhen', '12:15'), ('Priya', '03:01'), ('Tobey', '03:01')]")
    
    def test_change_reservation(self):
        '''tests whether the change reservation time accurately changes the resevation time'''
        self.test_waitlist.add_customer('Huizhen', '12:15')
        self.test_waitlist.add_customer('Tobey', '03:01')
        self.test_waitlist.add_customer('Priya', '03:01')

        self.assertEqual(self.test_waitlist.print_reservation_list(), "These are the current reservations [('Huizhen', '12:15'), ('Priya', '03:01'), ('Tobey', '03:01')]")
        
        self.test_waitlist.change_reservation('Tobey', '02:01')

        self.assertEqual(self.test_waitlist.print_reservation_list(), "These are the current reservations [('Huizhen', '12:15'), ('Priya', '03:01'), ('Tobey', '02:01')]")
    


        

unittest.main()
