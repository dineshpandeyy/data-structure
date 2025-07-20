class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        maps = {}
        for char in "qwertyuiop":
            maps[char] = 1

        for char in "asdfghjkl":
            maps[char] = 2

        for char in "zxcvbnm":
            maps[char] = 3

        res = []
        for word in words:
            val = maps[word[0].lower()]
            for i in range(1,len(word)):
                if maps[word[i].lower()] != val:
                    break
            else:
                res.append(word)
        
        return res






        