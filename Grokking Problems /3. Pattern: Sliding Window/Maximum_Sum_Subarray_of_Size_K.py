'''
Problem Statement #
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''

def maximumSumArray(nums, k):
    result = float("-inf")
    currSum = 0
    left = 0
    right = 0

    while right < len(nums):
        currSum += nums[right]

        if (right-left+1) == k:
            result = max(result, currSum)
            currSum -= nums[left]
            left += 1
        right += 1

    return result

nums = [2, 3, 4, 1, 5]
k = 2 
print(maximumSumArray(nums, k))

nums = [2, 1, 5, 1, 3, 2]
k=3 
print(maximumSumArray(nums, k))






