"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda x: x.start)
        n = len(intervals)
        for i in range(1,n):
            previousStart, previousEnd = intervals[i-1].start, intervals[i-1].end
            start, end = intervals[i].start, intervals[i].end
            if start >= previousEnd:
                continue
            elif end <= previousStart:
                continue
            else:
                return False
        return True