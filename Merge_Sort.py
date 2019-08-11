def MergeSort(A):

    if len(A) > 1:
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]

        MergeSort(left)
        MergeSort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i = i + 1
            else:
                A[k] = right[j]
                j = j + 1
            k = k+1

        while i < len(left):
            A[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            A[k] = right[j]
            j = j + 1
            k = k + 1


list1 = [82,34,56,87,21,54,98,14,72]
MergeSort(list1)
print('Sorted Array', list1)

