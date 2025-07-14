import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for num in arr:
            diff = abs(x - num)
            heap.append((diff, num))
        
        heapq.heapify(heap)

        res = []
        while k > 0:
            _, num = heapq.heappop(heap)
            res.append(num)
            k -= 1
        res.sort()
        return res



# (2, 1), (1, 2), (0,3), (1, 4) , (2,5)
#  [3,2,4,1]