class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        M = len(s)
        N = len(p)

        dp = {}

        def dfs(r, c):
            if r >= M and c >= N:
                return True

            if c >= N:
                return False

            if (r, c) in dp:
                return dp[(r, c)]

            isMatch = r < M and (p[c] == "." or s[r] == p[c])
            if (c + 1) < N and p[c + 1] == "*":
                isMatch = (isMatch and dfs(r + 1, c)) or dfs(r, c + 2)
            else:
                isMatch &= dfs(r + 1, c + 1)

            dp[(r, c)] = isMatch
            return isMatch

        return dfs(0, 0)
