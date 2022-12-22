class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            x = str(x)
            s = x[0]
            x = x.replace(s,"")
            y = int(s+(x[::-1]))
            
        y = int(str(x)[::-1])
        if x==y:
            return True
        else: 
            return False
        