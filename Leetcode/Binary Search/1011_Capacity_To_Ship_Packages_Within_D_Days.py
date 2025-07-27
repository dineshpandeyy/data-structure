class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        r = sum(weights)
        l = max(weights)

        def canSplit(mid):
            currSum = 0
            noOfArray = 0

            for num in weights:
                currSum += num
                if currSum > mid:
                    noOfArray += 1
                    currSum = num
            return noOfArray + 1 <= days

        while l <= r:
            mid = (l+r) // 2

            if canSplit(mid):
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return result
        