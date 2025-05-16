'''
Given an array arr[] of size n, having distinct integers from 1 to n, the task is to sort the array.

Input: arr[] = { 2, 1, 5, 4, 3} 
Output: {1, 2, 3, 4, 5}

Input: arr[] = {1, 2, 3, 4, 5, 6} 
Output: {1, 2, 3, 4, 5, 6} 

'''

def CyclicSort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[j] != nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums

nums = [2, 1, 5, 4, 3]
print(CyclicSort(nums))
nums = [1, 2, 3, 4, 5, 6]
print(CyclicSort(nums))

        