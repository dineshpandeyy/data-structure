class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        firstChildren = 0
        # FIRST CHILD CAN ONLY MOVE IN DIAGONAL
        for i in range(n):
            firstChildren += fruits[i][i]
        print(firstChildren)
        
        # SECOND CHILD AT POSITION (0, N-1)
        # HE CAN MOVE IN THREE DIRECTION UNTIL j > i
        @cache
        def secondChild(i,j):
            if i < 0 or i >= n or j < 0 or j >= n:
                return 0
            
            if not j > i:
                return 0
            
            downLeft = fruits[i][j] + secondChild(i+1, j-1)
            below = fruits[i][j] + secondChild(i+1, j)
            downRight = fruits[i][j] + secondChild(i+1, j+1)

            return max(downLeft, below, downRight)


        # THIRD CHILD AT POSITION (N-1,0) 
        # HE CAN MOVE IN THREE DIRECTION UNTIL i > j
        @cache
        def thirdChild(i,j):
            if i < 0 or i >= n or j < 0 or j >= n:
                return 0

            if not i > j:
                return 0
            
            upRight = fruits[i][j] + thirdChild(i-1, j+1)
            side = fruits[i][j] + thirdChild(i, j+1)
            downbelow = fruits[i][j] + thirdChild(i+1, j+1)

            return max(upRight, side, downbelow)
        

        second = secondChild(0, n-1)
        third = thirdChild(n-1, 0)

        return firstChildren + second + third

        