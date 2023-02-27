class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]
        
        for i in range(n-1):
            answer.append(answer[i] * nums[i])
        
        postfix = 1
        for i in range(n-1,-1,-1):
            answer[i] = postfix * answer[i]
            postfix = postfix * nums[i]
        return answer