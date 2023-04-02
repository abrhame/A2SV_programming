class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = None
        while n>0:
            tmp = n & 1
            if tmp == prev:
                return False
            else:
                prev = tmp
            n >>= 1
        return True