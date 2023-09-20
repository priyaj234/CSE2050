class Entry:
    def __init__(self, item, priority):
        """Initializing/creating a priority queue entry"""
        self.priority = priority
        self.item = item
class PQ_UL:
    def __init__(self):
        """Initializing the priority queue"""
        self._entries = []
    def insert(self, item, priority):
        """a function to append an entry to the priority queue"""
        self._entries.append(Entry(item, priority))
