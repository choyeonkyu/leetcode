class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])

        def dfs(cur, idx): # 현재 위치를 나타내는 idx를 input으로 넘김
            x, y = cur[0], cur[1]
            if idx == len(word): # 종료조건
                return True
            if x>=m or x < 0 or y >= n or y < 0: # 범위 외 cur 위치는 다 False 리턴
                return False
            if board[x][y] != word[idx]:
                return False
            temp = board[x][y]
            board[x][y] = '#'
            found = (
                dfs((x+1,y), idx+1) or
                dfs((x-1,y), idx+1) or
                dfs((x,y+1), idx+1) or
                dfs((x,y-1), idx+1)
            )
            # backtrack (원복)
            board[x][y] = temp
            return found
        for i in range(m):
            for j in range(n):
                if dfs((i,j),0):
                    return True
        return False
    