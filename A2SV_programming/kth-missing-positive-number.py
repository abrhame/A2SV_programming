class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        m = arr[-1]
        
        arr = set(arr)
        for i in range(1,m+1):
            if i not in arr:
                k -= 1

            if k == 0:
                return i

        return m + k