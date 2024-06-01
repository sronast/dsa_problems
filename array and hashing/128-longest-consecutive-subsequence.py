class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for n in nums:
            if n-1 in nums:
                continue
            temp = 0
            cur = n
            while cur in nums:
                temp += 1
                cur += 1
            res = max(res, temp)
        return res