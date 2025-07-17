# this question is similar to 3201. Find the Maximum Length of Valid Subsequence I
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        m = len(nums)
        dp = [[1 for i in range(m)] for i in range(k)]
        result = 0
        for i in range(1, len(nums)):
            for j in range(i):
                mod = (nums[i] + nums[j]) % k
                dp[mod][i] = max(dp[mod][i], dp[mod][j]+1)
                result = max(result, dp[mod][i])
        return result
        
