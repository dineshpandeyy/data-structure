class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        result = []
        curr = []

        def solve(index):
            if index >= len(s):
                result.append(curr[::])
                return 
            
            for i in range(index, len(s)):
                if palindrome(index, i):
                    curr.append(s[index:i+1])
                    solve(i+1)
                    curr.pop()
        
        solve(0)
        return result
        