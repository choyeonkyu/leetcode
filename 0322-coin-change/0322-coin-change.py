class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [False] * (amount+1)
        dp[amount] = 1
        for i in range(amount, -1, -1):
            for j in coins:
                if not dp[i]:
                    break
                if i-j < 0:
                    continue
                dp[i-j] = min(dp[i] + 1, dp[i-j]) if dp[i-j] else dp[i] + 1
        return dp[0]-1 if dp[0] else -1