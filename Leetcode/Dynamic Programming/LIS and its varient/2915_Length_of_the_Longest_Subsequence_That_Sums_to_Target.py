# Recursion 
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:

        def solve(index, target):
            if target == 0:
                return 0

            if index >= len(nums) or target < 0:
                return float("-inf")

            take = 1 + solve(index+1, target-nums[index])
            notTake = solve(index+1, target)

            return max(take, notTake)
        
        res = solve(0,target)
        return res if res != float("-inf")  else -1

            
# Memo
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        maps = {}
        def solve(index, target):
            if (index, target) in maps:
                return maps[(index, target)]
            if target == 0:
                return 0

            if index >= len(nums) or target < 0:
                return float("-inf")

            take = 1 + solve(index+1, target-nums[index])
            notTake = solve(index+1, target)

            maps[(index, target)] = max(take, notTake)
            return maps[(index, target)]
        
        res = solve(0,target)
        return res if res != float("-inf")  else -1

            
#Tabulation (#TODO)
