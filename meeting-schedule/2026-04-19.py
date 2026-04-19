"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        intervals.sort(key=lambda x: x.start)

        for i in range(1, n):
            curr = intervals[i]
            prev = intervals[i - 1]

            if curr.start < prev.end:
                return False

        return True
