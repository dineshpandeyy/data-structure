'''
Problem Statement #
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray 
whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
Example 2:

Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:

Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
'''

def smallestSubarrays(nums, S):
    result = float("inf")
    currSum = 0
    left = 0
    right = 0

    while right < len(nums):
        currSum += nums[right]
        while currSum >= S:
            result = min(result, right - left + 1)
            currSum -= nums[left]
            left += 1
        right += 1

    return result

input = [2, 1, 5, 2, 3, 2]
S= 7
print(smallestSubarrays(input, S))

input = [2, 1, 5, 2, 8]
S= 8
print(smallestSubarrays(input, S))

input = [3, 4, 1, 1, 6]
S= 8
print(smallestSubarrays(input, S))

            


