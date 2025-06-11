'''
3442. Maximum Difference Between Even and Odd Frequency
You are given a string s consisting of lowercase English letters.

Your task is to find the maximum difference diff = a1 - a2 between the 
frequency of characters a1 and a2 in the string such that:
a1 has an odd frequency in the string.
a2 has an even frequency in the string.
Return this maximum difference

Example 1:
Input: s = "aaaaabbc"
Output: 3
Explanation:
The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
The maximum difference is 5 - 2 = 3.

Example 2:
Input: s = "abcabcab"
Output: 1
Explanation:
The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
The maximum difference is 3 - 2 = 1.
 
Constraints:
3 <= s.length <= 100
s consists only of lowercase English letters.
s contains at least one character with an odd frequency and one with an even frequency.
'''

def maxDifference(s):
    maps = {}
    for char in s:
        if char not in maps:
            maps[char] = 1
        else:
            maps[char] += 1
    
    oddFreq = float("-inf")
    evenFreq = float("inf")

    for value in maps.values():
        if value % 2 == 1:
            oddFreq = max(oddFreq,value)
        else:
            evenFreq = min(evenFreq, value)
    
    return oddFreq - evenFreq


s = "aaaaabbc"
print(maxDifference(s))