class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        subset = []

        def dfs(subset, seen):
            if len(subset) == n:
                res.append(subset.copy())
                return

            for num in nums:
                if num in seen:
                    continue
                subset.append(num)
                seen.add(num)
                dfs(subset, seen)
                subset.pop()
                seen.remove(num)

        dfs([], set())

        return res
