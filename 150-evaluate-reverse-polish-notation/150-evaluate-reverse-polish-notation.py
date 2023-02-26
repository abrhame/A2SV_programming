class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == "+":
                tmp = stack.pop() + stack.pop()
                stack.append(tmp)
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                tmp = b - a
                stack.append(tmp)
            elif token == "*":
                tmp = stack.pop() * stack.pop()
                stack.append(tmp)
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                tmp = int(b / a)
                stack.append(tmp)
            else:
                stack.append(int(token))
        return stack[0]