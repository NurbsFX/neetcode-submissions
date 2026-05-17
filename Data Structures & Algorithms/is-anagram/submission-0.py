class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        n = len(s)

        for i in range(n):
            if s[i] not in countS:
                countS[s[i]]=1
            else:
                countS[s[i]]+=1
            
            if t[i] not in countT:
                countT[t[i]]=1
            else:
                countT[t[i]]+=1
        
        return countT == countS
        