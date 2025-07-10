class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        gapArray = []
        gapArray.append(startTime[0]-0)

        for i in range(1,len(startTime)):
            gapArray.append(startTime[i]-endTime[i-1])
        
        gapArray.append(eventTime-endTime[-1])
        result = 0
        summ = 0
        right = 0
        left = 0
        while right < len(gapArray):
            summ += gapArray[right]
            if right - left + 1 == k + 1:
                result = max(summ, result)
                summ -= gapArray[left]
                left += 1
            right += 1
        
        return result

# eventTime = 21
# k = 2
# startTime = [18,20]
# endTime = [20,21]     
# [18,0,0]




        