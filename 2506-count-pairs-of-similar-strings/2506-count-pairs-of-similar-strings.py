class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        
        # for i in range(len(words)):
        #     for j in range(i+1,len(words)):
        #         if set(words[i]) == set(words[j]):
        #             count+=1
        # return count
        l = []
        for word in words:
            tmp = list(set(word))
            tmp.sort()
            l.append("".join(tmp))
        print(l)
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if l[i] == l[j]:
                    count+=1
        return count
            