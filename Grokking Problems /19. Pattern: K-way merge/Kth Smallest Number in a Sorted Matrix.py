'''
Problem Statement #
Given an 
N
∗
N
N∗N matrix where each row and column is sorted in ascending order, 
find the Kth smallest element in the matrix.

Example 1:

Input: Matrix=[
    [2, 6, 8], 
    [3, 7, 10],
    [5, 8, 11]
  ], 
  K=5
Output: 7 #2 3 5 6 7 8 10 11
Explanation: The 5th smallest number in the matrix is 7.
'''
import heapq

def solve(matrix, k):
    heap = []

    for i in range(len(matrix)):
        heapq.heappush(heap, (matrix[i][0], 0, matrix[i]))
      
    while k - 1:
        value, index, mat = heapq.heappop(heap)

        if index < len(mat) - 1:
            heapq.heappush(heap, (mat[index+1], index+1, mat))
          
        k -= 1
    
    return heap[0][0]
      
    
matrix=[
    [2, 6, 8], 
    [3, 7, 10],
    [5, 8, 11]
  ], 
K=5
print(solve(matrix, K))