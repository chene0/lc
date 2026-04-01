class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            this = intervals[i]
            if newInterval[1] < this[0]:
                return res + [newInterval] + intervals[i:]
            elif newInterval[0] > this[1]:
                res.append(this)
            else:
                newInterval = [
                    min(newInterval[0], this[0]),
                    max(newInterval[1], this[1]),
                ]

        return res + [newInterval]
