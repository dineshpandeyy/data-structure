# This  question is very similar to 131. Palindrome Partitioning. Solve this one first.
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        res = []
        def solve(index, dots, currString):
            if index == len(s) and dots == 4:
                res.append(currString[:-1])
                return 
            
            if index > len(s) or dots > 4:
                return 
            
            for j in range(index, min(index+3, len(s))):
                currIP = int(s[index:j+1])

                if currIP < 256 and (index == j or s[index] != "0"):
                    solve(j+1, dots+1, currString + s[index:j+1] + ".")
        
        solve(0, 0, "")
        return res