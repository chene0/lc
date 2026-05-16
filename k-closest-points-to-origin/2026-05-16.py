class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []  # (-dist, x, y)

        for x, y in points:
            dist = x**2 + y**2

            if len(pq) >= k and -dist <= pq[0][0]:
                continue

            heapq.heappush(pq, (-dist, x, y))

            if len(pq) > k:
                heapq.heappop(pq)

        res = []

        for dist, x, y in pq:
            res.append([x, y])

        return res
