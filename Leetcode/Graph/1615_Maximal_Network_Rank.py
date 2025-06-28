from typing import List
from collections import defaultdict
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        result = 0

        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        
        for i in range(n):
            for j in range(i+1, n):
                ith = len(graph[i])
                jth = len(graph[j])

                summ = ith + jth
                if i in graph[j]:
                    summ -= 1
                result = max(result, summ)
        
        return result


