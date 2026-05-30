from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            x, y = point[0], point[1]
            distances.append((sqrt(x**2+y**2), point))
        heapq.heapify(distances)
        
        res = []
        i = 0
        print(distances)
        while i < k and distances: 
            res.append(heapq.heappop(distances)[1])
            i += 1
        return res