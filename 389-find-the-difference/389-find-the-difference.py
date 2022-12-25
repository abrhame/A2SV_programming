class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
            # 1.create a dictionary of s
            dictionary = {}
            for char in t:
                if char in dictionary:
                    dictionary[char] +=1
                else:
                    dictionary[char] = 1
                
            # 2.iterate over t and if you find a caharcter that is not in dictionary add the character to the dictionary with avlue of one.
            for char in s:
                if char in dictionary:
                    dictionary[char] -=1
                    
            # 3.iterate the dictionary adn return a key with value of 1
            for char in dictionary:
                    if dictionary[char] == 1:
                        return char;
                # extra={}
                # for i in t:
                #     if i in extra:
                #          extra[i]+=1
                #     else:
                #          extra[i]=1
                # for i in s:
                #      if i in extra:
                #         extra[i]-=1
                # for i in extra:  
                #         if extra[i]==1:
                #               return i