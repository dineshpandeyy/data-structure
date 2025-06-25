from collections import deque

class Solution:
    def minCost(grid) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque([(0,0,0)]) # starting point (0,0) and cost
        visited = set()

        while q:
            start, end, cost = q.popleft()
            if start == m -1 and end == n-1:
                return cost

            if (start,end) in visited:
                continue
            
            visited.add((start,end))

            direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for i, (dr,dc) in enumerate(direction):
                rc = dr + start
                cc = dc + end

                if rc < 0 or rc >= m or cc < 0 or cc >= n:
                    continue
                
                if grid[start][end] == i+1:
                    q.appendleft((rc,cc,cost))
                else:
                    q.append((rc,cc,cost+1))
        