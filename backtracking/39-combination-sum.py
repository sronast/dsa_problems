class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        tmp = []
        def helper(total, idx):
            if total == 0:
                res.append(tmp.copy())
                return
            elif total<0:
                return
            
            for i in range(idx, len(candidates)):
                tmp.append(candidates[i])
                helper(total-candidates[i], i)
                tmp.pop()
        helper(target, 0)
        return res
