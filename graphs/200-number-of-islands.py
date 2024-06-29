class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return False
            elif grid[r][c] == '0':
                return False
            
            grid[r][c] = '0'

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

            return True
        count = 0
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c):
                    count += 1
        return count 
            