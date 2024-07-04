#can be solved using union-find too

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for s,d in edges:
            graph[s].append(d)
            graph[d].append(s)
        
        res = 0
        visited = set()

        def dfs(n):
            if n in visited:
                return
            visited.add(n)
            
            for c in graph[n]:
                dfs(c)
            return
        
        for k in graph.keys():
            if k not in visited:
                dfs(k)
                res+=1
        res += n - len(graph.keys())
        return res