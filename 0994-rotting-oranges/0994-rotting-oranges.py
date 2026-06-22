class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        visited = [[False] * N for _ in range(M)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        two_pos = []
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 2:
                    two_pos.append((x, y))
        q = collections.deque()
        for i in two_pos:
            q.append(i)
            visited[i[0]][i[1]] = True
        answer = 0
        while q:
            answer += 1
            length = len(q)
            for _ in range(length):
                x, y = q.popleft()
                for dir_x, dir_y in directions:
                    cand_x, cand_y = x+dir_x, y+dir_y
                    if 0 <= cand_x < M and 0 <= cand_y < N and grid[cand_x][cand_y] == 1 and not visited[cand_x][cand_y]:
                        q.append((cand_x, cand_y))
                        visited[cand_x][cand_y] = True
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1 and not visited[i][j]:
                    return -1
        if not two_pos:
            return 0
        return answer - 1