class Solution:
    def numSquares(self, n: int) -> int:
        maps = {}
        def solve(index):
            if index in maps:
                return maps[index]
            if index == 0:
                return 0
            result = float('inf')

            for i in range(1, int(math.sqrt(n))+1):
                if index - i * i >= 0:
                    value = 1 + solve(index - i*i)
                    result = min(result, value)
            maps[index] = result
            return maps[index] 
        
        return solve(n)
        