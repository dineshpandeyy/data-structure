'''
Problem Statement #
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters 
with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
Example 2:

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
Example 3:

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
'''

def characterReplacement(s, k):
    longestSoFar = 0
    left = 0
    right = 0
    result = 0
    maps = {}

    while right < len(s):
        if s[right] not in maps:
            maps[s[right]] = 1
        else:
            maps[s[right]] += 1
        longestSoFar = max(longestSoFar, maps[s[right]])
        while (right-left+1)-longestSoFar > k:
            maps[s[left]] -= 1
            if  maps[s[left]] == 0:
                del maps[s[left]]
            left += 1
    
        result = max(result, right-left+1)
        right += 1
    
    return result

String="aabccbb" 
k=2       
print(characterReplacement(String, k))

String="abbcb"
k=1
print(characterReplacement(String, k))

String="abccde"
k=1
print(characterReplacement(String, k))
