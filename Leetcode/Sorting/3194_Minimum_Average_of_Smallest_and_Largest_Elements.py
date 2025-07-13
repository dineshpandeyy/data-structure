import deque
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        res = []
        q = deque([])
        for num in sorted(nums):
            q.append(num)

        while q:
            small = q.popleft()
            large = q.pop()
            val = (small + large) / 2
            res.append(val)
        
        return min(res)

