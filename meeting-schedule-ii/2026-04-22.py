"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x: x.start)

        pq = [intervals[0].end]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            closing = pq[0]

            if interval.start >= closing:
                heapq.heappop(pq)
            heapq.heappush(pq, interval.end)

        return len(pq)
