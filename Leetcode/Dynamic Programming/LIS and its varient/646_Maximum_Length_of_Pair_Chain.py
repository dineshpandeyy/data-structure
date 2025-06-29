'''
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
Return 
You do not need to use up all the given intervals. You can select pairs in any order.
Example 1:
Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].
Example 2:

Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
'''

# Note: the only different here from leetcode 300 is here we can select pairs in any order, so we can sort it
def lengthOfLIS(nums):
    dp = [1] * len(nums)
    nums.sort()


    for i in range(len(nums)):
        for j in range(i):
            if nums[i][0] > nums[j][1]:
                dp[i] = max(dp[j]+1, dp[i])
    
    return max(dp)

pairs = [[1,2],[2,3],[3,4]]
print(lengthOfLIS(pairs))

pairs = [[1,2],[7,8],[4,5]]
print(lengthOfLIS(pairs))