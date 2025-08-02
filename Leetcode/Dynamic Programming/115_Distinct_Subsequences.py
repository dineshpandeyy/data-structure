class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        maps = {}
        def solve(i,j):
            if j == len(t):
                return 1 
            
            if i == len(s):
                return 0
            
            if (i,j) in maps:
                return maps[(i,j)]

            matched = 0
            if s[i] == t[j]:
                maps[(i,j)] = solve(i+1,j+1) + solve(i+1,j)
                return maps[(i,j)]
            maps[(i,j)] = solve(i+1,j)
            return maps[(i,j)]
        
        return solve(0,0)
        

class Solution:
    def numDistinct(self, s: str, t: str) -> int:


        def solve(i,j):
            if j == len(t):
                return 1 
            
            if i == len(s):
                return 0

            matched = 0
            if s[i] == t[j]:
                return solve(i+1,j+1) + solve(i+1,j)
            return solve(i+1,j)
        
        return solve(0,0)
        