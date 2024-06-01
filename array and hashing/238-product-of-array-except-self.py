class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1] * N
        left = 1
        right = 1

        for i in range(N):
            res[i] *= left
            res[N-1-i] *= right  
            left *= nums[i]
            right *= nums[N-1-i]
        return res