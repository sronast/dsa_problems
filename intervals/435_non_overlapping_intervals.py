class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0

        intervals.sort()
        s1, e1 = intervals[0]

        for i, (s2,e2) in enumerate(intervals):
            if i == 0:
                continue
            if s2<e1:
                res +=1
            if s2>=e1 or e1>e2:
                s1, e1 = s2, e2
        return res