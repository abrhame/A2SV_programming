class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # change the given integer into array
        arr = [i+1 for i in range(n)]
        
        # remove all losers and return the last winner
        loser = 0
        while len(arr)>1:
            loser=(loser+k-1)%len(arr)
            arr.pop(loser)
        return arr[0]