class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries_pq = []  # (query, idx)
        for i in range(len(queries)):
            heapq.heappush(queries_pq, (queries[i], i))
        intervals.sort()

        res = [-1] * len(queries)
        pq = []  # (size, r)
        i = 0

        while queries_pq:
            query, idx = heapq.heappop(queries_pq)
            while i < len(intervals) and intervals[i][0] <= query:
                interval = intervals[i]
                size = interval[1] - interval[0] + 1
                heapq.heappush(pq, (size, interval[1]))
                i += 1

            while pq and pq[0][1] < query:
                heapq.heappop(pq)

            if pq:
                res[idx] = pq[0][0]

        return res
