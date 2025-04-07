'''
Longest Substring with K Distinct Characters (medium)

Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
'''

def longestSubString(nums, K):
    left = 0
    right = 0
    maps = {}
    result = 0

    while right < len(nums):
        if nums[right] not in maps:
            maps[nums[right]] = 1
        else:
            maps[nums[right]] += 1
        
        while len(maps) > K:
            maps[nums[left]] -= 1
            if maps[nums[left]] == 0:
                del maps[nums[left]]
            left += 1
        result = max(result, right-left+1)
        right += 1
    
    return result

String = "araaci"
K = 2
print(longestSubString(String, K))

String = "araaci"
K = 1
print(longestSubString(String, K))

String = "cbbebi"
K = 3
print(longestSubString(String, K))

