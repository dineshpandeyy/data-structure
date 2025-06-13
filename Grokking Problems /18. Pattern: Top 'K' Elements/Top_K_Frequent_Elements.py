'''
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

Example 1:

Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.
Example 2:

Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice, all other numbers appeared once.
'''
import heapq
def topK(nums,k):
    maps = {}

    for num in nums:
        if num not in maps:
            maps[num] = 1
        else:
            maps[num] += 1
    heap = []
    for key, value in maps.items():
        heapq.heappush(heap, (value, key))
        if len(heap) > k:
            heapq.heappop(heap)
    res = []
    while heap:
        res.append(heapq.heappop(heap)[1])
    
    return res

nums = [1, 3, 5, 12, 11, 12, 11]
K = 2
print(topK(nums, K))

nums = [5, 12, 11, 3, 11]
K = 2
print(topK(nums, K))

'''
1. another solution can be using heap by sorting it in the ascending value of 
value in heap which time complexity will be nlongn but the above solution is better with nlogk

2. Another solution is using bucket sort
'''



