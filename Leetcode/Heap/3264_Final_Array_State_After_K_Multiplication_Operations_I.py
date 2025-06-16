from collections import heapq
def getFinalState(nums, k: int, multiplier: int):
    heap = []

    for i, num in enumerate(nums):
        heap.append((num,i))
    heap.sort()

    while k > 0:
        num, index = heapq.heappop(heap)
        heapq.heappush(heap, (num * multiplier,index))
        k -= 1
    
    result = []

    heap.sort(key=lambda x: x[1])
    for num, index in heap:
        result.append(num)

    return result