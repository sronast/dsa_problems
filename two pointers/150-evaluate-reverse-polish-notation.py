class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+', '-', '*', '/'}
        stack = []
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
                continue
            b = stack.pop()
            a = stack.pop()
            stack.append(self.simplify(a,b,t))
        return stack[0]
    

    def simplify(self, a, b, op):
        if op == '+':
            return a+b
        elif op == '-':
            return a-b
        elif op == '*':
            return a*b
        else:
            return int(a/b)
        