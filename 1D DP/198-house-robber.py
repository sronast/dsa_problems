class Solution:
    def rob(self, nums: List[int]) -> int:
        im2 = 0
        im1 = 0

        for n in nums:
            tmp = im1
            im1= max(n+im2, im1)
            im2 = tmp
        return max(im1,im2)