class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(amount + 1):
                if i - coin >= 0:
                    dp[i] += dp[i - coin]

        return dp[amount]   
        
        # coins.sort()
        # count = 0

        # def dfs(curr: int, index: int):
        #     nonlocal count
        #     if curr == amount:
        #         count += 1
        #         return
        #     for i in range(index, len(coins)):
        #         val = coins[i]
        #         if curr + val <= amount:
        #             dfs(curr + val, i)
        #         else:
        #             return


        # dfs(0, 0)
        # return count


"""
0 1 2 3 4 5 6 7 8 9
0 0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 1 1
0 1 2 2 3 3 4 4 5 5
0 1 2 3 4 5 7 8 10 12

"""

