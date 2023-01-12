class Solution:
    def findArray(self, pref: List[int]) -> List[int]:

        '''
          101
          010
        '''
        # ans = []
        # ans.append(pref[0])
        # i = 0
        # while len(ans) < len(pref)  and i < float('inf'):
        #     if pref[len(ans) - 1] ^ i == pref[len(ans)]: 
        #         ans.append(i)
        #         i = -1
        #     i+=1
        # return ans    
        
        ans = []
        ans.append(pref[0])
        for i in range(1, len(pref)):
            tmp = pref[i]^pref[i-1]
            ans.append(tmp)
        return ans