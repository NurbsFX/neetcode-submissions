class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        solution = []
        numbers = sorted(nums)
        n = len(numbers)

        for k in range(n):
            target = -numbers[k]
            i, j = k + 1, n - 1
            while i < j:
                diff = target - numbers[i] - numbers[j]
                if diff == 0:
                    l = [numbers[k], numbers[i], numbers[j]]
                    if tuple(l) not in seen:
                        solution.append(l)
                        seen.add(tuple(l))
                    i += 1
                    j -= 1
                elif diff > 0:
                    i += 1
                else:
                    j -= 1

        return solution



        