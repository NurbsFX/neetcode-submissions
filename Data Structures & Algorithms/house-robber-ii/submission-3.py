class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        dp1 = [0,0]
        dp2 = [0,0]
        for n in nums[0:len(nums)-1]:
            newval = max(n + dp1[0], dp1[1])
            dp1[1], dp1[0] = newval, dp1[1]  
        for n in nums[1:]:
            newval = max(n + dp2[0], dp2[1])
            dp2[1], dp2[0] = newval, dp2[1]  
        return max(dp1[1], dp2[1])