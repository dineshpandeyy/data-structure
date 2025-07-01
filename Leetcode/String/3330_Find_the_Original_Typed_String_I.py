class Solution:
    def possibleStringCount(self, word: str) -> int:
        result = 0

        for i in range(1,len(word)):
            if word[i-1] == word[i]:
                result += 1
        
        return result + 1
        