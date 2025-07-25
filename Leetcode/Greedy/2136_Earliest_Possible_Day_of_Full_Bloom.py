class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        sortedArray = []

        for t, g in zip(plantTime,growTime):
            sortedArray.append([g,t])
        
        sortedArray.sort(reverse=True)
        print(sortedArray)
        
        result = 0
        prevEndTime = 0

        for growT, plantTime in sortedArray:
            prevEndTime = prevEndTime + plantTime
            bloomtime = prevEndTime + growT
            result = max(result, bloomtime)
        
        return result


        