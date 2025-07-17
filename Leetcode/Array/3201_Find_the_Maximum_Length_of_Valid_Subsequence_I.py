class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        evenCount = 0
        oddCount = 0

        for num in nums:
            if num % 2 == 0:
                evenCount += 1
            else:
                oddCount += 1
        
        # Alternative
        alternative = nums[0] % 2
        count = 1
        for i in range(1, len(nums)):
            if nums[i] % 2 != alternative:
                count += 1
                alternative = not alternative

        return max(evenCount, oddCount, count)

# Recursion (Time Limit Exceeded)
class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        # modulo 1
        def modulo1(prev, index):
            if index >= len(nums):
                return 0
            take = 0
            if prev == -1 or (nums[prev] + nums[index]) % 2 == 1:
                take = 1 + modulo1(index, index+1)
            notTake = modulo1(prev, index+1)

            return max(take, notTake)
        
        def modulo0(prev, index):
            if index >= len(nums):
                return 0
            take = 0
            if prev == -1 or (nums[prev] + nums[index]) % 2 == 0:
                take = 1 + modulo0(index, index+1)
            notTake = modulo0(prev, index+1)

            return max(take, notTake)
        
        return max(modulo1(-1, 0), modulo0(-1, 0))

# Recursion with memo (Memory Limit Exceeded)
class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        # modulo 1
        maps1 = {}
        def modulo1(prev, index):
            if (prev, index) in maps1:
                return maps1[(prev, index)]
            if index >= len(nums):
                return 0
            take = 0
            if prev == -1 or (nums[prev] + nums[index]) % 2 == 1:
                take = 1 + modulo1(index, index+1)
            notTake = modulo1(prev, index+1)

            maps1[(prev, index)] = max(take, notTake)
            return maps1[(prev, index)]
        
        maps2 = {}
        def modulo0(prev, index):
            if (prev, index) in maps2:
                return maps2[(prev, index)]
            if index >= len(nums):
                return 0
            take = 0
            if prev == -1 or (nums[prev] + nums[index]) % 2 == 0:
                take = 1 + modulo0(index, index+1)
            notTake = modulo0(prev, index+1)

            maps2[(prev, index)] = max(take, notTake)
            return maps2[(prev, index)]
        
        return max(modulo1(-1, 0), modulo0(-1, 0))

# Tabulation (TLE)
class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        dp0 = [1] * len(nums)
        dp1 = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if (nums[i] + nums[j]) % 2 == 0:
                    dp0[i] = max(dp0[i], dp0[j]+1)
                else:
                    dp1[i] = max(dp1[i], dp1[j]+1)
        return max(max(dp0), max(dp1))