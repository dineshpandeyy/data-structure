# This question is similar to 329. Longest Increasing Path in a Matrix
#Leetcode/Dynamic Programming/DP on Grid/329_Longest_Increasing_Path_in_a_Matrix.py
class Solution:
    def countPaths(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7
        memo = {}

        def dfs(i,j,prevNum):
            if i < 0 or i >= m or j < 0 or j >=n or grid[i][j] <= prevNum:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            up = dfs(i-1,j,grid[i][j])
            down = dfs(i+1,j,grid[i][j])
            left = dfs(i,j+1,grid[i][j])
            right = dfs(i,j-1,grid[i][j])
            memo[(i,j)] = (1 + up + down + left + right) % MOD
            return memo[(i,j)]

        result = 0
        for i in range(m):
            for j in range(n):
                result = (result +  dfs(i,j,-1))% MOD
        return result


        