# Do not modify this class
class Node:
    'Node object to be used in DoublyLinkedList'
    def __init__(self, item, _next=None, _prev=None):
        'initializes new node objects'
        self.item = item
        self._next = _next
        self._prev = _prev

    def __repr__(self):
        'String representation of Node'
        return f"Node({self.item})"


class DoublyLinkedList:
    def __init__(self, items=None):
        'Construct a new DLL object'
        self._head = None
        self._tail = None
        self._len = 0
        self._nodes = dict()    # dictionary of item:node pairs

        # initialize list w/ items if specified
        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self):
        'returns number of nodes in DLL'
        return self._len

    # TODO: Modify the 4 methods below to keep `self._nodes` up-to-date
    def add_first(self, item):
        'adds item to front of dll'
        # add new node as head
        self._head = Node(item, _next=self._head, _prev=None)
        self._len += 1
        
        # if that was the first node
        if len(self) == 1: self._tail = self._head

        # otherwise, redirect old heads ._tail pointer
        else: self._head._next._prev = self._head
        self._nodes[item] = self._head

    def add_last(self, item):
        'adds item to end of dll'
        # add new node as head
        self._tail = Node(item, _next=None, _prev=self._tail)
        self._len += 1
        
        # if that was the first node
        if len(self) == 1: self._head = self._tail

        # otherwise, redirect old heads ._tail pointer
        else: self._tail._prev._next = self._tail
        self._nodes[item] = self._tail
    def remove_first(self):
        'removes and returns first item'
        if len(self) == 0: raise RuntimeError("cannot remove from empty dll")

        # extract item for later
        item = self._head.item

        # move up head pointer
        self._head = self._head._next
        self._len -= 1

        # was that the last node?
        if len(self) == 0: self._tail = None

        else: self._head._prev = None
        
        del self._nodes[item]

        return item

        
    def remove_last(self):
        'removes and returns last item'
        if len(self) == 0: raise RuntimeError("cannot remove from empty dll")

        # extract item for later
        item = self._tail.item

        # move up tail pointer
        self._tail = self._tail._prev
        self._len -= 1

        # was that the last node?
        if len(self) == 0: self._head = None

        else: self._tail._next = None

        del self._nodes[item]

        return item
        
    # TODO: Add a docstring and implement
    def __contains__(self, item):
        '''this function tests membership of an item in dictionary _nodes'''
        return item in self._nodes
         
    # TODO: Add a docstring and implement
    def neighbors(self, item):
        '''This function tests if an item is in the dictionary, _nodes, and then returns the first and last item. If the 
        item is the head or the tail, it will return none and the next item or the previous item and none'''
        if item not in self._nodes:
            raise RuntimeError("Item not in Doubly Linked List")
        elif item == self._head.item:
            return (None, self._nodes[item]._next.item)
        elif item == self._tail.item:
            return (self._nodes[item]._prev.item, None)
        else:
            return (self._nodes[item]._prev.item, self._nodes[item]._next.item)

    # TODO: Add a docstring and implement
    def remove_node(self, item):
        '''removes a node from the doublylinkedlist that has a specific item stored in it'''
        if item not in self._nodes:
            raise RuntimeError("Item not in Doubly Linked List")
            self._node
        elif item == self._head.item:
            self.remove_first()
        elif item == self._tail.item:
            self.remove_last()
        else:
            self._nodes[item]._prev._next = self._nodes[item]._next
            self._nodes[item]._next._prev = self._nodes[item]._prev
            del self._nodes[item]
        self._len -= 1
        return item