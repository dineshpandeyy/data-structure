class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedHeight = sorted(heights)

        res = 0
        for i in range(len(sortedHeight)):
            if heights[i] != sortedHeight[i]:
                res += 1
        return res
# [1,1,4,2,1,3]
# [1,1,1,2,3,4]