class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        memo = {}
        def solve(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if j - i < 2:
                return 0  # No triangle can be formed
            result = float("inf")
            for k in range(i+1,j):
                result = min(result, values[i]* values[j] * values[k] + solve(i,k)+solve(k,j))
            memo[(i,j)] = result
            return memo[(i,j)]

        return solve(0,len(values)-1)

     
        