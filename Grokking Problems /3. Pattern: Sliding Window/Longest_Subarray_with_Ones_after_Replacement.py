'''
Problem Statement #
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, 
find the length of the longest contiguous subarray having all 1s.

Example 1:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
Example 2:

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
'''

def longestOnes(nums, k):
    left = 0
    right = 0
    result = 0
    zeroCount = 0


    while right < len(nums): 
        if nums[right] == 0:
            zeroCount += 1
        
        while zeroCount > k:
            if nums[left] == 0:
                zeroCount -= 1
            left += 1
        
        result = max(result, right - left + 1)
        right += 1
    
    return result

Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
k = 2
print(longestOnes(Array,k))

Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
k=3
print(longestOnes(Array,k))





