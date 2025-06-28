from collections import deque

class Solution:
    def highestPeak(self, isWater):
        m = len(isWater)
        n = len(isWater[0])
        matrix = [[-1 for i in range(n)] for j in range(m)] 

        q = deque([])
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    matrix[i][j] = 0
                    q.append((i,j))
        
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            for i in range(len(q)):
                row, col = q.popleft()

                for dr, dc in direction:
                    rr = row + dr
                    cc = col + dc

                    if rr < 0 or rr >= m or cc < 0 or cc >= n or matrix[rr][cc] != -1:
                        continue
                    matrix[rr][cc] = matrix[row][col] + 1
                    q.append((rr,cc))
        
        return matrix



