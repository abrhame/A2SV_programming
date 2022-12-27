class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in itertools.count(start = n):
            if i % 2 == 0 and i % n == 0:
                return i
            else:
                continue