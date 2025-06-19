#Recursion
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        def solve(down,left):

            if down < 0 or down >= m or left < 0 or left >=n or obstacleGrid[down][left] == 1:
                return 0

            if down == m - 1 and left == n - 1:
                return 1

            d =  solve(down+1,left)
            l = solve(down,left+1)

            return d + l
        

        return solve(0,0)
        
#Memo
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        maps = {}
        def solve(down,left):

            if down < 0 or down >= m or left < 0 or left >=n or obstacleGrid[down][left] == 1:
                return 0

            if down == m - 1 and left == n - 1:
                return 1
            
            if (down, left) in maps:
                return maps[(down, left)]

            d =  solve(down+1,left)
            l = solve(down,left+1)

            maps[(down, left)] = d + l
            return maps[(down, left)]
        

        return solve(0,0)
    
# Bottom  up
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [ [0 for i in range(n)] for j in range(m)]

        # filling first row as its always one
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
        
        # filling first column as it always one
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for i in range(1,m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0

        return dp[-1][-1]
        
