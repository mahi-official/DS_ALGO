class Empty(Exception):
    pass

class ArrayQueue:
    def __init__(self):
        self._data = []
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        self._data.append(e)
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        value = self._data[self._front]
        del self._data[0]
        #self._data[self._front] = None
        #self._front += 1
        self._size -= 1
        return value
    
    def first(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._data[self._front]


q = ArrayQueue()
q.enqueue(20)
q.enqueue(10)
q.enqueue(50)
print('Queue:', q._data)
print('Length:', len(q))
print('Dequeue:', q.dequeue())
print('Queue:', q._data)
print('Is-Empty:', q.is_empty())
print('First: ',q.first())
print('Length:', len(q))
q.enqueue(30)
q.enqueue(70)
print('Queue:', q._data)
print('First: ',q.first())
print('Length:', len(q))
print('Dequeue:', q.dequeue())
print('Queue:', q._data)
