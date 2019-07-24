class Empty(Exception):
    pass


class CircularLinkedList:
    class Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next=None):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_first(self, e):
        newest = self.Node(e)
        if self.is_empty():
            newest._next = newest
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            newest._next = self._head
        self._head = newest
        self._size += 1

    def add_last(self, e):
        newest = self.Node(e)
        if self.is_empty():
            self._head = newest
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def add_any(self, e, pos):
        newest = self.Node(e)
        temp = self._head
        i = 1
        while i < pos:
            temp = temp._next
            i += 1
        newest._next = temp._next
        temp._next = newest
        self._size += 1

    def delete_first(self):
        if self.is_empty():
            raise Empty('Linked list is Empty')
        oldhead = self._tail._next
        self._tail._next = oldhead._next
        self._head = oldhead._next
        self._size -= 1
        if self.is_empty():
            self._tail = None

    def delete_last(self):
        if self.is_empty():
            raise Empty('Linked list is Empty')
        temp = self._head
        i = 0
        while i < len(self) - 2:
            temp = temp._next
            i += 1
        self._tail = temp
        temp = temp._next
        self._tail._next = self._head
        self._size -= 1

    def delete_any(self, pos):
        if self.is_empty():
            raise Empty('Linked List is Empty')
        temp = self._head
        i = 1
        while i < pos - 1:
            temp = temp._next
            i += 1
        val = (temp._next)._element
        temp._next = (temp._next)._next
        self._size -= 1
        print(val)

    def display(self):
        temp = self._head
        i = 0
        while i < len(self):
            print(temp._element, end='--')
            temp = temp._next
            i += 1
        print('\n')


cl = CircularLinkedList()
cl.add_last(10)
cl.add_last(30)
cl.add_last(50)
cl.add_last(60)
cl.add_last(80)
cl.display()
cl.delete_first()
cl.delete_first()
cl.display()
cl.add_first(90)
cl.add_any(29, 2)
cl.delete_any(2)
cl.display()
