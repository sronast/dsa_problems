class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        op = []
        for i, num in enumerate(nums):
            if i>0 and nums[i-1] == num:
                continue
            j = i+1
            k = len(nums) - 1

            while j<k:
                res = num + nums[j] + nums[k]
                if res<0:
                    j+=1
                elif res>0:
                    k-=1
                else:
                    op.append([num,  nums[j],  nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1  
                
                    while k>j and nums[k] == nums[k+1]:
                        k-=1  
        return op 