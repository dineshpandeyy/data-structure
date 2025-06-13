'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 
Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''

def permutation(nums):
    res = []
    used = set()

    def solve(index, curr):
        if index == len(nums):
            res.append(curr[:])
            return 
        
        for num in nums:
            if num not in used:
                used.add(num)
                curr.append(num)
                solve(index+1, curr)
                used.remove(num)
                curr.pop()


    
    solve(0,[])
    return res


nums = [1,2,3]
print(permutation(nums))


