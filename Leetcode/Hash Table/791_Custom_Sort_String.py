class Solution:
    def customSortString(self, order: str, s: str) -> str:
        maps = {}

        for char in s:
            if char not in maps:
                maps[char] = 1
            else:
                maps[char] += 1
        
        res = []
        for char in order:
            if char in maps:
                for i in range(maps[char]):
                    res.append(char)
                del maps[char]
        
        for key, value in maps.items():
            for i in range(value):
                res.append(key)
        return "".join(res)

        