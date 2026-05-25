class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0

        if k == 0 or len(nums) == 0:
            return False

        for right in range(len(nums)):
            if abs(right - left) > k:
                window.remove(nums[left])
                left += 1
            if nums[right] in window and right != left:
                    return True
            window.add(nums[right])
        return False