"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def noConflict(self, intervals: List[Interval], currentInterval) -> bool:
        currentStart, currentEnd = currentInterval.start, currentInterval.end
        for interval in intervals:
            start, end = interval.start, interval.end
            if not (currentEnd <= start or currentStart >= end):
                return False
        return True

    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key= lambda x: x.start)

        dico = {}
        dico[0] = [intervals[0]]

        for i in range(1,len(intervals)):
            currentInterval = intervals[i]
            index = 0
            
            while index in dico and not self.noConflict(dico[index], currentInterval):
                index += 1
                
            if index in dico:
                dico[index].append(currentInterval)
            else:
                dico[index]= [currentInterval]
        return len(dico)