class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i ** 2 for i in range(0, int(n ** (1 / 2)) + 1)]

        dp = [n + 1] * (n + 1)
        dp[0] = 0

        for i in range(n + 1):
            for j in range(len(squares)):
                if squares[j] <= i:
                    dp[i] = min(1 + dp[i - squares[j]], dp[i])

        return dp[-1]
