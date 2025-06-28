from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = defaultdict(list)
        for (a, b), prob in zip(edges, succProb):
            graph[a].append((prob,b))
            graph[b].append((prob,a))
        
        distance = [0] * n
        distance[start_node] = 0
        pq = [(-1, start_node)]  # (distance, node)

        while pq:
            current_dist, current_node = heapq.heappop(pq)
            current_dist = current_dist * -1

            if current_node == end_node:
                return current_dist

            for weight, neighbor in graph[current_node]:
                new_dist = current_dist * weight
                if new_dist > distance[neighbor]:
                    distance[neighbor] = new_dist
                    heapq.heappush(pq, (-new_dist, neighbor))
        return 0


        