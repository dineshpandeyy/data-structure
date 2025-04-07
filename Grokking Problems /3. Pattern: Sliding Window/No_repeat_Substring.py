'''
Problem Statement #
Given a string, find the length of the longest substring which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
'''

def longestSubstring(s):
    mySet = set()
    left = 0
    right = 0
    result = 0

    while right < len(s):
        while s[right] in mySet:
            mySet.remove(s[left])
            left += 1
        mySet.add(s[right])
        result = max(result, right - left + 1)
        right += 1
    
    return result
String="aabccbb"
print(longestSubstring(String))

String="abbbb"
print(longestSubstring(String))

String="abccde"
print(longestSubstring(String))
