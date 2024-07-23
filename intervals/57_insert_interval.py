class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s1, e1 = newInterval
        res = []
        for s2, e2 in intervals:
            if e1<s2:
                res.append([s1,e1])
                s1 = s2
                e1 = e2
            elif s1>e2:
                res.append([s2,e2])
            
            else:
                s1 = min(s1, s2)
                e1 = max(e1, e2)
        if not res or e1!=res[-1][-1]:
            res.append([s1,e1])
        return res
