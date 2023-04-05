class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        arr = []
        ans = []
        def solve(idx, sub):
            if idx >= n:
                return
            
            
            for i in range(idx,n):
                sub.append(nums[i])
                arr.append(sub[:])
                solve(i+1,sub)
                sub.pop()
        solve(0,[])
        for i in range(len(arr)):
            temp = arr[i][0]
            if len(arr[i]) > 1:
                for j in range(1,len(arr[i])):
                    temp = temp | arr[i][j]
                arr[i] = temp
            else:
                arr[i] = temp
        max_ = max(arr)
        return arr.count(max_)