class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        visited = [False] * n
        nums = list(range(1,n+1))
        answer = []
        def dfs(start, path):
            if len(path) == k:
                path.sort()
                answer.append(path[:])
                return
            for i in range(start, n):
                if not visited[i]:
                    visited[i] = True
                    dfs(i+1, path+[nums[i]])
                    visited[i] = False
        dfs(0,[])
        return answer