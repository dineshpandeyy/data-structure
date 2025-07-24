class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1
        
        q = deque([])

        for i, val in enumerate(indegree):
            if val == 0:
                q.append(i)

        orderMap = defaultdict(set)

        while q:
            node = q.popleft()
            for pt in graph[node]:
                orderMap[pt].add(node)
                for item in orderMap[node]:
                    orderMap[pt].add(item)
                indegree[pt] -= 1
                if indegree[pt] == 0:
                    q.append(pt)
        
        res = []
        for a, b in queries:
            if a in orderMap[b]:
                res.append(True)
            else:
                res.append(False)
        return res


        