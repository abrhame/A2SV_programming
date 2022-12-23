class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        words = ""
        maxLength = min(len(word1),len(word2))
        list = []
        list.append(word1)
        list.append(word2)
        list.sort(key=len)
        
        long = list[-1]
        
        for it in range(int(maxLength)):
            words = words + word1[it]
            words = words + word2[it]
        # words = words + words not in word1
        # words = words + words not in word2
        word = words + long[maxLength:]
        return word
        