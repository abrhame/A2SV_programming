class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        stack = []
        count = Counter(s)
        seen = set()
        for ch in s:
            if ch not in seen:
                while stack and stack[-1] >= ch and count[stack[-1]] > 1:
                    c = stack.pop()
                    count[c] -= 1
                    seen.remove(c)
                stack.append(ch)
                seen.add(ch)
            else:
                count[ch] -= 1
        return "".join(stack)
                