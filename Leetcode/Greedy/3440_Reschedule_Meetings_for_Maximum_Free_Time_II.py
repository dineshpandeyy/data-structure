class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        gapArr = []
        gapArr.append(startTime[0]-0)

        for i in range(1,len(startTime)):
            gapArr.append(startTime[i]-endTime[i-1])
        
        gapArr.append(eventTime - endTime[-1])
        print(gapArr)

        leftMax = [0] * len(gapArr)
        for i in range(1, len(gapArr)):
            leftMax[i] = max(leftMax[i - 1], gapArr[i - 1])  

        rightMax = [0] * len(gapArr)
        for i in range(len(gapArr) - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], gapArr[i + 1])  

        result = 0

        for i in range(1, len(gapArr)):
            currEventTime = endTime[i-1] - startTime[i-1]

            # Move event to another place
            if currEventTime <= max(leftMax[i-1],rightMax[i]):
                result = max(result, currEventTime + gapArr[i-1] + gapArr[i])
            
            # move to side
            result = max(result, gapArr[i-1] + gapArr[i])
        
        return result
    


        




        