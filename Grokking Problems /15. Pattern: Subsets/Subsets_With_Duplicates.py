'''
Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:

Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]
Example 2:

Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3] 
'''

class Solution:
    def subsets(self,nums):
        self.res = []
        nums.sort()
        self.solve(nums,0, [])
        return self.res

    def solve(self,nums,index,currSubSet):
        if index == len(nums):
            self.res.append(currSubSet[::])
            return 
        
        currSubSet.append(nums[index])
        self.solve(nums,index+1,currSubSet)
        currSubSet.pop()

        while index + 1 < len(nums) and nums[index] == nums[index+1]:
            index += 1
        self.solve(nums,index+1,currSubSet)


nums = [1, 3,3]
sol = Solution()

result = sol.subsets(nums)
print(result)



        

