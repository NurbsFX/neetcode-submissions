class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        res = []
        subset = []

        if n == 0:
            return res

        mapping = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        mappedDigits = [mapping[i] for i in digits]

        def dfs(i):
            if i == n:
                if len(subset) == n:
                    newsubset = ''.join(subset)
                    res.append(newsubset)
                return
            for k in range(len(mappedDigits[i])):
                subset.append(mappedDigits[i][k])
                dfs(i+1)
                subset.pop()
            dfs(i+1)

        dfs(0)

        return res
    
        