class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def reverse(p1,p2):
            if p1< p2:
                s[p1] ,s[p2] = s[p2] ,s[p1]
                return reverse(p1 + 1,p2 - 1)
        p1 = 0
        p2 = len(s) - 1
        reverse(p1,p2)
        print(s)
        
        
            
        