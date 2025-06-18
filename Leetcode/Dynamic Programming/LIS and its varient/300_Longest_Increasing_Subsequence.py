# Buttom up
def lengthOfLIS(nums) -> int:
    dp = [1] * len(nums)


    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[j]+1, dp[i])
    
    return max(dp)


# Recursion
class Solution:
    def lengthOfLIS(nums) -> int:
        def solve(currIndex, prevIndex):
            if currIndex >= len(nums):
                return 0
            
            pick = 0
            if prevIndex == -1 or nums[prevIndex] < nums[currIndex]:
                pick = 1 + solve(currIndex+1,currIndex)
            notpick = solve(currIndex+1,prevIndex)

            return max(pick, notpick)
        
        return solve(0, -1)
        

