'''
844. Backspace String Compare
Given two strings s and t, return true if they are equal when both are typed into
 empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
'''

def backspaceCompare(s, t):
    s1 = solve(s)
    t1 = solve(t)

    return s1 == t1
        
    
def solve(s):
    stack = []

    for char in s:
        if stack and char == "#":
            stack.pop()
        elif char != "#":
            stack.append(char)
        
    return stack

s = "ab#c"
t = "ad#c"
print(backspaceCompare(s, t))

s = "a#c"
t = "b"
print(backspaceCompare(s, t))
