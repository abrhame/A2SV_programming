class Solution:
    def countArrangement(self, n: int) -> int:
        self.ans = 0
        def backtrack(arr, path):
            if len(arr) == n:
                self.ans += 1
                return

            for idx in range(1, n + 1):
                if path & (1 << idx) == 0:
                    if idx % (len(arr) + 1) == 0 or (len(arr) + 1) % idx == 0:
                        arr.append(idx)
                        path |= 1 << idx
                        backtrack(arr, path)
                        path ^= 1 << idx
                        arr.pop()

        backtrack([], 0)
        return self.ans