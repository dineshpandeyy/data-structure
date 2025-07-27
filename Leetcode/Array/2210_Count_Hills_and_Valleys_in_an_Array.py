class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        i = 0
        j = 1

        while j+ 1 < len(nums):
            if (nums[j] > nums[i] and nums[j] > nums[j+1]) or (nums[j] < nums[i] and nums[j] < nums[j+1]):
                count += 1
                i = j
                j += 1
            else:
                j += 1
        return count
        