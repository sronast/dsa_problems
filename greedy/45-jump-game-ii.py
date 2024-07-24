class Solution:
    def jump(self, nums: List[int]) -> int:
        near = 0
        far = 0
        jump = 0
        for i, n in enumerate(nums):
            if i==near+1:
                near = far
                jump+=1
            far = max(far, n+i)
        return jump