class Empty(Exception):
    pass


class LinkedStack:
    class Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next=None):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self.Node(e, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Empty('Empty Stack')
        else:
            self._head = self._head._next
        self._size -= 1

    def top(self):
        if self.is_empty():
            raise Empty('Empty Stack')
        return self._head._element

    def display(self):
        temp = self._head
        while temp:
            print(temp._element, end='-->')
            temp = temp._next
        print('\n')


l = LinkedStack()
l.push(10)
l.push(30)
l.push(50)
l.push(60)
l.push(80)
l.display()
l.pop()
l.pop()
l.display()
l.push(90)
l.top()
l.pop()
l.display()
