class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M = len(board)
        N = len(board[0])

        direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if r < 0 or r >= M or c < 0 or c >= N or board[r][c] != "O":
                return

            board[r][c] = "T"

            for dr, dc in direct:
                i = r + dr
                j = c + dc
                dfs(i, j)

        for r in range(M):
            dfs(r, 0)
            dfs(r, N - 1)

        for c in range(1, N - 1):
            dfs(0, c)
            dfs(M - 1, c)

        for r in range(M):
            for c in range(N):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
