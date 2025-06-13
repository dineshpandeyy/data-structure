'''
Problem Statement #
Given a string, sort it based on the decreasing frequency of its characters.

Example 1:

Input: "Programming"
Output: "rrggmmPiano"
Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.
Example 2:

Input: "abcbab"
Output: "bbbaac"
Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.
'''

import heapq
def sortFreq(nums):
    maps = {}

    for num in nums:
        if num not in maps:
            maps[num] = 1
        else:
            maps[num] += 1
    
    heap = []
    for key, value in maps.items():
        heapq.heappush(heap, (-value,key))
    
    res = []

    while heap:
        value, key = heapq.heappop(heap)
        for i in range(-value):
            res.append(key)
    
    return "".join(res)


s = "Programming"
print(sortFreq(s))

s = "abcbab"
print(sortFreq(s))