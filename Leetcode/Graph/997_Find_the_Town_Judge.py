class Solution:
    def findJudge(n, trust) -> int:
        outDegree = [0] * (n + 1)
        inDegree = [0] * (n + 1)

        for a, b in trust:
            outDegree[a] += 1
            inDegree[b] += 1
        
        for i in range(1,len(outDegree)):
            if outDegree[i] == 0 and inDegree[i] == n-1:
                return i
        
        return -1


        