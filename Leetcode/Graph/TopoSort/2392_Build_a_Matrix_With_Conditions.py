from typing import List
from collections import defaultdict, deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        def toposort(conditions):
            graph = defaultdict(list)
            indegree = [0] * (k + 1)

            for a, b in conditions:
                graph[a].append(b)
                indegree[b] += 1
            
            q = deque([])
            for i in range(1, k + 1):
                if indegree[i] == 0:
                    q.append(i)

            result = []

            while q:
                node = q.popleft()
                result.append(node)

                for pt in graph[node]:
                    indegree[pt] -= 1
                    if indegree[pt] == 0:
                        q.append(pt)
            
            return result if len(result) == k else []
        

        rowsort = toposort(rowConditions) #[1,3,2]
        colsort = toposort(colConditions) #[3, 2,1]

        if not rowsort or not colsort:
            return []

        matrix = [[0 for i in range(k)] for i in range(k)]

        for i in range(k):
            val = rowsort[i]
            colIndex = colsort.index(val)
            matrix[i][colIndex] = val
        
        return matrix
