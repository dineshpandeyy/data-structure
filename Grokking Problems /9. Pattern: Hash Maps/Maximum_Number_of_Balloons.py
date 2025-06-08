'''
1189. Maximum Number of Balloons
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given a string text, you want to use the characters of text to 
form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.


Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0
'''
from collections import defaultdict 
def solved(text):
    textMaps = mapsBuilder(text)
    bollonsMaps = mapsBuilder("balloon")

    result = float("inf")

    for char in bollonsMaps:
        result = min(result, textMaps[char]//bollonsMaps[char])
    
    return result

def mapsBuilder(text):
    maps = defaultdict(int)

    for t in text:
        maps[t] += 1
        
    return maps

text = "nlaebolko"
print(solved(text))

text = "loonbalxballpoon"
print(solved(text))

text = "leetcode"
print(solved(text))