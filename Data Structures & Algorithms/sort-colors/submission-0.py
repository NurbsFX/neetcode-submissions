class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0] ; result = []

        for n in nums:
            counts[n]+=1

        index = 0

        for i in range(3):
            number = counts[i]
            while number != 0:
                nums[index]=i
                index+=1
                number -= 1

        return result