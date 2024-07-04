class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # pre [c, p]
        graph = {i:[] for i in range(numCourses)}

        for c,p in prerequisites:
            graph[p].append(c)
        
        result = []
        visiting = [False for _ in range(numCourses)]
        visited = [False for _ in range(numCourses)]

        def dfs(c, res):
            if visiting[c]: return False
            if visited[c]: return True

            visiting[c] = True
            op = True
            for n in graph[c]:
                op = op and dfs(n, res)
            
            visiting[c] = False
            visited[c] = True
            res.append(c)
            return op
        
        for i in range(numCourses):
            if not dfs(i, result):
                return []
        return result[::-1]