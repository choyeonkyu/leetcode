class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        left, right = 0, 0
        answer, cur = [], ''
        def dfs(cur, left, right):
            if left < right or (left + right > 2*n):
                return
            elif (left + right == 2*n) & (left == n):
                answer.append(cur)
                return
            dfs(cur+'(', left+1, right)
            dfs(cur+')', left, right+1)
        dfs('', 0, 0)
        return answer