class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd = newInterval
        res = []
        merged = False

        for interval in intervals:
            start, end = interval 

            if end < newStart:
                res.append([start, end])
            
            elif start > newEnd: 
                if not merged:
                    res.append([newStart, newEnd])
                    merged = True
                res.append(interval)
            
            else:
                newStart = min(newStart, start)
                newEnd = max(newEnd, end)
            
        if not merged:
            res.append([newStart, newEnd])
        
        return res