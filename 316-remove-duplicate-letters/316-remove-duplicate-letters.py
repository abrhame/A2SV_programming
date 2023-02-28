class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        stack = []
        count = Counter(s)
        for ch in s:
            if ch not in stack:
                while stack and stack[-1] >= ch and count[stack[-1]] > 1:
                    count[stack.pop()] -= 1
                stack.append(ch)
            else:
                count[ch] -= 1
        return "".join(stack)
                