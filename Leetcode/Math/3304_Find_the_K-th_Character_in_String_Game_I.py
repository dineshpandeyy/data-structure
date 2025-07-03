class Solution:
    def kthCharacter(self, k: int) -> str:
        res = ["a"]

        while len(res) < k:
            copy = res[::]

            for char in res:
               # Increment character and wrap around from 'z' to 'a'
                newChar = chr(((ord(char) - ord('a') + 1) % 26) + ord('a'))
                copy.append(newChar)
            
            res = copy
        

        return res[k-1]
