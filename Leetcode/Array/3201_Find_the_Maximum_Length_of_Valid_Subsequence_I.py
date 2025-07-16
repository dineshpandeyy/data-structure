class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        evenCount = 0
        oddCount = 0

        for num in nums:
            if num % 2 == 0:
                evenCount += 1
            else:
                oddCount += 1
        
        # Alternative
        alternative = nums[0] % 2
        count = 1
        for i in range(1, len(nums)):
            if nums[i] % 2 != alternative:
                count += 1
                alternative = not alternative

        return max(evenCount, oddCount, count)


        