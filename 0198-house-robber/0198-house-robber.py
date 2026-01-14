class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}
        def solve(x):
            
            if x == 0:
                return nums[0]
            if x == 1:
                return max(nums[0], nums[1])
            if x in memo:
                return memo[x]
            if x > 1:
                memo[x] = max(solve(x-1), solve(x-2) + nums[x])
                return memo[x]
        return solve(len(nums)-1)
