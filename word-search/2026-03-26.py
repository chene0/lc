class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M = len(board)
        N = len(board[0])
        dir = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        def dfs(r, c, idx):
            if idx >= len(word):
                return True

            if (
                r < 0
                or r >= M
                or c < 0
                or c >= N
                or board[r][c] != word[idx]
                or board[r][c] == "*"
            ):
                return False

            char = board[r][c]
            board[r][c] = "*"

            for dr, dc in dir:
                i = r + dr
                j = c + dc

                curr = dfs(i, j, idx + 1)
                if curr:
                    return True

            board[r][c] = char

            return False

        for r in range(M):
            for c in range(N):
                #
                if dfs(r, c, 0):
                    return True

        return False
