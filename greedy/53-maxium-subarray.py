class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        ret = nums [0]
        for i,n in enumerate(nums):
            if i == 0:
                continue
            if n+res <= n:
                res = n
            else:
                res = n + res
            ret = max(ret, res)
        return ret