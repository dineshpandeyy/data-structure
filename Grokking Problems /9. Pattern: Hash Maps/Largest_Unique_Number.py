'''
Given an array of integers A, return the largest integer that only occurs once.

If no integer occurs once, return -1.

 
Example 1:
Input: [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: 
The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it's the answer.
Example 2:

Input: [9,9,8,8]
Output: -1
Explanation: 
There is no number that occurs only once.
'''
def firstUniqChar(arr):
    maps = {}

    for char in arr:
        if char not in maps:
            maps[char] = 1
        else:
            maps[char] += 1
    
    largestNumber = -1

    for key in maps:
        if maps[key] == 1:
            largestNumber = max(largestNumber, key)
    return largestNumber

arr = [5,7,3,9,4,9,8,3,1]
print(firstUniqChar(arr))

arr = [9,9,8,8]
print(firstUniqChar(arr))