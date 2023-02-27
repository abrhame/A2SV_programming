class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0] * (n+1)
        shifted_s = ["a"] * n
        for shift in shifts:
            start, end,direction = shift
            if direction == 1:
                prefix[start] += 1
                prefix[end + 1] -= 1
            else:
                prefix[start] -= 1
                prefix[end + 1] += 1
                
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i-1]
        print(prefix)
        ord_a = ord("a")
        for i in range(n):
            shifted_s[i] = chr(((ord(s[i]) - ord_a + prefix[i])%26) + ord_a)
            
        return "".join(shifted_s)    
        
        
            