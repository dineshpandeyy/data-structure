def maxProduct(nums):
    nums.sort()
    last = nums[-1]
    secondLast = nums[-2]

    return (last-1) * (secondLast-1)