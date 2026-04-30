class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        q = []
        for i in range(len(queries)):
            q.append((queries[i], i))

        q.sort()
        intervals.sort()

        res = [-1] * len(queries)
        pq = []  # (size, r)
        int_i = 0

        for query, idx in q:
            while int_i < len(intervals) and intervals[int_i][0] <= query:
                interval = intervals[int_i]
                size = interval[1] - interval[0] + 1
                heapq.heappush(pq, (size, interval[1]))
                int_i += 1

            while pq and pq[0][1] < query:
                heapq.heappop(pq)

            if pq:
                res[idx] = pq[0][0]

        return res
