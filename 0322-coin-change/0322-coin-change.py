class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        memo = {}
        def dfs(remain):
            if remain < 0:
                return float('inf')
            elif remain == 0:
                return 0
            if remain in memo:
                return memo[remain]
            
            best = float('inf')
            for i in coins:
                cand = dfs(remain - i) + 1
                best = min(cand, best)

            memo[remain] = best
            return best
        
        answer = dfs(amount)
        return answer if answer != float('inf') else -1