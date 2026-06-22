class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        memory = [float('inf')] * len(cost)
        memory[0], memory[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            memory[i] = min(memory[i-1], memory[i-2]) + cost[i]
        return min(memory[-1], memory[-2])