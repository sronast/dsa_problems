class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        neighbors = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(r, c, idx):
            if idx == len(word):
                return True
            elif r<0 or r>=rows or c<0 or c>=cols or board[r][c] != word[idx]:
                return False

            temp = board[r][c]
            board[r][c] = ""
            res = False
            for i,j in neighbors:
                res = res or dfs(r+i, c+j, idx+1)
                if res:
                    break
            board[r][c] = temp
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
                

        