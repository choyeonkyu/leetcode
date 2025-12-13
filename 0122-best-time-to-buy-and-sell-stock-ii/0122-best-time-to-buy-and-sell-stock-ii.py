class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0
        left= 0
        answer = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                # if i+1 == len(prices)-1:
                #     answer += prices[i+1] - prices[left]
                continue
            else:
                answer += prices[i] - prices[left]
                left = i+1
        if prices[i] < prices[i+1]:
            answer += prices[i+1] - prices[left]
        return answer