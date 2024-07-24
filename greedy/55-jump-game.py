class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur_max = 0
        target = len(nums) - 1

        for i,n in enumerate(nums):
            cur_max = max(cur_max, i+n)
            if cur_max >= target:
                return True
            if cur_max<=i:
                return False
        return True