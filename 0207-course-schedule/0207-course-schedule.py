class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = [[] for _ in range(numCourses)]
        in_degree = [0]*numCourses
        for prev, cur in prerequisites:
            adj[cur].append(prev)
            in_degree[prev] += 1
        q = collections.deque()
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                q.append(i)
        while q:
            cur = q.popleft()
            for i in adj[cur]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    q.append(i)
        return True if sum(in_degree) == 0 else False