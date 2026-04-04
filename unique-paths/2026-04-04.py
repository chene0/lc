class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[r][c] = dp[r+1][c]? + dp[r][c+1]?

        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                dp[r][c] += dp[r + 1][c] if (r + 1) < m else 0
                dp[r][c] += dp[r][c + 1] if (c + 1) < n else 0

        return dp[0][0]
