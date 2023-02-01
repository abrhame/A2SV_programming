class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1:
            ind = math.gcd(len(str2),len(str1))
            return str1[:ind]
        return ""