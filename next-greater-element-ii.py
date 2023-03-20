class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        result = [-1] * n
        
        for i in range(2*n-1):
            index = i % n
            
            while stack and stack[-1][1] < nums[index]:
                resIndex, _ = stack.pop()
                result[resIndex] = nums[index]
            
            stack.append([index, nums[index]])
        
        return result