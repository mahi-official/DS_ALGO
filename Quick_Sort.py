def QuickSort(A, low, high):
    if low < high:
        p = partition(A, low, high)
        QuickSort(A, low, p-1)
        QuickSort(A, p+1, high)


def partition(A, low, high):
    i = low-1
    pivot = A[high]
    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[high] = A[high], A[i+1]

    return i+1

list1 = [82,34,56,87,21,54,98,14,72]
QuickSort(list1, 0, len(list1)-1)
print('Sorted Array', list1)

