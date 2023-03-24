class Solution:
    def splitString(self, s: str) -> bool:
        cur = []

        def backtrack(idx):
            if idx == len(s):
                return len(cur) >= 2

            for i in range(idx + 1,len(s) + 1):
                num = int(s[idx:i])
                if len(cur) == 0 or cur[-1] - 1 == num:
                    cur.append(num)
                    if backtrack(i):
                        return True
                    cur.pop()

        return backtrack(0)