class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        q = collections.deque()
        q.append(entrance)
        answer = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        M, N = len(maze), len(maze[0])
        visited = [[False] * N for _ in range(M)]
        visited[entrance[0]][entrance[1]] = True
        while q:
            length = len(q)
            for i in range(length):
                x, y = q.popleft()
                for dir_x, dir_y in directions:
                    if 0 <= x+dir_x < M and 0 <= y+dir_y < N and (x+dir_x == 0 or x+dir_x == M-1 or y+dir_y == 0 or y+dir_y == N-1) and maze[x+dir_x][y+dir_y] == "." and not visited[x+dir_x][y+dir_y]:
                        return answer + 1
                    if 0 <= x+dir_x < M and 0 <= y+dir_y < N and maze[x+dir_x][y+dir_y] == "." and not visited[x+dir_x][y+dir_y]:
                        q.append([x+dir_x , y+dir_y])
                        visited[x+dir_x][y+dir_y] = True  
            answer += 1
        return -1