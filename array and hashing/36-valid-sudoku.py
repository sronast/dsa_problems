from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_map = defaultdict(set)
        cols_map = defaultdict(set)
        grid_map = defaultdict(set)

        ROWS = len(board)
        COLS = len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                val = board[r][c]
                if val == '.':
                    continue
                if (val in rows_map[r] or
                    val in cols_map[c] or
                    val in grid_map[(r//3, c//3)]
                ):
                    return False

                rows_map[r].add(val) 
                cols_map[c].add(val) 
                grid_map[(r//3, c//3)].add(val) 
        return True