class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operation = ['+', '-', '*', '/']

        for t in tokens:
            if t in operation:
                r = stack.pop()
                l = stack.pop()
                if t == '+':
                    result = l + r
                elif t == '-':
                    result = l - r
                elif t == '*':
                    result = l * r
                elif t == '/':
                    result = int(l / r)
                stack.append(result)
            else:
                stack.append(int(t))

        return stack[0]
