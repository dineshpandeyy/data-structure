class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def disWorks(mid):
            prevPos = position[0]
            ballCount = 1
            
            for i in range(1,len(position)):
                curr = position[i]

                if (curr - prevPos) >= mid:
                    prevPos = curr
                    ballCount += 1

                    if ballCount >= m:
                        break
            
            return ballCount == m


        position.sort()
        left = 1
        right = position[-1] - position[0]
        result = 0

        while left <= right:
            mid = (left+right) // 2
            if disWorks(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result



        