'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
'''

def firstUniqChar(s):
    maps = {}

    for char in s:
        if char not in maps:
            maps[char] = 1
        else:
            maps[char] += 1
    
    for i in range(len(s)):
        if maps[s[i]] == 1:
            return i

    return -1  


s = "aabb"
print( firstUniqChar(s))

s = "loveleetcode"
print( firstUniqChar(s))