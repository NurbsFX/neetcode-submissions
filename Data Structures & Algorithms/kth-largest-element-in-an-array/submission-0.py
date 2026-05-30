class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        reverseNums = [-x for x in nums]
        heapq.heapify(reverseNums)
        i = 0
        while i < k - 1 and reverseNums:
            heapq.heappop(reverseNums)
            i += 1
        if reverseNums:
            return -heapq.heappop(reverseNums)