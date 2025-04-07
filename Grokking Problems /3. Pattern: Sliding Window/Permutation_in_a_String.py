'''
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:
abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters it will have 
n
!
n! permutations.
Example 1:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
Example 2:

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.
Example 3:

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
'''

def checkInclusion(s1, s2):
    s1Maps = {}

    for char in s1:
        if char not in s1Maps:
            s1Maps[char] = 1
        else:
            s1Maps[char] += 1
    
    s2Maps = {}
    left = 0
    right = 0

    while right < len(s2):
        if s2[right] not in s2Maps:
            s2Maps[s2[right]] = 1
        else:
            s2Maps[s2[right]] += 1
        if (right-left+1) == len(s1):
            if s1Maps == s2Maps:
                return True
            else:
                s2Maps[s2[left]] -= 1
                if s2Maps[s2[left]] == 0:
                    del s2Maps[s2[left]]
                left += 1
        right += 1
    
    return False

String = "oidbcaf"
Pattern = "abc"
print(checkInclusion(Pattern, String))

String="odicf"
Pattern="dc"
print(checkInclusion(Pattern, String))

String="bcdxabcdy"
Pattern="bcdyabcdx"
print(checkInclusion(Pattern, String))

s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))

s1 = "ab"
s2 = "eidboaoo"
print(checkInclusion(s1, s2))
