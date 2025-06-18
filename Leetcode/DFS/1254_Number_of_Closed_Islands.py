'''
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.
Example 1:
Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:
Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example 3:
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 
Constraints:
1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
'''

class Solution:
    def closedIsland(self, grid) -> int:
        col = len(grid[0])
        row = len(grid)

        # DFS in first row and last row
        for i in range(col):
            # first row
            self.dfs(grid,0,i,row,col)
            # last row
            self.dfs(grid,row-1,i,row,col)

        # DFS in first col and last col
        for i in range(row):
            self.dfs(grid,i,0,row,col)
            self.dfs(grid,i,col-1,row,col)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.dfs(grid,i,j,row,col)
                    res += 1
        
        return res

    def dfs(self,grid,r,c,m,n):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != 0:
            return 
        grid[r][c] = 1
        self.dfs(grid,r-1,c,m,n)
        self.dfs(grid,r+1,c,m,n)
        self.dfs(grid,r,c-1,m,n)
        self.dfs(grid,r,c+1,m,n)




        