def binarysearch(A, key):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low+high) // 2
        if key == A[mid]:
            return True
        elif key < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

def bsearchrec(A, key, low, high):
    if low > high:
        return False
    else:
        mid = (low+high) // 2
        if key == A[mid]:
            return True
        elif key < A[mid]:
            return bsearchrec(A, key, low, mid-1)
        else:
            return bsearchrec(A, key, mid+1, high)
        
A = [12, 23, 34, 56, 78, 90]
found = binarysearch(A, 78)
fnd = bsearchrec(A, 56, 0, 6)
print("Element 78 is: ", found)
print("Element 56 is: ", fnd)
