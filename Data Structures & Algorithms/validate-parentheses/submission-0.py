class Solution:
    def isValid(self, s: str) -> bool:
        dico = {
            '{':'}',
            '(':')',
            '[':']'
        }
        stack = []
        for char in s:
            if stack and stack[-1] in dico and dico[stack[-1]] == char:
                stack.pop()
            else:
                stack.append(char)
        
        return stack == []

        