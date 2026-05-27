class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        dicoArea = {}
        for k in range(len(height)):
            dicoArea[k] = 0
        while left < right:
            level = min(height[left],height[right])
            for k in range(left + 1, right):
                waterLevel = level - height[k]
                if waterLevel > dicoArea[k]:
                    dicoArea[k] = waterLevel
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return sum(dicoArea.values())
