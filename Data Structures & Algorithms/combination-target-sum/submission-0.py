class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, subset):
            total = sum(subset)
            if i == len(nums) or total >= target:
                if total == target:
                    res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i, subset)
            subset.pop()
            dfs(i+1, subset)
        
        dfs(0, [])
        return res