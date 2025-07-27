# Copy and paste the code to 1011. Capacity To Ship Packages Within D Days, it will pass. 
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        r = sum(nums)
        l = max(nums)

        def canSplit(mid):
            currSum = 0
            noOfArray = 0

            for num in nums:
                currSum += num
                if currSum > mid:
                    noOfArray += 1
                    currSum = num
            return noOfArray + 1<= k

        while l <= r:
            mid = (l+r) // 2

            if canSplit(mid):
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return result



        