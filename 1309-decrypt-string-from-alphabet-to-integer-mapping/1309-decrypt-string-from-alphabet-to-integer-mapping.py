class Solution:
    def freqAlphabets(self, s: str) -> str:
         # given string formed with digits and #
        #map s to english lowecase letters
        #(a->i) => (1->9)
        #(j->z)=> (10#->26#)
        #create a dictionary 
        #loop and put them as key value pairs
        
        dictionary = {}
#         for digit in range(1,27):
#             #generate alpahbets automatically as keys
#             print(digit)
#             # dictionary = dict.fromkeys(string.ascii_lowercase, digit)
           

            
#         a =  {chr(i+96):i for i in range(1,27)}
#         print(a)

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