# Solution 1
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def kWorks(mid):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)
            return hours <= h

        minK = 1
        maxK = max(piles)

        while minK <= maxK:
            mid = (minK+maxK) // 2

            if kWorks(mid):
                maxK = mid
            else:
                minK = mid + 1
        
        return maxK

            
# Solution 2
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        def kWorks(mid):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)
            return hours <= h

        minK = 1
        maxK = max(piles)

        while minK < maxK:
            mid = (minK+maxK) // 2

            if kWorks(mid):
                maxK = mid
            else:
                minK = mid + 1
        
        return maxK
        

        