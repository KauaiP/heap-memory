from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, address, quantity):
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(address, quantity)
        else:
            self.head = Node(address, quantity)
        self._size = self._size + 1

    def __len__(self):
        return self._size
      
    def free(self):
        self.data = None
        self.head = None
        self.next = None
        self._size = None