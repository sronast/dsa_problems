class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
# 1 2 3 4 5
# 2 3 4 5 1
# 3 4 5 1 2
# 4 5 1 2 3
# 5 1 2 3 4 
        while left<right:
            mid = (left+right)//2
            if nums[mid]<nums[right]:
                right = mid
            else:
                left = mid + 1
            
        return nums[left]
                

