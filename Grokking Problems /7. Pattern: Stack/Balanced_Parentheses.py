'''
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

def isValid(s):
    maps = { ")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        if char in maps.values():
            stack.append(char)
        else:
            if not stack or stack.pop() != maps[char]:
                return False
    
    return len(stack) == 0

s = "()"
print(isValid(s))