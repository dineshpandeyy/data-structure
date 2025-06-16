from collections import defaultdict
from collections import deque

def validPath(n, edges, source, destination):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    q = deque([source])
    visited = set()
    visited.add(source)


    while q:
        node = q.popleft()
        if node == destination:
            return True
        
        for pt in graph[node]:
            if pt not in visited:
                q.append(pt)
                visited.add(pt)
    
    return False
