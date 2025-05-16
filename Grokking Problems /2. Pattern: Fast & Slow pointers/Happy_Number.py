'''
Problem Statement #
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of 
the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. 
Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
Example 2:

Input: n = 2
Output: false
'''

def happyNumber(num):
     
    def calc(num):
        result = 0
        while num > 0:
            carr = num % 10
            result += carr ** 2
            num = num // 10
        
        return result
    
    maps = set()

    while num != 1:
        sNum = calc(num)
        if sNum in maps:
            return False
        maps.add(sNum)
        num = sNum

    return True


print(happyNumber(19))
print(happyNumber(2))
    
   



