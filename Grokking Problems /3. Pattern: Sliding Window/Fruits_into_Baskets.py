'''
Problem Statement #
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put 
maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree 
until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
'''

def fruitsIntoBaskets(fruits):
    maps = {}
    left = 0
    right = 0
    result = float("-inf")

    while right < len(fruits):
        if fruits[right] not in maps:
            maps[fruits[right]] = 1
        else:
            maps[fruits[right]] += 1

        while len(maps) > 2:
            maps[fruits[left]] -= 1
            if maps[fruits[left]] == 0:
                del maps[fruits[left]]
            left += 1
        result = max(result, right - left + 1)
        right += 1
    return result

fruit = ['A', 'B', 'C', 'B', 'B', 'C']
print(fruitsIntoBaskets(fruit))


        




        


