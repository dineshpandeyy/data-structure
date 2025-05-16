'''
Problem Statement #
We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

Example 1:

Input: [4, 0, 3, 1]
Output: 2
Example 2:

Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7
'''

def CyclicSort(nums):
    i = 0
    while i < len(nums):
        j = nums[i]
        if nums[i] < len(nums) and nums[j] != nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    

    for i in range(len(nums)):
        if nums[i] != i:
            return i
    
nums = [4, 0, 3, 1]
print(CyclicSort(nums))
nums = [8, 3, 5, 2, 4, 6, 0, 1]
print(CyclicSort(nums))