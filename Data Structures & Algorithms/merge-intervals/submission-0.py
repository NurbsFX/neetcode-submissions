class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd = newInterval
        res = []

        merged = False

        for interval in intervals:
            start, end = interval

            if end < newStart: 
                res.append(interval)
            elif start > newEnd:
                if not merged:
                    merged = True
                    res.append([newStart, newEnd])
                res.append(interval)
            else:
                newStart = min(start, newStart)
                newEnd = max(end, newEnd)
        
        if not merged:
            res.append([newStart, newEnd])
        
        return res

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        for interval in intervals:
            res = self.insert(res, interval)
        return res