class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        if len(arr) < k:
            return count
        left = 0
        currentSum = 0
        for right in range(len(arr)):
            currentSum += arr[right]
            if right - left + 1 == k:
                if currentSum/k >= threshold:
                    count += 1
                currentSum -= arr[left]
                left += 1
            if right - left + 1 > k:
                currentSum -= arr[left]
                left += 1
        
        return count