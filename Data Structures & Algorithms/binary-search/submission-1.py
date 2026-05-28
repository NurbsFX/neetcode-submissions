class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1

        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                res = mid
                return res
            elif nums[mid] > target:
                if mid < right:
                    right = mid
                else:
                    right = mid - 1
            else:
                if mid > left:
                    left = mid
                else:
                    left = mid + 1

        return res