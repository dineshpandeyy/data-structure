class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maxValue = max(nums)
        if maxValue < 0:
            return maxValue
        maps = set()
        result = 0
        for num in nums:
            if num in maps or num < 0:
                continue
            result += num
            maps.add(num)
        
        return result




        