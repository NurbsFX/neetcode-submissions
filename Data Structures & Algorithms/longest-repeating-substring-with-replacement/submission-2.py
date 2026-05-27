class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        length = 0
        left = 0
        mostFrequent = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            mostFrequent = max(mostFrequent, count[s[right]])

            while (right - left + 1) - mostFrequent > k:
                count[s[left]] -= 1
                left += 1
            
            length = max(length, right - left + 1)
        
        return length