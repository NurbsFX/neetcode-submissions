class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = [0] * len(height)
        while left < right:
            level = min(height[left],height[right])
            for k in range(left + 1, right):
                waterLevel = level - height[k]
                area[k] = max(waterLevel, area[k])
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return sum(area)
