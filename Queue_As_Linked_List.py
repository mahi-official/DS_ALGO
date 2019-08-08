class Empty(Exception):
    pass


class LinkedQueue:
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

    def enqueue(self, e):
        NewNode = self.Node(e)
        if self.is_empty():
            self._head = NewNode
        else:
            self._tail._next = NewNode
        self._tail = NewNode
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        value = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return value

    def first(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._head._element

    def display(self):
        temp = self._head
        while temp:
            print(temp._element, end='-->')
            temp = temp._next
        print()


q = LinkedQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(40)
print('Queue:', q.display())
print('Dequeue:', q.dequeue())
print('Queue:', q.display())
print('Is-Empty:', q.is_empty())
print('First: ', q.first())
q.enqueue(10)
q.enqueue(80)
print('Queue:', q.display())
print('First: ', q.first())
print('Length:', len(q))
print('Dequeue:', q.dequeue())
print('Queue:', q.display())
