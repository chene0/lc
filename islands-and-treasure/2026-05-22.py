class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        M = len(grid)
        N = len(grid[0])

        q = deque()  # (r, c)

        for r in range(M):
            for c in range(N):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()

            for dr, dc in direct:
                i = r + dr
                j = c + dc

                if i < 0 or i >= M or j < 0 or j >= N or grid[i][j] != INF:
                    continue

                grid[i][j] = 1 + grid[r][c]
                q.append((i, j))
