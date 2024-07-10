def rob(self, nums: List[int]) -> int:
    
    def helper(s, e):
        h1 = 0
        h2 = 0

        for i in range(s, e):
            temp = h2
            h2 = max(h2, h1+nums[i])
            h1 = temp
        return h2
    if len(nums) == 1:
        return nums[0]
    return max(helper(0, len(nums)-1), helper(1, len(nums)))
