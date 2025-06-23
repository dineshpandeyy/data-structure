class Solution:
    def divideString(s,k,fill):
        res = []

        for i in range(0, len(s),k):
            sub = s[i:k+i]
            print(sub)
            res.append(sub)
        
        lastWord = res[-1]
        if len(lastWord) != k:
            filWord = lastWord + (k-len(lastWord)) * fill
            res[-1] = filWord
        return res

        