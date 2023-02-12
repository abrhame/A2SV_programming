class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        # compare the two strings and add the character from the 
        # larger string to the merged string
        merged = ""
        while word1 and word2:
            if word1 > word2:
                merged += word1[0]
                word1 = word1[1:]
            else:
                merged += word2[0]
                word2 = word2[1:]
        
        merged += word1
        merged += word2
        
        return merged
        
        