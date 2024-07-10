class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def rec(i, lookup):
            if i>=len(cost):
                return 0
            
            elif i in lookup:
                return lookup[i]
            
            
            c1 = rec(i+1, lookup)
            c2 = rec(i+2, lookup)

            res = cost[i] + min(c1, c2)

            lookup[i] = res
            return res
        
        lookup = {}
        return min(rec(0,lookup), rec(1,lookup))
            