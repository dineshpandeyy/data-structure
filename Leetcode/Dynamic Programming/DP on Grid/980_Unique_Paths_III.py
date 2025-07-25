class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        startX = 0
        startY = 0
        m = len(grid)
        n = len(grid[0])

        emptySquare = 1 # Including starting point as well so 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    startX = i
                    startY = j
                elif grid[i][j] == 0:
                    emptySquare += 1
        

        self.result = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(i, j, currEmptyCell):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == -1:
                return 0
            if grid[i][j] == 2:
                if currEmptyCell == emptySquare:
                    self.result += 1
                    return 
            originalValue = grid[i][j]
            grid[i][j] = -1
            for dr, dc in directions:
                rc = i + dr
                cc = j + dc
                dfs(rc, cc, currEmptyCell+1)

            grid[i][j]  = originalValue
        
        dfs(startX, startY, 0)
        return self.result
