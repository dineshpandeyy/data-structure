'''
Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat 
numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue; and since our 
input array also consists of three different numbers that is why it is called Dutch National 
Flag problem.

Example 1:

Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]
             r
[1, 0, 2, 1, 0]
 l
 m
Example 2:

Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]
'''

'''
We can use a Two Pointers approach while iterating through the array. 
Let’s say the two pointers are called low and high which are pointing to the 
first and the last element of the array respectively. So while iterating, we will move all 
0s before low and all 2s after high so that in the end, all 1s will be between low and high.
'''

def sort(nums):
    low = 0
    high = len(nums) - 1
    mid = 0

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1
    return nums


nums = [1, 0, 2, 1, 0]
print(sort(nums))

nums = [2, 2, 0, 1, 2, 0]
print(sort(nums))
