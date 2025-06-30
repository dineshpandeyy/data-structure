# memo with recursion
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        maps = {}

        def solve(index):
            if index in maps:
                return maps[index]
            if index >= len(days):
                return 0

            oneDay = costs[0] + solve(index+1)

            maxTravelWithSeven = days[index] + 7

            i = index
            while i < len(days) and days[i] < maxTravelWithSeven:
                i += 1
            sevenDay = costs[1] + solve(i)

            maxTravelWithThirty = days[index] + 30

            i = index
            while i < len(days) and  days[i] < maxTravelWithThirty:
                i += 1
            thirtyDay = costs[2] + solve(i)

            maps[index] = min(oneDay, sevenDay, thirtyDay)
            return maps[index]
        
        return solve(0)


#Bottom up
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        dp = [0] * (days[-1] + 1)
        daySet = set(days)

        for i in range(1,days[-1]+1):
            if i not in daySet:
                dp[i] = dp[i-1]
            else:
                oneDay = dp[max(0, i-1)] + costs[0]
                sevenDay = dp[max(0, i-7)] + costs[1]
                thirtyDay = dp[max(0, i-30)] + costs[2]
                dp[i] = min(oneDay, sevenDay,thirtyDay)
        
        return dp[-1]