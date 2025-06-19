# Bottom up
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ [0 for i in range(n)] for j in range(m)]

        # filling first row as its always one
        for i in range(n):
            dp[0][i] = 1
        
        # filling first column as it always one
        for i in range(m):
            dp[i][0] = 1

        for i in range(1,m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]
    

#Memo
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        maps = {}
    
        def solve(down,left):
            if down == m - 1 and left == n - 1:
                return 1
            
            if down < 0 or down >= m or left < 0 or left >=n:
                return 0
            
            if (down,left) in maps:
                return maps[(down,left)]
            
            d =  solve(down+1,left)
            l = solve(down,left+1)

            maps[(down,left)] = d + l
            return maps[(down,left)]
        

        return solve(0,0)


#Recursion
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def solve(down,left):
            if down == m - 1 and left == n - 1:
                return 1
            
            if down < 0 or down >= m or left < 0 or left >=n:
                return 0
            
            d =  solve(down+1,left)
            l = solve(down,left+1)

            return d + l
        

        return solve(0,0)
        
        