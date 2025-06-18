from collections import defaultdict
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for i in range(len(rooms)):
            graph[i].extend(rooms[i])
        
        visited = set()
        self.dfs(0,graph,visited)
        
        return len(visited) == len(rooms)

    
    def dfs(self,index,graph,visited):
        visited.add(index)
        for node in graph[index]:
            if node not in visited:
                self.dfs(node,graph,visited)