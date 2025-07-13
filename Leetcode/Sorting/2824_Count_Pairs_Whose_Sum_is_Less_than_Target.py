# 0(N)
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                pair = nums[i] + nums[j]
                if pair < target:
                    res += 1
        
        return res

#nlogn
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        result = 0

        while left < right:
            summ = nums[left] + nums[right]
            if summ < target:
                result += right - left
                left += 1
            else:
                right -= 1
        
        return result
        