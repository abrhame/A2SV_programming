class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        sum_ = 0
        n = len(arr)
        arr.append(0)
        stack = [-1]
        
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num: # (i)
                idx = stack.pop()
                sum_ += arr[idx] * (i - idx) * (idx - stack[-1])
                
            stack.append(i)
            
        return sum_ % (10**9 + 7)