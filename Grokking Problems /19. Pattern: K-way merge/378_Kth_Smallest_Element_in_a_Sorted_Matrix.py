'''
Problem Statement #
Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
Output: 4
Explanation: The 5th smallest number among all the arrays is 4, this can be verified from the merged 
list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:

Input: L1=[5, 8, 9], L2=[1, 7], K=3
Output: 7
Explanation: The 3rd smallest number among all the arrays is 7.
'''
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []

        for i in range(len(matrix)):
            if len(matrix[i]) >0:
                heapq.heappush(heap, (matrix[i][0], 0, matrix[i]))

        while k - 1:
            value, index, arr = heapq.heappop(heap)
            if index < len(arr)-1:
                heapq.heappush(heap, (arr[index+1], index+1, arr))
            k -= 1
        
        return heap[0][0]
        

sol = Solution()
R = [[2, 6, 8],[3, 6, 7],[1, 3, 4]]
K=5   
print(sol.kthSmallest(R,K))  

R=[[5, 8, 9],[1, 7]] 
K=3
print(sol.kthSmallest(R,K))  
