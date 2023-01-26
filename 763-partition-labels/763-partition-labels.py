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
    
            
              
#         for i in range(len(s)):
#         ans = []
#         ind = 0
#         for i in range(len(s)):
#             if s[i] in s[i+1:]:
#                 ind = s[i+1:].index(s[i])
#                 seeker = max(ind,seeker)
#             else:
#                 ans.append(seeker-holder)
#                 holder = seeker
#         return ans
                
        
        
#         while seeker < len(s):
#             if (s[seeker] in s[holder:seeker]) and (s[seeker] not in s[seeker+1:len(s)]):
#                 ans.append(seeker-holder)
#                 holder = seeker + 1
#                 seeker = holder
#             else:
#                 seeker += 1
#         return ans
                