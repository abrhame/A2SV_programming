class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = Counter()
        l = 0
        length = 0
        for r in range(len(s)):
            seen[s[r]] += 1
            print(seen)
            

            while seen.total() > max(seen.values()) + k:
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    del seen[s[l]]
                l += 1
            length = max(length,seen.total())
        # length = max(length,seen.total()) 
        return length
            