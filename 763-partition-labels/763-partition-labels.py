class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        start = 0
        last = 0
        ans = []
        
        for i in range(len(s)-1,-1,-1):
            if s[i] in d:
                continue
            else:
                d[s[i]] = i
        
        for i in range(len(s)):
            last = max(last,d[s[i]])
            if last == i:
                ans.append((last - start)+1)
                start = last + 1
        return ans
    
            
              

                