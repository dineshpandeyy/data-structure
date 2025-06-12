def numberOfIsland(grid):
    result = 0
    m = len(grid)
    n = len(grid[0])
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                dfs(grid,i,j,m,n)
                result += 1
    
    return result

def dfs(grid,row,col,m,n):
    if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] != "1":
        return 0
    
    grid[row][col] = "#"
    dfs(grid,row-1,col,m,n)
    dfs(grid,row+1,col,m,n)
    dfs(grid,row,col+1,m,n)
    dfs(grid,row,col-1,m,n)


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numberOfIsland(grid))
