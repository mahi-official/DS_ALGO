class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._data.pop()
    def top(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._data[-1]

s = ArrayStack()
s.push(20)
s.push(10)
print('Stack:', s._data)
print('Length:', len(s))
print('Popped:', s.pop())
print('Stack:', s._data)
print('Is-Empty:', s.is_empty())
