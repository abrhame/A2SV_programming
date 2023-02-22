class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagram = Counter()
        p_count = Counter(p)
        l = 0
        res = []
        for ch in s:
            anagram[ch] += 1
            if anagram.total() == len(p):
                if anagram == p_count:
                    res.append(l)
                if anagram[s[l]] > 1:
                    anagram[s[l]] -= 1
                else:
                    del anagram[s[l]]
                l += 1   
        return res
                    
                    
                
                
                
        
                