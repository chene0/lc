class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        fresh_count = 0
        rot_q = collections.deque()  # (r,c)

        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    rot_q.append((r, c))

        if fresh_count == 0:
            return 0

        time = 0
        while fresh_count > 0 and rot_q:
            new_rot_q = collections.deque()

            while rot_q:
                r, c = rot_q.popleft()

                for dr, dc in direct:
                    i = r + dr
                    j = c + dc
                    if i < 0 or i >= M or j < 0 or j >= N or grid[i][j] != 1:
                        continue

                    grid[i][j] = 2
                    fresh_count -= 1
                    new_rot_q.append((i, j))

            rot_q = new_rot_q
            time += 1

        return time if fresh_count == 0 else -1
