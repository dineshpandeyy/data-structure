from typing import List
from collections import defaultdict, deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)

        def bfs(src):
            q = deque([src])
            color[src] = 1

            while q:
                node = q.popleft()

                for pt in graph[node]:
                    if color[pt] == color[node]:
                        return False

                    if color[pt] == -1:
                        q.append(pt)
                        color[pt] = 1 - color[node]
            return True


        for i in range(len(color)):
            if color[i] == -1:
                if not bfs(i):
                    return False
        
        return True

        