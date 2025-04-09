'''
Problem Statement #
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
'''

def threeSum(nums):
    result = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        if nums[i] > 0:
            break

        left = i + 1
        right = len(nums) - 1

        while left < right:
            totalSum = nums[i] + nums[left] + nums[right]
            if totalSum == 0:
                result.append([nums[i],nums[left],nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left-1]:
                    left += 1
                
                while left < right and nums[right] == nums[right+1]:
                    right -= 1

            elif totalSum > 0:
                right -= 1
            else:
                left += 1
    
    return result

nums = [-3, 0, 1, 2, -1, 1, -2]
print(threeSum(nums))

nums = [-5, 2, -1, -2, 3]
print(threeSum(nums))