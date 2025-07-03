class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        left = 0
        result = 0

        for char in s:
            while char in mySet:
                mySet.remove(s[left])
                left += 1
            
            mySet.add(char)
            result = max(result, len(mySet))
        
        return result
            
            



        