class Solution:
    def findLHS(self, nums: List[int]) -> int:
        maps = {}

        for num in nums:
            if num not in maps:
                maps[num] = 1
            else:
                maps[num] += 1
        
        result = 0
        for key, value in maps.items():
            if key + 1 in maps:
                result = max(result, value + maps[key+1])
        
        return result