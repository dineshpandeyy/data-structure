def check(nums):
    switch = 0
    N = len(nums)

    for i in range(N):
        if nums[i%N] > nums[(i+1)%N]:
            switch += 1

    return switch <= 1 