class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # visited를 M * N size로 생성
        # 이중 for문을 돌면서 not visited면 하, 우 탐색하며 visited True로 바꿔줌 (0인 경우만)
        # 하, 우 못 옮기면 for문 하나 밖으로 나와서 위 for문 돌림 (이때 cnt += 1)
        M, N = len(grid), len(grid[0])
        visited = [[False] * N for _ in range(M)]
        q = collections.deque()
        cnt = 0
        mv = [(0,1), (1,0), (0,-1), (-1,0)]
        for x in range(M):
            for y in range(N):
                if grid[x][y] == "1" and not visited[x][y]:
                    q.append((x, y))
                    visited[x][y] = True
                    while q:
                        cur_x, cur_y = q.popleft()
                        for mv_x, mv_y in mv:
                            if 0 <= cur_x + mv_x < M and 0 <= cur_y + mv_y < N and grid[cur_x+mv_x][cur_y+mv_y] == "1" and not visited[cur_x+mv_x][cur_y+mv_y]:
                                q.append((cur_x+mv_x, cur_y+mv_y))
                                visited[cur_x+mv_x][cur_y+mv_y] = True
                    cnt += 1
        return cnt