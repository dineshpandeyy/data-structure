class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0 and high % 2 == 0:
            return (high-low) // 2
        else:
            return (high-low+2) // 2
        
# 10-8/2 = 1 
# 4+2/2 = 2