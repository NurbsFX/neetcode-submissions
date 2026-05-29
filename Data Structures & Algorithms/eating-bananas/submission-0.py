class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        

        while left <= right:
            k = (left + right)//2
            currentH = sum(math.ceil(piles[i]/k) for i in range(len(piles)))
            if currentH <= h:
                res = k
                right = k - 1
            else:
                left = k + 1

        
        return res