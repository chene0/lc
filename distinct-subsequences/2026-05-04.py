class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M = len(s)
        N = len(t)

        dp = [[-1] * N for _ in range(M)]

        def dfs(r, c):
            if c >= N:
                return 1

            if r >= M:
                return 0

            if dp[r][c] != -1:
                return dp[r][c]

            res = dfs(r + 1, c)
            if s[r] == t[c]:
                res += dfs(r + 1, c + 1)

            dp[r][c] = res
            return res

        return dfs(0, 0)
