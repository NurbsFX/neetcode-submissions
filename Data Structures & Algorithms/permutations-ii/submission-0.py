class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        def dfs(subset, seen):
            if len(subset) == n:
                res.append(subset.copy())
                return
            
            for (i, num) in enumerate(nums):
                if i in seen:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and i - 1 not in seen:
                    continue
        
                subset.append(num)
                seen.add(i)

                dfs(subset, seen)

                subset.pop()
                seen.remove(i)
            
        dfs([], set())
        return res