class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 != 0:
            return False
        maps = {}
        
        def solve(index, target):
            if (index, target) in maps:
                return maps[(index, target)]
            if index >= len(nums):
                return target == 0
            
            if target < 0:
                return False
            
            take = 0
            if nums[index] <= target:
                take = solve(index+1, target-nums[index])
            notTake = solve(index+1, target)

            maps[(index, target)] = take or notTake
            return maps[(index, target)]
        
        return solve(0,sum(nums)/2)
        