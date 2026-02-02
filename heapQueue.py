import heapq

h = []

# minHeap property - h = [1, 5, 3, 7]   # internal structure, not sorted

heapq.heapify(h)

# heapify converts a list into a min-heap

heapq.heappush(h, 5)
heapq.heappush(h, 1)
heapq.heappush(h, 3)
heapq.heappush(h, 7)

# Returns 2 largest elements (sorted descending)
print(heapq.nlargest(2, h))

# Returns 2 smallest elements (sorted ascending)
print(heapq.nsmallest(2, h))

# Removes and returns smallest element
print(heapq.heappop(h))


print(heapq.heappush(h, 2))
print(heapq.heappushpop(h, 4))
print(h)
print(heapq.heapreplace(h, 6))
print(heapq.merge([1,3,5], [2,4,6]))
print(heapq._heapify_max([1,3,5,2,4,6]))