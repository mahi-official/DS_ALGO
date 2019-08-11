class Empty(Exception):
    pass

class HeapSort:
    def __init__(self):
        self.maxsize = 10
        self.data = [-1] * self.maxsize
        self.size = 0

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def maxh(self):
        if self.size == 0:
            raise Empty('Heap is Empty')
        return self.data[1]

    def insert(self, element):
        if self.size == self.maxsize:
            raise Empty('No space in heap')

        self.size += 1
        i = self.size
        while i != 1 and element > self.data[i//2]:
            self.data[i] = self.data[i//2]
            i = i//2
        self.data[i] = element

    def deletemin(self):
        if self.size == 0:
            raise Empty('Heap is Empty')
        x = self.data[1]
        y = self.data[self.size]
        self.size -= 1
        i = 1
        ci = 2
        while ci <= self.size:
            if ci < self.size and self.data[ci] > self.data[ci+1]:
                ci += 1
            if y <= self.data[ci]:
                break
            self.data[i] = self.data[ci]
            i = ci
            ci = ci * 2
        self.data[i] = y
        return x



h = HeapSort()
h.insert(25)
h.insert(14)
h.insert(2)
h.insert(12)
h.insert(10)
h.insert(50)

print(h.data)
for i in range(h.size):
    print(h.deletemin(), end=',')
