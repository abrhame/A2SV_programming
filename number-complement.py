class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)
        num = "".join((["1" if b == "0" else "0" for b in num[2:]]))
        return int(num,2)