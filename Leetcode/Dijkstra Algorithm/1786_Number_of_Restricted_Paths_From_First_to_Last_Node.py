from collections import defaultdict
import heapq
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:

        MOD = 10**9 + 7
        distance  = [float("inf")] * (n + 1)
        distance[n] = 0
        pq = [(0,n)] # distance , node

        graph = defaultdict(list)

        for src, des, wei in edges:
            graph[src].append((des,wei))
            graph[des].append((src,wei))
        
        while pq:
            dis, node = heapq.heappop(pq)

            for nei, wei in graph[node]:
                newDis = dis + wei
                if newDis < distance[nei]:
                    distance[nei] = newDis
                    heapq.heappush(pq, (newDis, nei))
        memo = {}
        def dfs(src):
            if src == n:
                return 1
            if src in memo:
                return memo[src]

            answer = 0
            for des, wei in graph[src]:
                if distance[des] < distance[src]:
                    answer = (answer + dfs(des)) % MOD

            memo[src] = answer
            return answer

        return dfs(1)
    
        



        


        