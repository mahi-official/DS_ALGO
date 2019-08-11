def InsertionSort(A):
    for i in range(0, len(A)):
        val = A[i]
        pos = i
        while pos > 0 and A[pos-1] > val:
            A[pos] = A[pos-1]
            pos -= 1
        A[pos] = val


list1 = [82,34,56,87,21,54,98,14,72]
InsertionSort(list1)
print('Sorted Array', list1)
