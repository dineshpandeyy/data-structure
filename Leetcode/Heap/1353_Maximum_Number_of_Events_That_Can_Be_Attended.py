import heapq
class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort()
        heap = []
        startDay = events[0][0]
        count = 0
        i = 0

        while heap or i < len(events):

            while i < len(events) and events[i][0] == startDay:
                heapq.heappush(heap, events[i][1])
                i += 1
            
            # attend one event per day
            if heap:
                count += 1
                heapq.heappop(heap)
            
            startDay += 1
            
            while heap and heap[0] < startDay:
                heapq.heappop(heap)
        
        return count