class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        maps = Counter(nums)

        res = []
        for key, value in maps.items():
            if value > 1:
                res.append(key)
                
                if len(res) == 2:
                    return res
        