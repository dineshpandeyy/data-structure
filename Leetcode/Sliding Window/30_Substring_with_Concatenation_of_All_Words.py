# Time Limit Exceeded 181 / 182 testcases passed
from collections import Counter
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        maps1 = Counter(words)
        result = []
        perWord = len(words[0])
        length = perWord * len(words)

        for i in range(0, len(s)-length+1):
            copyOfMaps = maps1.copy()
            j = i
            while j < i + length:
                subString = s[j:j+perWord]
                if subString in copyOfMaps:
                    copyOfMaps[subString] -= 1
                    if copyOfMaps[subString] == 0:
                        del copyOfMaps[subString]
                else:
                    break
                j += perWord
            
            if not copyOfMaps:
                result.append(i)
        
        return result

#TODO (Optimization)