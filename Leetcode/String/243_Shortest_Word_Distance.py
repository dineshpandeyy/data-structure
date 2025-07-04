'''
243. Shortest Word Distance
Description
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

 

Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
Example 2:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
 

Constraints:

2 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
'''

def shortestDistance(wordsDict, word1, word2):
    first = -1
    second = -1
    res = float("inf")
    for i in range(len(wordsDict)):
        if wordsDict[i] == word1:
            first = i
        elif wordsDict[i] == word2:
            second = i
        
        if first != -1 and second != -1:
            res = min(res, abs(first-second))
    return res
wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"
# Output: 3
print(shortestDistance(wordsDict, word1, word2))

