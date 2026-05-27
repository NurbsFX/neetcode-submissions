import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(float(a) / b)  # division arrondie vers zéro
        }

        token = tokens.pop()

        if token in ops:
            b = self.evalRPN(tokens)
            a = self.evalRPN(tokens)
            return ops[token](a, b)
        else:
            return int(token)
