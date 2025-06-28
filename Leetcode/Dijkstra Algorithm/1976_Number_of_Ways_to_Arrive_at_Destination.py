class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        distance  = [float("inf")] * n
        distance[0] = 0
        pq = [(0,0)] # distance , node

        graph = defaultdict(list)

        for src, des, wei in roads:
            graph[src].append((des,wei))
            graph[des].append((src,wei))
        
        countWays = [0] * n
        countWays[0] = 1

        while pq:
            dis, node = heapq.heappop(pq)

            for nei, wei in graph[node]:
                newDis = dis + wei
                if newDis < distance[nei]:
                    distance[nei] = newDis
                    heapq.heappush(pq, (newDis, nei))
                    countWays[nei] = (countWays[node]) % MOD
                elif newDis == distance[nei]:
                    countWays[nei] = (countWays[nei] + countWays[node])%MOD
        
        return countWays[-1]



        