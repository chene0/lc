class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        interval_count = len(intervals)
        res = []

        for i in range(interval_count):
            interval = intervals[i]
            if newInterval[1] < interval[0]:
                # merging no longer possible, insert here
                return res + [newInterval] + intervals[i:]
            elif newInterval[0] > interval[1]:
                res.append(interval)
            else:
                newInterval = [
                    min(interval[0], newInterval[0]),
                    max(interval[1], newInterval[1]),
                ]

        return res + [newInterval]
