class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l =[]
        if n == 0:
            return l
        i, j = 0, n-1
        diff = target - numbers[i] - numbers[j]

        while diff != 0 and i < j:
            if diff < 0:
                j -= 1
            else:
                i += 1
            diff = target - numbers[i] - numbers[j]
        
        if diff == 0:
            return [i+1, j+1]
        else:
            return []