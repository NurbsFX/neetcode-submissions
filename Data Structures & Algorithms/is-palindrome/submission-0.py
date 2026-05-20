class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''.join(char.lower() for char in s if char.isalnum())
        n = len(word)
        if n == 0:
            return True
        elif word[0]!=word[n-1]:
            return False
        else:
            i, j = 0, n-1
            while word[i]==word[j] and i < j:
                i+=1
                j-=1
        return i >= n//2
            
        