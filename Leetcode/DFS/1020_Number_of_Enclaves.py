class Solution:
    def numEnclaves(self, grid) -> int:

        # DFS in first row and last row
        for i in range(len(grid[0])):
            # First Row
            if grid[0][i] == 1:
                self.dfs(grid, 0, i) 
            # Last Row
            if grid[len(grid)-1][i] == 1:
                self.dfs(grid, len(grid)-1, i)

        
         # DFS in first col and last col
        for i in range(len(grid)):
            # First col
            if grid[i][0] == 1:
                self.dfs(grid, i, 0) 
            # Last col
            if grid[i][len(grid[0])-1] == 1:
                self.dfs(grid, i, len(grid[0])-1)

        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += 1
        return res
    
    def dfs(self,grid,row,col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != 1:
            return 
        grid[row][col] = "#"
        self.dfs(grid,row-1,col)
        self.dfs(grid,row+1,col)
        self.dfs(grid,row,col-1)
        self.dfs(grid,row,col+1)


        