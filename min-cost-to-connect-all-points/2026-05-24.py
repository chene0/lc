class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        pq = [(0, 0)]  # (cost, idx)
        visited = set()  # idx

        while len(visited) < len(points):
            cost, idx = heapq.heappop(pq)

            if idx in visited:
                continue

            visited.add(idx)
            res += cost

            for i in range(len(points)):
                if i in visited:
                    continue
                x0, y0 = points[idx]
                x1, y1 = points[i]
                man = abs(x1 - x0) + abs(y1 - y0)
                heapq.heappush(pq, (man, i))

        return res
