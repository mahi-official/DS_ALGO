class Empty(Exception):
    pass


class DoublyLinkedList:
    class Node:
        __slots__ = '_prev', '_element', '_next'

        def __init__(self, element, prev=None, next=None):
            self._prev = prev
            self._element = element
            self._next = next

    def __init__(self):
        self._head = self.Node(None, None, None)
        self._tail = self.Node(None, None, None)
        self._head._next= self._tail
        self._tail._prev = self._head
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_first(self, e):
        newest = self.Node(e, None, None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head._prev = newest
        self._head = newest
        self._size += 1

    def add_last(self, e):
        newest = self.Node(e, None, None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            newest._prev = self._tail
        self._tail = newest
        self._size += 1

    def add_any(self, e, pos):
        newest = self.Node(e, None, None)
        temp = self._head
        i = 1
        while i < pos:
            temp = temp._next
            i += 1
        newest._next = temp._next
        temp._next = newest
        temp._next._prev = newest
        self._size += 1

    def delete_first(self):
        if self.is_empty():
            raise Empty('Linked list is Empty')
        self._head = self._head._next
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
        self._tail._next = None
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
        temp._next._next._prev = temp
        self._size -= 1
        print(val)

    def display(self):
        temp = self._head
        while temp:
            print(temp._element, end='--')
            temp = temp._next
        print('\n')


l = DoublyLinkedList()
l.add_last(10)
l.add_last(30)
l.add_last(50)
l.add_last(60)
l.add_last(80)
l.display()
l.delete_first()
l.delete_first()
l.display()
l.add_first(90)
l.add_any(29, 2)
l.delete_any(1)
l.display()
