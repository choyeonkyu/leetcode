class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for cur, preq in prerequisites:
            adj[preq].append(cur) # organize adjacent list
            in_degree[cur] += 1 # num of prerequisite courses
        q, answer = collections.deque(), [] # declare queue for topological sort and list to return order of courses
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                q.append(i)
                answer.append(i)
        # print('adj : ', adj, 'in_degree : ',in_degree, 'q : ', q)
        while q:
            cur = q.popleft()
            preq = adj[cur]
            for i in preq:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    q.append(i)
                    answer.append(i)
        # Need to add logic returning empty array when it's impossible to finish all courses
        if len(answer) != numCourses:
            return []
        return answer