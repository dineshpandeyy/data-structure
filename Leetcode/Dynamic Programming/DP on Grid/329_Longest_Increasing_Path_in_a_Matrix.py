# This question is similar to 2328. Number of Increasing Paths in a Grid
# Leetcode/Dynamic Programming/DP on Grid/2328_Number_of_Increasing_Paths_in_a_Grid.py
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        curr_length = [0] # 
        memo = {}
        def dfs(i,j,prevNum):

            if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] <= prevNum:
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]

            down = 1 + dfs(i-1,j,matrix[i][j])  # 0 # 0
            up = 1 + dfs(i+1,j,matrix[i][j])  # 0 # 3
            left  = 1 + dfs(i,j+1,matrix[i][j])  # 0 # 0
            right  = 1 + dfs(i,j-1,matrix[i][j])  # 0 # 1 
            total_length = max(up,left,right,down)
            memo[(i,j)]= total_length
            return memo[(i,j)]

        maxLen = 1
        for i in range(m):
            for j in range(n):
                maxLen = max(maxLen, dfs(i,j,-1))

        return maxLen
            