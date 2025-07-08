# This question is exactly same as 1235. Maximum Profit in Job Scheduling
class Solution(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """

        events.sort()

        def findNextIndex(left, currEnd):
            right = len(events) - 1
            ans = right + 1

            while left <= right:
                mid = (left+right) // 2
                if events[mid][0] > currEnd:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ans

        maps = {}
        def solve(index, k):
            if index >= len(events) or k <= 0:
                return 0
            if (index, k) in maps:
                return maps[(index, k)]
            #take
            nextIndex = findNextIndex(index+1, events[index][1])
            take = events[index][2] + solve(nextIndex,k-1)
            #not take
            notTake = solve(index+1,k)
            maps[(index, k)] = max(take, notTake)
            return maps[(index, k)]
        
        return solve(0, k)

        