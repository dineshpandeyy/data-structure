from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(points) -> int:
        graph = defaultdict(list)

        for i in range(len(points)):
            for j in range(i+1,len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)

                graph[i].append((j, distance))
                graph[j].append((i, distance))


        visited = set()
        pq = [(0, 0)] # (weight, node)
        totalWeighSum = 0

        while pq:
            wei, pt = heapq.heappop(pq)
            if pt in visited:
                continue
            visited.add(pt)
            totalWeighSum += wei

            for node, cost in graph[pt]:
                if node not in visited:
                    heapq.heappush(pq, (cost,node))
                
        return totalWeighSum



        



        