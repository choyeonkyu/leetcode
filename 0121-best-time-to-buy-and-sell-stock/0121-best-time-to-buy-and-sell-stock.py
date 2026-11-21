class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        start, end = 0, 1
        answer = 0
        while end < len(prices):
            cur = prices[end] - prices[start]
            answer = max(answer, cur)
            if cur <= 0:
                start = end
                end += 1
            else:
                end += 1
        return answer