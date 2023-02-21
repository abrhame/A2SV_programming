class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur = n
        while True:
            if str(cur) in seen:
                return False
            if cur == 1:
                return True
            
            cur = str(cur)
            seen.add(cur)
            cur = sum(list(map(lambda x: int(x)*int(x), cur)))
            
            
        