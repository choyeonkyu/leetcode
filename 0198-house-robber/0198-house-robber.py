class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = {} # (index, total) -> maximum money till index

        def backtrack(i):
            if i >= len(nums):
                return 0
            if i in dp:
                return dp[i]

            dp[i] = max(backtrack(i + 2)+nums[i], backtrack(i+1))
            return dp[i]
        return backtrack(0)