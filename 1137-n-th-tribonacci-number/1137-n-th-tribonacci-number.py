class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 1, 1]
        if n <= 2:
            return dp[n]
        dp += [0] * (n-2)
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[n]