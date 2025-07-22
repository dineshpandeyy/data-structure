# This question is simialr to 3. Longest Substring Without Repeating Characters

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        mySet = set()
        currSum = 0
        left = 0
        result = 0

        for num in nums:
            while num in mySet:
                currSum -= nums[left]
                mySet.remove(nums[left])
                left += 1
            
            mySet.add(num)
            currSum += num

            print("the cursum", currSum)
            result = max(currSum, result)
        
        return result
            
        