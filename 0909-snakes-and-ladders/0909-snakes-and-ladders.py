class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        N = len(board)**2
        def int_to_board(n):
            row = -1 - ((n-1)//len(board))
            if row % 2:
                col = (n-1)%len(board)
            else:
                col = -1*((n-1)%len(board))-1
            return row, col, n
        q = collections.deque()
        q.append((1,0)) # board number, tree level
        visited = set()
        visited.add(1)
        while q: # Add logic to handle impossible case
            pos, level = q.popleft()
            cand = [pos+i for i in range(1,7)]
            moved_cand = []
            for i in cand:
                moved_cand.append(int_to_board(i))
            for r,c,pos in moved_cand:
                if pos > N:
                    continue
                if board[r][c] == -1 and pos not in visited:
                    if pos == N:
                        return level+1
                    q.append((pos, level+1))
                    visited.add(pos)
                elif board[r][c] != -1 and board[r][c] not in visited:
                    if board[r][c] == N:
                        return level+1
                    q.append((board[r][c], level+1))
                    visited.add(board[r][c])
        return -1