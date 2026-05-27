class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if sum(nums) < target:
            return 0

        length = float("inf")
        left = 0
        currentSum = 0

        for right in range(len(nums)):
            currentSum += nums[right]
            while currentSum >= target:
                length = min(length, right - left + 1)
                currentSum -= nums[left]
                left += 1
        
        if length == float("inf"):
            return 0
        else:
            return length