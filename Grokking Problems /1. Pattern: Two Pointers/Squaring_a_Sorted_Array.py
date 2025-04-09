'''
Problem Statement #
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]
'''

def squaring(nums):
    left = 0
    right = len(nums) - 1
    result = [0] * len(nums)
    lastIndex = len(result) - 1

    while left <= right:
        leftNum = nums[left]
        rightNum = nums[right]

        if (leftNum**2) > (rightNum**2):
            result[lastIndex] = leftNum**2
            left += 1
        else:
            result[lastIndex] = rightNum**2
            right -= 1
        lastIndex -= 1
    
    return result

Input = [-2, -1, 0, 2, 3]
print(squaring(Input))

Input = [-3, -1, 0, 1, 2]
print(squaring(Input))
