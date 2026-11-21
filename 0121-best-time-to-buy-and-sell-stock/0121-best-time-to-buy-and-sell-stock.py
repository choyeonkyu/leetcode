class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        start, end = 0, 1
        answer = 0
        while start < end and end < len(prices):
            cur = prices[end] - prices[start]
            answer = max(answer, cur)
            if end - start == 1 and cur <= 0:
                start += 1
                end += 1
            elif cur <= 0:
                start += 1
            elif cur > 0:
                end += 1
        return answer