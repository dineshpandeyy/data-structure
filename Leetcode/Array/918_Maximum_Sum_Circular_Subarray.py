class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def minSubArray():
            summ = 0
            result = nums[0]

            for num in nums:
                summ += num
                result = min(result,summ)
                if summ > 0:
                    summ = 0
            
            return result
        
        def maxSubArray():
      
            summ = 0
            result = nums[0]

            for num in nums:
                summ += num
                result = max(result,summ)
                if summ < 0:
                    summ = 0
            
            return result
        
        a =  minSubArray()
        b =  maxSubArray()

        # If all numbers are negative, total == min_sum
        if b < 0:
            return b
        
        return max(b, sum(nums) -a)
        