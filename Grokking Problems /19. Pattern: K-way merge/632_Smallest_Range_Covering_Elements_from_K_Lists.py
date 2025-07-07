import heapq
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        heap = []
        rightPos = float("-inf")
        leftPos = float("inf")
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], 0, nums[i]))
            rightPos = max(rightPos, nums[i][0])
            leftPos = min(leftPos, nums[i][0])
        
        result = [leftPos, rightPos]

        while heap:
            value, index, arr = heapq.heappop(heap)

            if result[1] - result[0] > rightPos - value:
                result = [value, rightPos]

            if index+ 1 >= len(arr):
                break
            heapq.heappush(heap, (arr[index+1], index+1, arr))
            rightPos = max(rightPos, arr[index+1])

        return result