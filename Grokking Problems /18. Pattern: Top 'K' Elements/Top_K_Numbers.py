'''
Problem Statement #
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

Example 1:

Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]
Example 2:

Input: [5, 12, 11, -1, 12], K = 3
Output: [12, 11, 12]
'''
import heapq
def  topK(nums,k):
    heap = []

    for num in nums:
        heapq.heappush(heap,-num)
    
    res = []
    while k:
        res.append(-heapq.heappop(heap))
        k -= 1
    
    return res

def  anotherWaytopK(nums,k):
    heap = []

    for i in range(k):
        heapq.heappush(heap,nums[i])
    
    for i in range(k,len(nums)):
        num = nums[i]
        if heap[0] < num:
            heapq.heappop(heap)
            heapq.heappush(heap,num)

    return heap

    
nums = [3, 1, 5, 12, 2, 11]
k = 3
print(anotherWaytopK(nums,k))

nums = [5, 12, 11, -1, 12]
k = 3
print(anotherWaytopK(nums,k))
