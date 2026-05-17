class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = set(nums)
        n = len(nums)
        for i in range(n):
            diff = target - nums[i]
            if diff in numbers and nums.index(diff) != i:
                indexDiff = nums.index(diff)
                return [min(i, indexDiff), max(i, indexDiff)]
