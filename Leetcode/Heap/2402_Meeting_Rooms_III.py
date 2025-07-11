import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        availableRoom = [i for i in range(n)]
        heapq.heapify(availableRoom)
        busyRooom = [] # (endTime, room)
        meetingCount = [0 for i in range(n)]
        
        for start, end in meetings:
            while busyRooom and busyRooom[0][0] <= start:
                endtime, room = heapq.heappop(busyRooom)
                heapq.heappush(availableRoom, room)

            if availableRoom:
                room = heapq.heappop(availableRoom)
                meetingCount[room] += 1
                heapq.heappush(busyRooom, (end, room))
            else:
                endTime, room = heapq.heappop(busyRooom)
                meetingCount[room] += 1
                heapq.heappush(busyRooom, (endTime+end-start, room))
        
        return meetingCount.index(max(meetingCount))









