class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        def solve(i, j):
            if i == len(triangle) - 1:
                return triangle[i][j]
            
            below = triangle[i][j] + solve(i+1,j)
            belowSide = triangle[i][j] + solve(i+1,j+1)

            return min(below, belowSide)
        
        return solve(0, 0)

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        maps = {}
        def solve(i, j):
            if (i, j) in maps:
                return maps[(i, j)]
            if i == len(triangle) - 1:
                return triangle[i][j]
            
            below = triangle[i][j] + solve(i+1,j)
            belowSide = triangle[i][j] + solve(i+1,j+1)

            maps[(i, j)] = min(below, belowSide)
            return maps[(i, j)]
        
        return solve(0, 0)
        
# TODO (Tabulation)