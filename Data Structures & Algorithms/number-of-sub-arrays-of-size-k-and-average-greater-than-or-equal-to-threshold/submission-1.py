class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        if len(arr) == 0 or k == 0:
            return count
        
        left = 0
        currentSum = sum(arr[:k - 1])
        while left + k - 1 < len(arr):
            currentSum += arr[left + k - 1]
            average = currentSum/k
            if average >= threshold:
                count += 1
            currentSum -= arr[left]
            left += 1
            
        return count
            