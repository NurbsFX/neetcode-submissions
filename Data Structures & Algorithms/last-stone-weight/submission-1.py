import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        reverse = [-x for x in stones]
        heapq.heapify(reverse)
        while len(reverse) > 1:
            x = abs(heapq.heappop(reverse))
            y = abs(heapq.heappop(reverse))
            if x == y:
                continue
            else:
                remaining = abs(x-y)
                heapq.heappush(reverse, -remaining)
        return abs(heapq.heappop(reverse)) if reverse else 0