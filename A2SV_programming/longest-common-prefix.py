class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short = min(strs, key=len);
        
        for item in strs:
            while len(short) > 0:
                if item.startswith(short):
                    break
                else:
                    short = short[:-1]
        return short