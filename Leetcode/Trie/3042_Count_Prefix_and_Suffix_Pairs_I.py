class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        res = 0
        for i, word in enumerate(words):
            for j in range(i+1, len(words)):
                if words[j].startswith(word) and words[j].endswith(word):
                    res += 1
        return res

         