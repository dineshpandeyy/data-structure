class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        count = 0

        for num in nums:
            if num == 0:
                count += 1
            else:
                count = 0
            result = result + count
        
        return result

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        left = 0
        result = 0

        while left < len(nums):
            length = 0
            if nums[left] == 0:
                while left < len(nums) and nums[left] == 0:
                    length += 1
                    left += 1
            else:
                left += 1
            result += (length * (length + 1)) // 2
        return result
            
# the no of subarray of size of array n is n(n+1) //2.

        