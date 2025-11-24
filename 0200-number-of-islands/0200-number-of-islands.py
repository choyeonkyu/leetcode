class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return
        M, N = len(grid), len(grid[0]) # row, col
        islands = 0
        visited = set()
        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            while q:
                cur_x, cur_y = q.popleft()
                for dx, dy in directions:
                    row, col = cur_x + dx, cur_y + dy
                    if row in range(M) and col in range(N) and (row, col) not in visited and grid[row][col] == "1":
                        visited.add((row, col))
                        q.append((row,col))
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    islands += 1
        return islands