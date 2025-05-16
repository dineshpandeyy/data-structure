# 14. Longest Common Prefix
'''
14. Longest Common Prefix
Solved
Easy
Topics
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

def longestCommonPrefix(strs):
    # find the shortest length
    shortestLen = float("inf")
    shortestChar = ""
    for char in strs:
        if len(char) < shortestLen:
            shortestLen = len(char)
            shortestChar = char
    
    i = 0
    res = []
    while i < shortestLen:
        for char in strs:
            if char[i] != shortestChar[i]:
                return "".join(res) 
        res.append(char[i])
        i += 1

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))

strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))






