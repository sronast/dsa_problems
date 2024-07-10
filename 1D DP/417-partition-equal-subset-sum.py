class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        
        C = sum(nums)//2 +1
        R = len(nums)+1

        dp = [[False for _ in range(C)] for _ in range(R)]
        for i in range(R):
            dp[i][0] = True
        for r in range(1,R):
            for c in range(1,C):
                dp[r][c] = dp[r-1][c]
                if c>=nums[r-1]:
                    dp[r][c] = dp[r][c] or dp[r-1][c-nums[r-1]]
        return dp[-1][-1]
        
        # if sum(nums)%2:
        #     return False

        # half = sum(nums)//2
        # dp = set()

        # dp.add(0)

        # for n in nums:
        #     tmp = set()
        #     for e in dp:
        #         tmp.add(e)
        #         if e+n == half:
        #             return True
        #         elif e+n<half:
        #             tmp.add(e+n)
        #     dp = tmp
        # return False
        
                    
                