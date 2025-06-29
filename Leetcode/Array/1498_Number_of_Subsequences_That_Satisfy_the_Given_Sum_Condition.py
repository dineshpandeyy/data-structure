class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        i = 0
        j = len(nums) - 1
        result = 0

        while i <= j:
            if nums[i] + nums[j] <= target:
                result = (result + pow(2, j-i)) % MOD
                i += 1
            else:
                j -= 1
        
        return result