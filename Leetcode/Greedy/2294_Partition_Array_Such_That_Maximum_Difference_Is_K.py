class Solution:
    def partitionArray(self, nums, k: int) -> int:
        nums.sort()

        minVal = nums[0]
        count = 1

        for i in range(1, len(nums)):
            value = nums[i]
            if value - minVal > k:
                count += 1
                minVal = value
        
        return count