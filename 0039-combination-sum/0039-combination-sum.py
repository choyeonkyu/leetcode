class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        answer, path = [], []
        def backtracking(start, path):
            if sum(path) > target:
                return
            elif sum(path) == target:
                answer.append(path[:])
            for i in range(start, len(candidates)):
                backtracking(i, path + [candidates[i]])
        backtracking(0, [])
        return answer