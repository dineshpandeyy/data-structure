class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:

        maps = defaultdict(int)

        for num in basket1:
            maps[num] += 1
        
        for num in basket2:
            maps[num] -= 1

        arr = []
        for key, value in maps.items():
            if value % 2 != 0:
                return -1

            for i in range(abs(value)//2):
                arr.append(key)
        if not arr:
            return 0
        arr.sort()
        minElem = min(basket1 + basket2)
        res = 0

        for i in range(len(arr)//2):
            res += min(arr[i], minElem*2)
        
        return res

# 1,3,4     

# {2:2, 1:2}
        