class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.ans = set()
        stack = []
        def backtrack(idx):
            if idx == len(nums):
                if len(stack) >= 2:
                    self.ans.add(tuple(stack))
                return 
            
            if not stack or stack[-1] <= nums[idx]:
                stack.append(nums[idx])
                backtrack(idx+1)
                stack.pop()
            backtrack(idx+1)


        backtrack(0)
        return list(self.ans)