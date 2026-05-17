# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self,firstPairs, secondPairs):
        firstStart=0; secondStart=0;
        result=[]
        while firstStart< len(firstPairs) and secondStart < len(secondPairs):
            if firstPairs[firstStart].key > secondPairs[secondStart].key:
                result.append(secondPairs[secondStart])
                secondStart+=1
            else:
                result.append(firstPairs[firstStart])
                firstStart+=1

        result.extend(firstPairs[firstStart:])
        result.extend(secondPairs[secondStart:])
        return result

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        start = 0 ; end = len(pairs)

        if len(pairs) <= 1:
            return pairs
        
        mean = (start+end)//2

        firstMerged = self.mergeSort(pairs[:mean])
        secondMerged = self.mergeSort(pairs[mean:])

        newPairs = self.merge(firstMerged, secondMerged)

        return newPairs

