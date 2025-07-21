class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []

        for char in s:
            if stack:
                if stack[-1][0] == char:
                    if stack[-1][1] == 2:
                        continue
                    else:
                        char, value = stack.pop()
                        stack.append((char, value+1))
                else:
                    stack.append((char, 1))
            else:
                stack.append((char, 1))
        
        res = []

        for char, val in stack:
            for _ in range(val):
                res.append(char)
        
        return "".join(res)



        