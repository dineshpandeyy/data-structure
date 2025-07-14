# Recursion
class Solution:
    def tribonacci(self, n: int) -> int:

        def solve(index):
            if index <= 0:
                return 0
            elif index == 1:
                return 1
            
            return solve(index-1) + solve(index-2) + solve(index-3)
        
        return solve(n)

# Memo
class Solution:
    def tribonacci(self, n: int) -> int:
        maps = {}
        def solve(index):
            if index in maps:
                return maps[index]
            if index <= 0:
                return 0
            elif index == 1:
                return 1
            
            maps[index] = solve(index-1) + solve(index-2) + solve(index-3)
            return maps[index]
        
        return solve(n)

# Tabulation
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, len(dp)):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
        return dp[-1]
      


