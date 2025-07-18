class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums)
        n = len(nums) // 3

        leftHeap = []
        rightHeap = []

        leftMin = [0] * N # we have to remove biggerNumber from this side
        rightMax = [0] * N # we have to remove smallernumber from this side

        currSum = 0
        for i in range(2*n):
            heapq.heappush(leftHeap, -nums[i])
            currSum += nums[i]
            if len(leftHeap) > n:
                val = -heapq.heappop(leftHeap)
                currSum -= val
          
            leftMin[i] = currSum

        
        currSum = 0
        for i in range(N-1,n-1,-1):
            heapq.heappush(rightHeap, nums[i])
            currSum += nums[i]
            if len(rightHeap) > n:
                val = heapq.heappop(rightHeap)
                currSum -= val
            rightMax[i] = currSum
        
        result = float("inf")
            
        for i in range(n - 1, 2 * n):
            result = min(result, leftMin[i] - rightMax[i + 1])
        
        return result


            




        