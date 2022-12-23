class Solution:
    def freqAlphabets(self, s: str) -> str:
        maps = {}
        word = ""
        for i in range(1,27):
            if i < 10:
                maps[str(i)] = chr(96 + i)
            else:
                maps[str(i) + "#"] = chr(96 + i)
                
        i = 0
        
        while i < len(s):
            if i+2 <len(s) and s[i+2] == "#" :

                word = word + maps[str(s[i:i+3])]
                i = i + 3
            else:
                word = word + maps[str(s[i])]
                i = i + 1
        return word
