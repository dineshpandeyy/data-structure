#Recursion
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        def solve(string1, string2):
            if string1 == string2:
                return True

            if sorted(string1) != sorted(string2):  # Early return if character counts differ
                return False
            
            n = len(string1)

            for i in range(1,n):
                # Case 1 no swap
                if solve(string1[:i], string2[:i]) and solve(string1[i:], string2[i:]):
                    return True
                
                #case 2 swap
                if solve(string1[:i], string2[n-i:]) and solve(string1[i:], string2[:n-i]):
                    return True
            return False
        return solve(s1,s2)
    

# Memo
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}

        def solve(string1, string2):
            if (string1, string2) in memo:
                return memo[(string1, string2)]

            if string1 == string2:
                return True

            if sorted(string1) != sorted(string2):  # Early return if character counts differ
                return False
            
            n = len(string1)

            for i in range(1,n):
                # Case 1 no swap
                if solve(string1[:i], string2[:i]) and solve(string1[i:], string2[i:]):
                    memo[(string1, string2)] = True
                    return True
                
                #case 2 swap
                if solve(string1[:i], string2[n-i:]) and solve(string1[i:], string2[:n-i]):
                    memo[(string1, string2)] = True
                    return True
            
            memo[(string1, string2)] = False

            return  memo[(string1, string2)]
        
        return solve(s1,s2)