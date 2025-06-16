class Solution:
    def findCenter(edges) -> int:
        inDegree = [0] * (len(edges)+2)
# [0,1,3,1,1]
#  0 1 2 3 4
        for a, b in edges:
            inDegree[a] += 1
            inDegree[b] += 1
        
        for i in range(1,len(edges)+2):
            if inDegree[i] != 1:
                return i