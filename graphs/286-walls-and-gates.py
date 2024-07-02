import heapq
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = []
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((0, (r,c)))
        
        visited = set()
        heapq.heapify(q)
        while q:
            d, coor = heapq.heappop(q)
            if coor in visited:
                continue
            visited.add(coor)
            r,c = coor
            grid[r][c] = d
            
            for r_n, c_n in [(r+1,c), (r-1,c), (r, c-1), (r,c+1)]:
                if r_n>=rows or c_n>=cols or r_n<0 or c_n<0:
                    continue
                if grid[r_n][c_n] in {-1, 0}:
                    continue
                heapq.heappush(q, (d+1, (r_n,c_n)))
        
                