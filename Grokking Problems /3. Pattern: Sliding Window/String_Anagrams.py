'''
String Anagrams (hard) #
Given a string and a pattern, find all anagrams of the pattern in the given string.

Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:
abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:
Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
Example 2:

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
'''

def String_Anagrams(s1, s2):
    s1Maps = {}
    result = []

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
                result.append(left)
              
            s2Maps[s2[left]] -= 1
            if s2Maps[s2[left]] == 0:
                del s2Maps[s2[left]]
            left += 1
        right += 1
    
    return result

String="ppqp"
Pattern="pq"
print(String_Anagrams(Pattern, String))

String="abbcabc"
Pattern="abc"
print(String_Anagrams(Pattern, String))
