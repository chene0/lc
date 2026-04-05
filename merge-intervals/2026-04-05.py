class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        interval_count = len(intervals)
        intervals.sort(key=lambda x: x[0])
        res = []

        for i in range(interval_count):
            interval = intervals[i]

            if len(res) and interval[0] <= res[-1][1]:
                res[-1] = [res[-1][0], max(res[-1][1], interval[1])]
            else:
                res.append(interval)

        return res
