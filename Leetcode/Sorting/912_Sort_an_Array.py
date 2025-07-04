'''
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) 
time complexity and with the smallest space complexity possible.


Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not 
changed (for example, 2 and 3), while the positions of other numbers are changed 
(for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessarily unique.
'''
from collections import Counter
def sorting(nums):
    maps = Counter(nums)

    maxNum = max(nums)
    minNum = min(nums)

    res = []
    for i in range(minNum, maxNum+1):
        if i in maps:
            for j in range(maps[i]):
                res.append(i)
    
    return res

nums = [5,1,1,2,0,0]
print(sorting(nums))

nums = [5,2,3,1]
print(sorting(nums))
