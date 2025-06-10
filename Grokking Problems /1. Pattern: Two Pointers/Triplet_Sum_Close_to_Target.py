def threeSumClosest(self, nums, target):
    nums.sort()
    result = float("inf")

    for i in range(len(nums)):

        left = i + 1
        right = len(nums) - 1

        while left < right:
            totalSum = nums[i] + nums[left] + nums[right]
            if abs(totalSum-target) < abs(result-target):
                result = totalSum
            
            elif totalSum > target:
                right -= 1
            else:
                left += 1
    
    return result

nums = [-1,2,1,-4]
target = 1
print(threeSumClosest(None, nums, target))  # Output: 2