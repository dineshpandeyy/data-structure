class Solution:
    def removeStones(self, stones) -> int:
        n = len(stones)
        parent = [i for i in range(n)]
        rank = [0] * (n)

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            elif rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
        
        for i in range(n):
            for j in range(i+1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i,j)
        
        group = set()
        for i in range(n):
            group.add(find(i))

        return n - len(group)




        