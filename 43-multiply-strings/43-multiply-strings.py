class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convert(s):
            num = 0
            for i in s:
                num = num*10+(ord(i)-48)
            return num
        num1 = convert(num1)
        num2 = convert(num2)
        return str(num1*num2)
    