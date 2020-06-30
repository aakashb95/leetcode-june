# DP:
class Solution:
    def uniquePaths(self, m, n):
        aux = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i][j - 1] + aux[i - 1][j]
        return aux[-1][-1]


# DP 1-D:
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j - 1] + dp[j]
        return dp[-1] if m and n else 0


# Math:
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return round(
            math.factorial(m + n - 2) / (math.factorial(m - 1) * math.factorial(n - 1))
        )

