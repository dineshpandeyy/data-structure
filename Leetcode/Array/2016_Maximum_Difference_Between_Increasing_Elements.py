def maximumDifference(nums) -> int:
    maxDiff = -1

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]:
                maxDiff = max(maxDiff, nums[j]- nums[i])
    
    return maxDiff



# O(N) solution
def maximumDifference(nums):
    minElement = nums[0]
    result = -1

    for i in range(1, len(nums)):
        if nums[i] > minElement:
            result = max(result, nums[i]-minElement)
        minElement = min(minElement, nums[i])
    
    return result