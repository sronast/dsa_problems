class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        neighbors = [(1,0), (0,1),(-1,0), (0,-1)]
        q = []
        cnt = 0
        t=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    cnt+=1
        if not cnt:
            return 0
        while q:
            t+=1
            nxt = []
            for r,c in q:
                for x,y in neighbors:
                    r_n, c_n = r+x, c+y

                    if r_n<0 or c_n<0 or r_n>=rows or c_n>=cols or grid[r_n][c_n]!=1:
                        continue
                    cnt-=1
                    if cnt ==0:
                        return t
                    grid[r_n][c_n] = 2
                    nxt.append((r_n,c_n))
            q = nxt
        return t if not cnt else -1