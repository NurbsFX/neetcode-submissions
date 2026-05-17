class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternList = []
        stringList = s.split()
        dico = {}
        seen = set()

        for c in pattern:
            patternList.append(c)
        
        if len(patternList) != len(stringList):
            return False

        n = len(stringList)

        for i in range(n):
            if patternList[i] not in dico and stringList[i] not in seen:
                dico[patternList[i]] = stringList[i]
                seen.add(stringList[i])
            else:
                if patternList[i] not in dico or dico[patternList[i]] != stringList[i]:
                    return False
        
        return True