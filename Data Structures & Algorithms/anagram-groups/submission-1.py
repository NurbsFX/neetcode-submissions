class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dico = {}
        res = []

        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in dico:
                dico[sortedWord] = [word]
            else:
                dico[sortedWord].append(word)
        
        for value in dico.values():
            res.append(value)

        return res