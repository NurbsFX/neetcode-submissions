class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        newList = []
        index = 0

        while index < len(nums):
            if nums[index] not in seen:
                seen.add(nums[index])
                index += 1
            else:
                nums.pop(index)
            
        return len(nums)