class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        countS1 = {}
        countS2 = {}

        for i in range(len(s1)):
            countS1[s1[i]] = 1 + countS1.get(s1[i], 0)
        
        left = 0
        
        for right in range(len(s2)):
            countS2[s2[right]] = 1 + countS2.get(s2[right], 0)
            if right - left + 1 == len(s1):
                if countS1 == countS2:
                    return True
                else:
                    countS2[s2[left]] -= 1
                    if countS2[s2[left]] == 0:
                        del countS2[s2[left]]
                    left += 1
        
        return False