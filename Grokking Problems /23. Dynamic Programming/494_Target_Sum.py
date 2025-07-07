class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        maps = {}

        def solve(index, currSum):
            if (index, currSum) in maps:
                return maps[(index, currSum)]
            if index == len(nums):
                if currSum == target:
                    return 1
                else:
                    return 0
            
            # plus
            plus = solve(index+1, currSum+nums[index])
            # minun
            minus = solve(index+1, currSum-nums[index])

            maps[(index, currSum)] = plus + minus
            return maps[(index, currSum)]
        
        return solve(0,0)