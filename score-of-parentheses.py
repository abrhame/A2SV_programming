class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        output,val = 0,0

        for p in s:
            if p == "(":
                stack.append(0)
            elif p == ")":
                mul = stack.pop()
                if mul == 0:
                    val = 1
                else:
                    val = mul * 2
                if not stack:
                    output += val
                else:
                    stack[-1] += val
        
        return output