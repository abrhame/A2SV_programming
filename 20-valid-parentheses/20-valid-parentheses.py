class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if stack and (stack[-1] == "(" and ch == ")"):
                stack.pop()
            elif stack and (stack[-1] == "[" and ch == "]"):
                stack.pop()
            elif stack and (stack[-1] == "{" and ch == "}"):
                stack.pop()
            elif ch == "(" or ch == "[" or ch == "{":
                stack.append(ch)
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False