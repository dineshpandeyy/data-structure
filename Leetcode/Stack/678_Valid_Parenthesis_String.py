class Solution:
    def checkValidString(self, s: str) -> bool:
        openCount = 0

        for char in s:
            if char in ["(", "*"]:
                openCount += 1
            elif openCount:
                openCount -= 1
            else:
                return False
            
        
        closeCount = 0

        for char in s[::-1]:
            if char in [")", "*"]:
                closeCount += 1
            elif closeCount:
                closeCount -= 1
            else:
                return False
            
        return True



