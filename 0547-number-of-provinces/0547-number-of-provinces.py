class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = [False] * n
        answer = 0

        def dfs(city):
            visited[city] = True

            for nxt in range(n):
                if isConnected[city][nxt] == 1 and not visited[nxt]:
                    dfs(nxt)

        for city in range(n):
            if not visited[city]:
                dfs(city)
                answer += 1
        
        return answer
