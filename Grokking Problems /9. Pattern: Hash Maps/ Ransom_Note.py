'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    maps = {}

    for char in magazine:
        if char not in maps:
            maps[char] = 1
        else:
            maps[char] += 1
    
    for char in ransomNote:
        if char not in maps or maps[char] == 0:
            return False
        maps[char] -= 1
    return True   

ransomNote = "a"
magazine = "b"
print(canConstruct(ransomNote, magazine))

ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote, magazine))

ransomNote = "aa"
magazine = "ab"
print(canConstruct(ransomNote, magazine))
