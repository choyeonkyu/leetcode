class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for a, b in connections:
            graph[a] += [(b, 1)]
            graph[b] += [(a, 0)]
        visited = [False] * n

        def dfs(node):
            visited[node] = True
            answer = 0
            for nxt, cost in graph[node]:
                if not visited[nxt]:
                    answer += cost
                    answer += dfs(nxt)

            return answer
        
        return dfs(0)