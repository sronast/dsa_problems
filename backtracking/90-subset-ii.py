class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        tmp = []

        def helper(idx):
            res.append(tmp.copy())

            for i in range(idx, len(nums)):
                if i>idx and nums[i-1] == nums[i]:
                    continue
                
                tmp.append(nums[i])
                helper(i+1)
                tmp.pop()
        helper(0)