import random
class Time:
    """A class that represents time in the format HH:MM"""
    def __init__(self, hour, minute):
        self.hour = int(hour)
        self.minute = int(minute)

    def __lt__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self < other, and False otherwise"""
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour and self.minute < other.minute:
            return True
        else:
            return False
    
    def __eq__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self == other, and False otherwise"""
        if self.hour ==  other.hour and self.minute == other.minute:
            return True
        else:
            return False

    def __repr__(self):
        """Return the string representation of the time"""
        return f"{self.hour:02d}:{self.minute:02d}"

class Entry:
    """A class that represents a customer in the waitlist"""
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def __lt__(self, other):
        """Compare two customers based on their time, if equal then compare based on the customer name"""
        if self.time == other.time:
            return self.name < other.name
        return self.time < other.time

    def __repr__(self):
        'repr method to return the waitlist'
        return f'Waitlist({self.name}, {self.time})'

class Heap:
    def __init__(self):
        '''initializes the heap list'''
        self._L = []

    def __len__(self): 
        '''returns the length of the heap'''
        return len(self._L)

    def _i_parent(self, idx):
        '''returns which index the parents is at '''
        return (idx-1) // 2 if (idx-1) // 2 >= 0 else None
    
    def _i_left(self, idx):
        '''returns the left child'''
        il = idx*2+1
        return il if il<len(self) else None
    
    def _i_right(self, idx):
        ''' returns the right child'''
        ir = idx*2+2
        return ir if ir<len(self) else None

    def insert(self, item, priority):
        '''adds item to the heap using it's provided priority'''
        new_e = Entry(item, priority)
        self._L.append(new_e)
        self._upheap(len(self)-1)
    
    def _upheap(self, idx):
        '''upheaps item at the index specified'''
        i_p = self._i_parent(idx)

        while i_p is not None and self._L[i_p] > self._L[idx]:
            self._L[i_p], self._L[idx] = self._L[idx], self._L[i_p]
            idx = i_p
            i_p = self._i_parent(idx)
        
    def peek(self):
        '''returns but doesn't remove the item with the lowest priority'''
        return self._L[0].name
    
    def remove_min(self):
        '''removes and returns item with the lowest priority'''
        min_item = self._L[0]
        if len(self) == 1:
            self._L.pop()
            return min_item 

        self._L[0] = self._L.pop() 
        self._downheap(idx = 0)

        return (min_item.name, min_item.time)
        
    def _find_min_child(self, idx):
        '''returns the index of the minimum child and None if there is anything'''
        il = self._i_left(idx)
        ir = self._i_right(idx)

        if ir is None: 
            return il 
        else: 
            return il if self._L[il] < self._L[ir] else ir 
        
    def _downheap(self, idx):
        '''downheaps an item at a specifc index'''
        i_min = self._find_min_child(idx)

        while (i_min is not None) and (self._L[i_min] < self._L[idx]):
            self._L[i_min], self._L[idx] = self._L[idx], self._L[i_min]
            idx = i_min 
            i_min = self._find_min_child(idx)
    
class Waitlist:
    def __init__(self):
        '''initializes an empty priority queue'''
        self._entries = Heap()
        
    def add_customer(self, item, priority):
        ''' adds a customer to the priority queue and puts the person with the earliest customer at a higher priority'''
        self._entries.insert(item, priority)
    
        
        return f'{item} has been added to the waitlist at {priority}'

    def peek(self):
        '''returns but doesn't remove the first item in the waiting list''' 
        if self._entries._L == []:
            return 'There are no people in the waitlist'
        
        return self._entries.peek()
        
    

    def seat_customer(self):
        '''takes a customer out of the priority queue and returns them'''
        return self._entries.remove_min()



    def print_reservation_list(self):
        '''prints out the entire reservation list'''
        L = self._entries
        results = []
        for item in L._L:
            results.append((item.name, item.time))
            
        results.sort()
        print (f"These are the current reservations {results}")
        return (f"These are the current reservations {results}")
    
    def change_reservation(self, name, new_priority):
        '''changes the time of a specific customer's reservation'''
        for i in self._entries._L:
            if i.name == name:
                i.time = new_priority