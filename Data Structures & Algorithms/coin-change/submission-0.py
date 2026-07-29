class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        
        for i in range(amount + 1):
            local_min = dp[i]
            for coin in coins:
                if i - coin >= 0:
                    local_min = min(local_min, dp[i - coin] + 1)
            dp[i] = local_min

        return dp[-1] if dp[-1] != float('inf') else -1