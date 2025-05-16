'''
2381. Shifting Letters II
You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni].
 For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or 
 shift the characters backward if directioni = 0.

Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a').
 Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

Return the final string after all such shifts to s are applied.

Example 1:

Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
Output: "ace"
Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".
Example 2:

Input: s = "dztz", shifts = [[0,0,0],[1,1,1]]
Output: "catz"
Explanation: Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".
'''

def shiftingLetters(s, shifts):
    array = [0] * len(s)

    for shift in shifts:
        start = shift[0]
        end = shift[1]
        direction = shift[2]

        if direction == 1:
            array[start] += 1
            if end + 1 < len(array):
                array[end+1] -= 1
        else:
            array[start] -= 1
            if end + 1 < len(array):
                array[end+1] += 1
    
    summ = 0
    for i in range(len(array)):
        summ += array[i]
        array[i] = summ
    
    result = []
    for i in range(len(s)):
        shift_val = (ord(s[i]) - ord('a') + array[i]) % 26
        result.append(chr(ord('a') + shift_val))

    return "".join(result)

        
s = "abc"
shifts = [[0,1,0],[1,2,1],[0,2,1]]
print(shiftingLetters(s, shifts))

s = "dztz"
shifts = [[0,0,0],[1,1,1]]
print(shiftingLetters(s, shifts))