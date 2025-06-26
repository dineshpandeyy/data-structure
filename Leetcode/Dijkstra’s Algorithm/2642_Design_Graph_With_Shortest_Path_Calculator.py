from collections import defaultdict
import heapq
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = defaultdict(list)

        for a, b, c in edges:
            self.graph[a].append((b,c))

    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append((edge[1], edge[2]))
        
    def shortestPath(self, node1: int, node2: int) -> int:

        pq = [(0,node1)] # (distance, node)
        finalDis = [float("inf")] * self.n
        finalDis[node1] = 0

        while pq:
            dis, node = heapq.heappop(pq)
            if node == node2:
                return dis
            
            for pt, distance in self.graph[node]:
                newDis = dis + distance
                if newDis < finalDis[pt]:
                    finalDis[pt] = newDis
                    heapq.heappush(pq, (newDis, pt))
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)