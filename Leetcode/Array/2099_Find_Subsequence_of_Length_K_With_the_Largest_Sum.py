class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = []

        for i, num in enumerate(nums):
            arr.append([num,i])
        
        arr.sort(key=lambda x: -x[0])
        print(arr)

        topK = arr[:k]
        topK.sort(key=lambda x: x[1])

        result = []

        for num in topK:
            result.append(num[0])
        
        return result