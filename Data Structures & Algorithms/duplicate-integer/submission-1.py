class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dico = {}
        for num in nums: 
            if num not in dico:
                dico[num]=1
            else:
                return True
        return False