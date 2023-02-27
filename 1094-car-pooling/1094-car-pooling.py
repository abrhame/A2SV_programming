class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = 0
        for trip in trips:
            n = max(n,trip[2])
        prefix = [0] * (n+1)
        
        for trip in trips:
            num_pass, fromm, to = trip
            if num_pass > capacity:
                return False
            prefix[fromm] += num_pass
            prefix[to] -= num_pass

        for i in range(1,n):
            prefix[i] += prefix[i-1]
            if prefix[i-1] > capacity:
                return False
        return True
        