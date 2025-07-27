class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        result = []

        for num in reversed(heights):

            visible = 0

            while stack and stack[-1] < num:
                visible += 1
                stack.pop()
            
            if stack:
                visible += 1
            
            result.append(visible)
            stack.append(num)
        
        return result[::-1]


            

        