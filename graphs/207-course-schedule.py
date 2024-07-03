class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        deps = {i: 0 for i in range(numCourses)}

        for d, s in prerequisites:
            graph[s].append(d)
            deps[d] = deps[d]+1

        count = 0

        cur = []
        for k, v in deps.items():
            if v == 0:
                cur.append(k)
                count+=1
        
        while cur:
            nxt = []
            for s in cur:
                for d in graph[s]:
                    deps[d] = deps[d] - 1
                    if deps[d] == 0:
                        count+=1
                        nxt.append(d)
            cur = nxt
            
        return count == numCourses 

        