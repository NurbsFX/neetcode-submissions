class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = sorted(strs, key=len)
        n = len(l[0])
        res = ""
        for i in range(n):
            for s in l:
                if s[i] != l[0][i]:
                    return res
            res += l[0][i]
        
        return res