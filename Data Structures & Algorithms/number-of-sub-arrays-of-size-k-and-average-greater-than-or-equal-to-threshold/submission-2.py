class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        if len(arr) < k:
            return count
        left = 0

        for right in range(len(arr)):
            if right - left + 1 == k:
                if sum(arr[left:right+1])/k >= threshold:
                    count += 1
                left += 1
            if right - left + 1 > k:
                left += 1
        
        return count