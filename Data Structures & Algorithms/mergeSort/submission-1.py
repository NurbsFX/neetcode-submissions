# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, list1, list2):
        firstStart, secondStart = 0, 0
        result = []
        while firstStart < len(list1) and secondStart < len(list2):
            if list1[firstStart].key<=list2[secondStart].key:
                result.append(list1[firstStart])
                firstStart +=1
            else:
                result.append(list2[secondStart])
                secondStart += 1
        
        result.extend(list1[firstStart:])
        result.extend(list2[secondStart:])

        return result

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        middle = len(pairs)//2

        if len(pairs) <= 1:
            return pairs
        
        firstMerged = self.mergeSort(pairs[:middle])
        secondMerged = self.mergeSort(pairs[middle:])

        return self.merge(firstMerged, secondMerged)