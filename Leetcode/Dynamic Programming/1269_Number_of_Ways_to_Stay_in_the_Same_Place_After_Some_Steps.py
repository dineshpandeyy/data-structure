class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dfs(index,steps):
            #pruning: not enough remaining steps to get back to 0
            if index > steps:
                return 0
            if index < 0 or index >= arrLen:
                return 0
            
            if steps == 0:
                if index == 0:
                    return 1
                return 0
            
            count = 0
            count += dfs(index-1,steps-1)
            count += dfs(index,steps-1)
            count += dfs(index+1,steps-1)

            return count % MOD
        
        return dfs(0,steps)


