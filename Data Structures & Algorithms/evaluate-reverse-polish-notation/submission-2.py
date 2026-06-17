class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = set(['+', '-', '/', '*'])
        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                operand = token
                if operand == '+':
                    c = a + b
                elif operand == '-':
                    c = a - b
                elif operand == '*':
                    c = a * b
                else:
                    c = int(a / b)
                stack.append(c)

        return stack[-1]

"""
-792
10

"""