class Solution:
    def commonChars(self, words: List[str]) -> List[str]:   
        word = list(words[0])
        for i in range(1,len(words)):
            j = 0
            while j < len(word):
                if  word[j] not in words[i]:
                    word.remove(word[j])
                else:
                    j += 1
            for ch in words[i]:
                count1 = words[i].count(ch)
                count2 = word.count(ch)
                if count2 > count1:
                    for _ in range(count2-count1):
                        word.remove(ch)  
        return word
                
            