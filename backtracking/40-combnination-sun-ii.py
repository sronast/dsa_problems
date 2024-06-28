class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        tmp = []
        candidates.sort()
        def helper(idx, val):
            if val == 0:
                res.append(tmp.copy())
                return
            if val<0:
                return
            
            for i in range(idx, len(candidates)):
                if i>idx and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i]>val:
                    break
                tmp.append(candidates[i])
                helper(i+1, val-candidates[i])
                tmp.pop()
        helper(0, target)
        return res