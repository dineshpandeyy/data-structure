class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maximumValue = max(nums)
        result = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == maximumValue and nums[i-1] == maximumValue:
                count += 1
                result = max(result, count)
            else:
                count = 1
        
        return result



        