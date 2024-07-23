class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        intervals.sort()

        s1, e1 = intervals[0]

        for i, (s2,e2) in enumerate(intervals):
            if i == 0:
                continue
            if s2>e1:
                res.append([s1,e1])
                s1 = s2
                e1 = e2
            else:
                s1 = min(s1,s2)
                e1 = max(e1,e2)
        res.append([s1,e1])
        return res