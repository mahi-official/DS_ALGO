def linearsearch(A, key):
    position = 0
    flag = False
    while position < len(A) and not flag:
        if A[position] == key:
            flag = True
        else:
            position = position + 1

        return flag

A = [84, 21, 43, 56, 57, 86, 94, 15]
found = linearsearch(A,9)
print('Element 9 is present: ',found)
