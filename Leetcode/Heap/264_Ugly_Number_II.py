class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1

        minHeap = [1]
        visitedSet = set()
        count = 0

        while True:
            num = heapq.heappop(minHeap)
            count += 1

            if count == n:
                return num

            for factor in [2, 3, 5]:
                newNum = num * factor
                if newNum not in visitedSet:
                    heapq.heappush(minHeap, newNum)
                    visitedSet.add(newNum)

