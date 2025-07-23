class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        res = 0
        maxString = ""
        if x > y:
            maxString = "ab"
        else:
            maxString = "ba"

        for char in s:
            if stack and stack[-1] == maxString[0] and char == maxString[1]:
                stack.pop()
                res += max(x,y)
            else:
                stack.append(char)
        
        stack2 = []
        newS = "".join(stack)
        for char in newS:
            if stack2 and stack2[-1] == maxString[1] and char == maxString[0]:
                stack2.pop()
                res += min(x,y)
            else:
                stack2.append(char)
        
        return res