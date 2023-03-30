class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = x^y
        count = 0
        while ans > 0:
            count += ans & 1
            ans >>= 1
        return count