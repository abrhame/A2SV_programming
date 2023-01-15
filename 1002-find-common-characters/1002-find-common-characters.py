class Solution:
    def commonChars(self, words: List[str]) -> List[str]: 
        # take the first string as a reference
        word = list(words[0])
        
        for i in range(1,len(words)):
            j = 0
            while j < len(word):
                # iterate over the refernce string and chcek whtehr the character is found in other strings and remove if it is not found.
                if  word[j] not in words[i]:
                    word.remove(word[j]) 
                else:
                    j += 1
                    
            #check for the repeatd characters in the repeated characters in refernce with the word[i]
            for ch in words[i]:
                count1 = words[i].count(ch)
                count2 = word.count(ch)
                
                #remove n characters from the refernce string. n is the number of specific charcter found in word[i]
                if count2 > count1:
                    for _ in range(count2-count1):
                        word.remove(ch)  
        return word
                
            