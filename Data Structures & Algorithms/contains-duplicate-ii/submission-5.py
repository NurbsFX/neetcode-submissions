class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for left in range(0, len(nums)):
            for right in range(left + 1, min(len(nums), left + k + 1)):
                if nums[left] == nums[right]:
                    return True
        
        return False