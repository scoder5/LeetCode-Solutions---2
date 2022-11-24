class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def dfs(row, col, i):
            if i == len(word):
                return True
            original, board[row][col] = board[row][col], '#'
            spreaded = False
            for dy, dx in ((1, 0), (-1,0), (0, 1), (0, -1)):
                nr, nc = row + dy, col + dx
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == word[i] and dfs(nr, nc, i+1):
                    spreaded = True
                    break
            board[row][col] = original
            return spreaded
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 1):
                    return True
        return False