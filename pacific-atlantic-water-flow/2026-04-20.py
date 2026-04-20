class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M = len(heights)
        N = len(heights[0])
        direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        pac = [[False] * N for _ in range(M)]
        atl = [[False] * N for _ in range(M)]

        def dfs(r, c, dp):
            if r < 0 or r >= M or c < 0 or c >= N or dp[r][c]:
                return

            dp[r][c] = True

            for dr, dc in direct:
                i = r + dr
                j = c + dc
                if i < 0 or i >= M or j < 0 or j >= N or heights[i][j] < heights[r][c]:
                    continue
                dfs(i, j, dp)

        for r in range(M):
            dfs(r, 0, pac)
            dfs(r, N - 1, atl)

        for c in range(N):
            dfs(0, c, pac)
            dfs(M - 1, c, atl)

        res = []
        for r in range(M):
            for c in range(N):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])

        return res
