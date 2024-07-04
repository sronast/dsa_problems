class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = {i:[] for i in range(n)}
        for s,e in edges:
            graph[s].append(e)
            graph[e].append(s)

        visited = set()

        def dfs(n, parent):

            if n in visited:
                return False

            visited.add(n)
            res = True
            
            for c in graph[n]:
     
                if c == parent:
                    continue
                res = res and dfs(c, n)
            
            return res

        res = dfs(0, -1)
        return res and len(visited)==n