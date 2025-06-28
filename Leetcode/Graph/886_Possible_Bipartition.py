from typing import List
from collections import defaultdict, deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color = [-1] * (n+ 1)
        graph = defaultdict(list)

        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

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


        for i in range(1, len(color)):
            if color[i] == -1:
                if not bfs(i):
                    return False
        
        return True
        