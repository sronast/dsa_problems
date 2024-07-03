class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        
        neighbors = [(1,0), (-1,0), (0,1),(0,-1)]
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c] != 'O':
                return
            board[r][c] = '#'

            for x, y in neighbors:
                dfs(r+x, c+y)

        for r in range(rows):
            for c in range(cols):
                if r in {0, rows-1}:
                    dfs(r,c)
                if c in {0, cols-1}:
                    dfs(r,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == '#':
                    board[r][c] = 'O'
