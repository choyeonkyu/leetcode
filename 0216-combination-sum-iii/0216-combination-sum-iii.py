class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        answer = []
        def backtrack(cur_list, cur_sum):
            if cur_sum > n or len(cur_list) > k:
                return
            elif cur_sum == n and len(cur_list) == k:
                answer.append(cur_list)
            for i in range(cur_list[-1]+1, 10):
                backtrack(cur_list+[i], cur_sum+i)
        for i in range(1, 10):
            backtrack([i], i)
        return answer