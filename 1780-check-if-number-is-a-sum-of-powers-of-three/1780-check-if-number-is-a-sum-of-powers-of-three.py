class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        comb = []
        i = 0
        k = 0
        while k < 1 * 10**7:
            comb.append(3**i)
            i += 1
            k = comb[-1]
            
        i = len(comb) - 1
        while n > 0 and i >= 0:
            if comb[i] <= n:
                n -= comb[i]
            i -= 1
        if n == 0:
            return True
        return False