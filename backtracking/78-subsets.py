class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def helper(j):
            res.append(temp.copy())
            for i in range(j, len(nums)):
                temp.append(nums[i])
                helper(i+1)
                temp.pop()
        res = []
        temp = []
        helper(0)
        return res