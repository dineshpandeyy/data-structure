class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @cache
        def solve(index, curr):
            if index >= len(nums) or curr > target:
                return 0
            
            if curr == target:
                return 1
            
            take = solve(0, curr+nums[index])
            nottake = solve(index+1, curr)

            return take + nottake
        
        return solve(0, 0)


        