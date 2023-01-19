class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i+1 for i in range(n)]
        start = 0
        while len(arr)>1:
            start=(start+k-1)%len(arr)
            arr.pop(start)
        return arr[0]