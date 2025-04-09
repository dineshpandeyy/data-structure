# Group Anagrams -> https://leetcode.com/problems/group-anagrams/
'''
49. Group Anagrams
Solved
Medium
Topics
Companies
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
'''

def GroupAnagrans(strs):
    group = {}

    for char in strs:
        sortedChar = "".join(sorted(char))

        if sortedChar not in group:
            group[sortedChar] = [char]
        else:
            group[sortedChar].append(char)
    
    result = []

    for value in group.values():
        result.append(value)
    
    return result

strs = ["eat","tea","tan","ate","nat","bat"]
print(GroupAnagrans(strs))

strs = [""]
print(GroupAnagrans(strs))

strs = ["a"]
print(GroupAnagrans(strs))