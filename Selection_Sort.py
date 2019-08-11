def SelectionSort(A):
    for i in range(len(A)-1, 0, -1):
        max_pos = 0
        for j in range(1, i+1):
            if A[j] > A[max_pos]:
                max_pos = j
            A[i], A[max_pos] = A[max_pos], A[i]

list1 = [82,34,56,87,21,54,98,14,72]
SelectionSort(list1)
print('Sorted Array', list1)


