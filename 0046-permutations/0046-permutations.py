class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visited = [False]*len(nums)
        answer = []
        def dfs(path):
            if len(path) == len(nums):
                answer.append(path[:])
                return 
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    dfs(path+[nums[i]])
                    visited[i] = False
        dfs([])
        return answer 