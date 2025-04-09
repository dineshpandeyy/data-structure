'''
Problem Statement #
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; 
after removing the duplicates in-place return the new length of the array.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
Example 2:

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
'''


def removeElement(nums):
    i = 0
    result = 1

    for j in range(1, len(nums)):
        if nums[j] == nums[i]:
            j += 1
        else:
            i = j
            result += 1
    
    return result

print(removeElement([2, 3, 3, 3, 6, 9, 9]))
print(removeElement([2, 2, 2, 11]))




