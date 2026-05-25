class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        if len(arr) == 0 or k == 0:
            return count
        
        left = 0
        while left + k -1 < len(arr):
            currentSubArray = arr[left:left + k]
            average = sum(currentSubArray)/len(currentSubArray)
            if average >= threshold:
                count += 1
            left += 1
            
        return count
            