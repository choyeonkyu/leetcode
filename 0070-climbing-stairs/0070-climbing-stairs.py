class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # kind of decision tree approach
        dp = {} # total -> # of ways

        def backtrack(total):
            if total >= n: # count
                return 1 if total == n else 0
            if total in dp: # memorization
                return dp[total]
            
            dp[total] = backtrack(total + 1) + backtrack(total + 2)
            return dp[total]
        return backtrack(0)