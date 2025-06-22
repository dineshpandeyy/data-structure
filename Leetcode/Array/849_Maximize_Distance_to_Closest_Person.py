class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prevOneIndex = None
        distance = float("-inf")

        for i in range(len(seats)):
            if seats[i] == 1:
                if prevOneIndex == None:
                    prevOneIndex = i
                    distance = i
                else:
                    distance = max(distance, (i - prevOneIndex)//2)
                    prevOneIndex = i
        
        distance = max(distance, len(seats)-1-prevOneIndex) #sitting at lastindex if we don't have one
        return distance