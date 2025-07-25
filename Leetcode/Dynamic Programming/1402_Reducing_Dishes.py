class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        
        @cache
        def solve(index, time):
            if index >= len(satisfaction):
                return 0
            #Take
            take = time * satisfaction[index] + solve(index+1, time+1)
            #Nottake
            notTake = solve(index+1, time)
            return max(take, notTake)

        return solve(0, 1)
       

# TODO (Tabulation)