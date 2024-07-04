class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        ### union find ###

        def find(v):
            res = v
            while res != parent[res]:
                res = parent[parent[res]]
            return res
        
        def union(u,v):
            pu, pv = find(u), find(v)
            
            if pu == pv:
                return True
            
            if rank[pu]>rank[pv]:
                rank[pu] += rank[pv]
                parent[pu] = parent[pv]
            else:
                rank[pv] += rank[pu]
                parent[pv] = parent[pu]

            return False

        parent = [i for i in range(len(edges))]
        rank = [1 for _ in range(len(edges))]
        
        for u,v in edges:
            print(u,v)
            if union(u-1,v-1):
                return [u,v]


        ####### using dfs #####
        # def dfs(node, parent, visited, graph):
        #     if node in visited:
        #         return False

        #     visited.add(node)
        #     for child in graph[node]:
        #         if child == parent:
        #             continue
        #         if not dfs(child, node, visited, graph):
        #             return False
        #     return True
        
        # graph = defaultdict(list)

        # for s,d in edges:
        #     graph[s].append(d)
        #     graph[d].append(s)

        #     if not dfs(s, -1, set(), graph):
        #         return [s,d]