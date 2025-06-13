'''
Problem Statement #
Given an unsorted array of numbers, find Kth smallest number in it.
Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.
'''
import heapq

def kthSmallest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
    
    if len(heap) < k:
        return "None"
    while k-1:
        heapq.heappop(heap)
        k -= 1
    
    return heap[0]

nums = [1, 5, 12, 2, 11, 5]
k = 3
print(kthSmallest(nums, k))

nums = [1, 5, 12, 2, 11, 5]
K = 4
print(kthSmallest(nums, K))

nums = [5, 12, 11, -1, 12]
K = 3
print(kthSmallest(nums, K))