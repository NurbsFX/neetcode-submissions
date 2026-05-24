class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        subset = []

        def dfs(subset):
            if len(subset) == n:
                res.append(subset.copy())
                return

            for num in nums:
                if num in subset:
                    continue
                subset.append(num)
                dfs(subset)
                subset.pop()

        dfs([])

        return res
