import heapq as heap

L = []
heap.heappush(L,20)
heap.heappush(L,37)
heap.heappush(L,10)
heap.heappush(L,2)
heap.heappush(L,67)
heap.heappush(L,90)

print(L)
heap.heappushpop(L,50)
print(L)
heap.heapreplace(L, 25)
print(L)

l1 = heap.nlargest(3, L)
l2 = heap.nsmallest(3, L)
print(l1, l2)

