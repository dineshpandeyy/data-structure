from collections import defaultdict
import heapq
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        graph = defaultdict(list)
        for src, dest, wei in edges:
            graph[src].append((dest,wei))
            graph[dest].append((src,wei))

        def dijkstra(source):
            distance = [float('inf')] * n
            distance[source] = 0
            pq = [(0, source)]  # (distance, node)

            while pq:
                current_dist, current_node = heapq.heappop(pq)
                for neighbor, weight in graph[current_node]:
                    new_dist = current_dist + weight
                    if new_dist < distance[neighbor]:
                        distance[neighbor] = new_dist
                        heapq.heappush(pq, (new_dist, neighbor))

            result = 0
            for dis in distance:
                if dis <= distanceThreshold:
                    result += 1
            
            return result

        result = -1
        nodes = float("inf")
        for src in range(n):
            numberOfNodes = dijkstra(src)
            if numberOfNodes <= nodes:
                nodes = numberOfNodes
                result = src
        
        return result


        