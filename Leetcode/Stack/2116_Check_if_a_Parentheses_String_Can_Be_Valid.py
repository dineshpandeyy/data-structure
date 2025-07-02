class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        openCount = 0

        for i, char in enumerate(s):
            if char == "(" or locked[i] == "0":
                openCount += 1
            elif openCount:
                openCount -= 1
            else:
                return False
            
        
        closeCount = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == ")" or locked[i] == "0":
                closeCount += 1
            elif closeCount:
                closeCount -= 1
            else:
                return False
            
        return True


