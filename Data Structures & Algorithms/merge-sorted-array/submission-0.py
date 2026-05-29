class Solution:
    def mergeTwo(self, l1: List[int], l2: List[int]) -> List[int]:
        res = []
        i = j = 0
        while i < len(l1) and j < len(l2):
            if l1[i] <= l2[j]:
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1
        res.extend(l1[i:])
        res.extend(l2[j:])
        return res

    def mergeSort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        l1 = self.mergeSort(arr[:mid])
        l2 = self.mergeSort(arr[mid:])

        return self.mergeTwo(l1, l2)

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = self.mergeSort(nums1[:m]+nums2)
        return nums1