class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        dp = [0, 0]  
        for n in nums:
            new_val = max(n + dp[0], dp[1])
            dp[0], dp[1] = dp[1], new_val
        return dp[1]
