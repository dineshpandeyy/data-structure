class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Build left minimums
        leftMin = [0] * n
        leftMin[0] = nums[0]

        for i in range(1,len(nums)):
            leftMin[i] = min(leftMin[i-1], nums[i])
        
        rightMin = [0] * n
        rightMin[-1] = nums[-1]

        for i in range(len(nums)-2,-1,-1):
            rightMin[i] = min(rightMin[i+1], nums[i])

        result = float("inf")
        for i in range(1,len(nums)-1):
            left = leftMin[i-1]
            right = rightMin[i+1]

            if left < nums[i] and nums[i] > right:
                result = min(result, left+right+nums[i])
        
        return result if result != float("inf") else -1



        