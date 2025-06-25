from collections import deque
class Solution:
    def minimumObstacles(grid) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque([(0,0,0)]) # starting point (0,0) and obstacles
        visited = set()

        while q:
            start, end, obstacles = q.popleft()
            if start == m -1 and end == n-1:
                return obstacles
            
            if (start,end) in visited:
                continue 
            visited.add((start,end))
            
            direction = [(-1,0),(0,-1), (1,0),(0,1)]

            for dr,dc in direction:
                rc = dr + start
                cc = dc + end

                if rc < 0 or rc >= m or cc < 0 or cc >= n:
                    continue
                
                if grid[rc][cc] == 0:
                    q.appendleft((rc,cc,obstacles))
                else:
                    q.append((rc,cc,obstacles+1))
                


        