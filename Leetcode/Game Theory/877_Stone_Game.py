class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        maps = {}
        def solve(l,r):
            if l > r:
                return 0
            if (l,r) in maps:
                return maps[(l,r)]
            
            even = True if (r-l) % 2 == 1 else False
            left = piles[l] if even else 0
            right = piles[r] if even else 0
    
            maps[(l,r)] = max(solve(l+1,r) + left,solve(l+1,r-1) + right)
            return maps[(l,r)]
        

        total = solve(0, len(piles) - 1)
        return total > sum(piles) // 2




