class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        maps = {}
        for char in words[0]:
            if char not in maps:
                maps[char] = 1
            else:
                 maps[char] += 1
        
        for i in range(1, len(words)):
            count = Counter(words[i])

            for key, value in maps.items():
                if key not in maps:
                    del maps[key]
                else:
                    maps[key] = min(count[key], value)
        
        res = []

        for key, value in maps.items():
            for _ in range(value):
                res.append(key)
        
        return res





        
        