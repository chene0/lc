class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        M = len(s1)
        N = len(s2)

        if M + N != len(s3):
            return False

        dp = {}

        def dfs(r, c):
            if r >= M and c >= N:
                return True

            if (r, c) in dp:
                return dp[(r, c)]

            i = r + c
            res = False
            if r < M and s1[r] == s3[i]:
                res = dfs(r + 1, c)
            if c < N and not res and s2[c] == s3[i]:
                res = dfs(r, c + 1)

            dp[(r, c)] = res
            return res

        return dfs(0, 0)
