from collections import heapq
def numberGame(nums):
    heap = nums
    heapq.heapify(heap)
    res = []
    N = len(nums)

    while heap:
        alice = heapq.heappop(heap)
        bob = heapq.heappop(heap)

        res.append(bob)
        res.append(alice)
        N -= 1
    
    return res