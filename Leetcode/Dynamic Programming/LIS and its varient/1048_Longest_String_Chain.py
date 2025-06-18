class Solution:
    def longestStrChain(self, words) -> int:
        words = sorted(words, key=len)
        dp = [1] * len(words)

        for i in range(len(words)):
            for j in range(i):
                if self.isPredecessor(words[j],words[i]):
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)


    
    def isPredecessor(self,shorter, longer) -> bool:
        if len(longer) != len(shorter) + 1:
            return False
        i = j = 0
        mismatch = 0

        while i < len(shorter) and j < len(longer):
            if shorter[i] == longer[j]:
                i += 1
                j += 1
            else:
                if mismatch == 1:
                    return False
                mismatch += 1
                j += 1  # skip one character in longer

        return True