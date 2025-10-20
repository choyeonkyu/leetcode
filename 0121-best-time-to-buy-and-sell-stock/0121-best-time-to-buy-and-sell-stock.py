class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        start, end = 0, 1
        answer= 0
        while len(prices) > end:
            cur = prices[end] - prices[start]
            answer = max(answer, cur)
            if cur <= 0:
                start, end = end, start
                end = start + 1
            else:
                end += 1
        return answer
        