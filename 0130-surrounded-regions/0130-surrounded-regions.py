class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])
        visited = set()

        def bfs(r, c):
            visited.add((r,c))
            q = collections.deque()
            q.append((r,c))
            while q:
                cur_x, cur_y = q.popleft()
                directions = [(0,1), (0, -1), (1,0), (-1,0)]
                for dx, dy in directions:
                    x, y = cur_x + dx, cur_y + dy
                    if 0 <= x < M and 0 <= y < N and (x,y) not in visited and board[x][y] == 'O':
                        board[x][y] = '#'
                        visited.add((x,y))
                        q.append((x,y))
        for i in range(M):
            for j in range(N):
                if (i == 0 or i == M-1 or j == 0 or j == N-1) and board[i][j] == 'O':
                    board[i][j] = '#'
        for i in range(M):
            for j in range(N):
                if board[i][j] == '#':
                    bfs(i,j)
        for i in range(M):
            for j in range(N):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'