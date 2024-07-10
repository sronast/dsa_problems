class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        coins.sort()
        for i in range(1, amount+1):
            for c in coins:
                if i>=c:
                    dp[i] = min(dp[i], dp[i-c]+1)
                else:
                    break
        return -1 if dp[-1] == float('inf') else dp[-1]