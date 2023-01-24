class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        p1 = 0
        p2 = 1
        while p2 < n:
            if arr[p1] > arr[p2]:
                return 0
            p1 += 1
            p2 += 1
        return 1
