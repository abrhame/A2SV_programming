class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * (n+1)
        postfix = [0] * n
        res =  [0] * n
        prefix[0] = 1
        for i in range(1,n):
            prefix[i] = nums[i-1] * prefix[i-1]
            
        postfix[n-1] = 1
        for i in range(n-2,-1,-1):
            postfix[i] = postfix[i+1] * nums[i+1]
            
        for i in range(n):
            print(prefix[i],i)
            res[i] = prefix[i] * postfix[i]
        
        return res