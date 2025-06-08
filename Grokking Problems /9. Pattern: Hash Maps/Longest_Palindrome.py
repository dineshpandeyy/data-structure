'''
409. Longest Palindrome
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
'''

from collections import defaultdict 
def longestPalindrome(s):
        sMaps = mapsBuilder(s)
        oddValue = False
        result = 0

        for value in sMaps.values():
            if value % 2 == 0:
                result += value
            else:
                result += value - 1
                oddValue = True
        
        return result + 1 if oddValue else result

def mapsBuilder(text):
    maps = defaultdict(int)

    for t in text:
        maps[t] += 1
        
    return maps

s = "abccccdd"
print(longestPalindrome(s))

s = "a"
print(longestPalindrome(s))