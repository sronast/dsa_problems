class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp = 1
        minp = 1
        res = float('-inf')

        for n in nums:
            
            maxp = maxp*n
            minp = minp*n

            x = max(maxp, minp, n)
            y = min(maxp, minp, n)

            maxp = x
            minp = y

            res = max(res, maxp)
        return res
        