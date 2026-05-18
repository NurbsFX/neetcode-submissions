from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        countZero = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                countZero += 1
        
        if countZero > 1: 
            return [0]*n
        
        l = [1]*n

        for j in range(n): 
            if j == 0:
                l[j] = prod(nums[j:])
            elif j == n - 1:
                l[j] = prod(nums[:j-1])
            l[j]=prod(nums[:j])*prod(nums[j+1:])
        
        return l
        