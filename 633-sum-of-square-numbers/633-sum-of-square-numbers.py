class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = floor(sqrt(c))
        if c == 1:
            return True
        while a <= b:
            C = pow(a,2) + pow(b,2)
            if C == c:
                return True
            elif C < c:
                a += 1
            else:
                b -=1
        return False
        