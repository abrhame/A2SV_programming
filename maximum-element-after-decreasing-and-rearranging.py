class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        m = 1
        if arr[0] != 1:
            arr[0] = 1
        for i in range(n-1):
            # print(arr)
            if abs(arr[i+1] - arr[i]) > 1:
                arr[i + 1] = arr[i] + 1
                m = max(m,arr[i+1])
        m = max(m,arr[-1])
        return m