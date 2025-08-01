class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maps = {0: -1}
        currSum = 0
        result = 0


        for i in range(len(nums)):
            if nums[i] == 1:
                currSum += 1
            else:
                currSum -= 1
            
            if currSum in maps:
                result = max(result, i - maps[currSum])
            else:
                maps[currSum] = i
        
        return result



        