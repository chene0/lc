class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        M = len(matrix)
        N = len(matrix[0])

        res = []

        def fourSided(top, bot, left, right):
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            for r in range(top + 1, bot + 1):
                res.append(matrix[r][right])
            for c in range(right - 1, left - 1, -1):
                res.append(matrix[bot][c])
            for r in range(bot - 1, top, -1):
                res.append(matrix[r][top])

        for i in range(-(-min(M, N) // 2)):
            top = i
            bot = M - i - 1
            left = i
            right = N - i - 1
            if top > bot or left > right:
                break

            if top < bot and left < right:
                fourSided(top, bot, left, right)
            elif top == bot:
                for c in range(left, right + 1):
                    res.append(matrix[top][c])
            else:
                for r in range(top, bot + 1):
                    res.append(matrix[r][left])

        return res
