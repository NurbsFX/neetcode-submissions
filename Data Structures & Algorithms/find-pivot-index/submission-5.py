class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        if n > 1 and sum(nums[1:]) == 0 :
            return 0
        elif n > 1 and sum(nums[:n-1]) == 0:
            return n-1

        for i in range(0,n-1):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i

        return -1
        