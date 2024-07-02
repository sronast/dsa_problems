from typing import List 
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        neighbors = [(1,0),(-1,0),(0,1),(0,-1)]
        res = []

        visited = {'pacific':[[0]*cols for _ in range(rows)],
                    'atlantic': [[0]*cols for _ in range(rows)]}
        

        def dfs(r,c,parent, side='atlantic'):
            if r<0 or c<0 or r>=rows or c>=cols:
                return False
            elif heights[r][c]<parent or visited[side][r][c]:
                return False
            visited[side][r][c] = 1

            temp = True
            for k in visited.keys():
                temp = temp and visited[k][r][c]
            if temp:
                res.append([r,c])
            
            for x, y in neighbors:
                dfs(r+x, c+y, heights[r][c], side)
        
        for r in range(rows):
            dfs(r, 0, heights[r][0], 'pacific')
            dfs(r, cols-1, heights[r][cols-1], 'atlantic')

        for c in range(cols):
            dfs(0, c, heights[0][c], 'pacific')
            dfs(rows-1, c, heights[rows-1][c], 'atlantic')
        
        return res