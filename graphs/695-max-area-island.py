class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        area = 0

        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols:
                return 0
            elif grid[r][c] == 0:
                return 0
            res = 1
            grid[r][c] = 0

            res+=dfs(r,c-1)
            res+=dfs(r,c+1)
            res+=dfs(r-1,c)
            res+=dfs(r+1,c)

            return res
        
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r,c))
        return area

