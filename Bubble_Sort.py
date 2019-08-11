def BubbleSort(A):
    for i in range(len(A)-1, 0, -1):
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]


list1 = [82,34,56,87,21,54,98,14,72]
BubbleSort(list1)
print('Sorted Array', list1)
