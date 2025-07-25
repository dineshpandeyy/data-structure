class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        me = len(piles) - 2
        bob = 0
        result = 0

        while bob < me:
            result += piles[me]
            me -= 2
            bob += 1
        
        return result




        