def largestLocal(grid):
    n = len(grid)
    mat = [[0 for i in range(n-2)] for i in range(n-2)]

    def findMaxVal(mat, row, col):
        maxVal = 0
        for i in range(row, row+3):
            for j in range(col, col+3):
                maxVal = max(maxVal, grid[i][j])
        return maxVal

    for r in range(len(grid)-2):
        for c in range(len(grid)-2):
            mat[r][c] = findMaxVal(grid, r, c)
    
    return mat