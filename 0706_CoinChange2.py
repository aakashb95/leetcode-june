# 2D DP solution
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for i in range(amount + 1)] for j in range(len(coins) + 1)]

        for row in dp:
            row[0] = 1

        for row in range(1, len(coins) + 1):
            for col in range(1, amount + 1):
                if col >= coins[row - 1]:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - coins[row - 1]]
                else:
                    dp[row][col] = dp[row - 1][col]

        return dp[-1][-1]
