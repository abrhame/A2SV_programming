class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # sort the piles
        piles.sort()
        ans = 0
        count = 0       # the limit of piles I can take, which is piles/3
        
        # find the next largest pile I can take 
        for i in range(len(piles)-2,-1,-2):
            
            ans += piles[i]
            count+=1
            
            if count == len(piles)/3:   # if I take all the piles  I am allowed then break out of the loop
                break
        return ans
        