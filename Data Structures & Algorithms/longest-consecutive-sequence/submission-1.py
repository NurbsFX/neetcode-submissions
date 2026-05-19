class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dico = set(nums)
        if len(nums) == 0:
            return 0
        maxSequence=1
        for num in nums:
            sequence = [num]
            nextNum = num + 1
            while nextNum in dico:
                sequence.append(nextNum)
                nextNum += 1
            maxSequence = max(maxSequence, len(sequence))
        return maxSequence
            

        