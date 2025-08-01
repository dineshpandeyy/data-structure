class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] < nums[j] < nums[k]:
                        return True
        
        return False

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstSmaller = float("inf")
        secondSmaller = float("inf")

        for num in nums:
            if num <= firstSmaller:
                firstSmaller = num
            elif num <= secondSmaller:
                secondSmaller = num
            else:
                return True
        return False
        