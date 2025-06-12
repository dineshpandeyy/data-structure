'''
Given a set with distinct elements, find all of its distinct subsets.

Example 1:
Input: [1, 3]
Output: [], [1], [3], [1,3]

Example 2:
Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
'''

class  Solution:
    def subsets(self, nums):
        self.res = []

        self.solve(nums, 0, [])
        return self.res


    def solve(self, nums, index, curr):
        if index == len(nums):
            self.res.append(curr[:])
            return
        
      
        curr.append(nums[index])
        self.solve(nums, index+1, curr)

        curr.pop()
        self.solve(nums,index+1,curr)
    

nums = [1, 3]
sol = Solution()
print(sol.subsets(nums))