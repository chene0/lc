"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if n == 0:
            return 0
        intervals.sort(key=lambda x: x.start)

        ends = [intervals[0].end]

        for i in range(1, n):
            interval = intervals[i]
            if interval.start >= ends[0]:
                heapq.heappop(ends)

            heapq.heappush(ends, interval.end)

        return len(ends)
