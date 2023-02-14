class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _set = set()
        length = 0
        l = 0
        
        for r in range(len(s)):
            while s[r] in _set:
                _set.remove(s[l])
                l += 1
            _set.add(s[r])
            length = max(length, r-l + 1)
        return length